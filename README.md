Sales Report Application
The  Sales Report Application is a Flask web application designed to generate and send daily sales reports via email. It retrieves sales data from a MySQL database and sends an email containing detailed transaction information to the specified email address.

Features
Retrieve sales data for a specific store and date from the database.
Generate a formatted HTML email containing transaction details.
Send the email report to the provided email address.
Prerequisites
Before running the application, ensure you have the following installed:

Python 3.x
Flask
pymysql (Python MySQL client library)
smtplib (Python SMTP library)
Installation
Clone the repository to your local machine:

bash
Copy code
git clone https://github.com/your-username/vendy-sales-report.git
Install the required Python dependencies:

bash
Copy code
pip install Flask pymysql
Set up your MySQL database with the appropriate schema (vendy) and tables (invoice, invoice_details, store_set, product_information).

Configure your Gmail SMTP server settings in the send_email function of app.py.

Run the Flask application:

bash
Copy code
python app.py
Access the application in your web browser at http://localhost:8080.

Usage
Enter the store code, date, and recipient email address in the provided form.
Click the "Generate Report" button.
The application will fetch sales data for the specified store and date, generate an email report, and send it to the provided email address.
Troubleshooting
If you encounter any issues with the application, check the console output for error messages.
Ensure that your MySQL database is properly configured and accessible from the application.
Contributing
Contributions are welcome! Feel free to submit bug reports, feature requests, or pull requests to improve the application.

