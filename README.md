# Market Database Management System
This project focuses on creating a Supermarket Database Management System, designed to offer a range of endpoints for efficiently managing market-related data. The system is implemented using Python with Flask for the backend and MongoDB as the database. 

## Introduction
In this report, we will provide a detailed walkthrough of the steps involved in running the `market-app.py` file. To accomplish this, we will use the Linux terminal and the Postman application.

We will execute the Python file, students-app.py, along with a debugger, accessible at http://0.0.0.0:5000/. For your convenience, we recommend creating thirteen JSON files that can be imported into Postman. You can find a list of these JSON files in the [json-endpoints.txt](https://github.com/nataliakoliou/Market-Database-Management-System/blob/main/json-endpoints.txt) file in this repository. Copy and paste the endpoints from the file to quickly set up your requests in Postman.

## Requirements
To run this project, you need to ensure the following requirements are met:
- **Python:** The project is implemented using Python. You will need Python 3.8 or a higher version installed on your system. You can download Python from [Python's official website](https://www.python.org/downloads/).
- **Flask:** Flask is used as the web framework for the backend of the project. You can install Flask using pip:
  ```bash
  pip install Flask
  ```
- MongoDB: MongoDB is used as the database for the project. You can install MongoDB on your system by following the instructions provided on the MongoDB installation page.
- Docker (Optional): Docker is used to run MongoDB as a container. If you prefer to use Docker, make sure it's installed on your system, and you can start MongoDB as a Docker container using:
  ```bash
  sudo systemctl enable docker --now
  sudo docker start mongodb
  ```
- Postman: Postman is recommended for testing the API endpoints. You can download and install Postman from Postman's official website.

## 1st Endpoint | User creation
1. Open Postman and select the POST request method.
2. Enter the following URL: [http://0.0.0.0:5000/createUser](http://0.0.0.0:5000/createUser).
3. In the request Body, choose the "raw" option to specify that you are importing a JSON file.
4. Select "binary" and click "Select File" to upload the endpoint1.json file to the system.
5. Once the file is uploaded, click "Send" to get the response.

**Code Explanation:**
The system checks if there are any existing users in the Users collection using the `count_documents()` function. If it returns 0, the name, email, password, category, and order history provided in the data (via `data = json.loads(request.data)`) are stored in the user dictionary. This user dictionary is then added to the Users collection, and a success message is sent to the user. If the details you're trying to add already exist in the Users collection, you'll receive a corresponding failure message.

## 2nd Endpoint | Standard User Login
1. Open Postman and select the POST request method.
2. Enter the following URL: [http://0.0.0.0:5000/userLogin](http://0.0.0.0:5000/userLogin).
3. In the request Body, choose the "raw" option to specify that you are importing a JSON file.
4. Select "binary" and click "Select File" to upload the endpoint2.json file to the system.
5. Once the file is successfully loaded, click "Send" to retrieve the desired response.

**Code Explanation:**
The system verifies the presence of standard users in the Users collection using the email and password provided in the Postman request's Body. If such a user is found, the create_user_session() function is called to authenticate the user. Subsequently, a dictionary is returned to the user containing the user's unique identifier (UUID) and their email address. In the event that the requested user is not found, an appropriate failure message is returned.

## 3rd Endpoint | Administrator Login
1. Open Postman and select the POST request method.
2. Enter the following URL: [http://0.0.0.0:5000/adminLogin](http://0.0.0.0:5000/adminLogin).
3. In the request Body, choose the "raw" option to specify that you are importing a JSON file.
4. Select "binary" and click "Select File" to upload the endpoint3.json file to the system.
5. Once the file is successfully uploaded, click "Send" to receive the requested response.

**Code Explanation:**
The system checks if there are administrators in the Users collection with the email and password provided in the Postman Body. If such a user is found, the create_admin_session() function is called to authenticate the user. Consequently, a dictionary is returned to the user, containing keys for the user's unique identifier (UUID) and email. In case the requested user is not found, an appropriate failure message is returned.







## 4th Endpoint | Get all students who are exactly 30 years old
1. Open Postman and select the GET request method.
2. 2. Enter the following URL: [http://0.0.0.0:5000/getStudents/thirties](http://0.0.0.0:5000/getStudents/thirties).
5. In the Headers section, add a new header named "Authorization."
6. After successfully logging in as a user, copy the UUID (user unique identifier) and paste it into the Authorization field.
4. Leave the Body field empty.
7. Click the "Send" button to initiate the request and receive the response.

**Code Explanation:**
The system checks if your UUID in the Authorization field is valid by calling the `is_session_valid()` function. If it's valid, it looks for students aged 30 in the current year. It calculates their birth year (e.g., 1991 for 2021) and stores it as `yearMinus30`. Then, it checks the Students collection for students in this age group. If any are found, their details are printed using the `student_l1` list. To create this list, it goes through each 30-year-old student, stores their information in a dictionary called `student_d2`, and adds it to the `students_l1` list. It's important to note that because the `Students.json` file may have users with or without address information, the `student_d2` dictionary can have two forms – one with the address field and one without. If the UUID is invalid or the email doesn't belong to a 30-year-old student, it returns an error message.

## 5th Endpoint | Get all students who are at least 30 years old
1. Open Postman and select the GET request method.
2. Enter the following URL: [http://0.0.0.0:5000/getStudents/oldies](http://0.0.0.0:5000/getStudents/oldies).
3. In the Headers section, add a new header named "Authorization."
4. After successfully logging in as a user, copy your UUID (user unique identifier) and paste it into the Authorization field.
5. Leave the Body field empty.
6. Click the "Send" button to initiate the request and receive the response.

**Code Explanation:**
The system first checks if the UUID in the Authorization field exists in the users_session by using the `is_session_valid()` function. If it's valid, it proceeds to find students who are at least 30 years old in the current year. To do this, it calculates their birth year (e.g., 1991 for 2021) and stores it as `yearMinus30`. Then, it searches the Students collection for students in this age group. If any are found, their details are printed using the `student_l2` list. To create this list, the system iterates through each student who is 30 years old or older, stores their information in a dictionary named `student_d3`, and adds it to the `students_l2` list. It's important to note that because the `Students.json` file may contain users with or without address information, the `student_d3` dictionary can take two forms – one with the address field and one without. If the UUID is invalid or the email doesn't belong to a student who is at least 30 years old, it returns an error message.

## 6th Endpoint | Get students who have declared residence based on email
1. Open Postman and select the GET request method.
2. Enter the following URL: [http://0.0.0.0:5000/getStudentAddress](http://0.0.0.0:5000/getStudentAddress).
3. In the Body section, choose "raw" to specify that the input type will be JSON.
4. Click "Binary" and then "Select File" to upload the endpoint6.json file.
5. In the Headers section, add a new header named "Authorization."
6. After successfully logging in as a user, copy the UUID (User Unique Identifier) and paste it into the Authorization field.
7. Leave the Body field empty.
8. Click the "Send" button to initiate the request and receive the response.

**Code Explanation:**
The system first checks if the UUID in the Authorization field exists in the users_session by calling the `is_session_valid()` function. If it gets a positive response, it proceeds to check if there is a user in the Students collection with the email received via Postman. Additionally, it ensures that this user has also provided their address information. If such a user is found, the system returns their name, street, and postal code as per the `student_d4` dictionary.

## 7th Endpoint | Delete student by email
1. Open Postman and select the DELETE request method.
2. Enter the following URL: [http://0.0.0.0:5000/deleteStudent](http://0.0.0.0:5000/deleteStudent).
3. In the Body section, select the "raw" input type and specify JSON.
4. Click "binary," then "Select File" to upload the endpoint7.json file.
5. In the Headers section, add a new header named "Authorization."
6. After successfully logging in as a user, copy your UUID (Unique User Identifier) and paste it into the Authorization field.
7. Click the "Send" button to execute the request.

**Code Explanation:**
The system first checks the validity of your UUID in the Authorization field by calling the `is_session_valid()` function. If it's valid, the system proceeds to check if there is a user in the Students collection with the email provided in Postman. If such a user is found, they are completely removed from the Students collection using the `students.delete_one({"email": data["email"]})` command. If the UUID is invalid, the email doesn't correspond to a student, or the email exists in the Students collection but belongs to a student who hasn't provided an address, an error message is returned.

## 8th Endpoint | Add courses to student based on email
1. Open Postman and select the PATCH request method.
2. Enter the following URL: [http://0.0.0.0:5000/addCourses](http://0.0.0.0:5000/addCourses).
3. In the main section (Body), choose the "raw" option to specify that you're uploading a JSON file.
4. Click on "binary" and select "Select File" to upload the "endpoint8.json" file.
5. In the Headers section, add a new header named "Authorization."
6. After successfully logging in as a user, copy the UUID (user unique identifier) and paste it into the Authorization field.
7. Click the "Send" button to initiate the request and receive the response.

**Code Explanation:**
The system validates the UUID in the Authorization field by calling the `is_session_valid()` function. If it's valid, the system checks if a user with the provided email exists in the Students collection through Postman. If such a user is found, the system inserts the courses field with the courses received from `json.loads(request.data)`. To print these courses distinctly, they are stored one by one in a list called `courses_l`. This list is then used to update the `student` variable with the command `student.update({"courses": courses_l})` in dictionary format, just like they appear in the JSON file. This allows the system to print the student's information with the current email after inserting it into the `student_d5` dictionary. Since the `Students.json` file contains users with and without address details, the `student_d5` dictionary has two forms – one including the `address` field and one excluding it. If the UUID is invalid or the email doesn't correspond to any student, an error message is returned.

## 9th Endpoint | Get a Student's Previous Courses by Email
1. Open Postman and choose the GET request method.
2. Enter this URL: http://0.0.0.0:5000/getPassedCourses.
3. In the main section (Body), select "raw" to specify that we'll input JSON data.
4. Click "binary" and choose "Select File" to upload the endpoint9.json file from your system.
5. In the Headers section, add a new header named "Authorization," then paste your UUID (user unique identifier) into the Authorization field after successfully logging in.
6. Click "Send" to initiate the request and receive the response.

**Code Explanation:**
The system first checks if the UUID in the Authorization field exists in the users_session by using the `is_session_valid()` function. If it's valid, the system looks for a user in the Students collection with the email provided via Postman. It checks if this user has completed any courses in the Students collection. If such a user is found, the system extracts the courses in which they were examined and received a passing grade (a grade greater than or possibly equal to 5) and stores them in a dictionary called `passed`. This dictionary is constructed using the `passed.update(course_d)` command, where `course_d` represents each course-grade pair included in the dictionary. Finally, the system prints the student's name and the courses they have passed using a dictionary named `student_d6`. If the UUID is invalid, the email doesn't correspond to any student, or the student hasn't been examined in any course, an error message is returned. Likewise, if the student was examined but failed in all courses, an appropriate informative message is displayed.

## Author
Natalia Koliou: find me on [LinkedIn](https://www.linkedin.com/in/natalia-koliou-b37b01197/).
