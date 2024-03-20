#  Sales Report Application

The Sales Report Application is a Flask web application designed to generate and send daily sales reports via email. It facilitates the process of retrieving sales data from a MySQL database and automates the generation of formatted email reports, which include detailed transaction information.

## Features

The application offers the following key features:

- **Data Retrieval**: It retrieves sales data for a specific store and date from the designated MySQL database.
- **Email Generation**: The application dynamically generates an HTML email containing transaction details, such as invoice numbers, product names, quantities, rates, and total amounts.
- **Email Sending**: It utilizes SMTP to send the generated email report to the specified recipient email address.

## Prerequisites

Before running the application, ensure that you have the following prerequisites installed and configured:

- **Python 3.x**: Make sure you have Python 3.x installed on your system.
- **Flask**: Install Flask, a lightweight web framework for Python, using `pip install Flask`.
- **pymysql**: Install pymysql, a Python MySQL client library, using `pip install pymysql`.
- **SMTP Configuration**: Configure your Gmail SMTP server settings within the `send_email` function in the `app.py` file to enable email sending functionality.

## Installation

To install and run the application, follow these steps:

1. **Clone the Repository**: Clone the repository to your local machine using the command `git clone https://github.com/your-username/vendy-sales-report.git`.
2. **Install Dependencies**: Install the required Python dependencies by running `pip install Flask pymysql`.
3. **Database Setup**: Set up your MySQL database with the appropriate schema (`vendy`) and tables (`invoice`, `invoice_details`, `store_set`, `product_information`).
4. **SMTP Configuration**: Configure your Gmail SMTP server settings in the `send_email` function of `app.py` to enable email sending.
5. **Run the Application**: Execute the Flask application by running `python app.py`.
6. **Access the Application**: Access the application in your web browser at `http://localhost:8080`.

## Usage

To use the application effectively, follow these steps:

1. **Enter Details**: Enter the store code, date, and recipient email address in the provided form on the application's web interface.
2. **Generate Report**: Click the "Generate Report" button to initiate the report generation process.
3. **Email Delivery**: The application will fetch sales data for the specified store and date, generate an email report, and send it to the provided email address.

## Troubleshooting

If you encounter any issues with the application, follow these troubleshooting steps:

- **Check Console Output**: Examine the console output for any error messages or exceptions that may provide insight into the issue.
- **Database Configuration**: Ensure that your MySQL database is properly configured and accessible from the application.
- **SMTP Settings**: Verify that your SMTP server settings are correctly configured within the `send_email` function in `app.py`.

## Contributing

Contributions to the project are welcome! If you have bug fixes, feature enhancements, or other improvements, feel free to submit pull requests or open issues on the GitHub repository.


