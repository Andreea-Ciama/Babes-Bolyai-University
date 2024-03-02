# Determine the product p of all the proper factors of n

def get_divisors_sum(number) -> int:
    """
    purpose -> Get the product of all the proper factors of a give number
    :param number -> The number on which the product of all the proper factors will be built
    :return -> product of all the proper factors of a give number as parameter
    """
    divisors = 1
    for i in range(2, number - 1):
        if (number % i) == 0:
            divisors = divisors * i
    return divisors


if __name__ == '__main__':
    number = int(input("n= "))
    result = get_divisors_sum(number)
    if result != 1:
        print(result)
    else:
        print("The number don't have proper factors")

