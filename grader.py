"""PS05 Grader."""

import sys

from solution import Dictionary


if __name__ == '__main__':
    name, n = input(), int(input())
    got, want, ops = [None] * n, [None] * n, [None] * n
    ans, sol = dict(), Dictionary()
    for i in range(n):
        l = input().split(' ')
        op, k = l[0], int(l[1])
        if l[0] == 'S':
            v = int(l[2])
            ans[k] = v
            want[i], got[i] = None, sol.set(k, v)
            ops[i] = f'set({k}, {v})'
        elif l[0] == 'G':
            want[i], got[i] = ans.get(k, -1), sol.get(k)
            ops[i] = f'get({k})'
        else:
            if ans.get(k, None):
                del ans[k]
            want[i], got[i] = None, sol.remove(k)
            ops[i] = f'remove({k})'

    if got != want:
        print(f"\t❌ Test case #{name} failed")
        if n < 50:
            print(f"\t\tOps:\t{ops}")
            print(f"\t\tGot:\t{got}")
            print(f"\t\tWant:\t{want}")
        sys.exit(1)
    print(f"\t✅ Test case accepted #{name}")
