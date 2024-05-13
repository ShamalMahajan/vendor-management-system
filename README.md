# Vendor Management System

This project is a Vendor Management System developed using Django and Django REST Framework. It handles vendor profiles, tracks purchase orders, and calculates vendor performance metrics.

## Features

- **Vendor Profile Management**: Allows users to manage vendor profiles including creation, retrieval, update, and deletion.
- **Purchase Order Tracking**: Tracks purchase orders with details such as PO number, order date, items, quantity, and status.
- **Vendor Performance Evaluation**: Calculates vendor performance metrics including on-time delivery rate, quality rating, response time, and fulfillment rate.

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/vendor-management-system.git
   ```

2. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Run migrations:**

   ```bash
   python manage.py migrate
   ```

4. **Start the development server:**

   ```bash
   python manage.py runserver
   ```

5. **Access the API at [http://localhost:8000/api/](http://localhost:8000/api/)**

## API Documentation

The API endpoints are documented below:

### Vendor Management Endpoints:

- `POST /api/vendors/`: Create a new vendor.
- `GET /api/vendors/`: List all vendors.
- `GET /api/vendors/<vendor_id>/`: Retrieve details of a specific vendor.
- `PUT /api/vendors/<vendor_id>/`: Update a vendor's details.
- `DELETE /api/vendors/<vendor_id>/`: Delete a vendor.

### Purchase Order Endpoints:

- `POST /api/purchase_orders/`: Create a purchase order.
- `GET /api/purchase_orders/`: List all purchase orders.
- `GET /api/purchase_orders/<po_id>/`: Retrieve details of a specific purchase order.
- `PUT /api/purchase_orders/<po_id>/`: Update a purchase order.
- `DELETE /api/purchase_orders/<po_id>/`: Delete a purchase order.

### Vendor Performance Endpoint:

- `GET /api/vendors/<vendor_id>/performance`: Retrieve a vendor's performance metrics.

## Testing

To run the tests, execute:
please use postman application 

## Contributing

Contributions are welcome! Please submit a pull request with your changes.
