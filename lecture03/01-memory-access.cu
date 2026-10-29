#include <cstddef>
#include <cstdint>
#include <iomanip>
#include <iostream>
#include <vector>
#ifdef __CUDACC__
#include <cuda_runtime.h>
#endif

struct AccessCase {
    const char* name;
    std::size_t count;
    std::size_t first;
    std::size_t difference;
};

// 0x100+0*4=0x100; 0x100+7*4=0x11c; 0x100+8*4=0x120.
// These are teaching addresses, not measured GPU pointers.
static const AccessCase cases[] = {
    {"eight adjacent floats", 8, 0, 1},
    {"eight spaced floats", 8, 0, 8},
    {"thirty-two adjacent floats", 32, 0, 1},
    {"thirty-two spaced floats", 32, 0, 8},
    {"cross 32-byte boundary", 8, 7, 1},
};

bool enumerate_requested_indices(const AccessCase& test,
                                 std::vector<std::size_t>& indices) {
    // TODO 01: 8, first=7, difference=1 -> calculate all 8 indices.
    // TODO 02: 32, first=0, difference=8 -> calculate last index.
    // TODO 03: reject multiplication/addition exceeding size_t.
    (void)test;
    indices.clear();
    return false;
}

#ifdef __CUDACC__
__global__ void memory_load_exercise(const float* src, float* dst,
                                     std::size_t count, std::size_t difference) {
    // TODO 04: derive thread-to-element mapping on paper.
    // TODO 05: copy count valid floats; prove no out-of-range reads.
    // TODO 06: compare addresses for adjacent and spaced requests.
    (void)src; (void)dst; (void)count; (void)difference;
}
#endif

int main() {
    std::cout << std::fixed << std::setprecision(0);
    std::cout << "Lecture 3 / memory / unfinished exercises\n";
    std::size_t pending = 0;
    for (const AccessCase& test : cases) {
        std::vector<std::size_t> indices;
        bool implemented = enumerate_requested_indices(test, indices);
        std::cout << test.name << " | requested=" << test.count
                  << " | first=" << test.first
                  << " | difference=" << test.difference
                  << " | result=" << (implemented ? "CHECK MANUALLY" : "PENDING")
                  << '\n';
        if (!implemented) ++pending;
    }
    std::cout << "PENDING=" << pending << " (nonzero exit is intentional)\n";
    return pending == 0 ? 0 : 2;
}
