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

    def sell(self, item_name, amount=1):
        '''распродажа'''
        for good in self.stock:
            if item_name == good.name:
                good.decrease_amount(amount)
                break
        else:
            print('Такого товара не существует!')

    def buy(self, item_name, amount=1):
        '''закупка товаров'''
        for product in self.stock:
            if item_name == product.name:
                product.increase_amount(amount)
                break
        else:
            item_name = item.Item(item_name, amount)
            self.stock.append(item_name)