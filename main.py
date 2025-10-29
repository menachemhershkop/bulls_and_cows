from wsgiref.util import guess_scheme

from game.io import prompt_guess, print_feedback, print_result
from game.logic import score_guess, apply_guess, init_state
from game.secret import generate_secret
def play(length: int = 4, max_tries: int | None = 12, *, unique_digits: bool = True, allow_leading_zero: bool = False) -> None:
    secret_number=generate_secret()
    state = init_state(secret_number, 4, 20, True, True)
    while True:
        guess=prompt_guess(length)
        if guess:

            apply_guess(state,guess)

            bulls, cows = score_guess(state['secret'], guess)
            print_feedback(guess,bulls,cows)
            if bulls == state['length']:
                print_result(state)
                break



if __name__=="__main__":
    play()