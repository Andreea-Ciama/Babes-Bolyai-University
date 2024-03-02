def create_expenses(apartment, amount, types):
    return {'number_of_apartment': apartment, 'amount': amount, 'type': types}


def get_apartment(expenses):
    return expenses['number_of_apartment']


def get_amount(expenses):
    return expenses['amount']


def get_types(expenses):
    return expenses['type']


def set_apartment(expenses, number_of_apartment):
    expenses['number_of_apartment'] = number_of_apartment


def set_amount(expenses, amount):
    expenses['amount'] = amount


def set_type(expenses, types):
    expenses['type'] = types

def check_type(types):
    """
    It checks if the given type is one from the predefined categories: from one of the predefined categories water, heating, electricity, gas and other
    :param types: string
    :return: True or False
    """
    types = types.lower()
    if types == "water" or types == "heating" or types == "electricity" or types == "gas" or types == "other":
        return True
    return False


def add_expenses(expenses, apartment, amount, types):
    """
    It adds to the expenses list the apartment, amount and the types
    :param expenses: list
    :param apartment: positive integer
    :param amount: positive integer
    :param types: string
    :return none:
    """
    person = create_expenses(apartment, amount, types)
    expenses.append(person)


def sort_expenses_by_number_of_apartment(expenses):
    """
    It sorts the expenses list by the number of apartment.
    :param expenses: list
    :return: none
    """
    return sorted(expenses, key=lambda x: x['number_of_apartment'])


def find_apartment(expenses, number_of_apartment):
    """
    It checks if the given apartment is in the expenses.
    :param expenses: list
    :param number_of_apartment: positive integer
    :return: False or True
    """
    for index in range(len(expenses)):
        if get_apartment(expenses[index]) == number_of_apartment:
            return True
    return False


def sum_of_all_expenses_for_an_apartment(expenses, number_of_apartment):
    """
    It computes the sum of all expenses for a given apartment.
    :param expenses: list
    :param number_of_apartment: string
    :return: the sum
    """
    number_of_apartment = int(number_of_apartment)
    sum = 0
    for index in range(len(expenses)):
        element_from_dictionary = expenses[index]
        if int(get_apartment(element_from_dictionary)) == number_of_apartment:
            sum += int(get_amount(element_from_dictionary))
    return sum


def add(expenses, *list_of_commands):
    """
    It checks if the input is correct ( add <number of apartment> <type> <amount> ) and if it is, the function will add the input in expenses by using function add_expenses
    :param expenses: list
    :param *list_of_commands: a tuple read from keyboard.
    :return: none
    """
    list_of_commands = list(list_of_commands)   # convert from tuple to list
    if len(list_of_commands) != 3:
        raise ValueError("Invalid input: you need to insert 3 arguments: <number of apartment> <type> <amount>.")
    number_of_apartment = list_of_commands[0]
    types = list_of_commands[1]
    amount = list_of_commands[2]
    if check_type(types) == False:
        raise ValueError("Invalid input: you have to choose the type from one of the predefined categories: water, heating, electricity, gas and other.")
    if number_of_apartment.isdigit() == False:
        raise ValueError("Invalid input: you have to choose a positive integer for the number of apartment.")
    if amount.isdigit() == False:
        raise ValueError("Invalid input: you have to choose a positive integer for amount.")
    add_expenses(expenses, number_of_apartment, amount, types)


def initial_list():
    return [create_expenses(10, 20, "gas"),
            create_expenses(11, 153, "other"),
            create_expenses(13, 30, "electricity"),
            create_expenses(12, 80, "water"),
            create_expenses(11, 40, "gas"),
            create_expenses(13, 91, "heating"),
            create_expenses(15, 50, "water"),
            create_expenses(10, 80, "other"),
            create_expenses(16, 60, "electricity"),
            create_expenses(10, 70, "heating")]


def remove(expenses, *list_of_commands):
    """
    It checks if the input is valid ( remove <apartment>
                                      remove <start apartment> to <end apartment>
                                      remove <type> ) and if it is, then it removes from expenses the apartment or
                                      the type or the apartments from a start to an end.
    :param expenses: list
    :param *list_of_commands: tuple
    :return: none
    """
    list_of_commands = list(list_of_commands)   # convert from tuple to list
    if len(list_of_commands) > 3:
        raise ValueError("Invalid input: you can insert maximum 3 arguments")
    if len(list_of_commands) == 1:
        given_type = -1
        given_number_of_apartment = -1
        if check_type(list_of_commands[0]) == True:   # this is the case: remove <type> gas
            given_type = list_of_commands[0]
        else:
            given_number_of_apartment = int(list_of_commands[0])   # this is the case: remove <apartment>
        index = 0
        length_of_expenses = len(expenses)

        if given_number_of_apartment == -1:   # this is the: remove <type>
            while index < length_of_expenses:
                if get_types(expenses[index]) == given_type:
                    del expenses[index]
                    index -= 1
                    length_of_expenses -= 1
                index += 1
        else:   # for case: remove <apartment>
            while index < length_of_expenses:
                if int(get_apartment(expenses[index])) == given_number_of_apartment:
                    del expenses[index]
                    index -= 1
                    length_of_expenses -= 1
                index += 1
        return

    else:    # This is for case from <start_apartment> to <end_apartment>
        start_apartment = int(list_of_commands[0])
        end_apartment = int(list_of_commands[2])
        if end_apartment < start_apartment:
            raise ValueError("Input error: <start apartment> is greater than <end apartment>.")
        index = 0
        length_of_expenses = len(expenses)
        while index < length_of_expenses:
            if int(get_apartment(expenses[index])) >= start_apartment and \
                    int(get_apartment(expenses[index])) <= end_apartment:
                del expenses[index]
                index -= 1
                length_of_expenses -= 1
            index += 1
        return


def replace(expenses, *list_of_commands):
    """
    It checks if the input is correct ( replace <apartment> <type> with <amount> ) and it removes the expenses from that apartment, type;
     and it adds the new one with the given parameters
    :param expenses: dictionary
    :param *list_of_commands: tuple
    :return: none
    """
    if len(list_of_commands) != 4:
        raise ValueError("Invalid input: you can insert only 4 arguments: replace <apartment> <type> with <amount>")
    list_of_commands = list(list_of_commands)
    given_type = list_of_commands[1]

    if check_type(given_type) == False:
        raise ValueError("Invalid input: you have to choose the type from one of the predefined categories: water, heating, electricity, gas and other.")
    if list_of_commands[0].isdigit() == False:
        raise ValueError("Invalid input: you have to choose a positive integer for the number of apartment.")
    if list_of_commands[3].isdigit() == False:
        raise ValueError("Invalid input: you have to choose a positive integer for amount.")
    number_of_apartment = int(list_of_commands[0])
    if find_apartment(expenses,number_of_apartment) == False:
        raise ValueError("Invalid input: the given number of apartment is not found!")
    given_amount = int(list_of_commands[3])

    index = 0
    length_of_expenses = len(expenses)
    while index < length_of_expenses:
        if int(get_apartment(expenses[index])) == number_of_apartment and \
                get_types(expenses[index]) == given_type and \
                int(get_amount(expenses[index])) != given_amount:
            set_amount(expenses[index], given_amount)
            index -= 1
        index += 1

    return