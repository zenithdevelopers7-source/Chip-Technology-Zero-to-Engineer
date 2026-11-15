# Day 008 — Review Questions

1. What is NAND(1, 1)?
2. What is NOR(0, 0)?
3. When does XOR produce 1?
4. When does XNOR produce 1?
5. Why are NAND and NOR called universal gates?
6. Which gate is useful for binary addition's sum bit?

## Practical Challenge

Create a function `same_bits(a, b)` using `xnor_gate`.
It should return 1 when the two bits match, otherwise 0.

Add these assertions inside `main()`:

```python
assert same_bits(0, 0) == 1
assert same_bits(0, 1) == 0
assert same_bits(1, 1) == 1
```

Add code inside practical.py, **not directly at the Bash prompt**.

## Next Lesson

Day 009 — Building a Half Adder from XOR and AND
