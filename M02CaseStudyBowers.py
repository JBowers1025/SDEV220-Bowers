# M02 Lab Case Study: if... else and while
# Jennifer Bowers 11/1/2025
# M02CaseStudyBowers.py
# This program determines if a student is part of the dean's list and honor roll.

print("\nThis will determine if the student has made it onto the Dean's list and or Honor Roll.\n")
lastName = input("Please enter the student's last name: ")

while lastName != "ZZZ":
    firstName = input("Please enter the student's first name: ")
    gpa = input("Please enter the student's GPA: ")

    try:
        float(gpa)
        gpa = float(gpa)

        if 0 <= gpa <= 4:

            if 3.5 <= gpa:
                print(firstName + " " + lastName + " has made it on the Dean's list and the Honor Roll!\n")

            if 3.25 <= gpa < 3.5:
                print(firstName + " " + lastName + " has made it on the Honor Roll!\n")

            elif gpa < 3.25:
                print("Sorry, " + firstName + " " + lastName + " has not made it on either list.\n")

        else:
            print("The gpa value of " + str(gpa) + " is not value between 0.0 and 4.0.\n")

    except ValueError:
        print("The gpa value of " + str(gpa) + " is not a valid number.\n")

    lastName = input("Please enter the next student's last name: ")

print("Thanks for using this program. Have a great day!")
