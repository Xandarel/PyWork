from Products import TshirtProduct, SneakersProduct
from mysql_con import con, cur


def add_sneakers():
    name = input('введите название кросовок\n')
    count = int(input('введите количество\n'))
    manufacturer = input('введите производителя\n')
    price = float(input('введите цену\n'))
    size = int(input('введите размер\n'))
    color = input('введите цвет\n')
    return SneakersProduct(None, price, name, count, manufacturer, size, color)


def add_tshirt():
    name = input('введите название футболки\n')
    count = int(input('введите количество\n'))
    manufacturer = input('введите производителя\n')
    price = float(input('введите цену\n'))
    size = int(input('введите размер\n'))
    color = input('введите цвет\n')
    return TshirtProduct(None, price, name, count, manufacturer, size, color)


def add_item(type):
    print(f'1-добавить футболку\n2-добавить кросовки')
    item_choice = int(input())
    if item_choice == 1:
        item = add_tshirt()
        cur.execute('INSERT INTO tshirt(price, named, quantity, brand, size, color) VALUES (%s, %s, %s, %s, %s, %s)',
                    (item.price, item.name, item.quantity, item.brand, item.size, item.color))
    elif item_choice == 2:
        item = add_sneakers()
        cur.execute('INSERT INTO sneakers(price, named, quantity, brand, size, color) VALUES (%s, %s, %s, %s, %s, %s)',
                    (item.price, item.name, item.quantity, item.brand, item.size, item.color))
    con.commit()


def show_data():
    cur.execute('SHOW TABLES')
    tables = cur.fetchall()
    for table in tables:
        cur.execute(f'SELECT * FROM {table[0]}:')
        res = cur.fetchall()
        print(f'{table[0]}')
        if table[0] == 'sneakers':
            for r in res:
                product = SneakersProduct(r[0], r[1], r[2], r[3], r[4], r[5], r[6])
                print(product.show_product())
        elif table[0] == 'tshirt':
            for r in res:
                product = TshirtProduct(r[0], r[1], r[2], r[3], r[4], r[5], r[6])
                print(product.show_product())


def delete_product():
    print(f'1-удалить футболку\n2-удалить кросовки')
    item_choice = int(input())
    if item_choice == 1:
        id = int(input('Введите id футболки\n'))
        cur.execute(f'DELETE FROM tshirt WHERE id = {id}')
    elif item_choice == 2:
        id = int(input('Введите id красовок'))
        cur.execute(f'DELETE FROM sneakers WHERE id = {id}')


def show_stat(stat_param):
    cur.execute('SHOW tables')
    tables = cur.fetchall()
    for table in tables:
        print(table[0])
        cur.execute(f'SELECT DISTINCT {stat_param} FROM {table[0]}')
        stat = cur.fetchall()
        for st in stat:
            print(f'\t{st[0]}')
            cur.execute(f'SELECT * FROM {table[0]} WHERE {stat_param} = {st[0]}')
            for data in cur.fetchall():
                if table[0] == 'sneakers':
                    product = SneakersProduct(data[0], data[1], data[2], data[3], data[4], data[5], data[6])
                    print(product.show_product())
                elif table[0] == 'tshirt':
                    product = TshirtProduct(data[0], data[1], data[2], data[3], data[4], data[5], data[6])
                    print(product.show_product())


def load_file(filename):
    res_list = list()
    with open(filename) as file:
        data = file.read().split('\n')
    for d in data:
        row = d.split()
        if row[-1] == 'SN':
            res_list.append(SneakersProduct(None, row[3], row[0], row[1], row[2], row[4], row[5]))
        elif row[-1] == 'TH':
            res_list.append(TshirtProduct(None, row[3], row[0], row[1], row[2], row[4], row[5]))
    return res_list


while True:
    print(f'1-добавить товар\n2-отобразить все товары'
          f'\n3-удалить\n4-вывести статистику\n5-загрузить товары с файла\n6-выход')
    choice = int(input())
    if choice == 1:
        add_item()
    elif choice == 2:
        show_data()
    elif choice == 3:
        delete_product()
    elif choice == 4:
        stat = int(input('1-статистика по производителям\n2-статистика по размерам\n'))
        if stat == 1:
            show_stat('brand')
        elif stat == 2:
            show_stat('size')
    elif choice == 5:
        filename = input('Введите имя файла\n')
        res = load_file(filename)
        for item in res:
            if isinstance(item, TshirtProduct):
                cur.execute('INSERT INTO tshirt(price, named, quantity, brand, size, color) VALUES (%s, %s, %s, %s, %s, %s)',
                            (item.price, item.name, item.quantity, item.brand, item.size, item.color))
            elif isinstance(item, SneakersProduct):
                cur.execute('INSERT INTO sneakers(price, named, quantity, brand, size, color) VALUES (%s, %s, %s, %s, %s, %s)',
                            (item.price, item.name, item.quantity, item.brand, item.size, item.color))
            con.commit()
    elif choice == 6:
        break
