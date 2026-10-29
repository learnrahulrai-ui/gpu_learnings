Evidence is named before any calculation.

E01 DIRECT Lecture 3 PDF pages 2–6: course RTX 4000 Ada GPU (20 GB DRAM, 48 MB L2); data rates 360 GB/s DRAM and about 2.5 TB/s L2. Slide marks 2.5 TB/s "(to confirm)". Source https://accelerated-computing.academy/fall25/lectures/slides/Lecture3.pdf
E02 DIRECT PDF pages 7–9: DDR5-6400 32-bit interface, GDDR6 32-bit interface at 18 GT/s; five GDDR6 chips give 160 bits, 20 GB capacity and 360 GB/s.
E03 DIRECT PDF pages 10–11: HBM3, 2048-bit interface 3.2 GT/s per module; four modules, 96 GB, about 3.3 TB/s. Physical address mapping for the laptop NOT established.
E04 DIRECT PDF pages 13–20: a schematic of addresses spread among channels; 32 computation units × 32 bits/cycle = 1024 bits/cycle.
E05 DIRECT Lab 3 Part 0: PTX .ca, .cg, .cv load forms; compiler translates PTX to real SASS instructions; hints can change. https://accelerated-computing.academy/fall25/labs/lab3/
E06 DIRECT NVIDIA Programming Guide: for 4-byte values, 32-byte aligned memory transactions and data-use ratio matter. https://docs.nvidia.com/cuda/cuda-programming-guide/02-basics/writing-cuda-kernels.html
E07 DIRECT Official wave.cu CPU reference: older value, newer center plus four neighbors, borders, walls, sources, buffer swaps. https://github.com/accelerated-computing-class/lab3/blob/main/wave.cu
E08 VERIFIED SOURCE CHANGE 2024: RMSE print for shared-memory experiment incorrectly used naive_rel_rmse and was changed to shmem_rel_rmse; slit edge tolerance also adjusted. https://github.com/accelerated-computing-class/lab3/commit/43d51e2771b8b2108f495aa7d6742bbf6852e347
E09 VERIFIED SOURCE CHANGE 2025: memory coalescing test moved from one event measurement to repeated launches and added actual output checks. https://github.com/accelerated-computing-class/lab3/commit/f49d25e91a5dd0b761962ff0ced1c83b4867674e
E10 USER JOB DOCUMENT: custom CUDA kernels, low-latency inference, memory layouts, precision and profiling; course calculations are preparation, not proof of beating TensorRT.
E11 EXISTING REPOSITORY: gpu_learnings, branch main, 00–18 numbered exercise pages, 00–10 tutorial lessons, failures and AGENTS.md; prior observations GTX 1650 =14 SMs, NOT new measurement.
E12 UNVERIFIED: YouTube speech/transcript (video watch blocked); NVIDIA CUDA toolchain compilation not attempted here, because nvcc is absent in this environment.
