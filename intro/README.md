# Some notes

- `float` in Python is the same as the `double` type in C language as it is represented as double precision using IEEE 754
- `str.rfind()` and `str.rindex()` are the same, but `rfind()` returns `-1` if the target substring is not found, while `rindex()` throws an exception.
- Strings in Python are **immutable**
- Operations on strings create an entirely new string each time

## Answers to some exercises

- **Exercise 1.12:** We saw that `bool("False")` is `True` because `"False"` has numerical equivalent, if we add all the ASCII values of each letter. You can try this with any strings, even with `bool("0")` because character `"0"` is `48` in ASCII[^1].

[^1]: https://www.cs.cmu.edu/~pattis/15-1XX/common/handouts/ascii.html
