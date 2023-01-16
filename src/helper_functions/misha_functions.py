
def my_new_function(
        a: int = 0,
        b: float = 0.0,
        c: str = ''
) -> list:
    return [a, b, c]


def my_sum(a: int, b: int) -> int:
    return a + b


def my_multiply(a: int, b: int) -> int:
    return a * b


if __name__ == '__main__':

    print(type(my_new_function(a=4, b=4.5, c='qwerty')))
