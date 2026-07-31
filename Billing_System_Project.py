class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def get_total(self):
        return self.price * self.quantity
    
class Bill:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def calculate_total(self):
        return sum(p.get_total() for p in self.products)

    def calculate_tax(self, tax_rate=0.1):  # 10% tax
        return self.calculate_total() * tax_rate

    def display_bill(self):
        print("\n===== FINAL BILL =====")
        print(f"{'Name':<15}{'Price':<10}{'Qty':<10}{'Total':<10}")
        print("-" * 45)
        for p in self.products:
            print(f"{p.name:<15}{p.price:<10}{p.quantity:<10}{p.get_total():<10}")
        subtotal = self.calculate_total()
        tax = self.calculate_tax()
        total = subtotal + tax
        print("-" * 45)
        print(f"{'Subtotal':<35}{subtotal:.2f}")
        print(f"{'Tax (10%)':<35}{tax:.2f}")
        print(f"{'Grand Total':<35}{total:.2f}")

if __name__ == "__main__":
    p1 = Product("Pen", 10, 3)
    p2 = Product("Notebook", 50, 2)
    p3 = Product("Eraser", 5, 5)
    bill = Bill()
    bill.add_product(p1)
    bill.add_product(p2)
    bill.add_product(p3)
    bill.display_bill()