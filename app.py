# course = "AI and Machine Learning"
# print(len(course))
# print(course[0])
# print(course[0-3])
# print(course[0:5])
# print(course[-1x₹:0])

import statistics
print("Welcome to Python!")

# First test in Python - Basic If statement
score = 85
if score >= 60:
    print("Passed")
# 2nd test  for basic if statement
balance = 1000
if balance > 500:
    print("Sufficient balance")


fruits = ['apple', 'banana', 'cheery']
print('Original list', fruits)

fruits.insert(1, 'mango')
print('Appended list', fruits)

fruits.insert(0, 'grape')
print('print at statrt:', fruits)

more_fruits = ['melon', 'orange']
fruits.extend(more_fruits)
print('after extend', fruits)
fruits.insert(0, more_fruits)  # check this
print('print extended at start', fruits)

# fruits.pop(1)
print(fruits)
print(fruits.index('mango'))
print(fruits.index('melon'))

print(fruits.index('apple'))

fruits2 = ['fig', 'pom']
fruits2.append(more_fruits)
print('after append', fruits2)

Customer_Feedback_option = ['good', 'bad', 'Excellent']
print(Customer_Feedback_option)
Customer_Feedback_option.pop(-1)
print(Customer_Feedback_option)


Shop_cart = ['mouse', 'cpu', 'pencil']
print(Shop_cart)
Shop_cart.insert(1, 'Monitor')
print("after inser:", Shop_cart)
Extend_cart = ["table", 'desk']
print(Extend_cart)
Shop_cart.extend(Extend_cart)
print(Shop_cart)
last_item = Shop_cart.pop()
print("Removed", last_item)
print(Shop_cart, "ast_item")

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(numbers[0::2])
print(numbers[0::2])

print(numbers[1::2])
print(numbers[0::4])
print("Reversed", numbers[::-1])
print("Reversed", numbers[-1])
print("Reversed last 4", numbers[-4:][::-1])
print("sampek", numbers[2:9:2])
print("sampek", numbers[1:-1:1])

print("Exeercise 2")
numbers_Ex2 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print(numbers_Ex2)
print(numbers_Ex2[-5])

print("Reverse ex2 list", numbers_Ex2[::-1])
print("element 2 to 7", numbers_Ex2[2:7:2])
print("last 5 revers", numbers_Ex2[-5:][::-1])
print("ecept first and last", numbers_Ex2[1:][:-1])

print("last 5 revers even digit", numbers_Ex2[-5:][::-2])
print(numbers+numbers_Ex2)
print(100 in numbers_Ex2)

food_list1 = ['soya', 'paneer', 'yogurt']
print(food_list1)
food_list2 = ['sambar', 'rasam', 'curd']
print("combined", food_list1 + food_list2)
print(food_list1 * 2)
print("Python " * 5)
print('rasam' in food_list2)
print(food_list1 == food_list2)


print("Matrix")
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matrix)
print(type(matrix))
print(matrix[0][1])
print(matrix[1][2])
print(matrix[0])
matrix[1] = [40, 50, 60]
matrix[2][1] = 80
print("after update", matrix)

print("Exercise 4")
stud_matrix = [
    ['nams', 'math', 'Science', 'english'],
    ['alice', 80, 81, 82],
    ['bob', 90, 89, 79],
    ['cook', 65, 87, 76]
]
print(stud_matrix)
print("Name of 2nd student", stud_matrix[1][0])
print("math grade of 3rd student", stud_matrix[3][1])
stud_matrix[1][3] = 96
print(stud_matrix)
new_row = ['dan', 83, 88, 45]
stud_matrix.append(new_row)
print(stud_matrix)
for row in stud_matrix[1:]:
    print(row[0])


print("List and exercise 5")
list1 = [1, 2, 3]
list2 = list1
list3 = list1.copy()
list1.append(4)
list2.append(5)
list3.append(6)
print("List1:", list1)
print("List2:", list2)
print("List3:", list3)

print("sort vs sortes")
numbr = [4, 1, 7, 5, 6, 9]
numbr.sort()
print(numbr)
# numbr.sort(reverse=True)
print(numbr)
sorted_numbr = sorted(numbr, reverse=True)
print(sorted_numbr)
print(numbr)

print("Statistical Functions")
numbers = [5, 2, 8, 1, 9, 3]
print("numbers", numbers)
print("Minimum number", min(numbers))
print("Minimum number", max(numbers))
print("Minimum number", len(numbers))
print("Minimum number", sum(numbers))
print("Minimum number", sum(numbers)/len(numbers))
print(dir(statistics))
print("std DEv", statistics.stdev(numbers))

print("Practice test 7")
Test_score = [35, 56, 76, 98, 21]
print("the highest and lowest scores are :", "high",
      (max(Test_score)), "and low is", min(Test_score))
print("the Total  and avergae scores are :", "Total", (sum(Test_score)),
      "and Average is", sum(Test_score)/len(Test_score))
passed_list = [pass_score >= 40 for pass_score in Test_score]
print(passed_list)
print("has all passed", all(passed_list))
print("has any passed", any(passed_list))


print("basic Unpacking")
a, b, c = ['apple', 'boy', 'cat']
print("a for:", a, "b for", b, "c for", c)

# Get first and rest
numbers = [1, 2, 3, 4, 5]
first, *rest = numbers

print("First:", first)
print("Rest:", rest)

# Get first, middle, and last
first, *middle, last = numbers
print("First:", first)
print("Middle:", middle)
print("Last:", last)

# 1. Create a list and unpack into variables
values = [100, 200, 300]
a, b, c = values
print("a:", a, "b:", b, "c:", c)


# 2. Swap two variables using tuple unpacking
x = 10
y = 20
x, y = y, x
print("After swapping -> x:", x, "y:", y)


# 3. Unpack a list of 6 numbers into first, middle, and last
numbers = [1, 2, 3, 4, 5, 6]
first, *middle, last = numbers
print("First:", first)
print("Middle:", middle)
print("Last:", last)


# 4. Unpack a student record into name and grades
student = ['Alice', 85, 90, 88]
name, *grades = student
print("Name:", name)
print("Grades:", grades)


# Comprehensive exercise for List
stud_matrix = [
    ['nams', 'math', 'Science', 'english'],
    ['alice', 80, 81, 82],
    ['cook', 65, 87, 76],
    ['bob', 90, 89, 79],
    ['dan', 83, 88, 45]
]
print("All student data", stud_matrix)
print((stud_matrix[1]))
print((stud_matrix[2]))
print((stud_matrix[3]))
print((stud_matrix[4]))
# print("Average of:", stud_matrix[1][0], "is", sum(stud_matrix[1][1]+sum(stud_matrix[1][2]+sum(stud_matrix[1][3])))
Stud1_sum = (stud_matrix[1][1], stud_matrix[1][2], stud_matrix[1][3])
print("Average of ", stud_matrix[1][0], "-", (sum(Stud1_sum))/(len(Stud1_sum)))
Stud2_sum = (stud_matrix[2][1], stud_matrix[2][2], stud_matrix[2][3])
print("Average of ", stud_matrix[2][0], "-", (sum(Stud2_sum))/(len(Stud2_sum)))
Stud3_sum = (stud_matrix[3][1], stud_matrix[3][2], stud_matrix[3][3])
print("Average of ", stud_matrix[3][0], "-", (sum(Stud3_sum))/(len(Stud3_sum)))
Stud4_sum = (stud_matrix[4][1], stud_matrix[4][2], stud_matrix[4][3])
print("Average of ", stud_matrix[4][0], "-", (sum(Stud4_sum))/(len(Stud4_sum)))
Max_Math = (stud_matrix[1][1], stud_matrix[2][1],
            stud_matrix[3][1], stud_matrix[4][1])
print("Max of math score is", max(Max_Math))
Copy_matrix = stud_matrix.copy()
# Copy_matrix.sort()
header = Copy_matrix[0]
print("header", header)
data = Copy_matrix[1:]
print("data", data)
data.sort()
print("sorted", data)
new_student = ['Eva', 76, 87, 99]
stud_matrix.append(new_student)
print(stud_matrix)
stud_matrix[1][3] = 28
print(stud_matrix)
for student in stud_matrix[1:]:
    name = student[0]
    marks = student[1:]
    average = sum(marks) / len(marks)
    print(student)
    print("the avg of student", name, "is", average)

stud_matrix = [
    ['nams', 'math', 'Science', 'english'],
    ['alice', 80, 81, 82],
    ['cook', 65, 87, 76],
    ['bob', 90, 89, 79],
    ['dan', 83, 88, 45]
]

math_score = [student[1] for student in stud_matrix[1:]]
highest_math = max(math_score)
print("highest math score", highest_math)

Tuple_numbr = (4, 1, 7, 4, 5, 6, 9, 4)
count_4 = Tuple_numbr.count(4)
print(count_4)
count_1 = Tuple_numbr.index(7)
print(count_1)


my_tuple = (1, 3, 6, 5, 4, 7)
print("is 5 in the tuple", 5 in my_tuple)

tuple_1 = (1, 2, 3)
tuple_2 = (1, 3, 2)
print("tuple1 ==== tuple 2 is", tuple_1 == tuple_2)

data = (10, 20, 30, 40, 50, 60, 70, 80, 90, 100)
print("Reversed", data[::-1])

students = (
    ('Alice', 85, 90, 88),
    ('Bob', 78, 82, 80),
    ('Charlie', 92, 95, 93),
    ('David', 88, 85, 90)
)
name, math, science, english = students

print("All students info", students)

# for student in students:
# print(f" student 1", students[0])
# print(f" student 2", students[1])
# print(f" student 3", students[2])
# print(f" student 4", students[3])
for student in students:
    print(student)
    name = student[0]
    math = student[1]
    science = student[2]
    english = student[3]
    average = (math + science + english) / 3
    print(name, average)


students = (('Alice', 85, 90, 88), ('Bob', 78, 82, 80),
            ('Charlie', 92, 95, 93), ('David', 88, 85, 90))
math_score = []
math_score.append(student[1])
highest_math = max(math_score)
print("highest math score is", highest_math)


students = (
    ('Alice', 85, 90, 88),
    ('Bob', 78, 82, 80),
    ('Charlie', 92, 95, 93),
    ('David', 88, 85, 90)
)

# Collect math scores
math_scores = []

for student in students:
    math_scores.append(student[1])

# Use max()
highest_math = max(math_scores)

print("Highest math score:", highest_math)


students = (
    ('Alice', 85, 90, 88),
    ('Bob', 78, 82, 80),
    ('Charlie', 92, 95, 93),
    ('David', 88, 85, 90)
)
first_student = students[0]
name, math, science, english = first_student
print(name)
print(math)
print(english)
names = ()
for student in students:
    names = names + (student[0],)
print(names)
names = ()

for student in students:
    names = names + (student[0],)

print("Student names:", names)

print("------------------------")


numbers = {1, 2, 3, 4, 5}
print("Original:", numbers)

removed = numbers.pop()
print("Popped:", removed)
print("After pop:", numbers)
numbers = {1, 2, 3, 4, 5}
print("Original:", numbers)

removed = numbers.pop()
print("Popped:", removed)
print("After pop:", numbers)

python_course = {'Alice', 'Bob', 'Charlie', 'David'}
java_course = {'Bob', 'David', 'Eve', 'Frank'}
web_course = {'Alice', 'Eve', 'Grace'}
all_students = python_course | java_course | web_course

print(set(all_students))
print(len(set(all_students)))
print(python_course.issubset(all_students))
web_course.add('helen')
print(web_course)
java_course.remove('Bob')
print(java_course)
only_python = python_course.difference(java_course, web_course)
print("Students only in Python:", only_python)
only_one_course = (
    python_course ^
    java_course ^
    web_course
)

print("Students in exactly one course:", only_one_course)
total_students = len(all_students)
print("Total number of unique students:", total_students)
is_subset = python_course.issubset(all_students)
print("Is Python course a subset of all students?", is_subset)
# 🎯 Practice Exercise 9


students = {
    'Alice': {'math': 90, 'science': 85, 'english': 88},
    'Bob': {'math': 75, 'science': 80, 'english': 82},
    'Charlie': {'math': 95, 'science': 92, 'english': 90}
}
print(students['Alice']['math'])
print(students['Bob'])
students['Charlie']['english'] = 95
print(students['Charlie'])
students['Alice']['History'] = 87
print(students['Alice'])

for name in students:
    print(name)
print(students['Alice'])

print()
students = {
    'Alice': [85, 90, 88, 92],
    'Bob': [78, 82, 80, 85],
    'Charlie': [92, 95, 93, 96],
    'David': [65, 70, 68, 72],
    'Eve': [88, 85, 90, 87]
}
students_avg = {}
for student, scores in students.items():
    print(student, ":", scores)
    stud_avg = sum(scores)/len(scores)
    students_avg[student] = stud_avg
    print(f"Avg for {student} is :", stud_avg)
    print()
    if all(score > 85 for score in scores):
        print(" all scores >= 85 are ", student, ":", scores)
print(students_avg)
sorted_rank = sorted(students_avg.items(), key=lambda x: x[1], reverse=True)
print()

print("sorted rank", sorted_rank)
print("Students Ranking")
for rank, (student, avg) in enumerate(sorted_rank, start=1):
    print(rank, ":", student, "-", avg)
print("highest avg is", sorted_rank[0])
print("lowest avg is ", sorted_rank[-1])
avg_80 = 0
for avg in students_avg.values():
    if avg > 80:
        avg_80 += 1


print("count of students > 80 is ", avg_80)


print("-" * 40)
students = {
    'Alice': [85, 90, 88, 92],
    'Bob': [78, 82, 80, 85],
    'Charlie': [92, 95, 93, 96],
    'David': [65, 70, 68, 72],
    'Eve': [88, 85, 90, 87]
}

# 1 & 2: Display and calculate averages
students_avg = {}

print("Student Scores:")
print("-" * 40)

for student, scores in students.items():
    print(student, ":", scores)
    avg = sum(scores) / len(scores)
    students_avg[student] = avg
    print("Average:", avg)
    print()

# 3: Ranking
sorted_students = sorted(
    students_avg.items(),
    key=lambda x: x[1],
    reverse=True
)

print("🏆 Student Ranking")
for rank, (student, avg) in enumerate(sorted_students, start=1):
    print(rank, ":", student, "-", avg)

# 4: Highest & Lowest
print("\nHighest average:", sorted_students[0])
print("Lowest average:", sorted_students[-1])

# 5: Count above 80
count_above_80 = 0
for avg in students_avg.values():
    if avg > 80:
        count_above_80 += 1

print("\nStudents above 80%:", count_above_80)

# 6: All scores > 85
print("\nStudents with all scores > 85:")
for student, scores in students.items():
    for score in scores:
        if score <= 85:
            break
    else:
        print(student, ":", scores)

# 7: Grade report
print("\n📄 Grade Report")
print("-" * 40)
for student, avg in students_avg.items():
    print(f"{student:<10} | Average: {avg:.2f}")


# **Loan Approval Criteria:**
# 1. Age: Must be between 21 and 65
# 2. Income: Minimum $30,000 per year
# 3. Credit Score: Must be >= 650
# 4. Employment: Must be employed
# 5. Existing Loans: Must be <= 2

# **Bonus Conditions:**
# - If credit score >= 750, waive employment requirement
# - If income >= $100,000, allow up to 3 existing loans

# **Your Task:** Write the complete approval logic


age = int(input("Enter your age: "))
income = int(input("Enter your annual income ($): "))
credit_score = int(input("Enter your credit score: "))
employed = input("Are you employed? (Yes/No): ").strip().lower()
existing_loans = int(input("How many existing loans do you have? "))

approved = True   # assume approval first
if age < 21 or age > 65:
    print("NOt eligiblet due to age")
    approved = False

if income < 30000:
    print("Not eligible due to income")
    approved = False


if credit_score < 650:
    print("Not eligible due to Credit score")
    approved = False

if credit_score < 750 and employed.lower() != "yes":
    print("Must be employed or credit score gretaer than 750")
    approved = False

if income >= 100000:
    if existing_loans > 3:
        print(" rejected due to number of loans. Max allowed is 3")
        approved = False
else:
    if existing_loans > 2:
        print(" rejected due to number of loans.Max allowed is 2")
        approved = False

if approved:
    print("\n You are eligible.Loan approved")
else:
    print("\n You are not eligible. Loan not approved")

# library management system
# 1. Add Book with any number of attributes(**args/Kwargs)
# 2. Search Book by passing functions as arguments
# 4. Dcalcukate multiple status of book
# 5. sort using lambda funciton
# 6. filter books usiing custom filter conditions
library = []


def add_book(**book_info):
    library.append(book_info)
    print(f'Book "{book_info.get("title", "Unknown")}" added to the library.')


def search_book(condition_func):
    results = [book for book in library if condition_func(book)]
    return results


def calculate statistics(book):
    stats = {
        "is_long": book.get("pages", 0) > 300,
        "is_classic": book.get("year", 2024) < 2000,
    }
    return stats


def calculate_status(book):
    status = "Available"
    if book.get("pages", 0) > 200:
        status = "Long Book"
    return status


def display_books(books):
    if books:
        print("Books in the library:")
        for book in books:
            print(book)
    else:
        print("No books found.")


# Example usage
add_book(title="Book A", author="Author X", year=2020)
add_book(title="Book B", author="Author Y",
         year=2019, genre="Fiction", pages=300)
