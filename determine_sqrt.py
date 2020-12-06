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
    Repeat = input("More Number???").lower()
    if Repeat == "y":
        main()
    else:
        print("Ok Thanks!")
        exit()
main()




