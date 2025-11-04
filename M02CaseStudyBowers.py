# M02 Lab Case Study: if... else and while
# Jennifer Bowers 11/1/2025
# M02CaseStudyBowers.py
# This program determines if a student is part of the dean's list and honor roll.

import os
os.system("cls") # Clears the ouput (terminal) screen

print("\nThis will determine if the student has made it onto the Dean's list and/or Honor Roll.\n")

def deanHonor(name):
    firstName = input("Please enter the student's first name: ")
    gpa = input("Please enter the student's GPA: ")

    try:  # Tests if the GPA value is a float number
        float(gpa) # If true, the gpa is converted to a float
        gpa = float(gpa) 

        if 0 <= gpa <= 4:  # Tests to make sure the GPA is in the valid range

            if 3.5 <= gpa:  # Tests if the GPA is on the Dean's List range
                print(firstName + " " + lastName + " has made the Dean's list and the Honor Roll!\n")

            elif 3.25 <= gpa < 3.5:  # Tests if the GPA is on the Honor Roll range
                print(firstName + " " + lastName + " has made the Honor Roll!\n")

            else:  # (gpa < 3.25) Returns a statement that the student wasn't on either list
                print("Sorry, " + firstName + " " + lastName + " has not made either list.\n")

        else:  # Returns that the GPA was not in the correct number range.
            print("The gpa value of " + str(gpa) + " is not value between 0.0 and 4.0.\n")

    except ValueError:  # Returns that the GPA was not a float
        print("The gpa value of " + str(gpa) + " is not a valid number.\n")



# Begins defining the first student's last name to start the program
lastName = input("Please enter the student's last name: ")

# Looping the code until the lastName is entered as "ZZZ" or "zzz"
while lastName != "ZZZ" and lastName != "zzz":
   
   # Activates the deanHonor function to test the GPA
   deanHonor(lastName)

   # Test to repeat the while loop
   lastName = input("Please enter the next student's last name: ")

# Terminated program message
print("\nThanks for using this program. Have a great day!\n") 