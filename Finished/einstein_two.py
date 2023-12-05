def main():
    print("Lets convert mass to energy. \nFirst off we need a mass.")
    x = convert_energy(input("m: "))
    if x != False:
        print(int(x))
    else:
        pass


def convert_energy(number):
    try:
        number = float(number)
        new_number = number * (300000000 ** 2)
        return new_number
    except:
        print("Ain't gonna work with that input dumbass😂😂. \nDid you actaully think that your input could be converted to a mass!? 😂")
        return False


if __name__ == "__main__":
    main()
