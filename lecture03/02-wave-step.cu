#include <array>
#include <cmath>
#include <cstddef>
#include <iomanip>
#include <iostream>
#include <limits>
#ifdef __CUDACC__
#include <cuda_runtime.h>
#endif

struct WaveCase {
    std::array<float, 25> older{};
    std::array<float, 25> newer{};
    float damping = 0.125f;
    float coeff = 0.0625f;
};

WaveCase make_case() {
    WaveCase w;
    // 5*5=25; center=12; neighbors 12-5=7,12-1=11,12+1=13,12+5=17.
    w.older[12] = 3.0f;
    w.newer[12] = 4.0f;
    w.newer[7] = 3.0f;
    w.newer[11] = 1.0f;
    w.newer[13] = 2.0f;
    w.newer[17] = 5.0f;
    return w;
}

float compute_middle(const WaveCase& w) {
    // TODO 01: center=12 arithmetic from official wave_cpu_step.
    // TODO 02: show every intermediate calculation on paper.
    // TODO 03: decide border/wall/source/ordinary before writing result.
    (void)w;
    return std::numeric_limits<float>::quiet_NaN();
}

#ifdef __CUDACC__
__global__ void wave_exercise(const float* older, const float* newer, float* next,
                              int side, float damping, float coeff) {
    // TODO 04: map one thread to one valid cell.
    // TODO 05: test border/wall/source before neighbor arithmetic.
    // TODO 06: read older and newer, write next; account for every timestep.
    (void)older; (void)newer; (void)next;
    (void)side; (void)damping; (void)coeff;
}
#endif

int main() {
    const WaveCase w = make_case();
    std::cout << std::fixed << std::setprecision(6);
    std::cout << "Lecture 3 / wave / unfinished exercises\n";
    for (int index : {7, 11, 12, 13, 17}) {
        std::cout << "index=" << index << " older=" << w.older[index]
                  << " newer=" << w.newer[index] << '\n';
    }
    std::cout << "damping=" << w.damping << " coeff=" << w.coeff << '\n';
    const float actual = compute_middle(w);
    if (std::isnan(actual)) {
        std::cout << "PENDING: center result not implemented\n";
        return 2;
    }
    std::cout << "candidate=" << actual << " | CHECK AGAINST PAPER\n";
    return 0;
}
