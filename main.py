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
                x, y = calculator.get_two_numbers()
                z = calculator.add(x, y)
                calculator.print_result(z)
            case 2:
                print("2 selected")
            case 3:
                print("3 selected")
            case 4:
                print("4 selected")
            case 5:
                print("Exiting calculator app.")
                exit_menu = True
            case _:
                print("Invalid selection given, try again")



if __name__ == '__main__':
    main()

