# Задача 2: написать программу, которая будет иммитировать покупку товаров в магазине

user_vallet = [1, 1, 2, 5, 5, 5]
shop_kassa = [1, 1, 2, 2, 2, 1]
product_price = {'молоко': 2, 'сыр': 3, 'хлеб': 2, 'масло': 5, 'кефир': 2, 'персик': 1, 'сок': 5, 'лосось': 5, 'курица': 3, 'апельсин': 2}
bying = []

def print_shop():
    """
    Функция выводит на печать содержимое магазина и кошелька покупателя
    """
    for product, price in product_price.items():
        print(f'{product}: {price} руб')
    print(f'Монеты в кассе: {shop_kassa}')
    print('-'*40)
    print(f'У вас в кошельке монеты {user_vallet}')


def check_input():
    """
    Функция принимнет ввод пользователя, проверяет наличие товара, возвращает товар или флаг прекращения
    покупок
    """
    while True:
        prod = input('Что хотите купить? Если хочешь закончить покупки, пиши stop <<< ').strip().lower()
        if prod == 'stop':
            return False
        elif prod not in product_price:
            print('Такого товара у нас нет')
            continue
        return prod


def check_buy(prod):
    """
    Функция принимает на вход наименование покупаемого товара, выводит в консоль предложение выбрать другой,
     при невозможности покупки, при возможности производит перерасчет в кошельке и кассе магазина
    """
    price = product_price[prod]
    money = price
    if price > max(user_vallet):
        print('Недостаточно денег, выберите что-то подешевле')
        return
    while True:
        try:
            user_vallet.index(money)
            break
        except ValueError:
            money += 1
    change = money - price
    if  change:
        try:
           shop_kassa.remove(change)
           user_vallet.append(change)
        except ValueError:
            print('К сожалению нет сдачи, выберите что-то другое')
            return
    user_vallet.remove(money)
    bying.append(prod)
    product_price.pop(prod)
    shop_kassa.append(money)
    print(f'Вы купили {bying}')




def shopping():
    """
    Основная функция цикла покупок, предлагает купить товар, изменяет содержимое кошелька покупателя
    и кассы магазина
    """
    print('Доступные товары и их цена:')
    prolonged = True
    while prolonged:
        print_shop()
        product = check_input()
        if product:  # Если покупатель выбрал товар
            check_buy(product)  # Если покупка возможна, произведет изменения в кошельках
            if not user_vallet or min(product_price.values()) > max(user_vallet):
                print(f'Вы больше не можете совершать покупки, у вас в кошельке {user_vallet}')
                prolonged = False
        else:  # Если покупатель ввел stop
            prolonged = False

if __name__ == '__main__':
    shopping()
