def read_moves(path: str) -> list[tuple[str, int]]:
    moves: list[tuple[str, int]] = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            s = line.strip()
            if not s:
                continue
            moves.append((s[0], int(s[1:])))
    return moves

def count_zero_crossings(moves: list[tuple[str, int]]) -> int:
 
    pos = 50
    hits = 0
    MOD = 100

    for direction, n in moves:
        print(direction)
        print(n)
        print(hits)
        if direction == "R":
            first = (MOD - pos) % MOD
            if first == 0:
                first = MOD
            if n >= first:
                hits += 1 + (n - first) // MOD
            pos = (pos + n) % MOD

        elif direction == "L":
            first = pos if pos != 0 else MOD
            if n >= first:
                hits += 1 + (n - first) // MOD
            pos = (pos - n) % MOD
        else:
            raise ValueError(f"Unbekannte Richtung: {direction!r}")

    return hits       


if __name__ == "__main__":
    moves = read_moves("Day01-Input.txt")
    print(count_zero_crossings(moves))
    

    
