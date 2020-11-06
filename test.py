class Sneakers:
    def __init__(self, name, count):
        self.name = name
        self.count = count


class Warehouse:
    def __init__(self):
        self._id = 0
        self._sneakers = dict()

    def add(self, sneakers):
        self._id = self._id + 1
        self._sneakers[self._id] = sneakers

    def remove(self, sneakers):
        if sneakers is not None:
            for i in self._sneakers.keys():
                if self._sneakers[i] == sneakers:
                    self._sneakers.pop(i, None)

    def display(self):
        print("Товары на складе:")
        for key, value in self._sneakers.items():
            print(f'id - {key};name - {value.name};count - {value.count}')


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
