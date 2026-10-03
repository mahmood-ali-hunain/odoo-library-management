# Odoo 17 Library Management System

A custom Odoo 17 Community module to manage books, patrons, and issuance workflows.

## Features
- **Book Catalog:** Track book title, ISBN, author, and availability status.
- **Member Management:** Register patrons and track borrowing history.
- **Issuance Workflow:** Custom action buttons to borrow and return books with status badge transitions.
- **ORM Constraints:** Page validation and unique member ID checks.

## Architecture
- **Framework:** Odoo 17 Community
- **Language:** Python 3.10+ / Odoo ORM
- **Database:** PostgreSQL
- **Frontend Views:** XML (Tree, Form, Search) using Odoo 17 invisible/readonly attributes