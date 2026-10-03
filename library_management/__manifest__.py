{
    'name': 'Library Management System',
    'version': '17.0.1.0.0',
    'summary': 'Manage cataloged books, registered members, and borrowing status.',
    'description': """
        A streamlined library operations management tool built for Odoo 17.
        Tracks catalog inventory, borrower status, and membership histories.
    """,
    'category': 'Services/Library',
    'author': 'Your Name',
    'license': 'LGPL-3',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/library_book_views.xml',
        'views/library_member_views.xml',
        'views/library_menus.xml',
    ],
    'application': True,
    'installable': True,
    'auto_install': False,
}