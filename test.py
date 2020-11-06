class Sneakers:
    def __init__(self, name, count, manufacturer, price, size):
        self.name = name
        self.count = count
        self.manufacturer = manufacturer
        self.price = price
        self.size = size


class Warehouse:
    def __init__(self):
        self._id = 0
        self._sneakers = dict()

    def add(self, *sneakers):
        for sneaker in sneakers:
            self._id += 1
            self._sneakers[self._id] = sneaker

    def remove(self, sneakers):
        if sneakers is not None:
            for i in self._sneakers.keys():
                if self._sneakers[i] == sneakers:
                    self._sneakers.pop(i, None)

    def display(self):
        print("Товары на складе:")
        for key, value in self._sneakers.items():
            print(f'id - {key};name - {value.name};count - {value.count}; '
                  f'manufacturer - {value.manufacturer}; price - {value.price}; size - {value.size};')


def CreateSneakers():
    print('введите название кросовок')
    name = input()
    print('введите количество')
    count = int(input())
    return Sneakers(name, count)


warehouse = Warehouse()
while True:
    print(f'1-добавить товар\n2-отобразить все товары\n3-удалить\n4-выход')
    choice = int(input())
    if choice == 1:
        sneakers = list()
        while True:
            sneaker = CreateSneakers()
            sneakers.append(sneaker)
            print('\t1-добавить ещё товар\n\t2-закончить ввод товаров')
            ans = int(input())
            if ans == 2:
                break
        warehouse.add(sneaker)
    elif choice == 2:
        warehouse.display()
    elif choice == 3:
        warehouse.display()
        sneakers = CreateSneakers()
        warehouse.remove(sneakers)
    if choice == 4:
        break
