Lecture 3 — Memory, pencil notebook.
Sources: https://accelerated-computing.academy/fall25/lectures/slides/Lecture3.pdf (20 pages); https://accelerated-computing.academy/fall25/labs/lab3/ .
Video supplied: https://www.youtube.com/watch?v=NgrCQcU0Sbg ; its spoken transcript was not accessible for verification.

ACTIVE ONE TASK: lecture slide 7 shows an interface of 32 bits. One byte has 8 bits. DRAW four adjacent 8-bit boxes. FILL 32 / 8 = ____ bytes per transfer. Stop for the learner's answer.

LATER TASKS — NOT YET ASSIGNED:
01. DDR5-6400: 6.4 billion transfers each second × bytes per transfer = ____ billion bytes/s.
02. GDDR6: 18 billion transfers each second × bytes per transfer = ____ billion bytes/s.
03. Five GDDR6 chips × result 02 = ____ billion bytes/s; five chips × 4 GB = ____ GB.
04. HBM3: 2048 bits / 8 = ____ bytes; 3.2 billion transfers/s × that result = ____ billion bytes/s.
05. Four HBM3 modules × result 04 = ____ billion bytes/s; 4 × 24 GB = ____ GB.
06. 32 execution units × 32 bits each cycle = ____ bits per cycle.
07. Teaching addresses 0x100, 0x104, 0x108 ... : eight consecutive 4-byte words -> ____ aligned 32-byte regions.
08. Teaching addresses 0x100, 0x120, 0x140 ... : eight spaced words -> ____ aligned 32-byte regions.
09. Wave input: 5×5, center=12, older[12]=3, newer[12]=4, newer[7]=3, newer[11]=1, newer[13]=2, newer[17]=5, damping=0.125, coeff=0.0625; evaluate the published CPU reference by hand, do not write the answer now.
10. After timestep 1, 2, 3, name the physical buffers A/B holding older/newer states.

Course GPU = RTX 4000 Ada (48 SMs, 20 GB); learner's project records GTX 1650 (14 SMs). Never transfer device specifications between them.
No completed homework code, no invented time measurements, no solved TODOs.
