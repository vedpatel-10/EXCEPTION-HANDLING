def get_input():
    while True:
        try:
            num = int(input("Enter a number: "))
            break
        except ValueError:
            print("Enter a number !!")
        
    print("You have entered the number : ", num)            

get_input()    

#OUTPUT:
# Enter a number: ved
# Enter a number !!
# Enter a number: patel
# Enter a number !!
# Enter a number: 209
# You have entered the number :  209
