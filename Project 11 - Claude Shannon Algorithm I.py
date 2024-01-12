# -*- coding: utf-8 -*-
"""Copy of AT-Lesson 11 - Project_Question Copy.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1zmbRsppIod6HkLHjk_a3aplSBisFIhIE

### Instructions

#### Goal of the Project

This project is designed for you to practice and solve the activities that are based on the concepts covered in the following lessons:

  1.  Python List I
  2.  Python List II
  3.  NumPy Arrays I

---

#### Getting Started:

1. Click on this link to open the Colab file for this project.

    Link on Panel?usp=sharing

2. Create a duplicate copy of the Colab file as described below.

  - Click on the **File menu**. A new drop-down list will appear.

   <img src='https://student-datasets-bucket.s3.ap-south-1.amazonaws.com/images/lesson-0/0_file_menu.png' width=500>

  - Click on the **Save a copy in Drive** option. A duplicate copy will get created. It will open up in the new tab on your web browser.

  <img src='https://student-datasets-bucket.s3.ap-south-1.amazonaws.com/images/lesson-0/1_create_colab_duplicate_copy.png' width=500>

3. After creating the duplicate copy of the notebook, please rename it in the **YYYY-MM-DD_StudentName_Project11** format.

4. Now, write your code in the prescribed code cells.

---

#### Activity 1: Find Occurrences of an Element in a List

Create a function that returns the index or indices of all occurrences of an item in the list.

**Note**

- If an element does not exist in a list, return `[]`.

- Lists are zero-indexed.

**Examples**
```
get_indices(["a", "a", "b", "a", "b", "a"], "a") ➞ [0, 1, 3, 5]

get_indices([1, 5, 5, 2, 7], 7) ➞ [4]

get_indices([1, 5, 5, 2, 7], 5) ➞ [1, 2]

get_indices([1, 5, 5, 2, 7], 8) ➞ []
```

Follow the steps given below to achieve the desired result:

  - **Step 1**: Define a function with two parameters, first parameter will be the list of values i.e. `elements_list` and second parameter will be the item to be searched i.e. `key`.

  - **Step 2**: Inside this function, create an empty list to store the result i.e. `result_list`.

  - **Step 3**: Inside the function, `elements_list` list is iterated using `for` loop and `range()` function which traverses till the length of the `elements_list`. Use list indexing here.
  
    1. Inside `for` loop, check whether an element in the `elements_list` matches the item being searched i.e. `key`.
    2. If it matches, then append the index number or position of that item in the `elements_list` to the `result_list`.

    This `for` loop iterates till the end of `elements_list`.

  - **Step 4**: Return the `result_list` list which contains the indices or positions of the item `key` in `elements_list`.

  - **Step 5**: Call the function and pass the list of items and item to be searched to the list as parameters.
"""

def get_indices(elements_list, key):
    result_list = []
    for i in range(len(elements_list)):
        if elements_list[i] == key:
            result_list.append(i)
    return result_list

"""---

#### Activity 2: Subtract Elements of Two Lists

Subtract elements of two lists only if element in the first list is greater than element in second list, else display the element of the first list.  

Examples:
```
Original lists :
[10, 20, 30, 40, 50, 60]
[60, 50, 40, 30, 20, 10]

Output list:
[10, 20, 30, 10, 30, 50]
```
Follow the steps given below to achieve the desired result:

  - **Step 1**: Declare two lists having equal number of random numbers.

  - **Step 2**: Create a third empty list to store the result of subtraction.

  - **Step 3**: Start a `for` loop which iterates till the length of the list.
  
  - **Step 4**: Inside the `for` loop, check whether first list element is greater than the second list element. If the condition is true, subtract the list elements and append it to the third list else just append the first list element to the third list using the `append()` function.

  - **Step 5**: Print first and second lists.

  - **Step 6**: Print the third list to see the subtracted values.
"""

# step 1
list1 = [10, 20, 30, 40, 50, 60]
list2 = [60, 50, 40, 30, 20, 10]

# step 2
result_list = []

# step 3
for i in range(len(list1)):
    # step 4
    if list1[i] > list2[i]:
        result_list.append(list1[i] - list2[i])
    else:
        result_list.append(list1[i])

# step 5
print("List 1:", list1)
print("List 2:", list2)

# step 6
print("Result list:", result_list)

"""---

#### Activity 3: Convert Fahrenheit into Celsius

Write a program to convert the values in Fahrenheit degrees into Celsius degrees.

**Formula**:

```
celsius = (fahrenheit - 32) / 1.8
```

**Example**:

```
Values in Fahrenheit degrees:
[ 0  32   45.21]
Values in Celsius degrees:
[-17.78   0  7.34]
```

Follow the steps given below to achieve the desired result:

  - **Step 1**: Import `numpy` module.

  - **Step 2**: Declare a list with some random numbers which represents the temperatures in Fahrenheit degrees.

  - **Step 3**: Convert the list into NumPy array using `array()` function. Print this array

  - **Step 4**: Use the formula to convert Fahrenheit to Celsius and print the converted values.
"""

import numpy as np

# Step 1: Declare a list of temperatures in Fahrenheit
fahrenheit_list = [0, 32, 45.21]

# Step 2: Convert the list into a NumPy array
fahrenheit_array = np.array(fahrenheit_list)

# Step 3: Print the Fahrenheit array
print("Values in Fahrenheit degrees:")
print(fahrenheit_array)

# Step 4: Convert Fahrenheit to Celsius using the formula
celsius_array = (fahrenheit_array - 32) / 1.8

# Step 5: Print the Celsius array
print("Values in Celsius degrees:")
print(celsius_array)

"""### Submitting the Project:

1. After finishing the project, click on the **Share** button on the top right corner of the notebook. A new dialog box will appear.

  <img src='https://student-datasets-bucket.s3.ap-south-1.amazonaws.com/images/project-share-images/2_share_button.png' width=500>

2. In the dialog box, make sure that '**Anyone on the Internet with this link can view**' option is selected and then click on the **Copy link** button.

   <img src='https://student-datasets-bucket.s3.ap-south-1.amazonaws.com/images/project-share-images/3_copy_link.png' width=500>

3. The link of the duplicate copy (named as **YYYY-MM-DD_StudentName_Project11**) of the notebook will get copied

   <img src='https://student-datasets-bucket.s3.ap-south-1.amazonaws.com/images/project-share-images/4_copy_link_confirmation.png' width=500>

4. Go to your dashboard and click on the **My Projects** option.
   
   <img src='https://student-datasets-bucket.s3.ap-south-1.amazonaws.com/images/project-share-images/5_student_dashboard.png' width=800>

  <img src='https://student-datasets-bucket.s3.ap-south-1.amazonaws.com/images/project-share-images/6_my_projects.png' width=800>

5. Click on the **View Project** button for the project you want to submit.

   <img src='https://student-datasets-bucket.s3.ap-south-1.amazonaws.com/images/project-share-images/7_view_project.png' width=800>

6. Click on the **Submit Project Here** button.

   <img src='https://student-datasets-bucket.s3.ap-south-1.amazonaws.com/images/project-share-images/8_submit_project.png' width=800>

7. Paste the link to the project file named as **YYYY-MM-DD_StudentName_Project11** in the URL box and then click on the **Submit** button.

   <img src='https://student-datasets-bucket.s3.ap-south-1.amazonaws.com/images/project-share-images/9_enter_project_url.png' width=800>

---
"""