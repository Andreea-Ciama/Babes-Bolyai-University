# Largest perfect number smaller than natural given number n

def get_divisors_sum(number):
    """
    purpose -> Get the sum of the divisors for a give number
    :param number -> The number on which the sum of the divisors will be built
    :return -> Sum of the divisors of a give number as parameter
    """
    divisors = [1]
    for i in range(2, number):
        if (number % i) == 0:
            divisors.append(i)
    return sum(divisors)


def resolve(given_number):
    """
    purpose -> Recursively check if a number is perfect starting from the given number
    :param given_number:
    :return: -1 -> If no perfect number was found that is smaller than the parameter
            number -> If succes in finding the largest smallest number given as parameter was achieved
    """
    if given_number <= 0:
        return -1
    else:
        divisors_sum = get_divisors_sum(given_number)
        if divisors_sum == given_number:
            return given_number
    return resolve(given_number - 1)


if __name__ == '__main__':
    number = int(input("Give here the number to be checked >>"))
    result = resolve(number)
    if result != -1:
        print(result)
    else:
        print("I didn't found any number to match the problem!")

