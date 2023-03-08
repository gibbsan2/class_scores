#
# Class_Scores.py
# Author: Antonia Gibbs
# Date: 02/03/2023

# Useful Print Statments (But Unused)
  # the lowest score for each class & combined
    # print("The lowest score in class A is: {}".format(lowest_score))
    # print("The lowest score in class B is: {}".format(lowest_score))
    # print("The lowest score in both classes is therefore: {}".format(lowest_score))

  # the highest score for each class & combined
    # print("The highest score in class A is: {}".format(highest_score))
    # print("The highest score in class B is: {}".format(highest_score))
    # print("The highest score in both classes is therefore: {}".format(highest_score))

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
  print("3. Modify Score")
  option = float(input("Enter option: ").strip())
  if option == 2:
    # Skip this step
    print("Let's continue")
    break
  elif option == 1:
    # Enter students score
    user = int(input("Enter your test score: ").strip())
  elif option == 3: # Allow user to modify a list
    three = True
    while three == True:
      print("Which Class would you like to modify?")
      print("1. Class_A")
      print("2. Class_B")
      print("3. Skip")
      option = float(input("Enter option: ").strip())
      if option == 3:
        # Skip this step
        print("Let's move on")
        break
      elif option == 1:
        # Let user modify list
        original = int(input("Enter your original test score from Class A: ").strip)
        print (original)
        modify = int(input("Enter your modified test score from Class A: ").strip)
        print(modify)
        for score in Class_Combined:
          if score[0] == original:
            score [0] = modify
            break
          else:
            Class_Combined.append(modify)
      elif option == 2:
        # Let user modify list
        original = int(input("Enter your original test score from Class B: ").strip)
        print (original)
        modify = int(input("Enter your modified test score from Class B: ").strip)
        print(modify)
    
      elif option == 3:
        three = True

  # Allow the user to append the list
  Class_Combined.append(user)
  print("\nList of Combined Class Scores")
  print (Class_Combined)
  repeat = False

# Starter Code - start
""" Define functions for minimum scores """
def class_a_minimum(scores_a):
  # Find the lowest score in Class A
    scores_a = min (Class_A)
  #return the minimum
    return scores_a

def class_b_minimum(scores_b):
  # Find the lowest score in Class B
    scores_b = min (Class_B)
  #return the minimum
    return scores_b

def minimum(scores):
  # Find the lowest score in both classes combined
    scores = min (Class_Combined)
  #return the minimum
    return scores

""" Define functions for Maximum scores """
def class_a_maximum(scores_a):
  # Find the highest score in Class A
    scores_a = max (Class_A)
  #return the maximum
    return scores_a

def class_b_maximum(scores_b):
  # Find the highest score in Class B
    scores_b = max (Class_B)
  #return the maximum
    return scores_b

def maximum(scores):
  # Find the highest score in both classes combined
    scores = max (Class_Combined)
  #return the maximum
    return scores

""" Define function for average of all the scores combined """
def average(scores):
  total = 0
  count = 0
  for pupil in Class_Combined: # iterating through a list
    total += pupil # Total up the scores
    count += 1 # Count the number of scores
  # return the total divided by the number
    return(total/count)
  # Define variables for the mean of the scores
    mean = total/count
  # Print out the mean as a statement
  print("The mean is: {:.2f}".format(mean))

# Main rountine
if __name__ == "__main__":
    class_a = [44, 33, 28, 47, 12, 28, 32, 31, 11, 39, 40, 26, 36]
    class_b = [19, 26, 38, 31, 30, 42, 44, 14, 27, 43, 46, 49, 24, 26, 36]
    scores = class_a+class_b    # join two lists together
    print("The average is {}".format(average(scores)))
    print("The minimum is {}".format(minimum(scores)))
    print("The maximum is {}".format(maximum(scores)))
# Starter Code - Stop