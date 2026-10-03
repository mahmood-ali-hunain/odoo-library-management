from odoo import models, fields, api
from odoo.exceptions import ValidationError

class LibraryMember(models.Model):
    _name = 'library.member'
    _description = 'Library Member'
    _rec_name = 'name'

    name = fields.Char(string='Full Name', required=True, index=True)
    member_code = fields.Char(
        string='Member ID', 
        required=True, 
        copy=False,
        default='New'
    )
    email = fields.Char(string='Email')
    phone = fields.Char(string='Phone')
    join_date = fields.Date(string='Join Date', default=fields.Date.context_today)
    active = fields.Boolean(string='Active', default=True)

    # Reverse lookup relation
    borrowed_book_ids = fields.One2many(
        'library.book', 
        'borrower_id', 
        string='Borrowed Books'
    )
    
    # Computed Field with @api.depends
    borrowed_books_count = fields.Integer(
        string='Borrowed Count', 
        compute='_compute_borrowed_books_count',
        store=True
    )

    @api.depends('borrowed_book_ids')
    def _compute_borrowed_books_count(self):
        for member in self:
            member.borrowed_books_count = len(member.borrowed_book_ids)

    _sql_constraints = [
        ('member_code_unique', 'unique(member_code)', 'The Member ID must be unique!'),
    ]