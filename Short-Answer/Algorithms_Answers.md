#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)
```python
    a = 0 # O(1)
    while (a < n * n * n): # O(n^3)
      a = a + n * n # O(1)
```
O(n^3)

b)
```
    sum = 0 # O(1)
    for i in range(n): # O(n)
      j = 1 # O(1)
      while j < n: # O(n)
        j *= 2 # O(1)
        sum += 1 # O(1)
```
# O(n * n) => O(n^2)
c)
```
    def bunnyEars(bunnies):
      if bunnies == 0: # O(1)
        return 0 # O(1)

      return 2 + bunnyEars(bunnies-1) # O(n)
```
O(n)
## Exercise II
There is n floors
1. m = n / 2
2. Drop an egg from floor m
3. If egg was broken:
  4. o = 3 / 2 * m
5. Else:
  6. o = m / 2
7. If o - m == 1:
  8. Drop an egg
    9. If egg was broken:
      10. f = o - 1
      11. If f < 0:
        12. Floor can't be found
    12. Else:
      f = o
13. Else if o - m == -1:
  14. Drop an egg
    15. If egg was broken:
      16. f = o + 1
      17. If f > o:
        18. f = n
    19. Else:
      20. f = o
21. If f found:
  22. Return
23. Go to 2
