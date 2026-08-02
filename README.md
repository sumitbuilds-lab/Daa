# Design and Analysis of Algorithms (DAA) — Lab 01

**Course:** BTech CSE / CE, 3rd Semester
**Date:** July 28, 2026
**Instructor:** Dr. Ajaya Kumar Dash

This repository contains C implementations, algorithms, and time-complexity analysis for all six problems of DAA Lab-01.

## 📁 Repository Structure

```
DAA_Lab01/
├── Q1_order_of_growth/
│   └── q1_order_of_growth.c
├── Q2_fair_biased_coin/
│   └── q2_coin_simulation.c
├── Q3_bubble_sort_analysis/
│   └── q3_bubble_sort.c
├── Q4_towers_of_hanoi/
│   └── q4_towers_of_hanoi.c
├── Q5_partition_point/
│   └── q5_partition_point.c
├── Q6_element_uniqueness/
│   └── q6_element_uniqueness.c
└── README.md
```

Each program compiles standalone with `gcc`:

```bash
gcc -Wall -O2 <file>.c -o out -lm
./out
```

---

## Q1 — Put Them in Order

**Task:** Arrange the given 12 functions by increasing order of growth for large `n`.

**Algorithm:**
Direct evaluation overflows for `3^n` and `2^(32n)` even at moderate `n`, so instead of computing `f(n)` directly, we compute `log2(f(n))` for each function. Since `log2` is monotonically increasing, sorting by `log2(f(n))` preserves the true growth order while staying numerically stable.

| Step | Action |
|---|---|
| 1 | Fix a large `n` (e.g. `10^6`) |
| 2 | Compute `log2(f(n))` for each of the 12 functions using closed-form log identities |
| 3 | Sort the 12 `(name, log2-value)` pairs ascending |
| 4 | Print the resulting order |

**Result (increasing order of growth):**

```
1/n  <  log2 n  <  n^0.51  <  12√n ≈ 50√n  <  n log2 n  <  100n²+6n ≈ n²-324
     <  2n³  <  n^(log2 n)  <  3ⁿ  <  2^(32n)
```

> Note: `12√n` & `50√n` are both `Θ(√n)` (differ only by constant); same for `100n²+6n` and `n²-324`, both `Θ(n²)`.

**Time Complexity:** `O(1)` — fixed number (12) of functions evaluated and sorted, i.e. `O(k log k)` for `k` = constant.

---

## Q2 — Fair vs Biased Coin

**Task:** Simulate coin tosses to empirically verify `P(HEAD) ≈ 0.5` for a fair coin, and compare against a biased coin.

**Algorithm (Monte Carlo Simulation):**
```
toss(p):
    r ← uniform random number in [0, 1)
    return HEAD if r < p else TAIL

simulate(p, N):
    heads ← 0
    repeat N times: heads ← heads + toss(p)
    return heads / N
```

Run `simulate(0.5, N)` for a fair coin and `simulate(p_biased, N)` for a biased coin across increasing `N` (100 → 10⁶), and observe convergence via the Law of Large Numbers.

**Time Complexity:** `O(N)` — one constant-time random draw per toss.
**Space Complexity:** `O(1)`.

---

## Q3 — Performance Analysis of Bubble Sort

**Task:** Compare two bubble sort variants on randomized data by counting comparisons.

**Algorithm (i) — Adaptive (early termination):**
```
for i ← 0 to n-2:
    swapped ← false
    for j ← 0 to n-2-i:
        comparisons++
        if A[j] > A[j+1]: swap(A[j], A[j+1]); swapped ← true
    if not swapped: break
```

**Algorithm (ii) — Non-adaptive (always full n-1 passes):**
```
for i ← 0 to n-2:
    for j ← 0 to n-2-i:
        comparisons++
        if A[j] > A[j+1]: swap(A[j], A[j+1])
```

**Time Complexity:**

| Variant | Best Case | Average Case | Worst Case |
|---|---|---|---|
| Adaptive (early stop) | `O(n)` (already sorted) | `O(n²)` | `O(n²)` |
| Non-adaptive (full passes) | `O(n²)` | `O(n²)` | `O(n²)` |

**Observation:** For randomized input, both variants perform close to `n(n-1)/2` comparisons — the adaptive version's advantage only shows up clearly on already-sorted or nearly-sorted data. The program outputs CSV (`n, comparisons_adaptive, comparisons_full`) to stdout for plotting.

---

## Q4 — Towers of Hanoi (ToH)

**Task:** Simulate ToH and analyze the number of moves as a function of `n` discs.

**Algorithm (recursive):**
```
ToH(n, source, aux, dest):
    if n == 0: return
    ToH(n-1, source, dest, aux)       # move n-1 discs out of the way
    move disc n from source to dest   # move largest disc
    ToH(n-1, aux, source, dest)       # move n-1 discs onto dest
```

**Recurrence:** `T(n) = 2·T(n-1) + 1`, `T(0) = 0` → solves to `T(n) = 2ⁿ − 1`.

**Time Complexity:** `O(2ⁿ)` — exponential, since each call branches into two recursive calls of size `n-1`.
**Space Complexity:** `O(n)` — recursion stack depth.

**Conclusion from the plot:** `n` vs. moves grows exponentially (sharp upward curve); plotting `log2(moves)` vs `n` gives a straight line, confirming `Θ(2ⁿ)` growth.

---

## Q5 — Find the Partition Point

**Task:** Given array `A` with a run of 0's followed by a run of 1's, find the exact transition index.

**Algorithm (binary search on the answer):**
```
low ← 0, high ← n-1, result ← n
while low ≤ high:
    mid ← (low + high) / 2
    if A[mid] == 1:
        result ← mid
        high ← mid - 1      # look further left for an earlier 1
    else:
        low ← mid + 1       # A[mid] == 0, search right half
return result
```

**Why it works:** The array is monotonic in the sense that all 0's precede all 1's, so binary search can decide which half to discard at every step — the same principle used in "find first true in a sorted boolean array" problems.

**Time Complexity:** `O(log n)` (vs. `O(n)` for a naive linear scan).
**Space Complexity:** `O(1)`.

---

## Q6 — Element Uniqueness

**Task:** Given `n` random numbers, determine whether any duplicates exist.

**Method 1 — Brute Force:**
```
for i ← 0 to n-1:
    for j ← i+1 to n-1:
        if A[i] == A[j]: return true (duplicate found)
return false
```
**Time Complexity:** `O(n²)`, **Space:** `O(1)`.

**Method 2 — Sort + Adjacent Scan:**
```
sort(A)                              # O(n log n)
for i ← 0 to n-2:
    if A[i] == A[i+1]: return true (duplicate found)
return false
```
**Time Complexity:** `O(n log n)` (dominated by sorting), **Space:** `O(1)` extra if sorted in place.

**Conclusion for large n:** Sorting-based uniqueness check scales far better than brute force. For `n = 20,000`, brute force performs ~`2×10⁸` comparisons vs. ~`n log₂ n ≈ 2.9×10⁵` for sort-based — several orders of magnitude fewer operations. The program benchmarks both and prints CSV timing data for plotting.

---

## 📊 Summary Table

| Q | Problem | Best Approach | Time Complexity | Space Complexity |
|---|---|---|---|---|
| 1 | Order of growth | Log-based comparison | O(1) (fixed set) | O(1) |
| 2 | Coin toss simulation | Monte Carlo | O(N) | O(1) |
| 3 | Bubble sort analysis | Adaptive bubble sort | O(n) best / O(n²) worst | O(1) |
| 4 | Towers of Hanoi | Recursive divide & conquer | O(2ⁿ) | O(n) |
| 5 | Partition point | Binary search | O(log n) | O(1) |
| 6 | Element uniqueness | Sort + scan | O(n log n) | O(1) |

---

## 🛠️ How to Run

```bash
git clone <your-repo-url>
cd DAA_Lab01
gcc -Wall -O2 Q1_order_of_growth/q1_order_of_growth.c -o q1 -lm && ./q1
gcc -Wall -O2 Q2_fair_biased_coin/q2_coin_simulation.c -o q2 && ./q2
gcc -Wall -O2 Q3_bubble_sort_analysis/q3_bubble_sort.c -o q3 && ./q3 > q3_results.csv
gcc -Wall -O2 Q4_towers_of_hanoi/q4_towers_of_hanoi.c -o q4 && ./q4
gcc -Wall -O2 Q5_partition_point/q5_partition_point.c -o q5 && ./q5
gcc -Wall -O2 Q6_element_uniqueness/q6_element_uniqueness.c -o q6 && ./q6 > q6_results.csv
```

For Q3 and Q4, redirect stdout to CSV and plot `n` vs. the relevant column in Excel, Python (matplotlib), or gnuplot to visualize growth trends.
