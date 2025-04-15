# order_system.py 
def calculate_shipping(destination, total): 
    if destination == "local": 
        return 10 
    elif destination == "national": 
        return 20 
    elif destination == "international": 
        return 50 
    else: 
        return 0 
    
def create_order(customer_name, items, destination): 
    total = 0 

print(f"Pedido para: {customer_name}") 
for item in items: 
    print(f"{item['name']} - R${item['price']}") 
    total += item['price'] 

    shipping = calculate_shipping(destination, total) 
    print(f"Subtotal: R${total}") 
    print(f"Frete para {destination}: R${shipping}") 
    print(f"Total final: R${total + shipping}") 
# Exemplo de uso 
items = [ 
{"name": "Notebook", "price": 3000}, 
{"name": "Mouse", "price": 150}, 
{"name": "Teclado", "price": 200} 
] 
create_order("Maria", items, "national")