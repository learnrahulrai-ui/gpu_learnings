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

## Checking

`tools/check_banned.py` checks banned words, count-first sentences, forward-reference phrases, praise, common analogy phrases, and "think/imagine/understand" inside DO lines, on every `.html` page, skipping learner quotes. It cannot check the axiom rule, the honesty of numbers, or repetition; check those by reading every line yourself.
