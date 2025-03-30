try:
    numarator = float(input("Enter the Numarator: "))
    denominator = float(input("Enter the Denominator: "))

    if denominator == 0:
        raise ZeroDivisionError("Denominator zero not allowed")
    
    result = numarator / denominator
    print(f"The result is : {result}")
except ZeroDivisionError as e:
    print(e)
except ValueError:
    print("Invalid input!, please Enter a valid input")