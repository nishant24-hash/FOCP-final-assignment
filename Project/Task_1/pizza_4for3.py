# Beckett Pizza Plaza - Enhanced 4-for-3 Offer
# Features:
# 1. Welcome Message / Simple Menu
# 2. Multiple Orders
# 3. Delivery vs Collection
# 4. Itemized Receipt
# 5. Input Validation

def get_valid_price(pizza_number):
    """
    Prompt the user to enter a valid pizza price.
    Ensures the input is a positive number.
    """
    while True:
        try:
            price = float(input(f"Enter Price of Pizza #{pizza_number}: "))
            if price <= 0:  # Check for negative or zero price
                print("Please enter a valid price!")
            else:
                return price
        except ValueError:  # Catch non-numeric inputs
            print("Please enter a valid price!")


def get_delivery_choice():
    """
    Ask the user whether the order is for delivery or collection.
    Accepts only 'D' or 'C' (case-insensitive).
    """
    while True:
        choice = input("Do you want this order for Delivery or Collection? (D/C): ").strip().upper()
        if choice in ("D", "C"):
            return choice
        print("Please enter 'D' for Delivery or 'C' for Collection.")


def process_order(order_number):
    """
    Process a single order:
    - Get pizza prices
    - Determine the cheapest pizza (free under 4-for-3 offer)
    - Ask for delivery/collection and calculate fees
    - Display itemized receipt including discount and total
    """
    print(f"\nProcessing Order #{order_number}")
    print("---------------------------------\n")

    # Collect prices for 4 pizzas
    prices = []
    for i in range(1, 5):
        prices.append(get_valid_price(i))

    # Determine which pizza is free (cheapest one)
    cheapest_price = min(prices)
    free_index = prices.index(cheapest_price)

    # Delivery option and fee
    delivery_fee = 0.0
    delivery_type = get_delivery_choice()
    if delivery_type == "D":
        delivery_fee = 5.0  # Flat delivery fee

    # Calculations for totals and discount
    total_without_discount = sum(prices)
    total_with_discount = total_without_discount - cheapest_price + delivery_fee
    discount_percentage = (cheapest_price / total_without_discount) * 100

    # Display itemized receipt
    print("\n========== RECEIPT ==========")
    for idx, price in enumerate(prices):
        if idx == free_index:
            print(f"Pizza #{idx + 1}: Rs{price:.2f}  <-- FREE")
        else:
            print(f"Pizza #{idx + 1}: Rs{price:.2f}")

    # Show delivery fee or collection info
    if delivery_fee > 0:
        print(f"Delivery Fee: Rs{delivery_fee:.2f}")
    else:
        print("Collection: Rs0.00")

    print("-------------------------------------")
    print(f"Total: Rs{total_with_discount:.2f}")
    print(f"Discount: {round(discount_percentage)}%")
    print("=====================================\n")


def main():
    """
    Main function to run the Beckett Pizza Plaza program.
    Handles multiple orders and welcomes the user.
    """
    print("Welcome to Beckett Pizza Plaza!")
    print("Offer: 4-for-3 on all pizzas")
    print("====================================\n")

    order_number = 1  # Start with first order

    # Loop to allow multiple orders
    while True:
        process_order(order_number)
        order_number += 1

        # Ask if the user wants to place another order
        again = input("Do you want to place another order? (yes/no): ").strip().lower()
        if again != "yes":
            print("\nThank you for ordering from Beckett Pizza Plaza!")
            print("Have a great day!")
            break


# Run the program
main()


import sys

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python pizza_4for3.py orders.txt")
        sys.exit(1)

    filename = sys.argv[1]
    main()
