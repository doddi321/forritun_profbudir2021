class Order:
    def __init__(self, name: str, price: float) -> None:
        self._name = name
        self._price = price

    def price(self):
        return self._price

    def item(self):
        return self._name

    def __str__(self) -> str:
        return f'Item: {self.item()}, price: {self.price()}'

    def __gt__(self, other):
        return self.price() > other.price()

    def __add__(self, other):
        new_name = f'{self.item()}+{other.item()}'
        new_price = self.price() + other.price()
        return Order(new_name, new_price)

    