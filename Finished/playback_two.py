def main():
    x = convert_slow(input("Input: "))
    print(x)

def convert_slow(sentence):
    for i in sentence:
        new_sentence = sentence.replace(" ", "...")
        return new_sentence



if __name__ == "__main__":
    main()