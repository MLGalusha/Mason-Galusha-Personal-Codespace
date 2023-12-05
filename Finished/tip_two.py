def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")
    print(f"Your total bill is ${tip + dollars}.")


def dollars_to_float(d):
    for i in d:
        if "$" in d:
            d = d.strip("$")
            d = float(d)
        else:
            d = float(d)
        return d


def percent_to_float(p):
    for i in p:
        if "%" in p:
            p = p.strip("%")
            p = float(p)
            new_p = p/100
        else:
            p = float(p)
            new_p = p/100
        return new_p


if __name__ == "__main__":
    main()