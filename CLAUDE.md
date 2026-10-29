# Writing rules for this site (from the owner)

Full list of banned words and patterns, and the checker to run before every commit: see `AGENTS.md` and `python3 tools/check_banned.py`.

The site turns long Claude/ChatGPT chats into exercise pages. Pages are plain HTML5 plus `style.css`. No JavaScript, no Markdown rendering, no LaTeX. Drawings are ASCII inside `<pre>`. Answers hide inside `<details><summary>CHECK</summary>`.

## The axiom rule (every line)
- Each line is numbered (L01, L02, ...) and uses only what earlier lines on the same page made. A grey note names the source: an earlier line, the code, the learner's own output, or a stated hardware/intrinsic fact.
- If line N uses value X, an earlier line computed X. If it uses formula F, an earlier line derived F. If it uses address A, an earlier line computed A.
- No forward references: no "we will see later", "as mentioned below", or "page 05 explains".
- Every page restarts from zero. The learner has no working memory of other pages. Restate what is needed.
- Make the learner calculate (DO lines with ____ blanks). Use real numbers from the real run, long-hand. Don't write commentary, definitions everyone already knows, or praise.
- A reply in chat is at most one paragraph.

## Banned words and forms
- spot, slot, run (runs, running, runtime), pass (passes), lane, group, row, column, pixel, coordinate (pixel and coordinate must never be used as if they mean the same thing), threshold, width, drop, starting cx / "starting" anything, calculated pair, bounded, escape (say "leave the while loop"), horizontal, vertical (say left, right, up, down), positions, shared instruction, link(s), warp (allowed only after a line defines it as NVIDIA's 32-thread unit, since `warp_scheduler.cu` uses it), latency, throughput, pipelining, coalescing, and other bookish words.
- No sentence may begin with a count ("Two papers ...", "Three things ...", "8 lanes ...").
- Prefer the learner's own words: image paper, graph paper, middleman pair/number, repetition, iters, index 0..7, fat while loop, nearby, chain. Code identifiers are always allowed.
- Make up new names only when there is no other way, and define them in a line before using them (for example "index-repetition").

## Page structure (keep for every new page)
1. **The story**: plain English sentences for any reader, from someone who has only just heard of GPUs to a CEO. Say what the problem is, what the learner believed, and where the thinking broke. End on an open question. Never preview a result (that is a forward reference). No analogies.
2. **Your words**: quotes from the learner's chat at the point of struggle.
3. **Work it out**: the numbered L-lines with DO blanks and CHECK.
4. **Connect the numbers**: collect 5 to 10 earlier results (by line number) and ask for the one meaning behind them, often with a twist computed from real data. The CHECK states the meaning, then names the tempting answer that fails and the line that refutes it. The point of the site is this step, not the arithmetic.
5. **In plain words**: what it means for a non-coder, including one line for a manager.
- Never delete existing technical content; add around it.
- Every code block (C++, intrinsics, machine listing) gets a "Read the code in English, line by line" panel right under it: one plain sentence per code line.
- Every technical word used anywhere goes into `words.html` with a plain-English definition.
- Every page opens (after the story) with a "Guess first" box asking for one number or yes/no, and closes with "Your guess against the machine" (the real measured or computed value) and "The interviewer's next question" (a harder follow-up with its answer under CHECK). New pages also get a line in `symptoms.html`. Every new way a clean-looking result can be wrong goes into `failures.html`, pointing to the page that works it out.
- The GPU basics track (`tutorial.html`, `t1-...`, `t2-...`, `t3-...`) is a general tutorial in the same style and structure, not tied to the course. Where the learner's laptop has no measurement, numbers are computed from published specs with assumptions stated, and a DO line asks the reader to measure their own.

## Notes pages (`notes/`)
- Short reference pages for self-learners, one idea each. `notes/MIT-6.S894.html` lists them by lab part in course order; `notes/index.html` lists them A to Z and by topic.
- Each note, in order: crumbs line, h1, sub line with its topics, "The idea" (plain sentences that name the thing and end on the question the lines answer; no results, no analogies), "Work it out" (L-lines under the axiom rule, at least one DO with CHECK, real numbers), "Worked out in full" (the lab pages), "Related notes" (each with the question the other note answers, not its result), "Notes that point here" (generated).
- Notes do not need the story, guess, connect, plain-words or interviewer boxes, or entries in `symptoms.html` and `failures.html`; the lab pages they point to have those. Banned words, the axiom rule and `words.html` still apply.
- `<meta name="description">` is the note's line in the A-to-Z list; `<meta name="keywords">` holds its topics. After adding or editing a note, run `python3 tools/build_notes.py` (fills the generated lists, checks every address), then `python3 tools/check_banned.py`. Never edit the text between `<!-- ...:begin -->` and `<!-- ...:end -->` by hand.

## Lesson pages and the tutorial (`notes/lesson-*.html`, `notes/MIT-6.S894.html`)
The tutorial is written in continuous prose, de-slopped the way the owner's ml_blog is. The same content as every other page, in a different form:
- No bullet or numbered lists, no tables, no bold, no hero box, buttons or contents list, no label-colon openings ("Story:", "Source:", "For a manager:"), no L-numbers, no "from:" tags, no ____ blanks. The source and kind of every number is said inside the sentence: measured on the laptop, computed from the lab's code or counts, a published figure named by its source (NVIDIA's Turing tuning guide, the CUDA programming guide, Agner Fog's instruction tables, IEEE 754, the Fall 2025 handout), assumed, or not recorded.
- The axiom rule holds sentence by sentence, without line numbers: each sentence uses only the code shown on the page, a measurement or published source named in the sentence, or what an earlier sentence on the same page computed or defined. No result appears before its derivation, and a CHECK answer, the closing paragraphs or the final question never bring a fact, number, word or inference that the page has not built. Before publishing, write out "NEW THINGS INTRODUCED WITHOUT DERIVATION" for the page, sentence by sentence; it must be empty.
- Few h2 headings, each naming the step its section takes (what it reads, works out or splits), never the result, because a result in a heading comes before its derivation; a heading uses only words and numbers defined above it. No heading begins with "The" or with a count.
- Plain description first, NVIDIA's name last ("the identical blocks of hardware the chip is built from, which NVIDIA calls SMs"). Each page defines warp, SM and scheduler in words before it uses them. Restate a number instead of pointing back to where it was computed. No narrator ("the learner"), no "interviewer", no "tempting answer". Also banned in the tutorial: actually, just, really, model, hypothesis, honest, puzzle, meaning, property, mechanism, simply, essentially, basically, crucial, robust, intuition, concept.
- `notes/MIT-6.S894.html` is the front page: what the course is and where its handouts are; who the tutorial is for and what it needs; how a lesson works; the syllabus as one paragraph per lab part naming every lesson with what you build and what you work out (every lesson must appear there, and that heading keeps `id="syllabus"`); the notes as one paragraph per lab part naming each note with the question it answers, with the lessons and exercise pages that work it out; then the map.
- A lesson, in order: crumbs, h1 "Lesson N. ...", a sub line (lab part, what you build, what you need, and how the pencil paragraphs work), the story in plain sentences ending on its open question, a lead sentence and the learner's quote (`<p class="you">`, no "Your words:" label), the guess as a pencil paragraph, then the sections. A pencil paragraph is `<p class="do">`, a request to work something out with the numbers it needs, and its answer sits under `<details><summary>CHECK</summary>` as sentences or an ASCII `<pre>`. Every code or command block is followed by a plain paragraph that reads it in English, piece by piece.
- Where a lab part asks for code, a section describes each piece to write and the exact compile and execute commands; it never hands over finished lab code. Where the chats hold no measurement, say so and leave the measurement to the reader.
- The lesson closes, without a heading for each part: the gathered results and a pencil paragraph asking for the sentence that connects them (its CHECK states the meaning, then the reading that fails and the number that refutes it); the handout's questions, paraphrased from the Fall 2025 handout and never quoted, with the results that answer them; the failures that look like success, with their causes; the plain-words paragraph for a non-coder, which includes the line for a manager; the guess against the measured value; the harder follow-up question as a pencil paragraph; the lab pages and notes that work the same ground; then the previous/next pager.
- `<meta name="keywords" content="lesson">` marks a lesson. Every page in `notes/` carries the same `<header class="site">` and `<footer class="site">` (the footer says the material is independent and not affiliated with MIT).
- `tools/check_banned.py` enforces the prose rules above on the tutorial pages (lists, bold, "The" headings, label-colon openings, loose words, narrator phrases, L-numbers, a reading after every code block).
