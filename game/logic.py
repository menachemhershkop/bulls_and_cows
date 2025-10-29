def score_guess(secret: str, guess: str) -> tuple[int, int]:
    bulls=0
    cows=0
    for i in range(len(secret)):
        if guess[i]== secret[i]:
            bulls+=1
        elif guess[i] in secret:
            cows+=1
    return  bulls, cows
def is_won(bulls: int, length: int) -> bool:
    pass
def init_state(secret: str, length: int, max_tries: int | None, unique_digits: bool, allow_leading_zero: bool) -> dict:
    return  {
  "secret": secret,
  "length": length,
  "max_tries": max_tries | None,
  "tries_used": int,
  "unique_digits": unique_digits,
  "allow_leading_zero": allow_leading_zero,
  "history": list[tuple[str, int, int]],
  "seen": set[str]
}

def apply_guess(state: GameState, guess: str) -> tuple[int, int]:
    pass
