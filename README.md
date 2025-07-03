# Library Management System

This project is a simple command line application for managing library items and users. It allows viewing, adding, removing and updating books, magazines and DVDs as well as tracking borrowing and returning of items.

## Running the application

Execute the main program using Python:

```bash
python modules/main.py
```

This launches an interactive menu-driven interface in the terminal. All functionality is available without installing any third‑party packages.

## Data files

The application stores its data in the `data/` directory:

- `items.json` – a list of library items (books, magazines and DVDs) with fields such as `id`, `title`, `author`, `year`, `available` and either `genre` or `duration` depending on the item type.
- `users.json` – a list of users identified by `id`, `first_name` and `last_name`. Each user also keeps a list of `borrowed_items` referencing item IDs.

These JSON files are read on startup and overwritten on exit when the library data is saved.

No external dependencies are required; the code only relies on the Python standard library.

