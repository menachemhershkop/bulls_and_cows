import random
def generate_secret(length: int = 4, *, unique_digits: bool = True, allow_leading_zero: bool = False, rng: random.Random | None =  None) -> str:
    secret_number=""
    for i in range(length):
        if not allow_leading_zero:
            if unique_digits:
                number=random.randint(1,9)
                secret_number+=str(number)
    return secret_number
