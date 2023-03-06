#
# Class_Scores.py
# Author: Antonia Gibbs
# Date: 02/03/2023

# declaring my 2 lists
Class_A = [44, 33, 28, 47, 12, 28, 32, 31, 11, 39, 40, 26, 36]
Class_B = [19, 26, 38, 31, 30, 42, 44, 14, 27, 43, 46, 49, 24, 26, 36]

# Combine the 2 lists
Class_Combined = Class_A + Class_B
print(Class_Combined)

# Ask the user to enter a score of press no to continue
repeat = True
while repeat == True:
        print("Welcome to my Class Scores program")
        print("1. Enter Score")
        print("2. Skip")
        option = float(input("Enter option: "))
        if option == 2:
          # Skip this step
          print("Let's Continue")
          break
        elif option == 1:
          # Enter students score
          user = int(input("Enter your test score: "))

          # Allow the user to append the list
          Class_Combined.append(user)
          print("\nList of Combined Class Scores")
          print (Class_Combined)
          repeat = False
  
code = True
while code ==True:
  # Define variables for the mean of the scores
  total = 0
  count = 0

  # mean
  for pupil in Class_Combined:
    total += pupil
    count += 1
    
    # Calculate the mean
    mean = total/count
  # Print out the mean as a statement
  print("The mean is: {:.2f}".format(mean))

  # the lowest score for each class & combined
  lowest_score = min (Class_A)
  print("The lowest score in class A is: {}".format(lowest_score))

  lowest_score = min (Class_B)
  print("The lowest score in class B is: {}".format(lowest_score))

  lowest_score = min (Class_Combined)
  print("The lowest score in both classes is therefore:    {}".format(lowest_score))

  # the highest score for each class & combined
  highest_score = max (Class_A)
  print("The highest score in class A is: {}".format(highest_score))

  highest_score = max (Class_B)
  print("The highest score in class B is: {}".format(highest_score))

  highest_score = max (Class_Combined)
  print("The highest score in both classes is therefore: {}".format(highest_score))
  code == False