# M02 Lab Case Study: if... else and while
# Jennifer Bowers 11/1/2025
# M02CaseStudyBowers.py
# This program determines if a student is part of the dean's list and honor roll.

import os
os.system("cls") # Clears the ouput (terminal) screen

print("\nThis will determine if the student has made it onto the Dean's list and/or Honor Roll.\n")
# Beginning input to start the program
lastName = input("Please enter the student's last name: ")

# Repeating block of code until the lastName is inputted as 
while lastName != "ZZZ" and lastName != "zzz": # If the value is ZZZ or zzz the program will quit.
    firstName = input("Please enter the student's first name: ")
    gpa = input("Please enter the student's GPA: ")

    try: # Tests if the GPA value is a float number
        float(gpa)
        gpa = float(gpa)

        if 0 <= gpa <= 4: # Tests to make sure the GPA is a valid value

            if 3.5 <= gpa: # Tests if on the Dean's list
                print(firstName + " " + lastName + " has made it on the Dean's list and the Honor Roll!\n")

            elif 3.25 <= gpa < 3.5: # Tests if on the Honor Roll
                print(firstName + " " + lastName + " has made it on the Honor Roll!\n")

            else: # (gpa < 3.25) Returns a statement that the student wasn't on either list
                print("Sorry, " + firstName + " " + lastName + " has not made it on either list.\n")

        else: # Returns that the GPA was not in the correct number range.
            print("The gpa value of " + str(gpa) + " is not value between 0.0 and 4.0.\n")

    except ValueError: # Returns that the GPA was not a float
        print("The gpa value of " + str(gpa) + " is not a valid number.\n")

    lastName = input("Please enter the next student's last name: ") # Repeats the program

print("\nThanks for using this program. Have a great day!\n") # Ends the program
