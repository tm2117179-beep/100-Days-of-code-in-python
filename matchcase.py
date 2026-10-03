grade = input("enter the grade: ")

match grade:
    case "A" | "B":
        print("Excellent")
    case "C":
        print("Good")
    case _:
        print("Needs Improvement")