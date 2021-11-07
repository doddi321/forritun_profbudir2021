from order import Order

class TaxableOrder(Order):
    def __init__(self, name: str, price: float, tax: float) -> None:
        super().__init__(name, price)
        self.__tax = tax

    def price(self):
        return self._price * (1 + self.__tax)

