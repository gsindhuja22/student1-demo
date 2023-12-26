from jinja2 import Template
import pdfkit

# Sample invoice data (replace this with your actual data)
invoice_data = {
    "invoice_number": "INV-123",
    "date": "2023-12-31",
    "items": [
        {"description": "Item 1", "quantity": 2, "price": 10},
        {"description": "Item 2", "quantity": 1, "price": 20},
        # Add more items as needed
    ],
    "total": 40  # Total amount
}

# Create HTML template using Jinja2-style placeholders
template_str = '''
<!DOCTYPE html>
<html>
<head>
  <title>Invoice</title>
  <style>
    /* Your CSS styles here */
    body {
      font-family: Arial, sans-serif;
    }
    .invoice {
      width: 80%;
      margin: 0 auto;
      border: 1px solid #ccc;
      padding: 20px;
    }
    .header {
      background-color: #333;
      color: white;
      padding: 10px;
      text-align: center;
    }
    .header h1 {
      margin: 0;
    }
    .invoice-info {
      margin-top: 20px;
    }
    .invoice-info p {
      margin: 5px 0;
    }
    table {
      width: 100%;
      border-collapse: collapse;
      margin-top: 20px;
    }
    th, td {
      border: 1px solid #ccc;
      padding: 10px;
      text-align: left;
    }
    .footer {
      margin-top: 20px;
    }
    .footer p {
      margin: 5px 0;
      text-align: right;
    }
  </style>
</head>
<body>
  <div class="invoice">
    <div class="header">
      <h1>Invoice</h1>
    </div>
    <div class="invoice-info">
      <p>Invoice Number: {{ invoice_number }}</p>
      <p>Date: {{ date }}</p>
    </div>
    <table>
      <thead>
        <tr>
          <th>Description</th>
          <th>Quantity</th>
          <th>Price</th>
        </tr>
      </thead>
      <tbody>
        {% for item in items %}
          <tr>
            <td>{{ item['description'] }}</td>
            <td>{{ item['quantity'] }}</td>
            <td>${{ item['price'] }}</td>
          </tr>
        {% endfor %}
      </tbody>
    </table>
    <div class="footer">
      <p>Total: ${{ total }}</p>
      <!-- Add more footer content if needed -->
    </div>
  </div>
</body>
</html>
'''

# Specify the path to wkhtmltopdf executable
wkhtmltopdf_path = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'  # Replace with the actual path

# Convert the rendered HTML to PDF using pdfkit
output_file = "invoice.pdf"
pdfkit.from_string(template_str, output_file, configuration=pdfkit.configuration(wkhtmltopdf=wkhtmltopdf_path))

print(f'Invoice PDF has been generated and saved to "{output_file}" successfully.')
