#TODO усложнить программу, сдлеать ввод данных с клавиатуры
from item import Item
from shop import Shop


def main():
    mouse = Item('steelseries', 6, 'wireless')
    keyboard = Item('logitech', 4, 'bluetooth')
    monitor = Item('asus')
    shop = Shop(mouse, keyboard, monitor, Item('printer'))
    s = shop.list_items('было')
    print(s)
    shop.sell('logitech', 4)
    print(shop.list_items('стало'))

if __name__ == '__main__':
    main()