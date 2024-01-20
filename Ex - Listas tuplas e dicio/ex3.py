carrinho = [("Camiseta preta", 39.99), ("Calça jeans", 119.90), ("Boné", 29.90)]

totalCarrinho = 0

for produto in carrinho:
    totalCarrinho += produto[1]

print(f"O total R$ {totalCarrinho:.2f}")