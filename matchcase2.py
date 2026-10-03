fruit = input("enter the fruit: ")

match fruit:
    case "Apple":
        print("fruit is apple")
    case "Banana":
        print("fruit is banana")
    case _:
        print("unknown fruit")
    
