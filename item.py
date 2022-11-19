class Item:
    def __init__(self, name, amount=1, rarity='Usual'):
        self.name = name
        self.amount = amount
        self.rarity = rarity

    def decrease_amount(self, value=1):
        if self.amount >= value:
            self.amount -= value
        else:
            print('Не достаточно товара!')






