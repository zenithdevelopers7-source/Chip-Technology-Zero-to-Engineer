# Day 009 — Review Questions

1. Which gate calculates the SUM output?
2. Which gate calculates CARRY?
3. What are SUM and CARRY when A=1 and B=1?
4. What does the two-bit binary result `10` mean in decimal?
5. Why can a half adder not add a carry-in?

## Practical Challenge

Inside `practical.py`, define:

```python
def add_bits_as_integer(a, b):
    sum_bit, carry = half_adder(a, b)
    return carry * 2 + sum_bit
```

Add tests for all four input pairs. Do not paste Python function definitions
directly into the Bash prompt.

## Next Lesson

Day 010 — Full Adder and Carry-In
