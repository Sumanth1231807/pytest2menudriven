def area_square(side):
    Area = side * side
    return Area


def perimeter_rect(l, w):
    perimeter = 2 * (l + w)
    return perimeter


def area_rect(l, b):
    Area = l * b
    return Area

if __name__=="__main__":
    while True:
        print("1. Calculate area of Square ")
        print("2. Calculate perimeter of rectangle ")
        print("3. Calculate area of rectangle ")
        print("4. EXIT")

        choice = int(input("Enter your choice from the above Menu :"))

        if choice == 1:
            side = int(input("Enter the num for finding Area of square :"))
            squarearea = area_square(side)
            print(squarearea)

        elif choice == 2:
            l = int(input("Enter the Length for finding perimeter of rectangle :"))
            w = int(input("Enter the width for finding perimeter of rectangle :"))
            perimeterrect = perimeter_rect(l, w)
            print(perimeterrect)

        elif choice == 3:
            l = int(input("Enter the length for finding area of rectangle :"))
            b = int(input("Enter the breath for finding area of rectangle :"))
            arearect = area_rect(l, b)
            print(arearect)

        elif choice == 4:
            break

        else:
            print("oops you have entered INVALID choice...try again by choosing valid option!")