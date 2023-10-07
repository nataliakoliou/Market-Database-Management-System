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
The system verifies the presence of standard users in the Users collection using the email and password provided in the Postman request's Body. If such a user is found, the `create_user_session()` function is called to authenticate the user. Subsequently, a dictionary is returned to the user containing the user's unique identifier (UUID) and their email address. In the event that the requested user is not found, an appropriate failure message is returned.

## 3rd Endpoint | Administrator Login
1. Open Postman and select the POST request method.
2. Enter the following URL: [http://0.0.0.0:5000/adminLogin](http://0.0.0.0:5000/adminLogin).
3. In the request Body, choose the "raw" option to specify that you are importing a JSON file.
4. Select "binary" and click "Select File" to upload the endpoint3.json file to the system.
5. Once the file is successfully uploaded, click "Send" to receive the requested response.

**Code Explanation:**
The system checks if there are administrators in the Users collection with the email and password provided in the Postman Body. If such a user is found, the `create_admin_session()` function is called to authenticate the user. Consequently, a dictionary is returned to the user, containing keys for the user's unique identifier (UUID) and email. In case the requested user is not found, an appropriate failure message is returned.

## 4th Endpoint | Product Search
1. Open Postman and select the GET request method.
2. Enter the following URL: [http://0.0.0.0:5000/searchProduct](http://0.0.0.0:5000/searchProduct).
3. In the request Body, choose the "raw" option to specify that you are importing a JSON file.
4. Select "binary" and click "Select File" to upload the endpoint4.json file to the system.
5. In the Headers section, add a new header with the name "Authorization" and click on the square box to the left.
6. After successfully logging in as a standard user, copy the UUID and paste it into the Authorization field.
7. Click "Send" to retrieve the requested response.

**Code Explanation:**
The system checks if the UUID in the Authorization field exists in the `users_session` by calling the `is_user_session_valid()` function. If it receives a positive response, it then checks if there is a product in the Products collection with either the ID, name, or category received via Postman (the `endpoint4.json` file may contain either the ID, name, or category for searching a product). If one or more such products are found, their details are returned as a list of dictionaries in `products_l`, each containing a dictionary `product_d`. In case the UUID is invalid or the ID/name/category does not correspond to any product, an error message is returned.

## 5th Endpoint | Adding items to cart
1. Open Postman and select the GET request method.
2. Enter the following URL: [http://0.0.0.0:5000/addToCart](http://0.0.0.0:5000/addToCart).
3. In the request Body, choose the "raw" option to specify that you are importing a JSON file.
4. Select "binary" and click "Select File" to upload the endpoint5.json file to the system.
5. In the Headers section, add a new header with the name "Authorization" and click on the square box to the left.
6. After successfully logging in as a standard user, copy the UUID and paste it into the Authorization field.
7. Click "Send" to retrieve the requested response.

**Code Explanation:**
The system begins by checking if the UUID in the Authorization field exists in the `users_session` by calling the `is_user_session_valid()` function. If it receives a positive response, it proceeds to check if there is a product in the Products collection with the ID received via Postman. Simultaneously, it requires that this product is available in stock in quantities greater than or equal to the quantity specified by the user in the endpoint5.json file. If the requested product is indeed available, it is added to the cart using the product_d dictionary. To calculate the total cost of the items in the cart, two scenarios are considered: whether the cart is empty or whether it already contains at least one product. In the first scenario, the system checks if the desired product is already in the cart to avoid duplicate entries and updates the quantity based on the new order. In the second scenario, the product is simply added to the cart without further action. Finally, the system calculates the totalPrice by multiplying each product in the cart by its corresponding quantity. It then displays the cart details to the user and concludes the endpoint. If the UUID is invalid or the ID/quantity does not correspond to an available product, an error message is returned.

## 6th Endpoint | View cart
1. Open Postman and select the GET request method.
2. Enter the following URL: http://0.0.0.0:5000/displayCart.
3. In the Headers section, add a new header named "Authorization" and click on the square box to the left.
4. After successfully logging in as a standard user, copy the UUID and paste it into the Authorization field.
5. Leave the Body field empty.
6. Click "Send" to retrieve the requested response.

**Code Explanation:**
The system checks if the UUID in the Authorization field exists in the `users_session` by calling the `is_user_session_valid()` function. If it receives a positive response, it checks whether the cart is empty or not. In the case of an empty cart, the corresponding response message is displayed. If there are products in the cart, the total price is calculated as usual, and the cart details (product details and total cost) are displayed. In case the UUID is invalid, an error message is returned.





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
