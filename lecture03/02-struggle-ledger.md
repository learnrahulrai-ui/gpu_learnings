This is not a polished glossary. Record the exact point where numbers stopped connecting.

QUOTED LEARNER: "Everybody knows about all these definitions." "YOU INTRODUCED NEW THINGS IN THE LAST STEP." "My brain freezes in middle steps." "I only read English but skip the math." These are learner statements, not clinical facts.
ACTUAL PROJECT STATE: Lab 1/2 material present in 19 numbered pages and eleven course lessons; no measured Lecture 3 or Lab 3 output found before creating this scaffold. Lecture 3 source calculations are pending.
ONE ACTIVE TASK: 32-bit interface, 8 bits per byte, 32 / 8 = ____; draw four 8-bit boxes. Require an answer before continuing.
RECORD EACH ATTEMPT: exact input -> numeric prediction BEFORE executing -> every arithmetic line -> mistaken claim -> code/SASS evidence -> output or NOT MEASURED -> correction -> next one task.
ACTUAL UPSTREAM BUG: https://github.com/accelerated-computing-class/lab3/commit/43d51e2771b8b2108f495aa7d6742bbf6852e347 . Shared-memory error was printed from the naive result until the patch. This is NOT a reported user implementation bug.
POSSIBLE FAILURES TO TEST, NOT OBSERVED USER ERRORS:
F37: course 48 SM -> laptop 14 SM, hardware total copied across.
F38: GB capacity confused with GB/s transfer.
F39: addresses 0x11c, 0x120 treated as same aligned 32-byte region.
F40: PTX .ca cache instruction assumed to be exactly the executed SASS.
F41: buffer names u0/u1 mistaken for fixed allocations after std::swap.
F42: unfinished GPU TODO accepted as successful because code compiled.
F43: a printed speedup trusted before checking every output element.
F44: pre-2025 one-launch timing compared directly to post-2025 multi-launch timing.
STATUS: memory questions pending; wave questions pending; hardware measurements pending; failed-exercise records not invented.
NEW THINGS INTRODUCED WITHOUT DERIVATION IN ACTIVE TASK: none.
