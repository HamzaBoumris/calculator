def calculate_revenue(price_per_unit, units_sold):
    return price_per_unit * units_sold


def main():
    try:
        price_per_unit = float(input("Enter the price per unit: "))
        units_sold = int(input("Enter the number of units sold: "))

        total_revenue = calculate_revenue(price_per_unit, units_sold)

        print(f"Total Revenue: {total_revenue:.2f}DH")
    except ValueError:
        print("Please enter valid numeric values.")


if __name__ == "__main__":
    main()
