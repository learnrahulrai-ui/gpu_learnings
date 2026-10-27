# Writing rules for this site (from the owner)

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
- Every page opens (after the story) with a "Guess first" box asking for one number or yes/no, and closes with "Your guess against the machine" (the real measured or computed value) and "The interviewer's next question" (a harder follow-up with its answer under CHECK). New pages also get a line in `symptoms.html`.
- The GPU basics track (`tutorial.html`, `t1-...`, `t2-...`, `t3-...`) is a general tutorial in the same style and structure, not tied to the course. Where the learner's laptop has no measurement, numbers are computed from published specs with assumptions stated, and a DO line asks the reader to measure their own.
