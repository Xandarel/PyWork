class Sneakers:
    def __init__(self, name, count):
        self.name = name
        self.count = count


class Warehouse:
    def __init__(self):
        self._list = list()

    def add(self, sneakers):
        self._list.append(sneakers)

    def display(self):
        for l in self._list:
            print(f'name - {l.name}\ncount-{l.count}')


warehouse = Warehouse()
while True:
    print(f'1-добавить товар\n2-отобразить все товары\n3-выход')
    choice = int(input())
    if choice == 1:
        print('введите название кросовок')
        name = input()
        print('введите количество')
        count = int(input())
        sneakers = Sneakers(name, count)
        warehouse.add(sneakers)
    if choice == 2:
        warehouse.display()
    if choice == 3:
        break
