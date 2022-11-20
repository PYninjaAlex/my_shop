import copy
import item


class Shop:
    '''главный магазин'''
    def __init__(self, *items):
        self.stock = list(items) #склад

    def list_items(self, state):
        '''получение информации о всех товаров'''
        output = f'Количество товара {state}:\n'
        for item in self.stock:
            if item.amount != 0:
                output += f'{str(item.name)}: {str(item.amount)};\n'
        return output

    def sum_of_items(self, state):
        self.sum_of_goods = 0
        for items in self.stock:
            self.sum_of_goods += items.money
        return f'Cумма всех товаров {state}:{self.sum_of_goods};\n'

    def sell(self, item, amount=1):
        '''распродажа'''
        for good in self.stock:
            if item == good.name:
                good.decrease_amount(amount)
                break
        else:
            print('Такого товара не существует!')

    def buy(self, item_name, amount=1):
        '''закупка товаров'''
        for product in self.stock:
            if item_name == product.name:
                try:
                    product.increase_amount(amount)
                    break
                except ValueError:
                    print('Не удалось добавить товар!')
                    break
        else:
            item_copy = copy.deepcopy(item.Item(item_name))
            item_copy.set_amount(amount)
            self.stock.append(item_copy)