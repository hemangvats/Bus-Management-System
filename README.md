# Velocity Bus Booking (VBB) Management System 🚌

A comprehensive desktop application designed to streamline bus booking and fleet management. Developed using Python, this application utilizes `tkinter` for the graphical user interface and CSV handling for local, decentralized database management.

## 🚀 Key Features

*   **Customer Portal:** User authentication (sign-up/sign-in) and an intuitive booking interface.
*   **Booking Engine:** Allows customers to select destinations, choose bus types based on varying prices, and calculate total fares based on passenger count.
*   **Decentralized Storage:** Uses CSV files to maintain transparency and decentralization of records for users, locations, bus types, and bookings.
*   **Admin Panel:** Protected admin gateway for management of the application.
    *   **Manage Locations:** Add, edit, or delete travel destinations and their associated prices.
    *   **Manage Fleet:** Add, modify, or remove available bus types and standard rates.
*   **Receipts & Histories:** Customers can view past travel routes, bus types selected, and total fares paid.

## 🛠️ Technology Stack

*   **Programming Language:** Python 3.x
*   **GUI Framework:** Tkinter
*   **Database:** Local CSV File System (Data Structures)
*   **External Dependencies:** None (Relies entirely on standard Python libraries)

## 🗂️ Repository Structure

*   `main.py`: The core application file containing both the frontend GUI logic and backend data handling.
*   `Bustypedata.csv` : Backend storage for available bus types and pricing.
*   `locationdata.csv` : Backend storage for route destinations and pricing.
*   `userdata.csv` : Credentials and information for registered users.
*   `bookingrecords.csv` : Persistent records of all customer transactions.
*   `trial.png`: Background UI image resource.

## ⚙️ How to Run Locally

Since this program uses only built-in standard Python libraries, there are no extra packages to download.

1.  Clone the repository:
    ```bash
    git clone https://github.com/hemangvats/Bus-Management-System.git
    cd Bus-Management-System
    ```
2.  Ensure that all CSV files and `trial.png` are properly situated in the exact same directory.
3.  Run the application using Python:
    ```bash
    python main.py
    ```
    
## 🔑 Default Admin Credentials
To test the admin panel features (route addition, fleet modification, etc.):
*   **Admin Access Code:** `Hem@ng&cyph3r` 
*(Note: Change this hardcoded password in production scenarios)*
