
cont = "y"
while cont == "y":
    name = input("Enter student's name: ")
    marks = input("Enter marks: ")
    f = open("students.txt","a")
    f.write(name + "-" + marks + "\n")
    f.close()
    cont = input("Do you want to add another student? (y/n): ")

if cont == "n":
    print("Thank you for using this program")