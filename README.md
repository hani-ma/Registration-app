# Registration API Project

This project is a simple Registration API built using Flask for the backend and HTML/JavaScript for the frontend. It allows users to register by providing their details and manage the registrations through a web interface.

## Features
- Register new users with their details.
- View all registered users.
- Update user details.
- Delete users from the registration list.

## Technologies Used
- **Backend:** Flask
- **Frontend:** HTML, CSS, JavaScript
- **Database:** MySQL

## Setup Instructions

### Backend Setup
1. Clone this repository:
   git clone https://github.com/hani-ma/registration-app.git
   
2. Navigate to the backend directory:
   cd repository-name/backend

3. Install required Python packages:
   pip install Flask mysql-connector-python
4. Set up your MySQL database and create a table named Registration.

5. Run the Flask application:
   python app.py

Frontend Setup:

1. Navigate to the frontend directory:
   cd repository-name/frontend

2. Open the index.html file in your web browser.

Usage:

--Fill in the registration form to add a new user.
--View all registered users below the form.
--Click "Delete" next to a user to remove them from the list.

API Endpoints:

POST /register: Add a new registration.
GET /registrations: Get all registrations.
PUT /register/<id>: Update registration by ID.
DELETE /register/<id>: Delete registration by ID.