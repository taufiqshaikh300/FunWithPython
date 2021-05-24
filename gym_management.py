print("WELCOME")
users = int(input("Press '1' for Harry "
                  "Press '2' for Hammad "
                  "Press '3' for Rohan :  "))
def getdate():
    import datetime
    return datetime.datetime.now()

if users == 1:
    log = int(input("Enter '1' for diet "
                    "Enter '2' for exerxise :"))
    if log == 1:
        data = int(input("enter '1' for adding data "
                         "enter '2' for retriving data :"))
        if data == 1:
            with open("HeryDiet.txt","a") as f:
                data1 = input("Enter Diet : ")
                f.write(str(getdate())+" "+ str(data1))
        elif data == 2:
            with open("HeryDiet.txt", "r")as f:
                print(f.read())
    elif log == 2:
        data = int(input("enter '1' for adding data"
                         "enter '2' for retriving data :"))
        if data == 1:
            with open("HeryExercise.txt", "a") as f:
                data1 = input("Enter Exercise : ")
                f.write(str(getdate()) + " " + str(data1)+"\n")
        elif data == 2:
            with open("HeryExercise.txt", "r")as f:
                print(f.read())
if users == 2:
    log = int(input("Enter '1' for diet "
                    "Enter '2' for exerxise :"))
    if log == 1:
        data = int(input("enter '1' for adding data "
                         "enter '2' for retriving data :"))
        if data == 1:
            with open("RohanDiet.txt","a") as f:
                data1 = input("Enter Diet : ")
                f.write(str(getdate())+" "+ str(data1))
        elif data == 2:
            with open("RohanDiet.txt", "r")as f:
                print(f.read())
    elif log == 2:
        data = int(input("enter '1' for adding data"
                         "enter '2' for retriving data :"))
        if data == 1:
            with open("RohanExercise.txt", "a") as f:
                data1 = input("Enter Exercise : ")
                f.write(str(getdate()) + " " + str(data1)+"\n")
        elif data == 2:
            with open("RohanExercise.txt", "r")as f:
                print(f.read())
if users == 3:
    log = int(input("Enter '1' for diet "
                    "Enter '2' for exerxise :"))
    if log == 1:
        data = int(input("enter '1' for adding data "
                         "enter '2' for retriving data :"))
        if data == 1:
            with open("HammadDiet.txt","a") as f:
                data1 = input("Enter Diet : ")
                f.write(str(getdate())+" "+ str(data1))
        elif data == 2:
            with open("HammadDiet.txt", "r")as f:
                print(f.read())
    elif log == 2:
        data = int(input("enter '1' for adding data"
                         "enter '2' for retriving data :"))
        if data == 1:
            with open("HammadExercise.txt", "a") as f:
                data1 = input("Enter Exercise : ")
                f.write(str(getdate()) + " " + str(data1)+"\n")
        elif data == 2:
            with open("HammadExercise.txt", "r")as f:
                print(f.read())