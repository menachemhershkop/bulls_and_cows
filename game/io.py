def prompt_guess(length: int) -> str:
    user_guses=input(f'Enter a number in {length} digit: ')
    return user_guses
def print_feedback(guess: str, bulls: int, cows: int) -> None:
    print(f'Your guess is  {guess}, you have {bulls} bolls and {cows} cows. Keep trying')
def print_status(state: dict) -> None:
    print(f'History of guess {state['history']}. You try {state["tres_used"]}')
def print_result(state: dict, won: bool) -> None:
    print(f'Done: You {won}. The secret number is {state['secret']}')