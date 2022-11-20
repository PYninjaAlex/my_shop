class Item:
    '''товар'''
    def __init__(self, name, amount=1, money=1, rarity='Usual'):
        self.name = name
        self.amount = amount
        if amount < 0:
            raise ValueError('Количество товара не может быть отрицательным!')
        self.money = money
        if money < 0:
            raise ValueError('Стоимость товара не может быть отрицательной!')
        self.rarity = rarity

    def decrease_amount(self, value=1):
        '''уменьшение количества товра'''
        if self.amount >= value:
            self.amount -= value
        else:
            print('Не достаточно товара!')

    def increase_amount(self, value=1):
        '''добавление товаров в магазин'''
        if value >= 0:
              self.amount += value
        else:
            raise ValueError('Значение не может быть отрицательным!')

    def set_amount(self, amount):
        if amount >= 0:
              self.amount = amount
        else:
            raise ValueError('Значение не может быть отрицательным!')





