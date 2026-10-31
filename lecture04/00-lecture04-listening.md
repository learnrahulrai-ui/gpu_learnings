MIT 6.S894. Lecture 4: Memory. Jonathan Ragan-Kelley. 25 September 2025.
Slides: https://accelerated-computing.academy/fall25/lectures/slides/Lecture4.pdf
Source code: https://accelerated-computing.academy/fall25/labs/lab3/

ACTIVE TASK: One expression, different threads.
Given wave code: idx = idx_y * n_cells_x + idx_x. The scene fixes n_cells_x at 201. Three ordinary threads have (idx_x,idx_y) = (3,2), (4,2), (5,2). Every thread evaluates u1[idx - n_cells_x]. Fill the three flat-array indices: ____, ____, ____. Draw an arrow from each thread to its input entry. Stop after ONE task and wait for verification.

SLIDE QUESTIONS (PDF page numbers count the title as page 1)
1–3. Which devices does the 360 GB/s teaching figure connect? 48 SMs, 20 GB, 48 MB L2 and 6 MB L1/SRAM belong to the course GPU, NOT the user's GTX 1650.
4. Why can consecutive memory requests use multiple GDDR6 channels? Which actual laptop channel-address function is unknown?
5–7. NVIDIA calls its 32-thread execution unit a warp. How does the actual program select addresses for participating threads? Thread IDs alone do not prove adjacent addresses.
8–9. The first approach combines nearby requests. Which one source expression are DIFFERENT threads evaluating? Six reads from one thread cannot be declared a combined physical DRAM operation.
10–14. The slide draws a 128-byte cache line divided into 32-byte sectors. Which source requests may use that line while it remains cached? Addresses cannot establish an actual hit.
15–17. The slide prints 360 GB/s DRAM, 2.5 TB/s L2 and 13.4 TB/s L1/SRAM teaching figures. What movement does each describe? Why must they not be added?
18–20. Four warp schedulers are drawn around a shared hardware SRAM on one SM. Why does this NOT grant different CUDA blocks access to the same logical private array?
21–22. The slide draws L1 copies on distinct SMs without general CPU-style cache coherence. Does this legalize unsynchronized cross-block writes and reads? No.
23. PTX can contain ld.global.ca and ld.global.cg. CUDA can use __ldg() and const __restrict__. Which SASS instructions actually execute? Look at compiler output.
24. Explicit SRAM scratchpad. The slide writes block (SM), but a CUDA block is software work and an SM is hardware; multiple blocks may reside on one SM.

TASKS NOT YET ASSIGNED
01. For three adjacent x values and equal y, derive u1[idx-1], u1[idx+1], u1[idx-201] and u1[idx+201] separately. Do not combine the four different expressions.
02. Assume an aligned byte base of 0x100 and four bytes per float. Write eight addresses of src[t] for t=0..7 and the aligned 32-byte sectors.
03. Use the identical assumption for src[t*8]. Determine which address relation differs.
04. Shift the assumed first byte address to 0x104 for src[t]. Compare contiguous values with sector alignment.
05. Distinguish a source-level read, a compiled load instruction, a request satisfied by cache and a DRAM transfer. Name the evidence required for each.
06. Calculate 128 bytes/cycle/SM times 48 SMs times 2.18 GHz independently. Compare with 9.6 TB/s on PDF page 19; record any discrepancy without fixing the slide.
07. Draw which of 256 threads writes each entry of shared tile[256], the required barrier, and which other thread reads it.
08. Draw two software blocks resident on one SM. Determine whether each sees its own private tile[0].
09. Inspect both PTX and SASS from the compiled executable before claiming which hardware instruction appears.
10. Predict relative time BEFORE collecting a result. Verify every output entry and keep raw timing trials; do not infer a cache cause from timing alone.

GUARDRAILS FROM LAB 3
An ordinary naive wave thread evaluates six source-level inputs and writes one output. Other branches differ. One kernel expression can use many inputs without a loop. One source-level read does not prove one physical DRAM transfer. Request combining concerns participating threads executing a particular memory instruction, not six different operands of one thread.

STATUS: no Lecture 4 device experiment or compiled PTX/SASS has been observed. Learner answers are pending. NEW THINGS INTRODUCED WITHOUT DERIVATION IN THE ACTIVE TASK: none.
