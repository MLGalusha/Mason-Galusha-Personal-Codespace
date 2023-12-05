from playback_two import convert_slow

def main():
    upper_lower_test()


def upper_lower_test():
    assert convert_slow("what are you doing") == ("what...are...you...doing")
    assert convert_slow("WHAT ARE YOU DOING") == ("WHAT...ARE...YOU...DOING")
    assert convert_slow("WhAt ArE yOu DoInG") == ("WhAt...ArE...yOu...DoInG")


def punctuation_test():
    assert convert_slow("What's up kanye ! ?") == ("What's...up...kanye...!...?")
    assert convert_slow("! . , $") == ("!.......,...$")


if __name__ == "__main__":
    main()