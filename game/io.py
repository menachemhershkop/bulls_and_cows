from game.validate import is_valid_guess


def prompt_guess(length: int) -> str:
    # user_guess=is_valid_guess(input(f'Enter a number in {length} digit: '),length)
    user_guess=input("Enter number: ")
    if is_valid_guess(user_guess,length)[0]:

        return user_guess
    else:
        print("Try agin")

def print_feedback(guess: str, bulls: int, cows: int) -> None:
    print(f'Your guess is  {guess}, you have {bulls} bolls and {cows} cows. Keep trying')
def print_status(state: dict) -> None:
    print(f'History of guess {state['history']}. You try {state["tres_used"]}')
def print_result(state: dict) -> None:
    print(f'Done: You won. The secret number is {state['secret']}')
