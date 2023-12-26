from jinja2 import Template
import pdfkit

# Sample invoice data (replace this with your actual data)
invoice_data = {
    "invoice_number": "INV-123",
    "date": "2023-12-31",
    "items": [
        {"description": "Item 1", "quantity": 2, "price": 10},
        {"description": "Item 2", "quantity": 1, "price": 20},
        {"description": "Item 3", "quantity": 5, "price": 30}
        # Add more items as needed
    ],
    "total": 40  # Total amount
}
import base64

# Read the image file
with open("C:/Users/Hp/Documents/logo.jpg", "rb") as img_file:
    base64_image = base64.b64encode(img_file.read()).decode("utf-8")

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
      background-color: black;
      color: white;
      padding: 10px;
    }
    .footer {
      margin-top: 20px;
    }
    .footer p {
      margin: 5px 0;
    }
    table {
      width: 100%;
      border-collapse: collapse;
    }
    th, td {
      border: 1px solid #ccc;
      padding: 8px;
      text-align: left;
    }
  </style>
</head>
<body>
  <div class="invoice">
    <div class="header">
      <h1>Invoice</h1>
    </div>
    <p>Invoice Number: {{ invoice_number }}</p>
    <p>Date: {{ date }}</p>
     <div>
    <img src="data:image/jpeg;base64,{base64_image}" alt="Logo" style="max-width: 150px;">
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

# Create a Jinja2 Template object
template = Template(template_str)

# Render the template with the invoice data
rendered_html = template.render(invoice_number=invoice_data['invoice_number'],
                                date=invoice_data['date'],
                                items=invoice_data['items'],
                                total=invoice_data['total'])

# Convert the rendered HTML to PDF using pdfkit
pdfkit.from_string(rendered_html, 'invoice.pdf')
