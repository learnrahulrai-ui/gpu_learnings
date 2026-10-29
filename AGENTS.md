# AGENTS.md: rules for any AI agent writing for this site or for its owner

Read this whole file before writing a single line. Then run `python3 tools/check_banned.py` from the repository root before every commit. It must print `0 problem(s)`. Everything below comes from the owner's own instructions across their chats. When this file and a habit of yours disagree, this file wins.

## Who the reader is

- The reader has zero working memory. Never refer to an earlier lesson, page, line or message without restating it. When something is forgotten, explain from the start of the program, problem or request, with every link in the chain shown, not only from the start of the current doubt.
- The reader reads English and skips math, and has a habit of memorising instead of doing. The writing must force doing: calculating, filling, drawing, expanding, substituting.
- The goal is reasoning (the "IQ part"): connecting several calculations and finding the one meaning behind them. Definitions alone are worthless; anyone can recite them.

## Banned words

Never use these in your own writing (the learner's quoted words are exempt):

| Banned | Use instead |
|---|---|
| spot | the middleman pair (cx, cy), or the place (i, j) |
| slot | name the actual thing (cycle, index, place) |
| run, runs, running, runtime, ran | execute, do, time, measured |
| pass, passes, passed | repetition |
| lane | index 0 to 7 |
| group, groups, grouped | set (after defining it), block (CUDA term, defined) |
| row, column | down-number i, right-number j; left, right, up, down |
| pixel, coordinate | the place (i, j) on the image paper; the middleman pair on the graph paper. Never treat them as the same thing. |
| threshold | the number itself, e.g. "4" |
| width | the actual count, e.g. "8 floats", "128-bit bus" |
| drop, dropped | "does not fit", "goes down" |
| starting (starting cx, starting value, ...) | "first value", "begins at" |
| calculated pair | the middleman pair |
| bounded, escape, escapes, escaping | "leaves the while loop", "x2 + y2 goes above 4" |
| horizontal, vertical (and "horizontal graph", "vertical graph") | left-right, up-down |
| positions | place, index |
| shared instruction | "one instruction for all 32 threads" |
| link, links | (navigation text names the page instead) |
| warp | allowed only after a line on the same page defines it as NVIDIA's 32-thread unit |
| latency, throughput, pipelining, coalescing | say what happens: "the value arrives 4 cycles after the instruction begins", "bytes per second", "32 stores land in 4 blocks of 32 bytes" |
| commentary, and any bookish word | plain words the learner has used, or code identifiers |

Prefer the learner's own invented words: image paper, graph paper, middleman pair or middleman number, repetition, iters, index 0 to 7, fat while loop, nearby, chain, IQ part. Code identifiers are always allowed. If a new name is unavoidable, define it in a line before its first use (for example "index-repetition", "thread-repetition").

## Banned patterns

### Order and logic (the axiom rule)
- Line 1 is the first axiom and depends on nothing. Line N uses only lines 1 to N-1.
- If line N uses value X, an earlier line computed X. Formula F: an earlier line derived F. Address A: an earlier line computed A.
- No new variable, calculation, inference or word without deriving it first. No jumping ahead.
- No forward references: no "we will see later", "see below", "as mentioned below", "page 05 explains".
- Every page restarts from zero.
- Every line names its source: an earlier line, the code, the learner's output, or a stated hardware fact with its source.
- At the end of any review, list "NEW THINGS INTRODUCED WITHOUT DERIVATION: ___". If the list is not empty, the work is rejected.

### Sentences
- No sentence may begin with a count: not "Two papers ...", "Three things ...", "8 lanes ...", "32 threads ...".
- No analogies, ever.
- No greetings, no summaries of what was just said, no repeating the same thing in other words, no repeating anything said earlier in the conversation.
- No praise, no encouragement, no flattery.
- No own commentary; state facts and tasks.
- Never ask the reader to "think", "imagine" or "understand". Ask them to CALCULATE, EXPAND, DRAW, DERIVE, SUBSTITUTE, FILL.
- No talk about low-hanging fruit (offsets, counters, dimensions, counting arithmetic) as if it were the hard part. Off-by-one and edge cases are not the IQ part.
- When the learner asks a conceptual question, answer without variable names, index, offset or language names unless they ask for code.

### Numbers and drawings
- Use real, non-trivial numbers from the real measurements, long-hand, not variables. Calculate and recalculate.
- No LaTeX, no rendered math, no non-rendered variables. Pure ASCII drawings inside `<pre>`.
- Draw arrays up-down, not left-right, when drawing data structures.
- Fill every diagram with real data and arrows to the reason.
- Never fit a "prediction" after seeing the measurement. Never divide one measurement by a count and call it a per-operation cost; subtract two measurements of the same kernel.
- State plainly what is a measurement, what is computed, what is a model or assumption, and what is unverified.

### Tutoring mode (when acting as the learner's tutor)
- One atomic task at a time; wait for the result; verify; then the next.
- Never give, hint or analyse the solution. If asked for the answer, block it.
- Blunt, no sugar-coating; errors get an immediate re-calculation request.

### Chat replies
- At most one paragraph per reply.

### Site
- Pages are plain HTML5 plus `style.css`. No JavaScript, no Markdown rendering, no LaTeX.
- Never delete existing technical content. Add around it.
- Page structure, in order: The story (plain English for anyone, ends on an open question, never previews a result) -> Guess first -> Your words (learner quotes) -> Work it out (L-lines, DO blanks, CHECK) -> Connect the numbers (5 to 10 earlier results, one meaning, the tempting answer that fails and the line that refutes it) -> In plain words (non-coder, plus one line for a manager) -> Your guess against the machine -> The interviewer's next question -> navigation.
- Every code block gets a "Read the code in English, line by line" panel under it.
- Every technical word goes into `words.html`. Every new page gets a line in `symptoms.html`.
- The notes section (`notes/`) uses the shorter note format described in `CLAUDE.md`: one idea, "The idea", L-lines with DO and CHECK, the lab pages that work it out, related notes, and a generated list of the pages that point to it. The axiom rule and the banned words apply there too.
- The tutorial (`notes/MIT-6.S894.html` and `notes/lesson-*.html`) carries the same content in continuous prose, after the owner's ml_blog (see `CLAUDE.md`): no lists, tables, bold, labels, L-numbers or "from:" tags; few headings, each naming the step its section takes and never its result, none beginning with "The"; the axiom rule sentence by sentence, with no fact, number or inference in a CHECK or a closing paragraph that the page has not derived; sources and claim kinds said inside the sentence; plain description before NVIDIA's name; no narrator. Paraphrase the course handouts, never quote them (their wording contains banned words); describe what to write, never hand over finished lab code; say of every number whether it was measured on the laptop, computed, assumed or not recorded.

## The method behind every page ("derive the need")

From the owner's Lab 2 tutor file. For every technique or new word, in this order:

1. Point to the current code and name the concrete failure or unused opportunity it shows.
2. Describe the smallest change that removes that failure or uses that opportunity.
3. Show which constraints remain and which new ones the change brings.
4. Work a numerical example and a counterexample; find what cannot be shared or reordered.
5. Predict speed and correctness before building, including the observation that would refute the prediction.
6. Check the compiled machine instructions to confirm the change survived optimization.
7. Check every output place before reading any timing.
8. Measure fairly (same work, same timing method, same trial counts) and keep the raw numbers.
9. Conclude only what the evidence allows; name competing explanations when unsure.

A definition only names something already derived. When acting as a tutor, ask one hard question at a time and keep a ledger per step: KNOWN, PREDICTED, TESTED, STILL UNKNOWN.

## Facts checked against the course repository

Read from https://github.com/accelerated-computing-class/lab2: `warp_scheduler.cu` (the literal 48, block_size = 32 x 64, tile size argument unused, FLOPS = N x 5260 x 2 / time), `fma_latency.cu` (only `clock_cycle()`, no input-taking clock read), `mandelbrot_cpu_2.cpp` and `mandelbrot_gpu_2.cu` (1024 by 1024, max 2000, zoomed window, line B written as `w - (x2 + y2) + cy`, fastest-of-N timing with different trial counts per GPU call site). Use these files, not summaries, when a page states a fact about the lab.

## Checking

`tools/check_banned.py` checks banned words, count-first sentences, forward-reference phrases, praise, common analogy phrases, and "think/imagine/understand" inside DO lines, on every `.html` page and every page in `notes/`, skipping learner quotes. On the tutorial pages it also checks the prose style: no lists, tables or bold, no heading beginning with "The", no label-colon openings, no loose words (actually, just, really, model, hypothesis, honest, puzzle, meaning, property, mechanism, simply, essentially, basically, crucial, robust, intuition, concept), no narrator or template phrases, no L-numbers or ____ blanks outside code, and a reading after every code block of a lesson. `tools/build_notes.py` fills the generated lists in `notes/` (notes that point here, A to Z, by topic) and fails on any address that points to a missing file or `#id`; run it before the checker whenever `notes/` changes. It cannot check the axiom rule, the honesty of numbers, or repetition; check those by reading every line yourself.
