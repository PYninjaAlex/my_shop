#TODO усложнить программу, сдлеать ввод данных с клавиатуры
from item import Item
from shop import Shop


def main():
    mouse = Item('steelseries', 6, 20, 'wireless')
    keyboard = Item('logitech', 4, 20, 'bluetooth')
    monitor = Item('asus')
    shop = Shop(mouse, keyboard, monitor, Item('printer'))
    s = shop.list_items('было')
    print(shop.sum_of_items('было'))
    print(s)
    shop.sell('logitech', 4)
    print(shop.list_items('стало'))
    print(shop.sum_of_items('стало'))
    print(shop.list_items('перед закупкой'))
    print(shop.sum_of_items('перед закупкой'))
    shop.buy('ffdf', 3)
    shop.buy('logitech', 3)
    print(shop.list_items('после закупки'))
    print(shop.sum_of_items('после закупки'))

if __name__ == '__main__':
    main()