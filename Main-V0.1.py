import random
import time

balance = 0
power = 1
rock_price = 10
rock_quantity = 0
rock_power = 1
pickaxe_price = 1000
pickaxe_power = 5
pickaxe_quantity = 0
power_pickaxe = {
    'power': 25,
    'price': 10000,
    'quantity': 0
}
delve = 1
# коэффициент добычи камней. Будет увеличиваться с увеличением глубины
cf_stones = 0.5
# коэффициент добычи угля. Будет увеличиваться с увеличением глубины
cf_coal = 0.1
total_stones = 0
total_coal = 0
shovel_needed = 5
shovel = 0
delve_cost = 10

# ТЗ: Кликер в консоле(Добыча в шахте)
#
#
# Написать меню для кликера +
#  Написать магазин +
# # # Написать возможность покупки инструментов (3\3)+
# # # Написать возможность покупки рабочих
# # # Написать возможность покупки товаров в магазине (1\2)+
# Прописать возможность самостоятельно добывать в шахте +
# Прописать покупки в шопе +
# Добавить покупкам возможный вес +
# Прописать возможность покупки рабов, которые пассивно добывают основной ресурс
# Создать вложенные массивы для уменьшения нагрузки на код
# Расширяем возможности...
#

while True:
    main_menu = input("\nSHOP - 1\n"
                      "Your Stat - 2\n"
                      "Go to mine - 3\n"
                      "Go to trader - 4\n"
                      "Go to workers - 5\n"
                      "\nInput:")
    while main_menu == '1':
        shop_menu = input("\nTo Instruments - 1\n"
                          "To Workers - 2\n"
                          "To Delve Instruments - 3"
                          "\nBack - b\n"
                          "\nInput:")
        if shop_menu == 'b':

            break
        elif shop_menu == '1':
            shop_instruments = input("\nBuy rock(1) - 1\n"
                                     "Buy pickaxe(5) - 2\n"
                                     "Buy Power Pickaxe(25) - 3\n"
                                     "Back - b\n"
                                     "\nInput:")
            if shop_instruments == "b":
                shop_menu = input("\nTo Instruments - 1\n"
                                  "To Workers - 2\n"
                                  "To Delve Instruments - 3"
                                  "\nBack - b\n"
                                  "Input:")
            if shop_instruments == '1':
                shop_money_input = ("\nWanna buy rock? - 1\nPrice: " + str(rock_price) +
                                    "\nYour money: " + str(balance) +
                                    "\nExit - b\nInput:")
                shop_instruments_rock = input(shop_money_input)
                if shop_instruments_rock == 'b':
                    shop_menu = input("\nTo Instruments - 1\n"
                                      "To Workers - 2\n"
                                      "Back - b\n"
                                      "\nInput:")
                elif shop_instruments_rock == '1' and balance >= rock_price:
                    # камни
                    balance -= rock_price
                    power += rock_power
                    rock_quantity += 1
                    shop_money_input = ("\nCongrats! You Bought 1 Rock\n"
                                        "Now You have " + str(rock_quantity) +
                                        "\nWanna buy rock? - 1\nPrice: " + str(rock_price) +
                                        "\nYour money: " + str(balance) +
                                        "\nExit - b\n\nInput:")
                    shop_instruments_rock = input(shop_money_input)

                    while shop_instruments_rock == '1' and balance >= rock_price:
                        balance -= rock_price
                        power += rock_power
                        rock_quantity += 1
                        shop_money_input = ("\nCongrats! You Bought 1 Rock\n"
                                            "Now You have " + str(rock_quantity) +
                                            "\nWanna buy  another one? - 1\nPrice: " + str(rock_price) +
                                            "\nYour money: " + str(balance) +
                                            "\nExit - b\n\nInput:")
                        shop_instruments_rock = input(shop_money_input)
                        if shop_instruments_rock == 'b':
                            break

            if shop_instruments == '2':
                shop_money_input = ("\nWanna buy pickaxe? - 1\nPrice: " + str(pickaxe_price) +
                                    "\nYour money: " + str(balance) +
                                    "\nExit - b\n\nInput:")
                shop_instruments_pickaxe = input(shop_money_input)
                if shop_instruments_pickaxe == 'b':
                    shop_menu = input("\nTo Instruments - 1\n"
                                      "To Workers - 2\n"
                                      "Back - b\n"
                                      "\nInput:")
                elif shop_instruments_pickaxe == '1' and balance >= pickaxe_price:
                    balance -= pickaxe_price
                    power += pickaxe_power
                    pickaxe_quantity += 1
                    shop_money_input = ("\nCongrats! You Bought 1 Pickaxe\n"
                                        "Now You have " + str(pickaxe_quantity) +
                                        "\nWanna buy pickaxe? - 1\nPrice: " + str(pickaxe_price) +
                                        "\nYour money: " + str(balance) +
                                        "\nExit - b\n\nInput:")
                    shop_instruments_rock = input(shop_money_input)
                    while shop_instruments_rock == '1' and balance >= pickaxe_price:
                        balance -= pickaxe_price
                        power += pickaxe_power
                        pickaxe_quantity += 1
                        shop_money_input = ("\nCongrats! You Bought 1 Pickaxe\n"
                                            "Now You have " + str(pickaxe_quantity) +
                                            "\nWanna buy  another one? - 1\nPrice: " + str(pickaxe_price) +
                                            "\nYour money: " + str(balance) +
                                            "\nExit - b\n\nInput:")
                        shop_instruments_pickaxe = input(shop_money_input)
                        if shop_instruments_pickaxe == 'b':
                            break

            if shop_instruments == '3':
                shop_money_input = ("\nWanna buy Power Pickaxe? - 1\nPrice: " + str(power_pickaxe['price']) +
                                    "\nYour money: " + str(balance) +
                                    "\nExit - b\n\nInput:")
                shop_instruments_power_pickaxe = input(shop_money_input)
                if shop_instruments_power_pickaxe == 'b':
                    shop_menu = input("\nTo Instruments - 1\n"
                                      "To Workers - 2\n"
                                      "Back - b\n"
                                      "\nInput:")
                elif shop_instruments_power_pickaxe == '1' and balance >= power_pickaxe['price']:

                    balance -= power_pickaxe['price']
                    power += power_pickaxe['power']
                    power_pickaxe['quantity'] += 1
                    shop_money_input = ("\nCongrats! You Bought 1 Power Pickaxe\n"
                                        "Now You have " + str(power_pickaxe['quantity']) +
                                        "\nWanna buy Power pickaxe? - 1\nPrice: " + str(power_pickaxe['price']) +
                                        "\nYour money: " + str(balance) +
                                        "\nExit - b\nInput:")
                    shop_instruments_pickaxe = input(shop_money_input)
                while shop_instruments_power_pickaxe == '1' and balance >= power_pickaxe['price']:
                    balance -= power_pickaxe['price']
                    power += power_pickaxe['power']
                    power_pickaxe['quantity'] += 1
                    shop_money_input = ("\nCongrats! You Bought 1 Power Pickaxe\n"
                                        "Now You have " + str(power_pickaxe['quantity']) +
                                        "\nWanna buy  another one? - 1\nPrice: " + str(power_pickaxe['price']) +
                                        "\nYour money: " + str(balance) +
                                        "\nExit - b\n\nInput:")
                    shop_instruments_pickaxe = input(shop_money_input)
                    if shop_instruments_pickaxe == 'b':
                        break
        elif shop_menu == '3':
            shop_delve = input("\nBuy Shovel(10) - 1"
                               "\nBack - b"
                               "\nTo Mine - m"
                               "\n\nInput:")
            if shop_delve == 'b':
                break
            elif shop_delve == 'm':
                main_menu = '3'
            elif shop_delve == '1' and balance >= 10:
                while shop_delve == '1' and balance >= 10:
                    shovel += 1
                    balance -= 10
                    shop_delve_input = ("\nYou Have bought one! Now you have: " + str(shovel)+
                                        "\nBuy another one? - 1"
                                        "\nBack - b"
                                        "\n\nInput:")
                    shop_delve = input(shop_delve_input)
                    if shop_delve == 'b':
                        main_menu = '1'

                        break
            else:
                shop_delve = input("\nNot enough Gold!"
                                   "\nBack - b"
                                   "\nTo Mine - m"
                                   "\b\bInput:")

    while main_menu == '2':
        stat_menu_input = ("\nYour Gold: " + str(balance) +
                           "\nYour mining Power: " + str(power) +
                           "\nStones(not instrument, just stone): " + str(total_stones) +
                           "\nCoal: " + str(round(total_coal, 13)) +
                           "\nRocks: " + str(rock_quantity) +
                           "\nPickaxes: " + str(pickaxe_quantity) +
                           "\nPower Pickaxes: " + str(power_pickaxe['quantity']) +
                           "\nExit - b"
                           "\n\nInput:")
        info = input(stat_menu_input)
        if info == 'b':
            break
    while main_menu == '3':
        def delve_count():
            print("mining...")
        delve_menu = input("\nThis is your own mine!"
                           "\ndelve:" + str(delve) +
                           "\nStart mining - 1"
                           "\nGo to next delve - 2"
                           "\nExit to main menu - b"
                           "\n\nInput:")
        if delve_menu =='b':
            break
        while delve_menu == '1':
            for i in range(6):
                i += 1

                time.sleep(0.1)
                print("mining...\n" + str(6 - i))
# Увеличиваем силу в зависимости от глубины шахты
            if 1 <= power <= 10:
                power_range = 1
            elif 10 < power <= 25:
                power_range = 1.5
# Расчет добычи предметов в зависимости от следующих факторов: глубина(delve), коэффициент(cf_*item*)
# силы добычи(power) пороги добычи(power_range)
            got_stones = (random.randint(1, 4) * (delve * cf_stones) + 1) * 0.5 * power * power_range
            got_coal = random.random() * 100 + delve
            if got_coal > 50:
                got_coal = (random.randint(1, 4) * (delve * cf_coal) + 0.5) * 0.25 * power * power_range
            else:
                got_coal = 0
            total_stones += got_stones
            total_coal += got_coal
            delve_result = ("\nYou've got:\n"
                            "Stones: " + str(got_stones) +
                            "\nCoal: " + str(round(got_coal, 13)) +
                            "\nContinue mining - 1"
                            "\nBack - b\n\n"
                            "Input:")
            delve_menu = input(delve_result)
            if delve_menu == "b":
                break

        if delve_menu == '2':
            delve_menu_delve_input = ("\nNext delve is " + str(delve + 1) +
                                      "\nWant to go to next delve? - 1"
                                      "\nYou Need: " + str(shovel_needed) + "Shovels"
                                      "\nYou may pay for workers: " + str(delve_cost) +
                                      "\nback - b"
                                      "\n\nInput:")
            delve_menu_delve = input(delve_menu_delve_input)
            if delve_menu_delve == '1' and shovel >= shovel_needed and balance >= delve_cost:
                for i in range(11):
                    i += 1
                    time.sleep(2)
                    print("digging...\n" + str(11-i))
                delve += 1
                balance -= delve_cost
                shovel -= shovel_needed
                print("Congrats to You! \nYour worker finished digging! \nNow your delve: " + str(delve))

    while main_menu == '4':
        trader_menu = input("\nBuy gold:\n"
                            "10 Stones - 1 Gold\n"
                            "5 Coal - 1 Gold\n"
                            "Sell Stones - 1\n"
                            "Sell Coal - 2\n"
                            "Back - b\n\n"
                            "Input:")
        if trader_menu == 'b':
            break
        while trader_menu == '1':
            if total_stones >= 10 and trader_menu == '1':
                total_stones -= 10
                balance += 1
                print("Success! You Sold 10 Stones! "
                      "\nYour Gold now: " + str(balance) +
                      "\nYour Stones now: " + str(total_stones))
                trader_menu_stones = input("Sell More? - 1"
                                           "\nBack - b"
                                           "\n\nInput:")
                while trader_menu_stones == '1' and total_stones >= 10:
                    total_stones -= 10
                    balance += 1
                    print("Success! You Sold 10 Stones! "
                          "\nYour Gold now: " + str(balance) +
                          "\nYour Stones now: " + str(total_stones))
                    trader_menu_stones = input("Sell More? - 1"
                                               "\nBack - b"
                                               "\n\nInput:")
                    if total_stones < 10 and trader_menu_stones == '1':
                        print("\nNot Enough Stones! Go to Work!!\n")
                if trader_menu_stones == 'b' or total_stones < 10:
                    break
        while trader_menu == '2':
            if total_coal >= 5 and trader_menu == '2':
                total_coal -= 5
                balance += 1
                print("Success! You Sold 5 Coal! "
                      "\nYour Gold now: " + str(balance) +
                      "\nYour Coal now: " + str(total_coal))
                trader_menu_coal = input("Sell More? - 1"
                                         "\nBack - b"
                                         "\n\nInput:")
                while trader_menu_coal == '2' and total_coal >= 5:
                    total_coal -= 5
                    balance += 1
                    print("Success! You Sold 5 Coal! "
                          "\nYour Gold now: " + str(balance) +
                          "\nYour Coal now: " + str(total_coal))
                    trader_menu_coal = input("Sell More? - 1"
                                             "\nBack - b"
                                             "\n\nInput:")
                    if total_coal < 5 and trader_menu_coal == '2':
                        print("\nNot Enough Coal! Go to Work!!\n")
                if trader_menu_coal == 'b' or total_coal < 5:
                    break
