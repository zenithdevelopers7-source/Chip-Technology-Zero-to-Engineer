# Day 007 — Review Questions

1. What is a truth table?
2. What is AND(1, 0)?
3. What is OR(0, 1)?
4. What is NOT(0)?
5. Which of the three gates needs only one input?
6. How do logic gates relate to transistors?

## Practical Challenge

Build a NAND gate in `practical.py` using the existing functions:

```python
def nand_gate(a, b):
    return not_gate(and_gate(a, b))
```

Predict its four outputs for 00, 01, 10, and 11.
Add assertions to test your prediction.

## Next Lesson

Day 008 — NAND, NOR, XOR, and XNOR Gates
