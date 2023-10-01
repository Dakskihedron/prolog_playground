import math


def is_prime(p):
    """Trail division algorithm."""
    if p < 2 or (p % 2 == 0 and p != 2):
        return False
    s = math.floor(math.sqrt(p))
    for i in range(3, s + 1, 2):
        if p % i == 0:
            return False
    return True


if __name__ == "__main__":
    for i in range(-1, 6):
        print(i, is_prime(i))
