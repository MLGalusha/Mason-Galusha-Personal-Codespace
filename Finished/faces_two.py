def main():
    x = convert_face(input("Input: "))
    print(x)

def convert_face(face):
    for i in face:
        if ":)" in face:
            new_face = face.replace(":)", "🙂" )
            if ":(" in face:
                newer_face = new_face.replace(":(", "🙁" )
                break
            else:
                break
            
        elif ":(" in face:
            new_face = face.replace(":(", "🙁" )
            if ":)" in face:
                newer_face = new_face.replace(":)", "🙂" )
            else:
                break
            
        else:
            break
    return newer_face


if __name__ == "__main__":
    main()


#Heres a lot better and simpilar method to what i was doing
# def main():
#     x = convert_face(input("Input: "))
#     print(x)

# def convert_face(face):
#     face = face.replace(":)", "🙂").replace(":(", "🙁")
#     return face
# if __name__ == "__main__":
#     main()