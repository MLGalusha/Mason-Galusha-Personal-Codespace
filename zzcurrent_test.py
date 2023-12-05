x = input("Input: ")


image_list = ["gif", "jpg", "jpeg", "png"]
app_list = ["pdf", "zip"]
if x in image_list:
    print(f"image/{x}")
elif x in app_list:
    print(f"application/{x}")
elif x == "txt":
    print("text/plain")
else:
    print("application/octet-stream")