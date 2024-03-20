
from flask import Flask, render_template, request
import pymysql
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

app = Flask(__name__)

# Function to execute SQL query
def execute_query(store_code, date):
    conn = pymysql.connect(
        host="localhost",
        user="root",
        password="",
        database="vendy",
        port=3306
    )
    cur = conn.cursor()
    cur.execute("""
        SELECT 
            iv.`date`,  
            iv.invoice,
            ss.store_name,   
            pi.product_name,
            id.quantity,
            id.rate,   
            iv.total_amount 
        FROM 
            `invoice` iv
        JOIN 
            `invoice_details` id ON iv.invoice_id = id.invoice_id
        JOIN
            `store_set` ss ON iv.store_id = ss.store_id
        JOIN
            `product_information` pi ON id.product_id = pi.product_id
        WHERE 
            iv.`date` = %s 
            AND ss.store_code = %s
    """, (date, store_code))
    data = cur.fetchall()
    conn.close()
    return data

# Function to retrieve store name based on store_id
def get_store_name(store_id):
    conn = pymysql.connect(
        host="localhost",
        user="root",
        password="",
        database="vendy",
        port=3306
    )
    cur = conn.cursor()
    cur.execute("SELECT store_name FROM store_set WHERE store_id = %s", (store_id,))
    store_name_row = cur.fetchone()  # Retrieve the result row

    # Check if store_name_row is not None
    if store_name_row:
        store_name = store_name_row[0]  # Assuming store_name is the first column in the result
    else:
        store_name = None

    conn.close()
    return store_name


# Function to send email
def send_email(data, email_address, date, store_name, store_code):
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    sender_email = 'mohammadrakibur23@gmail.com'
    sender_password = 'mkia fvhe uxug znuh'

    # Calculate total quantity and total amount (taka)
    total_quantity = sum(row[4] for row in data)  # Summing the quantity (assuming it's the 5th column)
    total_amount = sum(row[6] for row in data)  # Summing the total amount (taka) (assuming it's the 7th column)

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = email_address
    msg['Subject'] = f"(No reply) Sales Report - {date} - {store_name}"

    # Constructing the HTML table for the email body
    body = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Daily Sales Report</title>
        <style>
            table {{
                border-collapse: collapse;
                width: 100%;
            }}
            th, td {{
                border: 1px solid #ddd;
                padding: 8px;
                text-align: left;
            }}
            th {{
                background-color: #f2f2f2;
            }}
        </style>
    </head>
    <body>
        <h1>Vendy Daily Sales Report</h1>
        <p>Report Date: {date}</p>
        <table>
            <tr>
                <th>Machine Code</th>
                <th>Store Name</th>
            </tr>
            <tr>
                <td>{store_code}</td>
                <td>{store_name}</td>
            </tr>
            <tr>
                <th>Total Quantity</th>
                <th>Total Sold (taka)</th>
            </tr>
            <tr>
                <td>{total_quantity}</td>
                <td>{total_amount}</td>
            </tr>
            <!--  <tr>
                <th>Last Refill Quantity</th>
                <th>Last Refill Date</th>
            </tr>
            <tr>
                <td></td>
                <td></td>
            </tr> -->
        </table>
        <h3>Last Days Transaction Details:</h3>
        <table>
            <tr>
                <th>Date</th>
                <th>Invoice</th>
                <th>Machine Name</th>
                <th>Product Name</th>
                <th>Quantity</th>
                <th>Rate (taka)</th>
                <th>Total Amount (taka)</th>
            </tr>
    """

    # Adding transaction details
    for row in data:
        body += "<tr>"
        for item in row:
            body += f"<td>{item}</td>"
        body += "</tr>"

    # Closing the HTML body
    body += """
        </table>
    </body>
    </html>
    """

    # Attach the HTML content to the email
    msg.attach(MIMEText(body, 'html'))

    # Sending the email
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(sender_email, sender_password)
    server.sendmail(sender_email, email_address, msg.as_string())
    server.quit()


# Route for the main page
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        try:
            store_code = request.form["store_code"]  # Corrected from data["store_id"] to form["store_code"]
            date = request.form["date"]
            data = execute_query(store_code, date)
            store_name = get_store_name(store_code)  # Retrieve store name using store_code
            if data:
                send_email(data, request.form["email"], date, store_name,store_code)
                return "Report sent successfully!"
            else:
                # No data found, sending email with zero sales report
                send_email([(date, None, store_name, None, None, None, 0)], request.form["email"], date, store_name,store_code)
                return "Email sent successfully!"
        except Exception as e:
            return f"Error: {str(e)}"
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True, port=8080)
