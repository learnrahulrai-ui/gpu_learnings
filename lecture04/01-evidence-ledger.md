Lecture 4 source ledger. DIRECT = visible PDF fact. DERIVED = stated arithmetic. PRIOR = earlier project record. UNVERIFIED = no observation.

E01 DIRECT PDF pages 1–4: lecture device 48 SMs, 20 GB main memory, 48 MB L2, 6 MB L1/SRAM, 12 MB registers, 360 GB/s DRAM figure, multiple GDDR6 channels. These figures are not GTX 1650 measurements.
E02 DIRECT PDF pages 5–9: 32 x 32 bits per cycle schematic; 1024 bits per cycle; gather/scatter drawing; first approach combines nearby memory requests.
E03 DIRECT PDF pages 10–14: second approach uses caching; 128-byte line and 32-byte sectors. Slide artwork cannot prove measured cache hits or DRAM transactions.
E04 DIRECT PDF pages 15–17: approximate 360 GB/s DRAM, 2.5 TB/s L2, 13.4 TB/s on-chip teaching figures.
E05 DIRECT PDF page 19: displayed 128 bytes/cycle/SM, 48 SMs, 2.18 GHz and 9.6 TB/s.
E06 DERIVED E05: 128 * 48 * 2.18 billion = 13.39392 trillion bytes per second, not the displayed 9.6 TB/s. Record this visible arithmetic inconsistency without rewriting either source figure.
E07 DIRECT PDF pages 19–20: SRAM under four warp schedulers on an SM. The CUDA Programming Guide, not physical residency alone, defines software shared-memory scope.
E08 DIRECT PDF pages 21–22: schematic distinct SM L1 caches need not be coherent. The slide is NOT a correct unsynchronized cross-block communication example.
E09 DIRECT PDF page 23: PTX ld.local, st.local, ld.global.ca, ld.global.cg; CUDA __ldg(), const __restrict__, textures. Actual executed SASS is separate evidence.
E10 DIRECT PDF page 24: explicit shared scratchpad. The slide's block (SM) phrase does not make a software block identical to an SM.
E11 DIRECT https://docs.nvidia.com/cuda/cuda-c-programming-guide/ : shared memory has block scope and synchronization rules.
E12 DIRECT https://docs.nvidia.com/cuda/cuda-c-best-practices-guide/ : actual participating-thread addresses matter for global memory request combination.
E13 DIRECT https://accelerated-computing.academy/fall25/labs/lab3/ : the naive wave mapping and branch-dependent input rules.
E14 PRIOR user's GPU learning project: GTX 1650 TU117, 14 SMs, 4 GB VRAM, nvcc 12.4. No new device query was made.
E15 UNVERIFIED: laptop PTX/SASS, Nsight counters, cache-hit count, physical DRAM traffic and timed measurements for this lecture.
