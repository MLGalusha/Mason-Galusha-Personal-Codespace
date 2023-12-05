def main():
    x = check_answer(input("What is the Answer to the Great Question of Life, the Universe, and Everything? "))
    if x == True:
        print("Yes")
    else:
        print("No")
def check_answer(x):
    x = x.strip().lower()
    if x == "42":
        return True
    elif x == "forty-two":
       return True
    elif x == "forty two":
        return True
    else:
        return False


if __name__ =="__main__":
    main()