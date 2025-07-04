# Library Management System

A comprehensive command-line library management system built in Python that allows librarians to manage books, DVDs, magazines, and users with full borrowing/returning functionality.

## 🚀 Features

- **Item Management**: Add, remove, update, and view books, DVDs, and magazines
- **User Management**: Register and manage library users
- **Borrowing System**: Track item borrowing and returns
- **Reservation System**: Reserve items (books and DVDs)
- **Data Persistence**: Automatic JSON file storage
- **Input Validation**: Comprehensive error handling and data validation
- **Interactive CLI**: User-friendly menu-driven interface

## 📋 Requirements

- Python 3.7+
- No external dependencies (uses only Python standard library)

## 🏗️ Architecture

### System Flow Chart

For a visual representation of the system architecture and data flow, view our [System Flow Chart on Miro](https://miro.com/app/board/uXjVIpKg5V4=/?embedMode=view_only_without_ui&moveToViewport=1565%2C921%2C4256%2C1926&embedId=371523897622).

### Core Classes

- **`Library`**: Main controller class managing items and users
- **`LibraryItem`**: Abstract base class for all library items
- **`Book`**: Represents books with genre information
- **`DVD`**: Represents DVDs with duration information  
- **`Magazine`**: Represents magazines with genre information
- **`User`**: Represents library users with borrowing history
- **`Reservable`**: Interface for items that can be reserved

### Data Structure

#### Item ID Format
- **Books**: `B-Aa-YYYY-N` (e.g., `B-JD-2020-1`)
- **DVDs**: `D-Aa-YYYY-N` (e.g., `D-SS-2019-2`)
- **Magazines**: `M-Aa-YYYY-N` (e.g., `M-NG-2021-3`)

Where:
- `T`: Item type (B/D/M)
- `Aa`: Author initials (first letter of first and last word)
- `YYYY`: Publication year
- `N`: Sequential item number

#### User ID Format
- **Users**: `U-Ff-Ll-N` (e.g., `U-Jo-Sm-1`)

Where:
- `U`: User identifier
- `Ff`: First name initials (first two characters)
- `Ll`: Last name initials (first two characters)
- `N`: Sequential user number

## 🚀 Quick Start

### Running the Application

```bash
# Navigate to the project directory
cd "Library Management System"

# Run the main application
python main.py
```

### Basic Usage

1. **Start the application**: The main menu will appear
2. **Navigate menus**: Use number keys to select options
3. **Add items**: Go to "Items" → "Add Item" to add books/DVDs/magazines
4. **Add users**: Go to "Users" → "Add User" to register new users
5. **Borrow items**: Go to "Borrow/Return" → "Borrow Item"
6. **Return items**: Go to "Borrow/Return" → "Return Item"
7. **Save and exit**: Choose "Exit" from main menu

## 📁 Project Structure

```
Library Management System/
├── data/                           # Data storage
│   ├── items.json                 # Library items data
│   └── users.json                 # User data
├── modules/                       # Source code
│   ├── main.py                   # Main application and CLI
│   ├── library.py                # Core library management
│   ├── library_item.py           # Abstract base class
│   ├── book.py                   # Book implementation
│   ├── dvd.py                    # DVD implementation
│   ├── magazine.py               # Magazine implementation
│   ├── user.py                   # User management
│   ├── reservable.py             # Reservation interface
│   └── exceptions.py             # Custom exceptions
├── methods_exceptions/           # Documentation
│   └── *.txt                     # Method documentation files
└── README.md                     # This file
```

## 🔧 API Documentation

### Library Class

The main controller class that manages all library operations.

#### Key Methods

- `add_item(item)`: Add a new item to the library
- `remove_item(item)`: Remove an item from the library
- `update_item(item, new_item)`: Update item attributes
- `add_user(user)`: Register a new user
- `remove_user(user)`: Remove a user from the system
- `borrow_item(user, item)`: Borrow an item for a user
- `return_item(user, item)`: Return a borrowed item
- `load_data()`: Load data from JSON files
- `save_data()`: Save data to JSON files

### Item Classes

#### Book
```python
book = Book(title, author, year, available, genre, custom_id=None)
```

#### DVD
```python
dvd = DVD(title, author, year, available, duration, custom_id=None)
```

#### Magazine
```python
magazine = Magazine(title, author, year, available, genre, custom_id=None)
```

### User Class
```python
user = User(first_name, last_name, custom_id=None)
```

## 🛡️ Error Handling

The system includes comprehensive error handling with custom exceptions:

- `InvalidDataTypeError`: Wrong data type provided
- `InvalidValueError`: Invalid value (empty, too short, etc.)
- `MissingFieldError`: Required field missing from data
- `ItemNotFoundError`: Item doesn't exist in library
- `UserNotFoundError`: User doesn't exist in system
- `ItemNotAvailableError`: Item is not available for borrowing
- `ItemNotBorrowedError`: User hasn't borrowed the item
- `ItemAlreadyExistsError`: Item already exists in library
- `UserAlreadyExistsError`: User already exists in system

## 💾 Data Storage

### Items JSON Structure
```json
{
  "id": "B-JD-2020-1",
  "type": "Book",
  "title": "The Great Gatsby",
  "author": "F. Scott Fitzgerald",
  "year": 1925,
  "available": true,
  "genre": "Fiction"
}
```

### Users JSON Structure
```json
{
  "id": "U-Jo-Sm-1",
  "first_name": "John",
  "last_name": "Smith",
  "borrowed_items": ["B-JD-2020-1", "D-SS-2019-2"]
}
```

## 🧪 Development

### Adding New Item Types

1. Create a new class inheriting from `LibraryItem`
2. Implement required abstract methods
3. Add validation logic
4. Update the `Library.__create_item()` method
5. Add to the main menu system

### Testing

The system includes comprehensive input validation and error handling. Test edge cases by:

- Providing invalid data types
- Using empty or invalid strings
- Testing boundary conditions
- Verifying data persistence

## 📝 License

This project is open source and available under the MIT License.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add appropriate documentation
5. Submit a pull request

## 📞 Support

For issues or questions, please open an issue in the repository or contact the development team (only me).

