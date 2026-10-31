Lecture 4 — examiner questions. No solutions given.

01. From idx=idx_y*201+idx_x, why do (3,2),(4,2),(5,2) reading u1[idx-201] request related entries? Does one thread need a loop for these three addresses?
02. The naive wave expression uses six inputs for one output. Why does that fail to prove six DRAM transactions?
03. Why must u1[idx-1] and u1[idx+1] be treated as separate read expressions when evaluating the address pattern?
04. Derive all eight byte addresses for src[t] and src[t*8] at an assumed aligned float base 0x100. Which 32-byte sectors are touched?
05. If eight floats are adjacent but the first begins at 0x104 instead of 0x100, can sector coverage differ? Why?
06. A cache has a 128-byte line and 32-byte sectors. What evidence establishes a cache hit? What evidence proves a physical DRAM transfer?
07. Recompute 128 bytes/cycle/SM * 48 SMs * 2.18 GHz and compare to the slide's 9.6 TB/s. What is inconsistent?
08. Why cannot the DRAM, L2 and on-chip bandwidth numbers be added to yield one external-memory bandwidth?
09. Thread 15 writes tile[15] while thread 14 later reads it in the same CUDA block. Which synchronization condition is required?
10. Two blocks share one SM. Can their independently declared shared tile[256] objects refer to one logical array?
11. Why does an incoherent-L1 diagram not make an unsynchronized CUDA data race safe?
12. If PTX shows ld.global.ca, what extra evidence identifies the actual GPU instruction?
13. A scattered-copy kernel has greater measured time. What must be checked before assigning the cause to request addresses?

Required answer form: KNOWN -> EXACT OPERANDS/ADDRESSES -> PREDICTION -> OBSERVATION -> STILL UNKNOWN. Evidence must be source code, slide, CUDA documentation, compiled code or an actual counter, not an invented benchmark.
