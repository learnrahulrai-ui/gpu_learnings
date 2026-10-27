"""Scan every page of the site for banned words and banned patterns listed in AGENTS.md.

Usage, from the repository root:  python3 tools/check_banned.py
Needs: beautifulsoup4.  Exit code 1 if anything is found.
Learner quotes (class "you") are skipped: they are the learner's own words.
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
WARP_OK = {"11-program-counter.html", "12-the-48-trap.html", "13-the-864-cliff.html", "14-ownership.html", "words.html"}
OUTPUT_OK = re.compile(r"Latency of \w+ code snippet")


def scan(path):
    name = os.path.basename(path)
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
    return [(name,) + f for f in found]


def main():
    problems = []
    for path in sorted(glob.glob(os.path.join(ROOT, "*.html"))):
        problems += scan(path)
    for name, label, hit, txt in problems:
        print(f"{name}: {label}: {hit!r} | {txt[:100]}")
    print(f"{len(problems)} problem(s)")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
