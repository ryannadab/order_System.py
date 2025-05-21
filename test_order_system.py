import unittest
from abc import ABC, abstractmethod

class Item:
    """Representa um item individual em um pedido."""
    def __init__(self, name: str, price: float):
        """Inicializa um novo item."""
        self.name = name
        self.price = price

class Customer:
    """Representa um cliente que faz um pedido."""
    def __init__(self, name: str):
        """Inicializa um novo cliente."""
        self.name = name

class ShippingStrategy(ABC):
    """Interface para estratégias de cálculo de frete."""
    @abstractmethod
    def calculate(self, order_total: float) -> float:
        pass

class LocalShipping(ShippingStrategy):
    def calculate(self, order_total: float) -> float:
        return 10.0

class NationalShipping(ShippingStrategy):
    def calculate(self, order_total: float) -> float:
        return 20.0

class InternationalShipping(ShippingStrategy):
    def calculate(self, order_total: float) -> float:
        return 50.0

class Order:
    """Representa um pedido feito por um cliente, contendo itens e uma estratégia de frete."""
    def __init__(self, customer: Customer, items: list[Item], shipping_strategy: ShippingStrategy):
        """Inicializa um novo pedido."""
        self.customer = customer
        self.items = items
        self.shipping_strategy = shipping_strategy

    def calculate_total(self) -> float:
        """Calcula o valor total dos itens no pedido."""
        return sum(item.price for item in self.items)

    def calculate_shipping_cost(self) -> float:
        """Calcula o custo de frete para o pedido usando a estratégia definida."""
        return self.shipping_strategy.calculate(self.calculate_total())

    def calculate_final_total(self) -> float:
        """Calcula o valor total final do pedido, incluindo o frete."""
        return self.calculate_total() + self.calculate_shipping_cost()

    def print_invoice(self):
        """Imprime a fatura do pedido com detalhes do cliente, itens, subtotal, frete e total final."""
        print(f"Pedido para: {self.customer.name}")
        for item in self.items:
            print(f"{item.name} - R${item.price:.2f}")
        print(f"Subtotal: R${self.calculate_total():.2f}")
        print(f"Frete: R${self.calculate_shipping_cost():.2f}")
        print(f"Total final: R${self.calculate_final_total():.2f}")

# Exemplo de uso
if __name__ == "__main__":
    items = [
        Item("Notebook", 3000),
        Item("Mouse", 150),
        Item("Teclado", 200)
    ]
    customer = Customer("Maria")
    shipping = NationalShipping()  # Substitua aqui para testar outros tipos de frete
    order = Order(customer, items, shipping)
    order.print_invoice()

# Testes unitários
class TestOrderSystem(unittest.TestCase):
    """Testes unitários para o sistema de pedidos."""

    def setUp(self):
        """Configuração inicial para os testes."""
        self.customer = Customer("João")
        self.item1 = Item("Caneta", 2.50)
        self.item2 = Item("Caderno", 10.00)
        self.items = [self.item1, self.item2]
        self.local_shipping = LocalShipping()
        self.national_shipping = NationalShipping()
        self.international_shipping = InternationalShipping()

    def test_item_creation(self):
        """Testa a criação de um item."""
        self.assertEqual(self.item1.name, "Caneta")
        self.assertEqual(self.item1.price, 2.50)

    def test_customer_creation(self):
        """Testa a criação de um cliente."""
        self.assertEqual(self.customer.name, "João")

    def test_local_shipping_calculation(self):
        """Testa o cálculo do frete local."""
        order = Order(self.customer, self.items, self.local_shipping)
        self.assertEqual(order.calculate_shipping_cost(), 10.0)

    def test_national_shipping_calculation(self):
        """Testa o cálculo do frete nacional."""
        order = Order(self.customer, self.items, self.national_shipping)
        self.assertEqual(order.calculate_shipping_cost(), 20.0)

    def test_international_shipping_calculation(self):
        """Testa o cálculo do frete internacional."""
        order = Order(self.customer, self.items, self.international_shipping)
        self.assertEqual(order.calculate_shipping_cost(), 50.0)

    def test_order_total_calculation(self):
        """Testa o cálculo do valor total dos itens no pedido."""
        order = Order(self.customer, self.items, self.local_shipping)
        self.assertEqual(order.calculate_total(), 12.50)

    def test_order_final_total_with_local_shipping(self):
        """Testa o cálculo do valor total final do pedido com frete local."""
        order = Order(self.customer, self.items, self.local_shipping)
        self.assertEqual(order.calculate_final_total(), 22.50)

    def test_order_final_total_with_national_shipping(self):
        """Testa o cálculo do valor total final do pedido com frete nacional."""
        order = Order(self.customer, self.items, self.national_shipping)
        self.assertEqual(order.calculate_final_total(), 32.50)

    def test_order_final_total_with_international_shipping(self):
        """Testa o cálculo do valor total final do pedido com frete internacional."""
        order = Order(self.customer, self.items, self.international_shipping)
        self.assertEqual(order.calculate_final_total(), 62.50)

if __name__ == "__main__":
    unittest.main()
