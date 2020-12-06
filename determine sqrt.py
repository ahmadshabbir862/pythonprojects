import math
def main():
    def a_perfect_squar(x):
            sqrt_value = math.sqrt(x)
            return int(sqrt_value) ** 2 == x
    number = int(input("Enter a number: "))

    if a_perfect_squar(number):
        print("It is a perfect square.")
    else:
        print("It is not a perfect square.")
    Repeat = input("More Numbers??? 'y' or 'n' ").lower()
    if Repeat == "y":
        main()
    elif Repeat == "n":
        print("Ok Thanks!")
    else:
        print("You specify wrong term.")
        exit()
main()




