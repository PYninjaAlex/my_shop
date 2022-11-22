from item import Item
from shop import Shop


def main():
    mouse = Item(input('Введите имя товара "1": '), int(input('Введите количество товаров: ')), int(input('Введите общую стоимость товаров: ')), input('Введите категорию товара: '))
    keyboard = Item(input('Введите имя товара "2": '), int(input('Введите количество товаров: ')), int(input('Введите общую стоимость товаров: ')), input('Введите категорию товара: '))
    monitor = Item(input('Введите имя товара "3": '), int(input('Введите количество товаров: ')), int(input('Введите общую стоимость товаров: ')), input('Введите категорию товара: '))
    shop = Shop(mouse, keyboard, monitor, Item('printer'))
    s = shop.list_items('было')
    print(shop.sum_of_items('было'))
    print(s)
    shop.sell('logitech', 4)
    print(shop.list_items('стало'))
    print(shop.sum_of_items('стало'))
    print(shop.list_items('перед закупкой'))
    print(shop.sum_of_items('перед закупкой'))
    shop.buy(keyboard, 3)
    shop.buy(mouse, 3)
    print(shop.list_items('после закупки'))
    print(shop.sum_of_items('после закупки'))

if __name__ == '__main__':
    main()
