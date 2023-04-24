import random

from CellPhone import CellPhone
from Money import Money
from Stock import Stok
from Tax import Tax
from View import View
from Fire import Fire


class Model():

    def activity(self):
        flag = True
        money = Money()

        view = View()
        view.initialString()

        while flag == True:

            num = view.display()

            match(num):
                case 1:

                    print("Ведите параметры телефона:" +
                            "Бренд:")
                    brand = str(input("Бренд: "))
                    model = str(input("Модель: "))
                    price = int(input("Цена закупки: "))

                    if money.amount > price:
                        localPhone = CellPhone(brand, model, price)
                        Stok.add(localPhone, Stok.listOfPhonesOnStock)
                        print("вы добавили на склад" + localPhone.brand)
                        money.amount = money.amount - localPhone.price
                        print("У вас осталось")
                        print(money.amount)

                    else:
                        print("У вас не хватает денег(")


                case 2:
                    rndInspection = random.randint(0, 1)
                    print(rndInspection)

                    if rndInspection == 1:
                        tax = Tax()
                        tax.inspectionCome()
                        tiket = tax.tiketAmount()
                        money.amount = money.amount - tiket
                        print(f"У вас осталось {money.amount} - вас"
                              f" оштрафовали вас на {tiket}")

                    else:
                        fire = Fire()
                        fire.inspectionCome()


                case 3:
                    print(f"У вас на складе: {len(Stok.listOfPhonesOnStock)} + телефон(ов)")

                    # print(Stok.show(Stok.listOfPhonesOnStock))
                    for i in range(len(Stok.listOfPhonesOnStock)):
                        Stok.show(Stok.listOfPhonesOnStock[i])

                    print(f"А еще у вас {money.amount} наличкой")

                case 4:
                    flag = False
                    break


