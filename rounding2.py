def add_one(someVarible): 
    someVarible[0] = someVarible[0] + 1 
    someVarible[1] = someVarible[1] + 2
    
def main(): 
    # this functions gets an input 
    someNumber = []
    # input 
    temp_num = int(input("enter a number: "))
    someNumber.append(temp_num)
    someNumber.append(temp_num)
    add_one(someNumber)
    add_one(someNumber)
    print(someNumber[0])
    print(someNumber[1])

    
if __name__ == "__main__":
        main()