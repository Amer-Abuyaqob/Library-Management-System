# Library Management System API Documentation

This document provides comprehensive API documentation for the Library Management System, including all classes, methods, properties, and their usage.

## Table of Contents

1. [Core Classes](#core-classes)
2. [Item Classes](#item-classes)
3. [User Management](#user-management)
4. [Exception Classes](#exception-classes)
5. [Utility Functions](#utility-functions)
6. [Data Storage](#data-storage)

## Core Classes

### Library Class

The main controller class that manages all library operations.

#### Constructor

```python
Library()
```

Creates a new Library instance and loads existing data from JSON files.

#### Properties

- `items` (list): Returns all library items
- `users` (list): Returns all registered users

#### Methods

##### Item Management

```python
add_item(item: LibraryItem) -> bool
```
Adds a new item to the library.

**Parameters:**
- `item`: LibraryItem object to add

**Returns:** True if successful

**Raises:**
- `InvalidDataTypeError`: If item is not a valid library item
- `ItemAlreadyExistsError`: If item already exists

```python
remove_item(item: LibraryItem) -> bool
```
Removes an item from the library.

**Parameters:**
- `item`: LibraryItem object to remove

**Returns:** True if successful

**Raises:**
- `InvalidDataTypeError`: If item is not a valid library item
- `ItemNotFoundError`: If item doesn't exist

```python
update_item(item: LibraryItem, new_item: LibraryItem) -> bool
```
Updates an item's attributes.

**Parameters:**
- `item`: Original item to update
- `new_item`: New item with updated attributes

**Returns:** True if successful

**Raises:**
- `InvalidDataTypeError`: If items are not valid library items
- `ItemNotFoundError`: If original item doesn't exist
- `ItemAlreadyExistsError`: If new item already exists

##### User Management

```python
add_user(user: User) -> bool
```
Adds a new user to the library.

**Parameters:**
- `user`: User object to add

**Returns:** True if successful

**Raises:**
- `InvalidDataTypeError`: If user is not a valid User
- `UserAlreadyExistsError`: If user already exists

```python
remove_user(user: User) -> bool
```
Removes a user from the library.

**Parameters:**
- `user`: User object to remove

**Returns:** True if successful

**Raises:**
- `InvalidDataTypeError`: If user is not a valid User
- `UserNotFoundError`: If user doesn't exist

```python
update_user(user: User, new_user: User) -> bool
```
Updates a user's attributes.

**Parameters:**
- `user`: Original user to update
- `new_user`: New user with updated attributes

**Returns:** True if successful

**Raises:**
- `InvalidDataTypeError`: If users are not valid User objects
- `UserNotFoundError`: If original user doesn't exist
- `UserAlreadyExistsError`: If new user already exists

##### Borrowing Operations

```python
borrow_item(user: User, item: LibraryItem) -> bool
```
Borrows an item for a user.

**Parameters:**
- `user`: User borrowing the item
- `item`: Item to borrow

**Returns:** True if successful

**Raises:**
- `UserNotFoundError`: If user doesn't exist
- `ItemNotFoundError`: If item doesn't exist
- `ItemNotAvailableError`: If item is not available

```python
return_item(user: User, item: LibraryItem) -> bool
```
Returns an item from a user.

**Parameters:**
- `user`: User returning the item
- `item`: Item to return

**Returns:** True if successful

**Raises:**
- `UserNotFoundError`: If user doesn't exist
- `ItemNotFoundError`: If item doesn't exist
- `ItemNotBorrowedError`: If user hasn't borrowed the item

##### Data Persistence

```python
load_data() -> None
```
Loads library data from JSON files.

**Raises:**
- `FileNotFoundError`: If data files don't exist
- Various validation errors if data is corrupted

```python
save_data() -> None
```
Saves library data to JSON files.

**Raises:**
- `IOError`: If writing to files fails

##### Utility Methods

```python
get_item(item_id: str) -> LibraryItem | None
```
Gets an item by its ID.

**Parameters:**
- `item_id`: The item's unique identifier

**Returns:** The item if found, None otherwise

```python
get_user(user_id: str) -> User | None
```
Gets a user by their ID.

**Parameters:**
- `user_id`: The user's unique identifier

**Returns:** The user if found, None otherwise

## Item Classes

### LibraryItem (Abstract Base Class)

Abstract base class for all library items.

#### Constructor

```python
LibraryItem(title: str, author: str, year: int, available: bool)
```

**Parameters:**
- `title`: Item title (non-empty string)
- `author`: Item author (at least 2 characters)
- `year`: Publication year (positive integer)
- `available`: Availability status (boolean)

**Raises:**
- `InvalidDataTypeError`: If parameters have wrong types
- `InvalidValueError`: If parameters have invalid values

#### Properties

- `title` (str): Item title
- `author` (str): Item author
- `year` (int): Publication year
- `available` (bool): Availability status
- `id` (str): Unique identifier

#### Abstract Methods

```python
display_info() -> str
```
Returns formatted information about the item.

```python
check_availability() -> bool
```
Returns the current availability status.

### Book Class

Represents a book in the library system.

#### Constructor

```python
Book(title: str, author: str, year: int, available: bool, genre: str, custom_id: str = None)
```

**Parameters:**
- `title`: Book title (non-empty string)
- `author`: Book author (at least 2 characters)
- `year`: Publication year (positive integer)
- `available`: Availability status (boolean)
- `genre`: Book genre (non-empty string)
- `custom_id`: Custom ID (optional, auto-generated if None)

#### Properties

- `genre` (str): Book genre

#### Methods

```python
reserve(user: User) -> None
```
Reserves the book for a user.

**Parameters:**
- `user`: User reserving the book

```python
reserved_by() -> User | None
```
Returns the user who has reserved the book.

### DVD Class

Represents a DVD in the library system.

#### Constructor

```python
DVD(title: str, author: str, year: int, available: bool, duration: int, custom_id: str = None)
```

**Parameters:**
- `title`: DVD title (non-empty string)
- `author`: DVD director/creator (at least 2 characters)
- `year`: Publication year (positive integer)
- `available`: Availability status (boolean)
- `duration`: Duration in minutes (positive integer)
- `custom_id`: Custom ID (optional, auto-generated if None)

#### Properties

- `duration` (int): Duration in minutes

#### Methods

```python
reserve(user: User) -> None
```
Reserves the DVD for a user.

**Parameters:**
- `user`: User reserving the DVD

```python
reserved_by() -> User | None
```
Returns the user who has reserved the DVD.

### Magazine Class

Represents a magazine in the library system.

#### Constructor

```python
Magazine(title: str, author: str, year: int, available: bool, genre: str, custom_id: str = None)
```

**Parameters:**
- `title`: Magazine title (non-empty string)
- `author`: Magazine author/editor (at least 2 characters)
- `year`: Publication year (positive integer)
- `available`: Availability status (boolean)
- `genre`: Magazine genre (non-empty string)
- `custom_id`: Custom ID (optional, auto-generated if None)

#### Properties

- `genre` (str): Magazine genre

## User Management

### User Class

Represents a library user.

#### Constructor

```python
User(first_name: str, last_name: str, custom_id: str = None)
```

**Parameters:**
- `first_name`: User's first name (at least 2 characters)
- `last_name`: User's last name (at least 2 characters)
- `custom_id`: Custom ID (optional, auto-generated if None)

#### Properties

- `id` (str): Unique user identifier
- `first_name` (str): User's first name
- `last_name` (str): User's last name
- `borrowed_items` (list): List of borrowed item IDs

#### Methods

```python
display_info() -> str
```
Returns formatted information about the user.

```python
add_borrowed_item(item_id: str) -> None
```
Adds an item to the user's borrowed items list.

**Parameters:**
- `item_id`: ID of the item being borrowed

```python
remove_borrowed_item(item_id: str) -> None
```
Removes an item from the user's borrowed items list.

**Parameters:**
- `item_id`: ID of the item being returned

## Exception Classes

### Base Exceptions

```python
InvalidDataTypeError(expected_type: str, received_type: str)
```
Raised when an input has an incorrect data type.

```python
InvalidValueError(message: str)
```
Raised when a value is invalid.

```python
MissingFieldError(field_name: str)
```
Raised when a required field is missing.

### Library-Specific Exceptions

```python
LibraryError
```
Base class for library-related exceptions.

```python
ItemAlreadyExistsError(item: str)
```
Raised when trying to add an item that already exists.

```python
UserAlreadyExistsError(user: str)
```
Raised when trying to add a user that already exists.

```python
ItemNotFoundError(item: str)
```
Raised when an item is not found.

```python
UserNotFoundError(user: str)
```
Raised when a user is not found.

```python
ItemNotAvailableError(item: str)
```
Raised when an item is not available for borrowing.

```python
ItemNotBorrowedError(item: str, user: str)
```
Raised when a user tries to return an item they haven't borrowed.

```python
InvalidItemIDFormatError(item_id: str)
```
Raised when an item ID doesn't follow the required format.

```python
InvalidUserIDFormatError(user_id: str)
```
Raised when a user ID doesn't follow the required format.

## Utility Functions

### Input Validation Functions

```python
validate_choice(choice, num_options: int) -> int
```
Validates a menu choice input.

```python
validate_type(kind: str) -> None
```
Validates an item type input.

```python
validate_author(author: str) -> None
```
Validates an author name input.

```python
validate_title(title: str) -> None
```
Validates a title input.

```python
validate_available(available: str) -> bool
```
Validates an availability input.

```python
validate_year(year: str) -> int
```
Validates a year input.

```python
validate_genre(genre: str) -> None
```
Validates a genre input.

```python
validate_duration(duration: str) -> int
```
Validates a duration input.

```python
validate_item_id(item_id: str) -> None
```
Validates an item ID format.

```python
validate_user_name(name: str, kind: str) -> None
```
Validates a user name input.

```python
validate_user_id(user_id: str) -> None
```
Validates a user ID format.

### Input Collection Functions

```python
take_choice(num_options: int) -> int
```
Gets a validated menu choice from the user.

```python
take_type() -> str
```
Gets a validated item type from the user.

```python
take_author() -> str
```
Gets a validated author name from the user.

```python
take_title() -> str
```
Gets a validated title from the user.

```python
take_available() -> bool
```
Gets a validated availability status from the user.

```python
take_year() -> int
```
Gets a validated year from the user.

```python
take_genre() -> str
```
Gets a validated genre from the user.

```python
take_duration() -> int
```
Gets a validated duration from the user.

```python
take_item_id() -> str
```
Gets a validated item ID from the user.

```python
take_user_name(kind: str) -> str
```
Gets a validated user name from the user.

```python
take_user_id() -> str
```
Gets a validated user ID from the user.

### Utility Functions

```python
print_menu_header(title: str) -> None
```
Prints a formatted menu header.

```python
print_menu_options(options: list[str]) -> None
```
Prints menu options using a consistent style.

```python
insure_decision() -> bool
```
Gets a yes/no decision from the user with validation.

```python
get_item_data() -> tuple
```
Collects all item data from the user.

```python
create_item() -> LibraryItem
```
Creates an item based on collected data.

```python
get_user_data() -> tuple
```
Collects all user data from the user.

```python
create_user() -> User
```
Creates a user based on collected data.

## Data Storage

### File Structure

The system uses JSON files for data persistence:

- `data/items.json`: Stores all library items
- `data/users.json`: Stores all registered users

### JSON Formats

#### Items JSON Structure

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

#### Users JSON Structure

```json
{
  "id": "U-Jo-Sm-1",
  "first_name": "John",
  "last_name": "Smith",
  "borrowed_items": ["B-JD-2020-1", "D-SS-2019-2"]
}
```

### ID Formats

#### Item IDs

Format: `T-Aa-YYYY-N`

- `T`: Item type (B=Book, D=DVD, M=Magazine)
- `Aa`: Author initials (first character of each word)
- `YYYY`: Publication year
- `N`: Sequential item number

Examples:
- `B-JD-2020-1`: Book by John Doe, 2020, #1
- `D-SS-2019-2`: DVD by Steven Spielberg, 2019, #2
- `M-NG-2021-3`: Magazine by National Geographic, 2021, #3

#### User IDs

Format: `U-Ff-Ll-N`

- `U`: User identifier (always 'U')
- `Ff`: First name initials (first two characters)
- `Ll`: Last name initials (first two characters)
- `N`: Sequential user number

Examples:
- `U-Jo-Sm-1`: John Smith, user #1
- `U-Ja-Do-2`: Jane Doe, user #2

## Usage Examples

### Creating and Adding Items

```python
from library import Library
from book import Book
from dvd import DVD
from magazine import Magazine

# Create library instance
library = Library()

# Create items
book = Book("The Great Gatsby", "F. Scott Fitzgerald", 1925, True, "Fiction")
dvd = DVD("The Godfather", "Francis Ford Coppola", 1972, True, 175)
magazine = Magazine("National Geographic", "National Geographic Society", 2021, True, "Science")

# Add items to library
library.add_item(book)
library.add_item(dvd)
library.add_item(magazine)
```

### Creating and Adding Users

```python
from user import User

# Create users
user1 = User("John", "Smith")
user2 = User("Jane", "Doe")

# Add users to library
library.add_user(user1)
library.add_user(user2)
```

### Borrowing and Returning Items

```python
# Borrow an item
library.borrow_item(user1, book)

# Return an item
library.return_item(user1, book)
```

### Saving Data

```python
# Save all changes to files
library.save_data()
```

### Error Handling

```python
from exceptions import ItemNotFoundError, UserNotFoundError

try:
    library.borrow_item(user1, book)
except ItemNotFoundError as e:
    print(f"Item not found: {e}")
except UserNotFoundError as e:
    print(f"User not found: {e}")
``` 