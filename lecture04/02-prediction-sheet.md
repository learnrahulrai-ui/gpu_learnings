Lecture 4 — one experiment sheet. Complete on paper before execution.

Source expression: ____________________________
Participants and input indices: ______________
First byte address: __________________________  [ASSUMED / OBSERVED]
Requested byte address A: ____________________
Requested byte address B: ____________________
Requested byte address C: ____________________
Distinct aligned 32-byte sectors: ____________  [PENCIL PREDICTION]
Executed SASS instruction: ___________________  [OBSERVED / UNKNOWN]
Hardware sector counter: _____________________  [MEASURED / UNKNOWN]
All output entries correct: __________________ [YES / NO]
Trial 1 batch time: __________________________
Trial 2 batch time: __________________________
Trial 3 batch time: __________________________
Prediction written BEFORE test: ______________
Observation that would refute it: ____________
Uncontrolled alternative explanation: ________

ADDRESS A: with first byte 0x100, float size 4 bytes, t=0..7, derive src[t] byte addresses and their 32-byte sector IDs.
ADDRESS B: keep assumptions and use src[t*8]. Derive each separately.
ADDRESS C: change only first byte to 0x104; keep src[t]. Distinguish adjacent requests from sector alignment.
SCRATCHPAD: src[g]=g for g=0..511. Blocks use 256 threads. Expected dst[base+t]=src[base+((t+1)%256)]. Write expected values for g=0,254,255,256,510,511. Place a barrier between shared writes and cross-thread reads.
CONDITIONS: validate every output before timing. Compiled load count, cache state and physical DRAM traffic are NOT established by the source expressions or by timing alone. Tests with different input spans can have different cache behavior.
No measured results are supplied.
