import argparse
import math

parser = argparse.ArgumentParser(description="This program calculates loan of differentiated or annuity payment.")

parser.add_argument("--type", choices=["annuity", "diff"],
                    help="You need to choose only one type of the payment.")

parser.add_argument("--payment", type=int,
                    help="Specify this argument only if you would like to calculate annuity payment.")

parser.add_argument("--principal", type=int,
                    help="Specify loan principal.")

parser.add_argument("--periods", type=int,
                    help="Specify number of monthly payments.")

parser.add_argument("--interest", type=float,
                    help="Specify loan interest.")

args = parser.parse_args()

choice = ""

i = 0

try:
    i = (args.interest / 100) / (12 * 100 / 100)
except TypeError:
    print("Incorrect parameters")
    quit()

args_dict = vars(args).items()

check_if_negative = [value for key, value in args_dict if key != "type" and value is not None]

for number in check_if_negative:
    if number < 0:
        print("Incorrect parameters")
        quit()

if args.type is None:
    print("Incorrect parameters")
    quit()

elif args.type == "diff":

    choice = "diff"

    for key, value in args_dict:
        if key == "payment" and value is not None:
            print("Incorrect parameters")
            quit()
        elif key != "payment" and value is None:
            print("Incorrect parameters")
            quit()

elif args.type == "annuity":
    if args.principal and args.periods and args.interest:
        choice = "annuity"
    elif args.payment and args.periods and args.interest:
        choice = "principal"
    elif args.principal and args.payment and args.interest:
        choice = "periods"

if choice == "periods":

    i = (args.interest / 100) / (12 * 100 / 100)

    months = math.ceil(math.log(args.payment / (args.payment - i * args.principal), 1 + i))

    years_to_repay = months // 12

    months_to_repay = months % 12

    if years_to_repay != 0 and months_to_repay != 0:
        print(f"It will take {years_to_repay} years and {months_to_repay} months to repay this loan!")
    elif years_to_repay == 0:
        print(f"It will take {months_to_repay} months to repay this loan!")
    elif months_to_repay == 0:
        print(f"It will take {years_to_repay} years to repay this loan!")

    print("Overpayment = ", args.payment * months - args.principal)


elif choice == "annuity":

    annuity = math.ceil(args.principal * ((i * math.pow((1 + i), args.periods)) / ((math.pow((1 + i), args.periods)) - 1)))

    print("Your annuity payment = {0}!".format(annuity))

    print("Overpayment = ", annuity * args.periods - args.principal)

elif choice == "principal":

    principal = math.floor(args.payment / ((i * math.pow((1 + i), args.periods)) / ((math.pow((1 + i), args.periods)) - 1)))

    print("Your loan principal = {0}!".format(principal))

    print("Overpayment = ", args.payment * args.periods - principal)

elif choice == "diff":

    m = 0

    overpayment = 0

    while m != args.periods:

        m += 1

        diff = math.ceil(
            (args.principal / args.periods) + i * (args.principal - (args.principal * (m - 1)) / args.periods))

        print(f"Month {m}: payment is {diff}")

        overpayment += diff

    print("Overpayment = ", overpayment - args.principal)
