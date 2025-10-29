def score_guess(secret: str, guess: str) -> tuple[int, int]:
    bulls=0
    cows=0

    for i in range(len(secret)):
        print("guess", guess[i])
        if guess[i]== secret[i]:
            bulls+=1
        elif guess[i] in secret:
            cows+=1
    return  bulls, cows
def is_won(bulls: int, length: int) -> bool:
    return bulls==length
def init_state(secret: str, length: int, max_tries: int | None, unique_digits: bool, allow_leading_zero: bool) -> dict:
    return  {
  "secret": secret,
  "length": length,
  "max_tries": max_tries,
  "tries_used": 0,
  "unique_digits": unique_digits,
  "allow_leading_zero": allow_leading_zero,
  "history": [],
  "seen": set()
}

def apply_guess(state: dict, guess: str) -> tuple[int, int]:
    bulls, cows = (score_guess(state["secret"],guess))
    print(state['history'])
    state['history'].append([guess, bulls, cows])
    state['tries_used']+=1
    state['seen'].add(guess)
    return bulls,cows
