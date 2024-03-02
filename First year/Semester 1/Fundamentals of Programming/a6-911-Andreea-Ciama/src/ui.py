from functions import *
from tests import tests

def print_all_expenses (expenses):
    for index in range(len(expenses)):
        print("Number of apartment:", get_apartment(expenses[index]), ", amount:", get_amount(expenses[index]), ", type:", get_types(expenses[index]), sep='')


def print_all_expenses_for_an_apartment(expenses, number_of_apartment):
    for index in range(len(expenses)):
        if int(get_apartment(expenses[index])) == int(number_of_apartment):
            print("Number of apartment:", get_apartment(expenses[index]), ", amount:", get_amount(expenses[index]), ", type:", get_types(expenses[index]), sep='')


def ui_list(expenses, *list_of_commands):
    """
    It prints all the dictionary if the given instruction is "list"
    It prints all expenses for a given apartment if the given instruction is "list <apartment>"
    It prints all apartments having total expenses "</=/>" than an amount ( instruction is: list [ < | = | > ] <amount> )
    :param expenses: list
    :param *list_of_commands: tuple
    :return: none
    """
    list_of_commands = list(list_of_commands)    # convert from tuple to list
    if len(list_of_commands) == 0:
        print_all_expenses(expenses)
        return

    if len(list_of_commands) == 1:
        number_of_apartment = list_of_commands[0]
        print_all_expenses_for_an_apartment(expenses, number_of_apartment)
        return

    sorted_list_of_expenses = sort_expenses_by_number_of_apartment(expenses)    # it sorts the old dictionary by number of apartments in an ascending order and now it's a list
    given_amount = int(list_of_commands[1])

    for index in range(len(sorted_list_of_expenses)):
        if index != len(sorted_list_of_expenses)-1:
            next_list_of_expenses = sorted_list_of_expenses[index+1]
        else:
            next_list_of_expenses = sorted_list_of_expenses[index]
        if (get_apartment(sorted_list_of_expenses[index]) != get_apartment(next_list_of_expenses) and index < len(sorted_list_of_expenses))\
            or index == (len(sorted_list_of_expenses)-1):
            sum_for_an_apartment = sum_of_all_expenses_for_an_apartment(expenses, get_apartment(sorted_list_of_expenses[index]))
            if list_of_commands[0] == "<":
                if sum_for_an_apartment < given_amount:
                    print(get_apartment(sorted_list_of_expenses[index]))

            elif list_of_commands[0] == "=":
                if sum_for_an_apartment == given_amount:
                    print(get_apartment(sorted_list_of_expenses[index]))
            else:
                if sum_for_an_apartment > given_amount:
                    print(get_apartment(sorted_list_of_expenses[index]))
    return


def get_command_and_list(command_line):
    position = command_line.find(' ')
    if position == -1:
        return command_line, []
    command = command_line[:position]
    list_of_commands = command_line[position:]
    list_of_commands = list_of_commands.split(' ')
    list_of_commands = [elements.strip() for elements in list_of_commands]    # now is a list
    del list_of_commands[0]    # the first element is ''
    return command, list_of_commands


def print_commands(commands):
    """
    It prints all the commands ( add, remove, replace, list, exit )
    :param commands: dictionary
    :return: none
    """
    print(*list(commands.keys()), 'exit', sep='\n')


def run_command():

    commands = {'add': add, 'remove': remove, 'replace': replace, 'list': ui_list}
    expenses = initial_list()
    tests()
    while True:
        print_commands(commands)
        command_line = input("Enter command line: ")
        if command_line == "exit":
            break
        command, list_of_commands = get_command_and_list(command_line)
        try:
            commands[command](expenses, *list_of_commands)
        except KeyError:
            print("This option is not implemented yet!")
        except ValueError as ve:
            print("The following exception was:", ve)