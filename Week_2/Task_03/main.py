import json


def average_score(**students):
    result = dict()
    for student in students:
        avg_score = sum(students[student]) / len(students[student])
        result.update({student: avg_score})
    return result

def unique_grades(**students):
    result = set()
    for student in students:
        result.update(students[student])
    return result


file_path = "data"
with open(file_path) as json_file:
    data = json.load(json_file)


print("Average score for every student:")
print(average_score(**data))
print(f"Unique grades:")
grades = unique_grades(**data)
print(grades)
print(f"Total of {len(grades)} grades")