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

## Lesson pages and the tutorial (`notes/lesson-*.html`)
- `notes/MIT-6.S894.html` is the tutorial's front page: the course, who it is for, what you need, how a lesson works, the syllabus table (every lesson must appear in it), then the notes by lab part and the map.
- A lesson keeps the full page structure and adds the tutorial sections, in this order: crumbs, h1 "Lesson N. ...", meta row (lab part, you build, you need), "In this lesson" contents, The story, Guess first, Your words, Work it out, Build it, Check it, Measure it, Connect the numbers, When it goes wrong, The lab's questions (paraphrased from the Fall 2025 handout, never quoted, each pointing to the lines that answer it), In plain words, Your guess against the machine, The interviewer's next question, Go deeper, then a previous/next pager.
- Build it describes each piece to write and the exact compile and execute commands, with an English panel under every command block; it never hands over finished lab code. Measured numbers are the laptop's; where the chats hold no measurement, say so and leave a DO blank for the reader's own.
- `<meta name="keywords" content="lesson">` marks a lesson. Every page in `notes/` carries the same `<header class="site">` and `<footer class="site">` (the footer says the material is independent and not affiliated with MIT).
