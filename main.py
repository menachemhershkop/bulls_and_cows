from game.io import prompt_guess
from game.logic import score_guess, apply_guess, init_state
from game.secret import generate_secret
def play(length: int = 4, max_tries: int | None = 12, *, unique_digits: bool = True, allow_leading_zero: bool = False) -> None:
    secret_number=generate_secret()

    while True:
        guess=prompt_guess(length)


if __name__=="__main__":
    print(apply_guess(init_state("1234",4,5,True,True),"1234"))
