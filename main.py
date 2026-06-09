import calculator
import menu


def main():
    exit_menu = False

    # menu loops until user exits
    while not exit_menu:
        menu.display_menu()
        user_selection = int(input("\nEnter your menu selection: "))

        match user_selection:
            case 1:
                # basic addition
                x, y = calculator.get_two_numbers()
                z = calculator.add(x, y)
                calculator.print_result(z)
            case 2:
                # basic subtraction
                x, y = calculator.get_two_numbers()
                z = calculator.subtract(x, y)
                calculator.print_result(z)
            case 3:
                # basic multiplication
                x, y = calculator.get_two_numbers()
                z = calculator.multiply(x, y)
                calculator.print_result(z)
            case 4:
                # basic division
                x, y = calculator.get_two_numbers()
                z = calculator.divide(x, y)
                calculator.print_result(z)
            case 5:
                print("Running expression evaluator")
                calculator.evaluate_expression(input("Enter math expression: "))
            case -1:
                print("Exiting calculator app.")
                exit_menu = True
            case _:
                print("Invalid selection given, try again")



if __name__ == '__main__':
    main()

