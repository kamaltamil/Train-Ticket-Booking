# Train Ticket Booking System

A simple command-line based Train Ticket Booking System built with Python. This system allows passengers to book train tickets and administrators to manage trains and view passenger details.

## Features

### For Passengers:
- **Signup**: Create a new account with name, address, phone number, and password
- **Login**: Authenticate using phone number and password
- **Book Tickets**: Search and book tickets between locations, with seat availability checking

### For Administrators:
- **Login**: Secure admin login (default: username 'kamaltamil', password '1101')
- **Add Trains**: Add new trains with details like name, from/to locations, ticket price, and seat count
- **View Passengers**: Check passenger details and booking history

## Technologies Used

- **Python**: Core programming language
- **CSV**: Data storage for trains and passengers
- **Command Line Interface**: Text-based user interaction

## Project Structure

```
Train-Ticket-Booking/
├── main.py              # Main application entry point
├── passenger.py         # Passenger class with signup, login, booking functionality
├── train.py             # Train class for train management
├── train_list.csv       # CSV file storing train information
├── passenger_list.csv   # CSV file storing passenger information
└── README.md           # Project documentation
```

## Installation and Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/kamaltamil/Train-Ticket-Booking.git
   cd Train-Ticket-Booking
   ```

2. **Ensure Python is installed:**
   - This project requires Python 3.x
   - No external dependencies needed (uses only built-in modules)

3. **Run the application:**
   ```bash
   python main.py
   ```

## Usage

1. **Start the application** by running `python main.py`
2. **Choose your role:**
   - Option 1: Admin
   - Option 2: Passenger
   - Option 3: Exit

### Admin Workflow:
1. Login with admin credentials
2. Add trains or view passenger details

### Passenger Workflow:
1. Signup or login to your account
2. Book tickets by specifying from/to locations
3. View available trains and seat counts
4. Confirm booking

## Data Files

- **train_list.csv**: Contains train information (Name, From, To, Price, Seat Count)
- **passenger_list.csv**: Contains passenger information (Name, Address, Phone, Password, Seats Booked)

## Security Note

This is a basic implementation for educational purposes. In a production environment, consider:
- Proper password hashing
- Database instead of CSV files
- Input validation and sanitization
- Secure admin credentials

## Contributing

Feel free to fork this repository and submit pull requests for improvements.

## License

This project is open source and available under the [MIT License](LICENSE).

## Author

Kamal Tamil</content>
<parameter name="filePath">/workspaces/Train-Ticket-Booking/README.md