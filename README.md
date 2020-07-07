# PS07: Designing a dictionary

Complete the implementation of the `Dictionary` data structure without using built-in set or dict.

The `Dictionary` class must expose the following methods.
* `Dictionary()` constructor that takes no arguments.
* `set(k, v)` sets the item with key `k` to the value `v`.
* `get(k)` returns the value of item with key `k` if exist, else returns -1.
* `remove(k)` removes the item with key `k` from the dictionary if exist, else do nothing.

Remember that dictionary operations must be *efficient* in space and time.

The following is a usage example of the `Dictionary` class:

```python
data = Dictionary()
data.set(1, 1)
data.set(2, 1)
data.set(3, 3)
data.get(2)  # Returns 1
data.get(4)  # Returns -1
data.set(3, 5)
data.set(3, 2)
data.get(3)  # Returns 2
data.remove(1)
data.get(1)  # Returns -1
```

**Constraints**

Your dictionary is expected to:
* Support up to 10^5 operations
* Keys and values are integers in the range [0, 10^9]

# How to submit.

* Implement the methods listed above under `solution.py`.
* All code will be checked for readability using [**pylint**](https://www.pylint.org/).
* A grader is included, and all test cases must pass.
* ***DO NOT** modify the grader!*
* ***DO NOT** use built-in set or dict!*

# Debugging

* You can run the grader with the command `python3 grader.py < test_cases/a.txt` where `a` is the test case you want to run.
* Yo can run all test cases with the command: `for f in test_cases/*.txt; do python3 grader.py < "$f"; done`