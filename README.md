# Velocity Bus Booking (VBB) Management System 🚌

A full-stack desktop application designed for efficient bus fleet management and passenger bookings. This system leverages a robust **MySQL Relational Database** to ensure high data integrity, secure user authentication, and real-time management of travel resources.

---

## 🚀 Key Features

### 👤 Customer Experience
*   **Secure Authentication:** Integrated Sign-up and Login systems for personalized access.
*   **Booking Engine:** Real-time selection of destinations and bus types with automated fare calculation.
*   **Travel History:** Instant access to digital receipts and detailed logs of all previous bookings.

### 🛠️ Administrative Control
*   **Fleet Management:** Add, modify, or retire bus types and adjust pricing models instantly.
*   **Location Management:** Dynamic CRUD (Create, Read, Update, Delete) operations for travel routes and destinations.
*   **Financial Tracking:** Centralized oversight of total revenue and passenger distributions.

---

## 🛠️ Technology Stack

*   **Programming Language:** Python 3.x
*   **GUI Library:** Tkinter
*   **Database:** MySQL Server
*   **Database Connector:** `mysql-connector-python`

---

## 🗂️ Core Architecture

*   `main.py`: Drives the primary application logic and user interface design.
*   `database.py`: A modular database handler that manages all SQL transactions, schema initialization, and data persistence.
*   `trial.png`: UI asset for an enhanced visual experience.

---

## ⚙️ Local Development Setup

### 1. Database Initialization
Ensure you have a MySQL server running locally. Create the database schema by executing the scripts included in the repository.

### 2. Environment Configuration
Update the connection string in `database.py` to match your local credentials:
```python
# database.py
self.host = "localhost"
self.user = "root"
self.password = "YOUR_MYSQL_PASSWORD"
```

### 3. Installation
Install the required Python driver:
```bash
pip install mysql-connector-python
```

### 4. Launching the Application
Execute the main entry point to start the management system:
```bash
python main.py
```

---

## 🔑 Admin Gateway
The Administrative Panel is restricted and requires a dedicated access key.
*   **Default Admin Access Code:** `Hem@ng&cyph3r`

---
*Developed with ❤️ by [Hemang Vats](https://github.com/hemangvats)*
