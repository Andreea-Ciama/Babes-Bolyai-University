from domain import *

def add_warehouse(warehouse_list,parameters):
    """
    We add a warehouse in the list
    :param warehouse_list: the list
    :param parameters: a list with name,price and quantity
    :return:
    """
    if len(parameters)!=3:
        raise ValueError("we need to have 3 parameters")
    if int(parameters[1])<0:
        raise ValueError("the price needs to be positive")
    if int(parameters[2])<0:
        raise ValueError("the quantity needs to be positive")
    if unique_name(warehouse_list,parameters[0]):
        raise ValueError("We already have this warehouse")
    warehouse_list.append(create_warerhouse(parameters[0],parameters[1],parameters[2]))

def unique_name(warehouse_list,name):
    for i in range(len(warehouse_list)):
        if name==get_name(warehouse_list[i]):
            return True
    return False

def remove_warehouse(warehouse_list,name):
    """
    We remove a warehouse from the list
    :param warehouse_list: the list
    :param name: the name of the warehouse we want to delete
    :return:
    """
    for i in range(len(warehouse_list)):
        if name==get_name(warehouse_list[i]):
            warehouse_list.remove(warehouse_list[i])

def interchange(warehouse_list,i,j):
    a=warehouse_list[i]
    warehouse_list[i]=warehouse_list[j]
    warehouse_list[j]=a

def list_all(warehouse_list):
    for i in range(len(warehouse_list)):
        for j in range(len(warehouse_list)):
            if get_name(warehouse_list[i]) > get_name(warehouse_list[j]):
                interchange(warehouse_list,i,j)


def list_total(warehouse_list):
    sum=0
    s=0
    for i in range(len(warehouse_list)):
        s=get_price(warehouse_list[i]) * get_quantity(warehouse_list[i])
        sum=sum+s
        s=0
    return sum