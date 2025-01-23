## **Python Cheat Sheet: Common Scripts and Functions**

### **1. File Operations**
- **Read and Write Files**
```python
# Reading a file
with open('file.txt', 'r') as file:
    content = file.read()

# Writing to a file
with open('file.txt', 'w') as file:
    file.write('Hello, World!')
```

- **Working with CSV Files**
```python
import csv

# Reading CSV
with open('data.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

# Writing CSV
with open('data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Name', 'Age'])
    writer.writerow(['Alice', 30])
```

---

### **2. Data Analysis (Pandas)**
- **Basic Pandas Operations**
```python
import pandas as pd

# Load CSV
df = pd.read_csv('data.csv')

# Display DataFrame
print(df.head())

# Basic Stats
print(df.describe())

# Filter Data
filtered_df = df[df['Age'] > 25]
```

- **Export DataFrame to CSV**
```python
df.to_csv('output.csv', index=False)
```

---

### **3. Data Visualization (Matplotlib)**
```python
import matplotlib.pyplot as plt

# Line Plot
plt.plot([1, 2, 3], [4, 5, 6])
plt.title('Line Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()

# Bar Chart
categories = ['A', 'B', 'C']
values = [10, 15, 7]
plt.bar(categories, values)
plt.title('Bar Chart')
plt.show()
```

---

### **4. GitHub Repository Management**
- **List All Files in a Directory**
```python
import os

# List files
for root, dirs, files in os.walk('.'):
    for file in files:
        print(file)
```

- **Write a README.md Template**
```python
readme_content = """
# Project Title
A brief description of what this project does and who it's for.

## Installation
```bash
pip install -r requirements.txt
```

## Usage
```bash
python script.py
```
"""

with open('README.md', 'w') as file:
    file.write(readme_content)
```

---

### **5. Data Processing**
- **Process JSON Files**
```python
import json

# Read JSON
with open('data.json', 'r') as file:
    data = json.load(file)

# Write JSON
with open('output.json', 'w') as file:
    json.dump(data, file, indent=4)
```

- **Basic String Operations**
```python
# String Formatting
name = 'Alice'
age = 30
print(f'My name is {name} and I am {age} years old.')

# Replace Words
text = "Hello World"
print(text.replace("World", "Python"))
```

---

### **6. Scripts for Game Development**
- **Basic Random Generator**
```python
import random

# Random number between 1 and 100
print(random.randint(1, 100))

# Random choice from a list
choices = ['Apple', 'Banana', 'Cherry']
print(random.choice(choices))
```

- **Basic Timer**
```python
import time

start_time = time.time()

# Code block
time.sleep(2)

end_time = time.time()
print(f'Execution time: {end_time - start_time} seconds')
```

---

### **7. Automation with Python**
- **Rename Files in a Directory**
```python
import os

directory = 'path/to/directory'

for count, filename in enumerate(os.listdir(directory)):
    src = f"{directory}/{filename}"
    dst = f"{directory}/file_{count}.txt"
    os.rename(src, dst)
```

- **Send an Email**
```python
import smtplib

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login('your_email@gmail.com', 'your_password')
server.sendmail('from_email@gmail.com', 'to_email@gmail.com', 'Subject: Hello\n\nThis is a test email.')
server.quit()
```

---

### **8. Debugging Tips**
- **Using `pdb`**
```python
import pdb

def buggy_function(x):
    pdb.set_trace()  # Add breakpoint
    return x / 0

buggy_function(5)
```

- **Printing Variables**
```python
var = 42
print(f'Debug: var = {var}')
```

---

### **9. Math and Algorithms**
- **Basic Math**
```python
import math

print(math.sqrt(16))  # Square root
print(math.factorial(5))  # Factorial
```

- **Sorting a List**
```python
numbers = [3, 1, 4, 1, 5]
sorted_numbers = sorted(numbers)
print(sorted_numbers)
```

---

### **10. Key Python One-Liners**
- **List Comprehensions**
```python
squared_numbers = [x**2 for x in range(10)]
print(squared_numbers)
```

- **Lambda Functions**
```python
add = lambda x, y: x + y
print(add(3, 5))
```

- **Zip Two Lists**
```python
names = ['Alice', 'Bob']
ages = [30, 25]
print(dict(zip(names, ages)))
