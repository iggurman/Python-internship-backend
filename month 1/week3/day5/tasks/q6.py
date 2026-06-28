try:
    file = input("Enter filename: ")

    f = open(file)

    print(f.read())

    f.close()

except FileNotFoundError:
    print("File Not Found")