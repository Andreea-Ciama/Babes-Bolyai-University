from functions import*

def test():
    warehouse_list = [create_warerhouse("Best_Napkins_100", "12", "100")]
    assert len(warehouse_list)==1
    name='sfd'
    price='34'
    quantity='345'
    parameters=[name,price,quantity]
    add_warehouse(warehouse_list,parameters)
    assert len(warehouse_list)==2
    remove_warehouse(warehouse_list,name)
    assert len(warehouse_list) == 1