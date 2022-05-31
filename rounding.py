# this function will round decimals
def rounding(decimal_num, decimal_place):
    decimal_num[0] = decimal_num[0] * (10 ** decimal_place)
    decimal_num[0] = decimal_num[0] + 0.5
    decimal_num[0] = int(decimal_num[0])
    decimal_num[0] = decimal_num[0] / (10 ** decimal_place)
    return decimal_num[0]
# this function gets input from the user and displays information


def main():
    dec_num = 0
    decimal_place = 0
    try:
        dec_num = float(input("Enter a decimal number: "))
        decimal_place = int(input("Enter a desired decimal place: "))
        decimal_num = []
        decimal_num.append(dec_num)
        rounding(decimal_num, decimal_place)
        num = rounding(decimal_num, decimal_place)
        print("{} converted to the decimal place of {} is {}".format(
            dec_num, decimal_place, num))
    except ValueError:
        print("Please enter a decimal number and interger.")


if __name__ == "__main__":
    main()
