# Library Management System Development Guide

This guide provides comprehensive information for developers working on the Library Management System, including setup, architecture, coding standards, and contribution guidelines.

## Table of Contents

1. [Getting Started](#getting-started)
2. [Project Architecture](#project-architecture)
3. [Coding Standards](#coding-standards)
4. [Testing Guidelines](#testing-guidelines)
5. [Adding New Features](#adding-new-features)
6. [Debugging](#debugging)
7. [Performance Considerations](#performance-considerations)
8. [Security Considerations](#security-considerations)

## Getting Started

### Prerequisites

- Python 3.7 or higher
- No external dependencies required (uses only Python standard library)

### Development Environment Setup

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd "Library Management System"
   ```

2. **Verify Python installation**
   ```bash
   python --version
   # Should be 3.7 or higher
   ```

3. **Run the application**
   ```bash
   python modules/main.py
   ```

### Project Structure

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
├── README.md                     # User documentation
├── API_DOCUMENTATION.md          # API reference
└── DEVELOPMENT_GUIDE.md          # This file
```

## Project Architecture

### Design Patterns

The system follows several key design patterns:

1. **Abstract Factory Pattern**: `LibraryItem` serves as an abstract base class
2. **Strategy Pattern**: Different item types implement different behaviors
3. **Observer Pattern**: Items notify the library of state changes
4. **Factory Method**: Item creation is handled through factory methods

### Class Hierarchy

```
LibraryItem (Abstract)
├── Book (implements Reservable)
├── DVD (implements Reservable)
└── Magazine

User

Library (Main Controller)

Reservable (Interface)
├── Book
└── DVD
```

### Data Flow

1. **User Input** → **Validation** → **Business Logic** → **Data Persistence**
2. **Data Loading** → **Object Creation** → **Validation** → **Memory Storage**

### Key Components

#### Library Class
- Central controller for all operations
- Manages data persistence
- Handles validation and error handling
- Coordinates between items and users

#### Item Classes
- Inherit from `LibraryItem` abstract base class
- Implement type-specific functionality
- Handle their own validation
- Generate unique IDs

#### User Class
- Manages user information and borrowing history
- Handles user-specific operations
- Generates unique user IDs

#### Exception System
- Comprehensive error handling
- Custom exceptions for specific scenarios
- Descriptive error messages

## Coding Standards

### Python Style Guide

Follow PEP 8 guidelines:

```python
# Good
def add_item(self, item):
    """Add a new item to the library."""
    self.__validate_item(item)
    self.__items.append(item)
    return True

# Bad
def add_item(self,item):
    self.__validate_item(item)
    self.__items.append(item)
    return True
```

### Naming Conventions

- **Classes**: PascalCase (e.g., `LibraryItem`, `User`)
- **Methods**: snake_case (e.g., `add_item`, `validate_input`)
- **Private methods**: Leading underscore (e.g., `__validate_item`)
- **Constants**: UPPER_CASE (e.g., `MAX_ITEMS`)
- **Variables**: snake_case (e.g., `item_count`, `user_name`)

### Documentation Standards

#### Module Documentation
```python
"""
Module Name

Brief description of the module's purpose and functionality.

Key Features:
- Feature 1
- Feature 2
- Feature 3

Usage:
    Basic usage examples
"""
```

#### Class Documentation
```python
class ClassName:
    """
    Brief description of the class.
    
    Detailed description including:
    - Purpose and functionality
    - Key attributes and methods
    - Usage examples
    
    Attributes:
        attr1 (type): Description
        attr2 (type): Description
    """
```

#### Method Documentation
```python
def method_name(self, param1, param2=None):
    """
    Brief description of what the method does.
    
    Detailed description including:
    - What the method accomplishes
    - How it works
    - Side effects
    
    Args:
        param1 (type): Description
        param2 (type, optional): Description
        
    Returns:
        type: Description of return value
        
    Raises:
        ExceptionType: When and why this exception is raised
        
    Example:
        >>> obj.method_name("example")
        "result"
    """
```

### Error Handling

#### Exception Guidelines

1. **Use specific exceptions**: Create custom exceptions for specific error conditions
2. **Provide context**: Include relevant information in error messages
3. **Handle gracefully**: Don't let exceptions crash the application
4. **Log errors**: Record errors for debugging (when logging is implemented)

```python
# Good
try:
    self.__validate_item(item)
except InvalidDataTypeError as e:
    raise ItemValidationError(f"Invalid item data: {e}")

# Bad
try:
    self.__validate_item(item)
except Exception as e:
    print("Error occurred")
```

### Input Validation

#### Validation Guidelines

1. **Validate early**: Check inputs as soon as they're received
2. **Be specific**: Provide clear error messages
3. **Check types**: Ensure correct data types
4. **Validate ranges**: Check for reasonable values
5. **Sanitize inputs**: Remove unwanted characters

```python
def validate_title(self, title):
    """Validate item title."""
    if not isinstance(title, str):
        raise InvalidDataTypeError("string", type(title).__name__)
    
    if not title.strip():
        raise InvalidValueError("Title must be a non-empty string")
    
    return title.strip()
```

## Testing Guidelines

### Testing Strategy

1. **Unit Tests**: Test individual methods and classes
2. **Integration Tests**: Test interactions between components
3. **System Tests**: Test the entire application workflow
4. **Error Tests**: Test error conditions and edge cases

### Test Structure

```python
import unittest
from library import Library
from book import Book
from exceptions import InvalidDataTypeError

class TestLibrary(unittest.TestCase):
    """Test cases for Library class."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.library = Library()
        self.test_book = Book("Test Book", "Test Author", 2020, True, "Test Genre")
    
    def test_add_item_success(self):
        """Test successful item addition."""
        result = self.library.add_item(self.test_book)
        self.assertTrue(result)
        self.assertIn(self.test_book, self.library.items)
    
    def test_add_item_duplicate(self):
        """Test adding duplicate item."""
        self.library.add_item(self.test_book)
        
        with self.assertRaises(ItemAlreadyExistsError):
            self.library.add_item(self.test_book)
    
    def test_add_item_invalid_type(self):
        """Test adding invalid item type."""
        with self.assertRaises(InvalidDataTypeError):
            self.library.add_item("not an item")
```

### Test Categories

#### Unit Tests
- Individual method functionality
- Input validation
- Error handling
- Edge cases

#### Integration Tests
- Class interactions
- Data flow between components
- File I/O operations

#### System Tests
- Complete user workflows
- End-to-end scenarios
- Performance under load

### Running Tests

```bash
# Run all tests
python -m unittest discover

# Run specific test file
python -m unittest test_library.py

# Run with verbose output
python -m unittest -v test_library.py
```

## Adding New Features

### Feature Development Process

1. **Plan**: Define requirements and design
2. **Implement**: Write code following standards
3. **Test**: Create comprehensive tests
4. **Document**: Update documentation
5. **Review**: Code review and testing
6. **Deploy**: Integrate into main codebase

### Adding New Item Types

To add a new item type (e.g., AudioBook):

1. **Create the class**
   ```python
   class AudioBook(LibraryItem, Reservable):
       """Represents an audiobook in the library system."""
       
       def __init__(self, title, author, year, available, narrator, duration, custom_id=None):
           super().__init__(title, author, year, available)
           self.__validate_narrator(narrator)
           self.__narrator = narrator
           self.__validate_duration(duration)
           self.__duration = duration
           # ... rest of implementation
   ```

2. **Update Library class**
   ```python
   def __create_item(self, item):
       # ... existing code ...
       elif item_type == "AUDIOBOOK":
           # Add audiobook creation logic
           pass
   ```

3. **Update main.py**
   ```python
   def validate_type(kind):
       if kind not in ["Book", "DVD", "Magazine", "AudioBook"]:
           raise InvalidValueError("Item type must be 'Book', 'DVD', 'Magazine', or 'AudioBook'.")
   ```

4. **Add tests**
   ```python
   class TestAudioBook(unittest.TestCase):
       """Test cases for AudioBook class."""
       # ... test implementation
   ```

5. **Update documentation**
   - Update README.md
   - Update API_DOCUMENTATION.md
   - Add usage examples

### Adding New User Features

To add new user functionality (e.g., user roles):

1. **Extend User class**
   ```python
   class User:
       def __init__(self, first_name, last_name, role="member", custom_id=None):
           # ... existing code ...
           self.__role = role
   ```

2. **Add validation**
   ```python
   def __validate_role(self, role):
       valid_roles = ["member", "librarian", "admin"]
       if role not in valid_roles:
           raise InvalidValueError(f"Role must be one of: {valid_roles}")
   ```

3. **Update business logic**
   ```python
   def borrow_item(self, user, item):
       if user.role == "member" and len(user.borrowed_items) >= 5:
           raise BorrowingLimitError("Members can only borrow 5 items at a time")
       # ... rest of implementation
   ```

## Debugging

### Debugging Tools

1. **Print Statements**: For quick debugging
   ```python
   print(f"DEBUG: Adding item {item.title} to library")
   ```

2. **Python Debugger**: For interactive debugging
   ```python
   import pdb; pdb.set_trace()
   ```

3. **Logging**: For production debugging (when implemented)
   ```python
   import logging
   logging.debug("Adding item to library")
   ```

### Common Issues

#### Data Persistence Issues
- Check file permissions
- Verify JSON format
- Ensure proper error handling

#### Validation Errors
- Check input data types
- Verify validation logic
- Review error messages

#### Performance Issues
- Monitor memory usage
- Check for infinite loops
- Optimize data structures

### Debugging Workflow

1. **Reproduce**: Create a minimal test case
2. **Isolate**: Identify the problematic component
3. **Analyze**: Use debugging tools to understand the issue
4. **Fix**: Implement the solution
5. **Test**: Verify the fix works
6. **Document**: Record the solution for future reference

## Performance Considerations

### Optimization Strategies

1. **Efficient Data Structures**
   - Use lists for small collections
   - Consider dictionaries for large lookups
   - Optimize search algorithms

2. **Memory Management**
   - Avoid unnecessary object creation
   - Use generators for large datasets
   - Implement proper cleanup

3. **File I/O Optimization**
   - Batch file operations
   - Use buffered I/O
   - Implement caching when appropriate

### Performance Monitoring

```python
import time

def performance_monitor(func):
    """Decorator to monitor function performance."""
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} took {end_time - start_time:.4f} seconds")
        return result
    return wrapper

@performance_monitor
def load_data(self):
    """Load library data with performance monitoring."""
    # ... implementation
```

## Security Considerations

### Input Validation

1. **Sanitize all inputs**: Remove potentially harmful characters
2. **Validate file paths**: Prevent directory traversal attacks
3. **Check file sizes**: Prevent memory exhaustion
4. **Validate JSON**: Ensure proper JSON structure

### Data Protection

1. **Sensitive Data**: Don't store sensitive information in plain text
2. **Access Control**: Implement proper access controls
3. **Data Backup**: Regular backups of important data
4. **Error Messages**: Don't expose sensitive information in error messages

### Security Best Practices

```python
import os
import json

def safe_file_operation(file_path, operation):
    """Safely perform file operations."""
    # Validate file path
    if not os.path.exists(os.path.dirname(file_path)):
        raise FileNotFoundError("Invalid file path")
    
    # Check file size
    if os.path.exists(file_path) and os.path.getsize(file_path) > MAX_FILE_SIZE:
        raise ValueError("File too large")
    
    # Perform operation
    return operation(file_path)
```

## Contributing

### Contribution Guidelines

1. **Fork the repository**
2. **Create a feature branch**
3. **Follow coding standards**
4. **Write comprehensive tests**
5. **Update documentation**
6. **Submit a pull request**

### Code Review Process

1. **Automated checks**: Ensure tests pass
2. **Manual review**: Code review by maintainers
3. **Documentation review**: Verify documentation updates
4. **Integration testing**: Test with existing codebase

### Release Process

1. **Version bump**: Update version numbers
2. **Changelog**: Document changes
3. **Testing**: Comprehensive testing
4. **Documentation**: Update all documentation
5. **Release**: Tag and release

## Support and Resources

### Getting Help

- **Documentation**: Check README.md and API_DOCUMENTATION.md
- **Issues**: Report bugs and request features
- **Discussions**: Ask questions and share ideas

### Additional Resources

- **Python Documentation**: https://docs.python.org/
- **PEP 8 Style Guide**: https://www.python.org/dev/peps/pep-0008/
- **Unit Testing**: https://docs.python.org/3/library/unittest.html

---

This development guide should be updated as the project evolves. Please contribute improvements and suggestions.
