def add_to_order(item, quantity, order=[]):
    """
    Adds an item and its quantity to the current order.
    If no order list is provided, it should start a new one.
    """
    order.append({"item": item, "quantity": quantity})
    return order

def main():
    # Customer 1: orders 2 apples
    order1 = add_to_order("Apple", 2)
    print(f"Customer 1 order: {order1}")

    # Customer 2: orders 1 banana (should be a fresh order!)
    order2 = add_to_order("Banana", 1)
    print(f"Customer 2 order: {order2}")

    # Customer 3: brings an existing order list
    order3 = add_to_order("Orange", 3, [{"item": "Pear", "quantity": 1}])
    print(f"Customer 3 order: {order3}")

if name == "main":
    main()
