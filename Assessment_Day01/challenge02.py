# Challenge 2: Shopping Cart Calculator

def shopping_cart():
    item1, item2, item3 = 50, 40, 30
    total = item1 + item2 + item3
    if total > 100:
        discount = total * 0.1
        final_total = total - discount
    else:
        discount = 0
        final_total = total
    print("Cart Total:", total)
    print("Discount Applied:", discount)
    print("Final Total:", final_total)

shopping_cart()