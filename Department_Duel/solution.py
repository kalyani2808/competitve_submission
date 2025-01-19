"""Problem: Department Duel 
Principal of VIIT wants to know who are the best at programming: CSE or ACSE. 
CSE says HOD of CSE. ACSE says HOD of ACSE.
To find out who are better, the principal suggests conducting a coding contest which consists of 5 questions, each carrying 100 marks. 
You have to determine which department won the contest based on the average scores of the students.
The winner is declared by calculating the average of each department’s scores. The higher average percentage wins and is declared the best programmers.

Input Specification:
- input1: Two space-separated integers, denoting the number of students in CSE and ACSE respectively.
- input2: An array of integers representing the scores of the CSE students.
- input3: An array of integers representing the scores of the ACSE students.
The scores of non-participating students are taken as 0.

Output Specification:
Return 'CSE' if CSE wins, 'ACSE' if ACSE wins, otherwise return 'Tie'.

Example 1:
Input:
3 2
100 90 85
100 80
Output:
CSE

Example 2:
Input:
2 3
50 60
40 30 70
Output:
ACSE
"""

# Input parsing
cse_students, acse_students = map(int, input().split())
cse_scores = list(map(int, input().split()))
acse_scores = list(map(int, input().split()))

# Total students for CSE and ACSE
total_cse_students = cse_students
total_acse_students = acse_students

# Calculate average for CSE and ACSE
cse_average = sum(cse_scores) / total_cse_students
acse_average = sum(acse_scores) / total_acse_students

# Compare averages and output the result
if cse_average > acse_average:
    print("CSE")
elif acse_average > cse_average:
    print("ACSE")
else:
    print("Tie")
