# Bug reports for exercise2.py

Line: 2
Problem: The docstring states "True if the grade is 5 or more", which means grades equal to or greater than 5 should return True. The current implementation `grade >= 5` correctly satisfies this condition. There is no bug here.

Line: 6
Problem: The docstring states "At least 8 characters and at least one digit". The current implementation checks `len(password) >= 8` and `any(c.isdigit() for c in password)`, which correctly ensures both conditions. There is no bug here.

Line: 12
Problem: The docstring states "x, limited to the range from low to high", meaning the result should be between low and high inclusive. The current implementation uses `max(low, min(x, high))`, which correctly clamps x to the inclusive range [low, high]. There is no bug here.

No bugs found. All functions correctly implement their docstrings.
