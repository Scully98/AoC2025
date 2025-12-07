from typing import List

def load_lines(path: str) -> List[List[int]]:
    with open(path, "r", encoding="utf-8") as f:
        return [[ord(ch)-48 for ch in line.rstrip("\n")] for line in f]

def max_joltage(line: List[int]) -> int:
    best_right = line[-1]  # beste Einerstelle rechts
    best = -1
    for i in range(len(line) - 2, -1, -1):
        best = max(best, 10 * line[i] + best_right)
        best_right = max(best_right, line[i])
    return best

if __name__ == "__main__":
    banks = load_lines("Day03-Input.txt")
    total = sum(max_joltage(line) for line in banks)
    print(total)
    