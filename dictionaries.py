from collections import defaultdict


student = {"name": "Alice", "age": 24, "major": "Computer Science"}

print(student["name"])

student["grade"] = "A"
student['age'] = 25
del student["major"]

print(student)
print()

course = {"title": "Python Basics",
          "instructor": "Dr.smith", "duration": 10, "student": 50}
for key, value in course.items():
    print(f"Key:{key},Value:{value}")
print()
key_to_check = "duration"
if key_to_check in course:
    print("Key Exists!")
else:
    print("Key does not exist")
new_info = {'level': 'Beginner', 'credits': 3}
course.update(new_info)
print(course)
print()

# Create a dictionary called cubes where the keys are numbers from 1 to 5, and the values are the cubes of those numbers.

cubes = {i: i**3 for i in range(1, 6)}
print(cubes)
# Create a dictionary called char_count that counts the number of occurrences of each character in the string "hello world"
string_name = "hello world"


char_count = {char: string_name.count(char) for char in set(string_name)}
print(char_count)

list = ["apple", "banana", "apple", "orange", "banana", "apple"]

word_count = defaultdict(int)

for i in list:
    word_count[i] += 1

print(word_count)

school = {
    'class1': {'students': 20, 'teacher': 'Mrs. Smith'},
    'class2': {'students': 25, 'teacher': 'Mr. Brown'}
}

school["class3"] = {'students': 22, 'teacher': 'Ms Johnson'}

student_num = school["class2"]["students"]

print(student_num)
print()

is_principal = school.get("principal", "Not Assigned")
print(is_principal)
print()

dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}

dict3 = dict1 | dict2
print(dict3)
print()

team = {
    'team1': {
        'members': ['Alice', 'Bob'], 'project': 'AI Research'},
    'team2': {
        'members': ['Carol', 'Dave'], 'project': 'Web Development'}
}

for teamname, members in team.items():
    print(teamname)
    for membername, projectname in members.items():
        print(membername, projectname)

        # for members, membername in members.items():
    #     print(f"member name:{membername}")
    #     for membername, projectname in membername.items():
    #         print(projectname)
