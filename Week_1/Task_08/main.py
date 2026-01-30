"""
Завдання 8. Виконати завдання 7 із застосуванням бібліотеки Pandas, зберігаючи дані
про студентів у зовнішньому файлі.
"""

import pandas as pd
import json

file_path = 'data'

with open(file_path) as file:
    content = json.load(file)
    marks = content[0]
    students = content[1]


df = pd.DataFrame(marks, index=students)
print(f"The average mark for every student is: ")
print(df.mean(axis=1))
print("\nThe average mark for every discipline is: ")
print(df.mean(axis=0))