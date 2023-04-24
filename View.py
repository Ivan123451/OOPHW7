

# class View(InitialMassage, RepetedMassage):
class View():


    def display(self):
        num = int(input("\n Введите число: \n" +
                        "1. Купить  телефон на склад\n" +
                        "2. Вызвать инспекцию \n" +
                        "3. Показать что есть на складе\n" +
                        "4. Завершить работу\n"))

        return num

    def initialString(self):
        print("Начинаем, у вас 100 т.р. и 2 телефона на складе, что хотите сделать")

