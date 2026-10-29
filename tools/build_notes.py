"""Fill the generated parts of the notes/ section, and check every address the notes point to.

Usage, from the repository root:  python3 tools/build_notes.py
Needs: beautifulsoup4.  Exit code 1 if a note points to a file or #id that does not exist.

It rewrites only the text between these markers, so run it after adding or editing any page there:
  <!-- backlinks:begin --> ... <!-- backlinks:end -->   in every note: the lessons and notes that point to it
  <!-- lessons:begin --> ... <!-- lessons:end -->       in notes/index.html: every lesson, in order
  <!-- all:begin --> ... <!-- all:end -->               in notes/index.html: every note, A to Z
  <!-- topics:begin --> ... <!-- topics:end -->         in notes/index.html: notes by topic
A page's title is its <h1>, its one-line summary is <meta name="description">, its topics are
<meta name="keywords">; the topic "course" marks the course page and "lesson" marks a lesson,
and neither is listed as a note. Addresses inside <nav>, <header>, <footer>, the crumbs line and
the backlinks block are not counted as one page pointing to another. It also fails when a lesson
is missing from the course page.
"""
import glob
import html
import os
import re
import sys

import bs4

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
NOTES = os.path.join(ROOT, "notes")


def read(path):
    return open(path, encoding="utf-8").read()


def fill(text, name, body):
    rx = re.compile(r"(<!-- %s:begin -->\n).*?(<!-- %s:end -->)" % (name, name), re.S)
    if not rx.search(text):
        raise SystemExit(f"markers for {name} not found")
    return rx.sub(lambda m: m.group(1) + body + m.group(2), text)


def main():
    pages = {}
    for path in sorted(glob.glob(os.path.join(NOTES, "*.html"))):
        name = os.path.basename(path)
        soup = bs4.BeautifulSoup(read(path), "html.parser")
        desc = soup.find("meta", attrs={"name": "description"})
        keys = soup.find("meta", attrs={"name": "keywords"})
        pages[name] = dict(
            soup=soup,
            title=soup.h1.get_text(" ", strip=True),
            desc=desc["content"] if desc else "",
            topics=[k.strip() for k in keys["content"].split(",")] if keys else [],
        )

    problems = []
    pointed = {name: set() for name in pages}
    for name, page in pages.items():
        for a in page["soup"].find_all("a", href=True):
            href = a["href"]
            if re.match(r"[a-z]+:", href):
                continue
            target, _, anchor = href.partition("#")
            path = os.path.normpath(os.path.join(NOTES, target)) if target else os.path.join(NOTES, name)
            if not os.path.exists(path):
                problems.append(f"{name}: points to missing file {href}")
                continue
            if anchor:
                tname = target or name
                tsoup = pages[tname]["soup"] if tname in pages else bs4.BeautifulSoup(read(path), "html.parser")
                if not tsoup.find(id=anchor):
                    problems.append(f"{name}: points to missing #{anchor} in {target or name}")
            skip = (a.find_parent("nav") or a.find_parent("header") or a.find_parent("footer")
                    or a.find_parent(class_="crumbs") or a.find_parent(class_="backlinks"))
            if not skip and target in pages and target not in (name, "index.html") and name != "index.html":
                pointed[target].add(name)

    def item(name, with_desc):
        p = pages[name]
        tail = f": {html.escape(p['desc'], quote=False)}" if with_desc and p["desc"] else ""
        return f'<li><a href="{name}">{html.escape(p["title"], quote=False)}</a>{tail}</li>\n'

    def is_note(name):
        return name != "index.html" and not {"course", "lesson"} & set(pages[name]["topics"])

    for name in pages:
        if not is_note(name):
            continue
        sources = sorted(pointed[name], key=lambda n: pages[n]["title"].casefold())
        body = "<ul class=\"related\">\n" + "".join(item(n, False) for n in sources) + "</ul>\n" if sources else "<p>None yet.</p>\n"
        path = os.path.join(NOTES, name)
        text = fill(read(path), "backlinks", body)
        open(path, "w", encoding="utf-8").write(text)

    notes = [n for n in pages if is_note(n)]
    lessons = sorted(n for n in pages if "lesson" in pages[n]["topics"])
    courses = [n for n in pages if "course" in pages[n]["topics"]]
    for lesson in lessons:
        for course in courses:
            if not pages[course]["soup"].find("a", href=lesson):
                problems.append(f"{course}: does not list {lesson}")
    notes.sort(key=lambda n: pages[n]["title"].casefold())
    all_body = '<ul class="related">\n' + "".join(item(n, True) for n in notes) + "</ul>\n"
    topics = sorted({t for n in notes for t in pages[n]["topics"]}, key=str.casefold)
    topic_body = "".join(
        f'<p><b>{html.escape(t)}</b></p>\n<ul class="related">\n'
        + "".join(item(n, False) for n in notes if t in pages[n]["topics"])
        + "</ul>\n"
        for t in topics
    )
    index = os.path.join(NOTES, "index.html")
    lesson_body = '<ul class="related">\n' + "".join(item(n, True) for n in lessons) + "</ul>\n"
    text = fill(fill(fill(read(index), "lessons", lesson_body), "all", all_body), "topics", topic_body)
    open(index, "w", encoding="utf-8").write(text)

    for p in problems:
        print(p)
    print(f"{len(lessons)} lessons, {len(notes)} notes, {len(topics)} topics, {len(problems)} problem(s)")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
