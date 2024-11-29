# E-Commerce Django Project

## Overview

This project is for Question 1 of the CAT2.
This project is a simple e-commerce system built using Django. It includes models for `Customer` and `Order` with a one-to-many relationship where each customer can place multiple orders. i have written a summary of what i did.

## Features

- Manage customers and orders.
- List all customers.
- View customer details and their orders.
- Add new customers and orders.

## Prerequisites

- Python 
- Django

## Installation

1. **Clone the repository:**

    ```sh
    I cloned the repository from github to github desktop then opened it in vscode.
    ```

2. **Navigate to the project directory:**

    ```sh
    cd <project_directory>
    ```

3. **Create a virtual environment:**

    ```sh
    python -m venv venv
    ```

4. **Activate the virtual environment:**
   
    - I have Windows so I used:

        ```sh
        venv\Scripts\activate
        ```

5. **Install the required packages:**

    ```sh
    pip install -r requirements.txt
    ```

6. **Apply migrations:**

    ```sh
    python manage.py makemigrations
    python manage.py migrate
    ```

## Running the Project

1. **Start the development server:**

    ```sh
    python manage.py runserver
    ```

2. **Access the application:**
    I opened my  web browser and went to `http://127.0.0.1:8000/` to see the customer list and add customers and orders.

## Project Structure

- `models.py`: Defines the `Customer` and `Order` models and their relationships.
- `views.py`: Handles the display and functionality for listing, viewing, and adding customers and orders.
- `urls.py`: Maps URLs to views.
- `forms.py`: Contains forms for creating and updating `Customer` and `Order` records.
- `admin.py`: Registers the models with the Django admin site.

## I was not sure if this templates are necessary but I added them anyway

- `templates/`: Contains HTML templates for the views.
  - `customer_list.html`: Template to list all customers.
  - `customer_detail.html`: Template to show customer details and their orders.
  - `add_customer.html`: Template to add a new customer.
  - `add_order.html`: Template to add a new order for a customer.

## Comments on Choices

- **Customer Model:** Includes `first_name`,`last_name`, `email`, `phone_number`and  `address` fields. The `email` field is unique to ensure no duplicate entries.
- **Order Model:** Includes `customer`, `order_date`, `payment_method`,`payment_status` and `shipping_address` fields. The `customer` field is a ForeignKey linking each order to a specific customer.


## Testing

1. **Run tests:**

    ```sh
    python manage.py test
    ```
