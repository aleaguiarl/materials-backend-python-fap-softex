sex = int(input("Insert your gender:\n1 - Male\n2 - Female\n"))
height = float(input("\nInsert the height in meters(ex. 1.76): "))
ideal_weight = 72.7 * height - 58

if sex == 1:
    ideal_weight = 72.7 * height - 58
    print(f"\n+------------------------------+")
    print(f"The ideal weight for a male person {height}m tall is {ideal_weight:.2f}kg")
    print(f"+------------------------------+")
elif sex == 2:
    ideal_weight = 62.1 * height - 44.7
    print(f"\n+------------------------------+")
    print(f"The ideal weight for a female person {height}m tall is {ideal_weight:.2f}kg")
    print(f"+------------------------------+")
else:
    print("Error: Invalid input in sex identification.")