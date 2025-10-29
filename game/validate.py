def is_valid_guess(guess: str, length: int, *, unique_digits: bool = True) -> tuple[bool, str]:
    if (len(guess))!=length:
        return False, "Length is incorrect"
    if not int(guess):
        return False ,"Number only"
    if len(set(guess)) == length:
        return True, "God guess"


def is_new_guess(guess: str, history: set[str]) -> bool:
    return guess in history


