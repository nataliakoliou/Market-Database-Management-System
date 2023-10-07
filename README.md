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

## 2nd Endpoint | Standard user login
1. Open Postman and select the POST request method.
2. Enter the following URL: [http://0.0.0.0:5000/userLogin](http://0.0.0.0:5000/userLogin).
3. In the request Body, choose the "raw" option to specify that you are importing a JSON file.
4. Select "binary" and click "Select File" to upload the endpoint2.json file to the system.
5. Once the file is successfully loaded, click "Send" to retrieve the desired response.

**Code Explanation:**
The system verifies the presence of standard users in the Users collection using the email and password provided in the Postman request's Body. If such a user is found, the `create_user_session()` function is called to authenticate the user. Subsequently, a dictionary is returned to the user containing the user's unique identifier (UUID) and their email address. In the event that the requested user is not found, an appropriate failure message is returned.

## 3rd Endpoint | Administrator login
1. Open Postman and select the POST request method.
2. Enter the following URL: [http://0.0.0.0:5000/adminLogin](http://0.0.0.0:5000/adminLogin).
3. In the request Body, choose the "raw" option to specify that you are importing a JSON file.
4. Select "binary" and click "Select File" to upload the endpoint3.json file to the system.
5. Once the file is successfully uploaded, click "Send" to receive the requested response.

**Code Explanation:**
The system checks if there are administrators in the Users collection with the email and password provided in the Postman Body. If such a user is found, the `create_admin_session()` function is called to authenticate the user. Consequently, a dictionary is returned to the user, containing keys for the user's unique identifier (UUID) and email. In case the requested user is not found, an appropriate failure message is returned.

## 4th Endpoint | Product search
1. Open Postman and select the GET request method.
2. Enter the following URL: [http://0.0.0.0:5000/searchProduct](http://0.0.0.0:5000/searchProduct).
3. In the request Body, choose the "raw" option to specify that you are importing a JSON file.
4. Select "binary" and click "Select File" to upload the endpoint4.json file to the system.
5. In the Headers section, add a new header with the name "Authorization" and click on the square box to the left.
6. After successfully logging in as a standard user, copy the UUID and paste it into the Authorization field.
7. Click "Send" to retrieve the requested response.

**Code Explanation:**
The system checks if the UUID in the Authorization field exists in the `users_session` by calling the `is_user_session_valid()` function. If it receives a positive response, it then checks if there is a product in the Products collection with either the ID, name, or category received via Postman (the `endpoint4.json` file may contain either the ID, name, or category for searching a product). If one or more such products are found, their details are returned as a list of dictionaries in `products_l`, each containing a dictionary `product_d`. In case the UUID is invalid or the ID/name/category does not correspond to any product, an error message is returned.

## 5th Endpoint | Add product to the cart
1. Open Postman and select the GET request method.
2. Enter the following URL: [http://0.0.0.0:5000/addToCart](http://0.0.0.0:5000/addToCart).
3. In the request Body, choose the "raw" option to specify that you are importing a JSON file.
4. Select "binary" and click "Select File" to upload the endpoint5.json file to the system.
5. In the Headers section, add a new header with the name "Authorization" and click on the square box to the left.
6. After successfully logging in as a standard user, copy the UUID and paste it into the Authorization field.
7. Click "Send" to retrieve the requested response.

**Code Explanation:**
The system begins by checking if the UUID in the Authorization field exists in the `users_session` by calling the `is_user_session_valid()` function. If it receives a positive response, it proceeds to check if there is a product in the Products collection with the ID received via Postman. Simultaneously, it requires that this product is available in stock in quantities greater than or equal to the quantity specified by the user in the endpoint5.json file. If the requested product is indeed available, it is added to the cart using the product_d dictionary. To calculate the total cost of the items in the cart, two scenarios are considered: whether the cart is empty or whether it already contains at least one product. In the first scenario, the system checks if the desired product is already in the cart to avoid duplicate entries and updates the quantity based on the new order. In the second scenario, the product is simply added to the cart without further action. Finally, the system calculates the totalPrice by multiplying each product in the cart by its corresponding quantity. It then displays the cart details to the user and concludes the endpoint. If the UUID is invalid or the ID/quantity does not correspond to an available product, an error message is returned.

## 6th Endpoint | Display customer's cart
1. Open Postman and select the GET request method.
2. Enter the following URL: http://0.0.0.0:5000/displayCart.
3. In the Headers section, add a new header named "Authorization" and click on the square box to the left.
4. After successfully logging in as a standard user, copy the UUID and paste it into the Authorization field.
5. Leave the Body field empty.
6. Click "Send" to retrieve the requested response.

**Code Explanation:**
The system checks if the UUID in the Authorization field exists in the `users_session` by calling the `is_user_session_valid()` function. If it receives a positive response, it checks whether the cart is empty or not. In the case of an empty cart, the corresponding response message is displayed. If there are products in the cart, the total price is calculated as usual, and the cart details (product details and total cost) are displayed. In case the UUID is invalid, an error message is returned.

## 7th Endpoint | Delete product from the cart
1. Open Postman and choose the GET request method.
2. Enter the following URL: http://0.0.0.0:5000/removeFromCart.
3. In the request Body, select the "raw" option to indicate that you're importing a JSON file.
4. Click on "binary" and then "Select File" to upload the endpoint7.json file into the system.
5. In the Headers section, add a new header named "Authorization" and click on the square box to the left.
6. After successfully logging in as a standard user, copy the UUID and paste it into the Authorization field.
7. Click "Send" to retrieve the requested response.

**Code Explanation:**
The system checks if the UUID in the Authorization field exists in the `users_session` by calling the `is_user_session_valid()` function. If it receives a positive response, it verifies if a product with the provided ID exists in the Products collection, obtained through Postman. If the requested product is found, it is removed from the cart list, taking into account its unique ID (used to locate the product in the cart). Then, the system calculates the total monetary amount of the remaining items in the cart and stores the result in the `totalPrice` variable. It displays the updated cart information to the user and concludes the endpoint. In case the UUID is invalid or the ID doesn't correspond to any product, an error message is returned.

## 8th Endpoint | Purchase products
1. Open Postman and select the PATCH request method.
2. Enter the following URL: http://0.0.0.0:5000/buyProduct.
3. In the request Body, choose the "raw" option to specify that you are importing a JSON file.
4. Click on "binary" and then "Select File" to upload the endpoint8.json file into the system.
5. In the Headers section, add a new header named "Authorization" and click on the square box to the left.
6. After successfully logging in as a standard user, copy the UUID and paste it into the Authorization field.
7. Click "Send" to retrieve the requested response.

**Code Explanation:**
The system examines whether the UUID in the Authorization field exists in the `users_session` by invoking the `is_user_session_valid()` function. If it receives a positive response, it checks if the user's card number is a valid sixteen-digit code. If the card number is valid, the transaction process proceeds successfully. From `users_sessions`, the system identifies the user's email and stores it in the email variable. This data will be needed later to update the `orderHistory` field of the user with the provided email. Initially, the system checks if the cart is empty or has at least one product to purchase. In the first case, the corresponding response message is displayed, while in the second case, the system constructs a for loop to update the Products collection for each product in the cart. Upon completing the update process, the details of each product are added to the receipt list, and simultaneously, we sum up the prices multiplied by the quantity for each product in the `totalPrice` variable. Inside the for loop, there's an if case that handles the update to the `orderHistory` of the Users collection for each product added to the user's receipt. If the product has been previously purchased by the user, the conditions of the if case are not met, and the system never enters it. Finally, the cart is emptied, and the requested transaction receipt is displayed to the user. In case the UUID is invalid, an error message is returned.

## 9th Endpoint | Display order history
1. Open Postman and select the GET request method.
2. Enter the following URL: http://0.0.0.0:5000/showOrderHistory.
3. In the Headers section, add a new header named "Authorization," then click on the square box to the left.
4. After successfully logging in as standard users, copy the UUID and paste it into the Authorization field.
5. Leave the Body field empty.
6. Click "Send" to retrieve the requested response.

**Code Explanation:**
The system checks if the UUID in the Authorization field exists in the `users_session` by calling the `is_user_session_valid()` function. If it receives a positive response, it proceeds to locate the email of the current user (via `users_sessions`) and stores it in the `email` variable. Based on this data, it checks the `orderHistory` field of the user with the corresponding email and verifies if it's empty. If it is indeed empty, the appropriate response message is displayed. If it's not empty, the list of the user's orders stored in this field is displayed. In case the UUID is invalid, an error message is returned.

## 10th Endpoint | Delete user account
1. Open Postman and select the DELETE request method.
2. Enter the following URL: http://0.0.0.0:5000/deleteUser.
3. In the request Body, choose the "raw" option to specify that you are importing a JSON file.
4. Click on "binary" and then select "Select File" to upload the endpoint1.json file to the system.
5. Once the file is uploaded, click "Send" to receive the requested response.

**Code Explanation:**
The system first checks if the UUID in the Authorization field exists in the `users_session` by invoking the `is_user_session_valid()` function. If it receives a positive response, it proceeds to locate the email of the current user (via `users_sessions`) and stores it in the variable `email`. With this data, the system can safely remove the current user from the Users collection. If the deletion is successful, the corresponding response message is returned. In the case of an invalid UUID, an error message is returned.

## 11th Endpoint | Add product to the market
1. Open Postman and select the PATCH request method.
2. Enter the following URL: http://0.0.0.0:5000/addToMarket.
3. In the request Body, choose the "raw" option to specify that you are importing a JSON file.
4. Click "binary" and then select "Select File" to upload the endpoint11.json file to the system.
5. In the Headers section, add a new header with the name "Authorization" and click on the square box to the left.
6. After successfully logging in as an administrator user, copy the UUID and paste it into the Authorization field.
7. Click "Send" to receive the requested response.

**Code Explanation:**
The system checks if the UUID in the Authorization field exists in the `admins_session` by calling the `is_admin_session_valid()` function. If it receives a positive response, it checks if there is a product in the Products collection with the ID received via Postman. If the requested product already exists in the store's stock, an appropriate response message is printed (adding an existing product to the system is not possible). If the product is not found in the Products collection, it is added through the `product_d` dictionary. Upon successful addition to the system, the corresponding success message is displayed. In case the UUID is invalid, an error message is returned.

## 12th Endpoint | Delete product from the market
1. Open Postman and select the PATCH request method.
2. Enter the following URL: http://0.0.0.0:5000/removeFromMarket.
3. In the request Body, choose the "raw" option to specify that you are importing a JSON file.
4. Select "binary" and click "Select File" to upload the endpoint12.json file to the system.
5. In the Headers section, add a new header with the name "Authorization" and click on the square box to the left.
6. After successfully logging in as an administrator user, copy the UUID and paste it into the Authorization field.
7. Click "Send" to receive the requested response.

**Code Explanation:**
The system checks if the UUID in the Authorization field exists in the `admins_session` by calling the `is_admin_session_valid()` function. If it receives a positive response, it verifies if there is a product in the Products collection with the ID received via Postman. If the requested product indeed exists in the store's stock, it is completely removed, and a success message is printed. In case the UUID is invalid or the ID does not correspond to an existing product in the Products collection, an error message is returned.

## 13th Endpoint | Update product in the market
1. Open Postman and select the PATCH request method.
2. Enter the following URL: http://0.0.0.0:5000/updateProduct.
3. In the request Body, choose the "raw" option to specify that you are importing a JSON file.
4. Select "binary" and click "Select File" to upload the endpoint13.json file to the system.
5. In the Headers section, add a new header with the name "Authorization" and click on the square box to the left.
6. After successfully logging in as an administrator user, copy the UUID and paste it into the Authorization field.
7. Click "Send" to receive the requested response

**Code Explanation:**
The system verifies if the UUID in the Authorization field exists in the `admins_session` by calling the `is_admin_session_valid()` function. If it receives a positive response, it checks if there is a product in the Products collection with the ID received via Postman. If the requested product exists in the store's stock, it is updated according to the data provided by the user, and a success message is printed. The `endpoint13.json` file can contain either the new product ID, name, price, or category (in general, one of these four fields of the product is updated). In case the UUID is invalid or the ID does not correspond to an existing product in the Products collection, an error message is returned.

## Author
Natalia Koliou: find me on [LinkedIn](https://www.linkedin.com/in/natalia-koliou-b37b01197/).
