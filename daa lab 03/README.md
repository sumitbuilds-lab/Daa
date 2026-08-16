# Divide and Conquer Assignment

## Questions

1. Binary vs Ternary Search
2. Search the Defective Coin
3. Max and Min using Divide & Conquer
4. Matrix Multiplication using Strassen's Method
5. Special-Pattern Matrix Multiplication
6. Loop Invariants in Sorting

### Q1 Graph Validation

`Q1_Binary_vs_Ternary_Search.c` counts the comparisons made by both
search algorithms.

`plot_search_comparisons.py` generates a comparison graph.

Run:

```bash
gcc Q1_Binary_vs_Ternary_Search.c -o q1
./q1
```

Then collect comparison counts for different input sizes and put them
into `plot_search_comparisons.py`.

The graph should show that Binary Search generally requires fewer
comparisons than Ternary Search.

The included PNG is an illustrative graph. For a lab report, replace
the example values with measurements from your own C implementation.
