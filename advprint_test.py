from advprint import adv_print


def fib_iter():
    yield from (0, 1)
    n2 = 0
    n1 = 1
    while True:
        n0 = n1 + n2
        n1, n2 = n0, n1
        yield n0


LOREM_IPSUM = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod
incididut ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis
nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu
fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in
culpa qui officia deserunt mollit anim id est laborum ut et
"""

FIBNUMS_100 = [n for _, n in zip(range(100), fib_iter())]

with open("ipsum.txt", "w", encoding="utf-8") as in_file:
    adv_print(*LOREM_IPSUM.split(),
              start="-->\n",
              end="\n<--\n\n",
              max_line=80,
              in_file=in_file)

adv_print(*FIBNUMS_100,
          start="[",
          end="]",
          sep=", ",
          max_line=60)
