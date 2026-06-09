
import menu


def main():
    exit_menu = False

    # menu loops until user exits
    while not exit_menu:
        menu.displayMenu()
        user_selection = int(input("\nEnter your menu selection: "))

        match user_selection:
            case 1:
                print("1 selected")
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

