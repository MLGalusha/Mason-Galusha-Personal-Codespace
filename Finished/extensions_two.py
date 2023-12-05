def main():
    x = split(input("File name: "))
    print(convert(x))

def split(split):
    if "." in split:
        done_split = split.strip().lower().split(".")
        return done_split[1]
    else:
        return split

def convert(x):
    image_list = ["gif", "jpg", "jpeg", "png"]
    app_list = ["pdf", "zip"]
    if x in image_list:
        if x == "jpg":
            return f"image/jpeg"
        else:
            return f"image/{x}"
    elif x in app_list:
        return f"application/{x}"
    elif x == "txt":
        return "text/plain"
    else:
        return "application/octet-stream"

if __name__ == "__main__":
    main()