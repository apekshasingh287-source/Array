# Program to process an array of scores

scores = list(map(float, input("Enter scores separated by spaces: ").split()))

if len(scores) == 0:
    print("No scores entered.")
else:
    total = sum(scores)
    average = total / len(scores)

    print("\nScores:", scores)
    print("Sum of scores:", total)
    print("Average of scores:", average)
