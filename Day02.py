
from pathlib import Path
from typing import List, Tuple
import re


def load_ranges(path: str | Path) -> List[Tuple[int, int]]:
    """Return the ranges stored as 'start-end' pairs separated by commas."""
    raw_text = Path(path).read_text(encoding="utf-8").strip()
    ranges: List[Tuple[int, int]] = []
    for token in raw_text.split(","):
        if not token:
            continue
        start_str, end_str = token.split("-", maxsplit=1)
        ranges.append((int(start_str), int(end_str)))
    return ranges

def is_invalid(n: int) -> bool:
    s = str(n)
    if len(s) % 2 == 1:
        return False
    half = len(s) // 2
    return s[:half] == s[half:]

def is_invalid02(n: int) -> bool:
    s = str(n)
    L = len(s)

    for d in range(1, L // 2 + 1):
        if L % d != 0:
            continue
        block = s[:d]
        if block * (L // d) == s:
            return False
    return True

def sum_invalid_bruteforce_pairs_02(pairs) -> int:
    total = 0
    for a, b in pairs:
        for n in range(a, b + 1):
            if not is_invalid02(n):
                total += n
    return total

def sum_invalid_bruteforce_pairs(pairs) -> int:
    total = 0
    for a, b in pairs:
        for n in range(a, b + 1):
            if is_invalid(n):
                total += n
    return total


if __name__ == "__main__":
    print(load_ranges("Day02-Input.txt"))
    ranges = load_ranges("Day02-Input.txt")
    total = sum_invalid_bruteforce_pairs_02(ranges)
    print(total)
