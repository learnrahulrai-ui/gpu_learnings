"""Scan every page of the site for banned words and banned patterns listed in AGENTS.md.

Usage, from the repository root:  python3 tools/check_banned.py   (scans *.html and notes/*.html)
Needs: beautifulsoup4.  Exit code 1 if anything is found.
Learner quotes (class "you") are skipped: they are the learner's own words.
The tutorial pages (notes/MIT-6.S894.html and notes/lesson-*.html) are also held to the prose style:
no lists, tables or bold, no heading that begins with "The", no label-colon openings, no loose words,
no narrator or template phrases, no L-numbers or ____ blanks, and on lessons a reading after every code block.
Pages in REBUILT also may not use the word line or template openers such as "Read in English".
"""
import glob
import os
import re
import sys

import bs4

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")

BANNED = re.compile(
    r"\b(spots?|slots?|run|runs|running|runtime|ran|pass|passes|passed|lanes?|groups?|grouped|"
    r"rows?|columns?|pixels?|coordinates?|threshold|width|drop|dropped|starting|calculated pair|"
    r"bounded|escape[sd]?|escaping|horizontal|vertical|positions?|shared instruction|links?|"
    r"warps?|latency|throughput|pipelin\w*|coalesc\w*|commentary)\b",
    re.I,
)
COUNT_START = re.compile(
    r"(^|[.!?]\s+)(\d+|one|two|three|four|five|six|seven|eight|nine|ten)\s+[a-zA-Z]", re.I
)
FORWARD_REF = re.compile(
    r"\b(we will see|you will see|see below|as mentioned below|mentioned later|explained later|"
    r"later on this page|in the next page|page \d+ explains)\b",
    re.I,
)
PRAISE = re.compile(r"\b(great job|well done|excellent|good job|congratulations|awesome)\b", re.I)
ANALOGY = re.compile(r"\b(think of it as|it is like a|just like a|imagine a|similar to a)\b", re.I)
THINK_IN_DO = re.compile(r"\b(think|imagine|understand)\b", re.I)

# Allowed exceptions: warp is defined on these pages before use; program output quoted verbatim.
WARP_OK = {"11-program-counter.html", "12-the-48-trap.html", "13-the-864-cliff.html", "14-ownership.html", "17-hardware-or-launch.html", "18-two-places-per-thread.html", "words.html",
           "notes/warp.html", "notes/filling-the-wait.html", "notes/register-budget.html", "notes/program-counter.html", "notes/index.html",
           "notes/lesson-04-gpu-32-threads.html", "notes/lesson-06-how-many-threads.html", "notes/lesson-08-independent-work.html",
           "notes/lesson-09-many-cores.html", "notes/lesson-10-many-threads.html"}
OUTPUT_OK = re.compile(r"Latency of \w+ code snippet")

# Prose style of the tutorial (notes/MIT-6.S894.html, notes/lesson-*.html).
TUTORIAL = re.compile(r"notes/(MIT-6\.S894|lesson-[^/]*)\.html$")
LOOSE = re.compile(
    r"\b(actually|just|really|models?|hypothes[ie]s|honest(ly)?|puzzles?|meaning|property|mechanisms?|simply|"
    r"essentially|basically|crucial|robust|intuition|intuitive|concepts?)\b",
    re.I,
)
NARRATOR = re.compile(r"\b(the learner|interviewer|tempting answer)\b", re.I)
LABEL = re.compile(
    r"(^|[.!?]\s+)(notes?|tips?|answer|examples?|sources?|summary|results?|key (idea|point)|story|goals?|hint|warning|"
    r"pitfalls?|measured|computed|assumed|prediction|check|fix|cause|symptom|rule|takeaway|bottom line|in short|"
    r"for a manager|your words|guess first|in plain words|go deeper|you need|you build|lab part|topics|lessons?|"
    r"full exercises|from|step \d+|question \d+|read the code[^:]*)\s*:",
    re.I,
)
LEFTOVER = re.compile(r"\bL\d\d\b|____")
# Tutorial pages rebuilt under the axiom audit (see CLAUDE.md); a lesson joins this set once it is rebuilt.
REBUILT = {"notes/MIT-6.S894.html", "notes/lesson-01-reference.html"}
LABELLING = re.compile(
    r"\b(lines?|read in english|gathered together|without code|for a manager|the guess at the top|"
    r"a harder question to finish with)\b",
    re.I,
)


def scan(path):
    name = os.path.relpath(path, ROOT)
    soup = bs4.BeautifulSoup(open(path, encoding="utf-8").read(), "html.parser")
    for q in soup.select(".you"):
        q.decompose()
    found = []
    for t in soup.find_all(["p", "li", "h1", "h2", "summary", "title", "a", "dd", "dt", "pre"]):
        txt = t.get_text(" ", strip=True)
        txt = OUTPUT_OK.sub("", txt)
        for m in BANNED.finditer(txt):
            if m.group(0).lower().startswith("warp") and name in WARP_OK:
                continue
            found.append(("BANNED WORD", m.group(0), txt))
        if t.name == "pre":
            continue
        body = re.sub(r"^L\d+\s+(DO\s+)?", "", txt)
        for m in COUNT_START.finditer(body):
            found.append(("COUNT-FIRST SENTENCE", m.group(0).strip(), body))
        for rx, label in ((FORWARD_REF, "FORWARD REFERENCE"), (PRAISE, "PRAISE"), (ANALOGY, "ANALOGY")):
            for m in rx.finditer(body):
                found.append((label, m.group(0), body))
        if "do" in (t.get("class") or []):
            for m in THINK_IN_DO.finditer(body):
                found.append(("ASKS TO THINK, NOT DO", m.group(0), body))
    if TUTORIAL.search(name.replace(os.sep, "/")):
        found += scan_tutorial(name, soup)
    return [(name,) + f for f in found]


def scan_tutorial(name, soup):
    found = []
    main = soup.find("main")
    for t in main.select("nav"):
        t.decompose()
    for t in main.find_all(["ul", "ol", "li", "table", "b", "strong"]):
        found.append(("LIST, TABLE OR BOLD IN THE TUTORIAL", t.name, t.get_text(" ", strip=True)[:80]))
    for h in main.find_all("h2"):
        if re.match(r"the\b", h.get_text(" ", strip=True), re.I):
            found.append(("HEADING BEGINS WITH THE", h.get_text(" ", strip=True), ""))
    for t in main.find_all(["p", "h1", "h2", "summary", "pre"]):
        txt = t.get_text(" ", strip=True)
        for rx, label in ((LOOSE, "LOOSE WORD"), (NARRATOR, "NARRATOR OR TEMPLATE PHRASE")):
            for m in rx.finditer(txt):
                found.append((label, m.group(0), txt))
        if t.name != "pre":  # code copied from the lab pages may hold its own blanks and colons
            for rx, label in ((LEFTOVER, "TEMPLATE LEFTOVER"), (LABEL, "LABEL-COLON OPENING")):
                for m in rx.finditer(txt):
                    found.append((label, m.group(0).strip(), txt))
    if name.replace(os.sep, "/") in REBUILT:
        for t in main.find_all(["p", "h1", "h2", "summary", "pre"]):
            if t.name == "pre" and not t.find_parent("details"):
                continue  # code copied from the starter keeps its own words
            txt = t.get_text(" ", strip=True)
            for m in LABELLING.finditer(txt):
                found.append(("LABEL OR TEMPLATE OPENER", m.group(0), txt))
    if "lesson-" in name:
        for pre in main.find_all("pre"):
            if pre.find_parent("details"):
                continue
            nxt = pre.find_next_sibling()
            if nxt is None or nxt.name != "p" or "do" in (nxt.get("class") or []):
                found.append(("CODE WITHOUT A READING AFTER IT", pre.get_text()[:60], ""))
    return found


def main():
    problems = []
    for path in sorted(glob.glob(os.path.join(ROOT, "*.html")) + glob.glob(os.path.join(ROOT, "notes", "*.html"))):
        problems += scan(path)
    for name, label, hit, txt in problems:
        print(f"{name}: {label}: {hit!r} | {txt[:100]}")
    print(f"{len(problems)} problem(s)")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
