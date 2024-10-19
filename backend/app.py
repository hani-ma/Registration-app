from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

# MySQL Database configuration
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'  # Replace with your MySQL username
app.config['MYSQL_PASSWORD'] = '123456'  # Replace with your MySQL password
app.config['MYSQL_DB'] = 'assignment'  # Replace with your MySQL database name

# Establish a MySQL connection
mysql = mysql.connector.connect(
    host=app.config['MYSQL_HOST'],
    user=app.config['MYSQL_USER'],
    password=app.config['MYSQL_PASSWORD'],
    database=app.config['MYSQL_DB']
)

from flask import send_from_directory

@app.route('/')
def home():
    return send_from_directory('.', 'index.html')  # assuming your HTML file is named index.html


# Create a new registration (CREATE)
@app.route('/register', methods=['POST'])
def create_registration():
    data = request.json
    name = data['Name']
    email = data['Email']
    dob = data['DateOfBirth']
    phone = data.get('PhoneNumber', None)
    address = data.get('Address', None)

    cursor = mysql.cursor()
    try:
        cursor.execute(
            "INSERT INTO Registration (Name, Email, DateOfBirth, PhoneNumber, Address) VALUES (%s, %s, %s, %s, %s)", 
            (name, email, dob, phone, address)
        )
        mysql.commit()
        return jsonify({"message": "Registration successful!"}), 201
    except mysql.connector.Error as err:
        return jsonify({"message": f"Error: {err}"}), 400
    finally:
        cursor.close()

# Read all registrations (GET)
@app.route('/registrations', methods=['GET'])
def get_registrations():
    cursor = mysql.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Registration")
    results = cursor.fetchall()
    cursor.close()
    return jsonify(results), 200

# Update registration (PUT)
@app.route('/register/<int:id>', methods=['PUT'])
def update_registration(id):
    data = request.json
    name = data['Name']
    email = data['Email']
    dob = data['DateOfBirth']
    phone = data.get('PhoneNumber', None)
    address = data.get('Address', None)

    cursor = mysql.cursor()
    try:
        cursor.execute(
            "UPDATE Registration SET Name=%s, Email=%s, DateOfBirth=%s, PhoneNumber=%s, Address=%s WHERE ID=%s",
            (name, email, dob, phone, address, id)
        )
        mysql.commit()
        return jsonify({"message": "Registration updated successfully!"}), 200
    except mysql.connector.Error as err:
        return jsonify({"message": f"Error: {err}"}), 400
    finally:
        cursor.close()

# Delete registration (DELETE)
@app.route('/register/<int:id>', methods=['DELETE'])
def delete_registration(id):
    cursor = mysql.cursor()
    try:
        cursor.execute("DELETE FROM Registration WHERE ID=%s", (id,))
        mysql.commit()

        # Check if any rows were affected
        if cursor.rowcount == 0:
            return jsonify({"message": "No registration found with this ID."}), 404

        return jsonify({"message": "Registration deleted successfully!"}), 200
    except mysql.connector.Error as err:
        return jsonify({"message": f"Error: {err}"}), 400
    finally:
        cursor.close()


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5001, debug=True)
