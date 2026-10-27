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
- spot, slot, run (runs, running, runtime), pass (passes), lane, group, row, column, pixel, coordinate (pixel and coordinate must never be used as if they mean the same thing), threshold, width, drop, starting cx / "starting" anything, calculated pair, bounded, escape (say "leave the while loop"), horizontal, vertical (say left, right, up, down), positions, shared instruction, link(s), warp, latency, throughput, pipelining, coalescing, and other bookish words.
- No sentence may begin with a count ("Two papers ...", "Three things ...", "8 lanes ...").
- Prefer the learner's own words: image paper, graph paper, middleman pair/number, repetition, iters, index 0..7, fat while loop, nearby, chain. Code identifiers are always allowed.
- Make up new names only when there is no other way, and define them in a line before using them (for example "index-repetition").
