import Switcher as a

n = 1
while n == 1:
    print("*******Welcome!, please select an option*****")
    print("To register, choose option 1")
    print("To delete an attended name, choose 2")
    print("To find out if there are pending registrations, choose 3")
    print("To know the number of missing patients, choose 4")
    print("To know the names of the upcoming patients, choose 5")
    print("To finish the programg, choose 6")
    print(" ")
    
    option = input()
    z = a.Switcher()
    z.numbers_of_options(option)
