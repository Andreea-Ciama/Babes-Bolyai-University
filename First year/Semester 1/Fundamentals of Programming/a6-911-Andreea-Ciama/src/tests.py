from functions import *

def tests_add():
    test_expenses = []
    add(test_expenses, ('15'), ('gas'), ('200'))
    assert test_expenses == [create_expenses('15','200','gas')]
    add(test_expenses, ('17'), ('gas'), ('200'))
    assert test_expenses == [create_expenses('15','200','gas'), create_expenses('17', '200', 'gas')]
    add(test_expenses, ('13'), ('water'), ('186'))
    assert test_expenses == [create_expenses('15','200','gas'), create_expenses('17', '200', 'gas'), create_expenses('13', '186', 'water')]
    add(test_expenses, ('12'), ('heating'), ('1385'))
    assert test_expenses == [create_expenses('15','200','gas'), create_expenses('17', '200', 'gas'), create_expenses('13', '186', 'water'), create_expenses('12','1385','heating')]
    add(test_expenses, ('10'), ('other'), ('2654'))
    assert test_expenses == [create_expenses('15','200','gas'), create_expenses('17', '200', 'gas'), create_expenses('13', '186', 'water'), create_expenses('12','1385','heating'),
                             create_expenses('10','2654','other')]
    add(test_expenses, ('16'), ('electricity'), ('6548'))
    assert test_expenses == [create_expenses('15','200','gas'), create_expenses('17', '200', 'gas'), create_expenses('13', '186', 'water'), create_expenses('12','1385','heating'),
                             create_expenses('10','2654','other'), create_expenses('16','6548','electricity')]
    add(test_expenses, ('685'), ('other'), ('3247'))
    assert test_expenses == [create_expenses('15','200','gas'), create_expenses('17', '200', 'gas'), create_expenses('13', '186', 'water'), create_expenses('12','1385','heating'),
                             create_expenses('10','2654','other'), create_expenses('16','6548','electricity'), create_expenses('685','3247','other')]
    add(test_expenses, ('13'), ('water'), ('87986'))
    assert test_expenses == [create_expenses('15','200','gas'), create_expenses('17', '200', 'gas'), create_expenses('13', '186', 'water'), create_expenses('12','1385','heating'),
                             create_expenses('10','2654','other'), create_expenses('16','6548','electricity'), create_expenses('685','3247','other'), create_expenses('13','87986','water')]


def test_check_type():
    assert check_type("water")
    assert check_type("heating")
    assert check_type("electricity")
    assert check_type("gas")
    assert check_type("other")
    assert check_type("asdf") == False
    assert check_type("gAs")
    assert check_type("heATIng")
    assert check_type("WATER")
    assert check_type("HEATing")
    assert check_type("ELecTRiciTY")
    assert check_type("gaz") == False
    assert check_type("type") == False
    assert check_type("0ther") == False
    assert check_type("Other")
    assert check_type("heat") == False
    assert check_type("electric") == False


def test_remove():
    expenses = [create_expenses(17, 19, "gas"),
            create_expenses(38, 34, "other"),
            create_expenses(16, 384, "electricity"),
            create_expenses(10, 1986, "water"),
            create_expenses(161, 6540, "gas"),
            create_expenses(618, 321, "heating"),
            create_expenses(156, 648, "water"),
            create_expenses(987, 213, "other"),
            create_expenses(10, 13, "electricity"),
            create_expenses(51, 7654, "other"),
            create_expenses(12, 16, "gas"),
            create_expenses(14, 168, "electricity"),
            create_expenses(16, 50, "heating"),
            create_expenses(13, 65, "water"),
            create_expenses(19, 561, "electricity")]

    remove(expenses, ('10'))
    assert [create_expenses(17, 19, "gas"),
            create_expenses(38, 34, "other"),
            create_expenses(16, 384, "electricity"),
            create_expenses(161, 6540, "gas"),
            create_expenses(618, 321, "heating"),
            create_expenses(156, 648, "water"),
            create_expenses(987, 213, "other"),
            create_expenses(51, 7654, "other"),
            create_expenses(12, 16, "gas"),
            create_expenses(14, 168, "electricity"),
            create_expenses(16, 50, "heating"),
            create_expenses(13, 65, "water"),
            create_expenses(19, 561, "electricity")] == expenses

    remove(expenses, ('160'), ('to'), ('1000'))
    assert [create_expenses(17, 19, "gas"),
            create_expenses(38, 34, "other"),
            create_expenses(16, 384, "electricity"),
            create_expenses(156, 648, "water"),
            create_expenses(51, 7654, "other"),
            create_expenses(12, 16, "gas"),
            create_expenses(14, 168, "electricity"),
            create_expenses(16, 50, "heating"),
            create_expenses(13, 65, "water"),
            create_expenses(19, 561, "electricity")] == expenses

    remove(expenses, ('electricity'))
    assert [create_expenses(17, 19, "gas"),
            create_expenses(38, 34, "other"),
            create_expenses(156, 648, "water"),
            create_expenses(51, 7654, "other"),
            create_expenses(12, 16, "gas"),
            create_expenses(16, 50, "heating"),
            create_expenses(13, 65, "water")] == expenses

    remove(expenses, ('12'))
    assert [create_expenses(17, 19, "gas"),
            create_expenses(38, 34, "other"),
            create_expenses(156, 648, "water"),
            create_expenses(51, 7654, "other"),
            create_expenses(16, 50, "heating"),
            create_expenses(13, 65, "water"),] == expenses

    remove(expenses,('12'),('to'),('30'))
    assert [create_expenses(38, 34, "other"),
            create_expenses(156, 648, "water"),
            create_expenses(51, 7654, "other")] == expenses

    remove(expenses,('other'))
    assert [create_expenses(156, 648, "water")] == expenses

    remove(expenses,('156'))
    assert [] == expenses


def test_replace():
    expenses = [create_expenses(17, 19, "gas"),
            create_expenses(38, 34, "other"),
            create_expenses(16, 384, "electricity"),
            create_expenses(10, 1986, "water"),
            create_expenses(161, 6540, "gas"),
            create_expenses(618, 321, "heating"),
            create_expenses(156, 648, "water"),
            create_expenses(987, 213, "other"),
            create_expenses(10, 13, "electricity"),
            create_expenses(51, 7654, "other"),
            create_expenses(12, 16, "gas"),
            create_expenses(14, 168, "electricity"),
            create_expenses(16, 50, "heating"),
            create_expenses(13, 65, "water"),
            create_expenses(19, 561, "electricity")]

    replace(expenses, '10','electricity','with','775')
    assert [create_expenses(17, 19, "gas"),
            create_expenses(38, 34, "other"),
            create_expenses(16, 384, "electricity"),
            create_expenses(10, 1986, "water"),
            create_expenses(161, 6540, "gas"),
            create_expenses(618, 321, "heating"),
            create_expenses(156, 648, "water"),
            create_expenses(987, 213, "other"),
            create_expenses(10, 775, "electricity"),
            create_expenses(51, 7654, "other"),
            create_expenses(12, 16, "gas"),
            create_expenses(14, 168, "electricity"),
            create_expenses(16, 50, "heating"),
            create_expenses(13, 65, "water"),
            create_expenses(19, 561, "electricity")] == expenses

    replace(expenses, '987','other','with','4312')
    assert [create_expenses(17, 19, "gas"),
            create_expenses(38, 34, "other"),
            create_expenses(16, 384, "electricity"),
            create_expenses(10, 1986, "water"),
            create_expenses(161, 6540, "gas"),
            create_expenses(618, 321, "heating"),
            create_expenses(156, 648, "water"),
            create_expenses(987, 4312, "other"),
            create_expenses(10, 775, "electricity"),
            create_expenses(51, 7654, "other"),
            create_expenses(12, 16, "gas"),
            create_expenses(14, 168, "electricity"),
            create_expenses(16, 50, "heating"),
            create_expenses(13, 65, "water"),
            create_expenses(19, 561, "electricity")] == expenses

    replace(expenses, '10', 'water', 'with', '65')
    assert [create_expenses(17, 19, "gas"),
            create_expenses(38, 34, "other"),
            create_expenses(16, 384, "electricity"),
            create_expenses(10, 65, "water"),
            create_expenses(161, 6540, "gas"),
            create_expenses(618, 321, "heating"),
            create_expenses(156, 648, "water"),
            create_expenses(987, 4312, "other"),
            create_expenses(10, 775, "electricity"),
            create_expenses(51, 7654, "other"),
            create_expenses(12, 16, "gas"),
            create_expenses(14, 168, "electricity"),
            create_expenses(16, 50, "heating"),
            create_expenses(13, 65, "water"),
            create_expenses(19, 561, "electricity")] == expenses

    replace(expenses, '161', 'gas', 'with', '79')
    assert [create_expenses(17, 19, "gas"),
            create_expenses(38, 34, "other"),
            create_expenses(16, 384, "electricity"),
            create_expenses(10, 65, "water"),
            create_expenses(161, 79, "gas"),
            create_expenses(618, 321, "heating"),
            create_expenses(156, 648, "water"),
            create_expenses(987, 4312, "other"),
            create_expenses(10, 775, "electricity"),
            create_expenses(51, 7654, "other"),
            create_expenses(12, 16, "gas"),
            create_expenses(14, 168, "electricity"),
            create_expenses(16, 50, "heating"),
            create_expenses(13, 65, "water"),
            create_expenses(19, 561, "electricity")] == expenses

    replace(expenses, '16', 'heating', 'with', '98')
    assert [create_expenses(17, 19, "gas"),
            create_expenses(38, 34, "other"),
            create_expenses(16, 384, "electricity"),
            create_expenses(10, 65, "water"),
            create_expenses(161, 79, "gas"),
            create_expenses(618, 321, "heating"),
            create_expenses(156, 648, "water"),
            create_expenses(987, 4312, "other"),
            create_expenses(10, 775, "electricity"),
            create_expenses(51, 7654, "other"),
            create_expenses(12, 16, "gas"),
            create_expenses(14, 168, "electricity"),
            create_expenses(16, 98, "heating"),
            create_expenses(13, 65, "water"),
            create_expenses(19, 561, "electricity")] == expenses


def test_sum():
    expenses = [create_expenses(17, 19, "gas"),
            create_expenses(13, 34, "other"),
            create_expenses(16, 384, "electricity"),
            create_expenses(10, 1986, "water"),
            create_expenses(15, 6540, "gas"),
            create_expenses(12, 321, "heating"),
            create_expenses(13, 648, "water"),
            create_expenses(12, 213, "other"),
            create_expenses(10, 13, "electricity"),
            create_expenses(16, 7654, "other"),
            create_expenses(12, 16, "gas"),
            create_expenses(14, 168, "electricity"),
            create_expenses(16, 50, "heating"),
            create_expenses(13, 65, "water"),
            create_expenses(19, 561, "electricity")]

    assert sum_of_all_expenses_for_an_apartment(expenses,"10") == 1999
    assert sum_of_all_expenses_for_an_apartment(expenses,"11") == False
    assert sum_of_all_expenses_for_an_apartment(expenses,"12") == 550
    assert sum_of_all_expenses_for_an_apartment(expenses,"13") == 747
    assert sum_of_all_expenses_for_an_apartment(expenses,"14") == 168
    assert sum_of_all_expenses_for_an_apartment(expenses,"15") == 6540
    assert sum_of_all_expenses_for_an_apartment(expenses,"16") == 8088
    assert sum_of_all_expenses_for_an_apartment(expenses,"17") == 19
    assert sum_of_all_expenses_for_an_apartment(expenses,"18") == False
    assert sum_of_all_expenses_for_an_apartment(expenses,"19") == 561

def tests():
    tests_add()
    test_check_type()
    test_sum()
    test_remove()
    test_replace()
