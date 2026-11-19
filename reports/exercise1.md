# Bug reports for exercise1.py

Line: 3
Problem: The function `is_even(n)` returns `True` when `n % 2 == 1`, which means it returns `True` for odd numbers, contradicting the docstring that states "true for even numbers". It should return `True` when `n % 2 == 0`.
Example: is_even(4) → returns False (wrong), should return True; is_even(3) → returns True (wrong), should return False
Fix: return n % 2 == 0

Line: 8
Problem: The function `rectangle_area(width, height)` returns the sum of width and height, but the docstring states "area of a rectangle", which should be width multiplied by height, not added.
Example: rectangle_area(4, 5) → returns 9 (wrong), should return 20
Fix: return width * height

Line: 13
Problem: The function `double(n)` is described as "twice the number n", but it returns `n + 2`, which is not twice the number. It should return `n * 2`.
Example: double(5) → returns 7 (wrong), should return 10
Fix: return n * 2
