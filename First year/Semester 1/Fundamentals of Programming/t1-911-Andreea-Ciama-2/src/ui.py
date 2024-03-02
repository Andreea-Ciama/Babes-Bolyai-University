from domain import *
from functions import *
from tests import *


def add_ui_warehouse(warehouse_list):
    name = input("name:")
    quantity = int(input("quantity: "))
    price = int(input("price: "))
    parameters = [name, price, quantity]
    add_warehouse(warehouse_list, parameters)


def remove_ui_warehouse(warehouse_list):
    name = input("name: ")
    remove_warehouse(warehouse_list, name)


def list_all_ui(warehouse_list):
    list_all(warehouse_list)
    for i in range(len(warehouse_list)):
        print("Name " + get_name(warehouse_list[i]) + " Price " + get_price(
            warehouse_list[i]) + " Quantity" + get_quantity(
            warehouse_list[i]))


def list_total_ui(warehouse_list):
    print(list_total(warehouse_list))


def menu():
    print("Choose one:")
    print("add")
    print("remove")
    print("list all")
    print("list total")
    print("exit")


def start():
    menu()
    warehouse_list = [create_warerhouse("Best_Napkins_100", "12", "100")]
    while True:

        n = input(">>")
        if n == 'add':
            add_ui_warehouse(warehouse_list)
        if n == 'remove':
            remove_ui_warehouse(warehouse_list)
        if n == "list all":
            list_all_ui(warehouse_list)
        if n == "list total":
            list_total_ui(warehouse_list)
        if n == 'exit':
            break


start()
test()
