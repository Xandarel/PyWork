class Sneakers:
    def __init__(self, name, count, manufacturer, price, size):
        self.name = name
        self.count = count
        self.manufacturer = manufacturer
        self.price = price
        self.size = size


class Warehouse:
    def __init__(self):
        self._manufacturers = dict()
        self._size = dict()
        self._id = 0
        self._sneakers = dict()

    def add(self, sneakers):
        for sneaker in sneakers:
            self._sneakers[self._id] = sneaker

            if sneaker.manufacturer in self._manufacturers.keys():
                self._manufacturers[sneaker.manufacturer].append(self._id)
            else:
                self._manufacturers[sneaker.manufacturer] = list()
                self._manufacturers[sneaker.manufacturer].append(self._id)

            if sneaker.size in self._size:
                self._size[sneaker.size].append(self._id)
            else:
                self._size[sneaker.size] = list()
                self._size[sneaker.size].append(self._id)
            self._id += 1

    def get_stat(self, stat_pos):
        if stat_pos == 'manufacturer':
            print('Производители:')
            for manufacturer in self._manufacturers.keys():
                print(f'{manufacturer}:')
                for sneaker in self._manufacturers[manufacturer]:
                    print(f'\n\tid - {sneaker};name - {self._sneakers[sneaker].name};\n\tcount - {self._sneakers[sneaker].count}; '
                          f'\n\tmanufacturer - {self._sneakers[sneaker].manufacturer}; '
                          f'\n\tprice - {self._sneakers[sneaker].price}; \n\tsize - {self._sneakers[sneaker].size};')
        elif stat_pos == 'size':
            print('Размеры:')
            for size in self._size.keys():
                print(f'{size}:')
                for sneaker in self._size[size]:
                    print(f'\tid - {sneaker};\n\tname - {self._sneakers[sneaker].name};\n\tcount - {self._sneakers[sneaker].count}; '
                          f'\n\tmanufacturer - {self._sneakers[sneaker].manufacturer}; '
                          f'\n\tprice - {self._sneakers[sneaker].price}; \n\tsize - {self._sneakers[sneaker].size};')



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
    manufacturer = input('введите производителя\n')
    price = float(input('введите цену\n'))
    size = int(input('введите размер\n'))
    return Sneakers(name, count, manufacturer, price, size)


def GetStat():
    print('1-статистика по производителям\n2-статистика по размерам')
    stat_choise = int(input())
    if stat_choise == 1:
        return 'manufacturer'
    elif stat_choise == 2:
        return 'size'


def LoadFile(filename):
    res_list = list()
    with open(filename) as file:
        data = file.read().split('\n')
    for d in data:
        row = d.split()
        res_list.append(Sneakers(row[0], row[1], row[2], row[3], row[4]))
    return  res_list



warehouse = Warehouse()
while True:
    print(f'1-добавить товар\n2-отобразить все товары\n3-удалить\n4-вывести статистику\n5-загрузить товары с файла\n6-выход')
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
        warehouse.add(sneakers)
    elif choice == 2:
        warehouse.display()
    elif choice == 3:
        warehouse.display()
        sneakers = CreateSneakers()
        warehouse.remove(sneakers)
    elif choice == 4:
        key = GetStat()
        warehouse.get_stat(key)
    elif choice == 5:
        filename = input('Введите имя файла\n')
        data = LoadFile(filename)
        warehouse.add(data)
    elif choice == 6:
        break
