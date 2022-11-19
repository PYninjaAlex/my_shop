from item import Item

class Shop:
    def __init__(self, *items):
        self.stock = list(items)

    def list_items(self, state):
        output = f'Количество товара {state}:\n'
        for item in self.stock:
            if item.amount != 0:
                output += f'{str(item.name)}: {str(item.amount)};\n'
        return output

    def sell(self, item_name, amount=1):
        for good in self.stock:
            if item_name == good.name:
                good.decrease_amount(amount)
                break
        else:
            print('Такого товара не существует!')









