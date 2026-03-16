# Day 1 Python Task: Student Score Analyzer

# Write a Python program that analyzes a list of student scores.

# Given Data

# Create a list called scores containing at least 7 student scores.

# Example format (you choose the values):

# scores = [...]
# Requirements

# Your program must implement the following functions.

# 1️⃣ Count Passing Students

# Create a function:

# count_pass(scores)

# It should return how many students scored 50 or above.

# 2️⃣ Count Failing Students

# Create a function:

# count_fail(scores)

# It should return how many students scored below 50.

# 3️⃣ Find the Highest Score

# Create a function:

# highest_score(scores)

# It should return the highest score in the list.

# 4️⃣ Calculate Average Score

# Create a function:

# average_score(scores)

# It should return the average score of all students.

# Final Output

# Print the following information:

# Total Students:
# Passed:
# Failed:
# Highest Score:
# Average Score:
# Constraints

# Do not use built-in functions like:

# max()
# sum()

# Use:

# loops

# conditions

# variables

# functions

# Bonus Challenge (Optional)

# Extend the program to count grades:

# Grade A : >= 80
# Grade B : 60–79
# Grade C : 50–59
# Fail : < 50

# Print how many students fall into each category.


scores = [98,34,56,77,32,40,60]

def count_pass(scores):
    passed = 0
    for score in scores:
        if score >= 50:
            passed += 1
    return passed

def count_fail(scores):
    failed = 0
    for score in scores:
        if score < 50:
            failed += 1
    return failed


def highest_score(scores):
    highest = scores[0]
    for score in scores:
        if score > highest:
            highest = score
    return highest



def average_score(scores):
    total = 0
    for score in scores:
        total += score
    avg = total / len(scores)
    return avg

def getGrade(scores):
    gradeA = 0
    gradeB = 0
    gradeC = 0
    failed = 0
    for score in scores:
        if score >= 80:
            gradeA += 1
        elif score >=60:
            gradeB += 1
        elif score >=50:
            gradeC += 1
        else:
            failed += 1
    print(f"{gradeA} students got Grade A \n")
    print(f"{gradeB} students got Grade B \n")
    print(f"{gradeC} students got Grade C \n")
    print(f"{failed} students failed\n")


passed_count = count_pass(scores)
failed_count = count_fail(scores)
highest = highest_score(scores)
average = average_score(scores)

print(f"Passed student: {passed_count}\n")
print(f"Failed student: {failed_count}\n")
print(f"Highest Score: {highest}\n")
print(f"Average Score: {average}\n")
getGrade(scores)