Lecture 4 laptop checklist.

DIRECT LECTURE FIGURES: teaching GPU 48 SMs, 20 GB external memory, 48 MB L2, 128 KB on-chip SRAM per SM and the slide's approximate memory rates. They are NOT the laptop's values.
PRIOR PROJECT RECORD (not re-measured): NVIDIA GTX 1650 TU117, compute capability sm_75, 14 SMs, 4 GB VRAM, nvcc 12.4 and prior driver version 580.178.04.

Check the laptop before experiments:
nvidia-smi --query-gpu=name,memory.total,clocks.sm,clocks.mem,driver_version --format=csv
nvcc --version

From repository root, after writing the unfinished kernels:
nvcc -arch=sm_75 -std=c++17 -O2 -lineinfo lecture04/01-access-pattern.cu -o /tmp/lecture04-access
nvcc -arch=sm_75 -std=c++17 -O2 -lineinfo lecture04/02-block-scratchpad.cu -o /tmp/lecture04-shared

Inspect compiled instructions:
cuobjdump --dump-ptx /tmp/lecture04-access
cuobjdump --dump-sass /tmp/lecture04-access

Do not claim that compilation proves correctness. The TODO versions must report PENDING. No Lecture 4 CUDA compilation or GPU measurement was made by the assistant in its environment.
