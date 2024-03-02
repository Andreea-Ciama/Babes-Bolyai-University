def create_expenses(apartament, amound, types):
    return {"number_of_apartament": apartament, "amound": amound, "types": types}

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

def check_type(types):
    """
    It checks if the given type is one from the predefined categories: from one of the predefined categories water, heating, electricity, gas and other
    :param types: string
    :return: True or False
    """

    if types == "water" or types == "heating" or types == "electricity" or types == "gas" or types == "other":
        return True
    return False
