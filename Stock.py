from typing import Type

from CellPhone import CellPhone


class Stok():
    listOfPhonesOnStock = [CellPhone("Iphone13", "Apple", 50000), CellPhone("S22", "Samsung", 40000 )]



    def add(localPhone, listOfPhone):
        listOfPhone.append(localPhone)

    def show(listOfPhones):
        print(listOfPhones.brand, listOfPhones.model, listOfPhones.price)

