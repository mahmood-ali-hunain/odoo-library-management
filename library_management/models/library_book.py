from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError

class LibraryBook(models.Model):
    _name = 'library.book'
    _description = 'Library Book'
    _order = 'name asc'

    name = fields.Char(string='Title', required=True, index=True)
    isbn = fields.Char(string='ISBN')
    author = fields.Char(string='Author', required=True)
    published_date = fields.Date(string='Publication Date')
    pages = fields.Integer(string='Number of Pages')
    
    # State tracking
    state = fields.Selection([
        ('available', 'Available'),
        ('borrowed', 'Borrowed'),
        ('lost', 'Lost'),
    ], string='Status', default='available', required=True, tracking=True)

    # Relational foreign key
    borrower_id = fields.Many2one('library.member', string='Current Borrower', index=True)
    borrow_date = fields.Date(string='Borrow Date')

    # Business Logic Actions
    def action_borrow(self):
        for record in self:
            if not record.borrower_id:
                raise UserError("Please select a borrower before issuing the book.")
            if record.state == 'borrowed':
                raise UserError("This book is already marked as borrowed.")
            record.write({
                'state': 'borrowed',
                'borrow_date': fields.Date.context_today(record),
            })

    def action_return(self):
        for record in self:
            if record.state != 'borrowed':
                raise UserError("Only borrowed books can be returned.")
            record.write({
                'state': 'available',
                'borrower_id': False,
                'borrow_date': False,
            })

    # Validation Constraint
    @api.constrains('pages')
    def _check_pages(self):
        for record in self:
            if record.pages and record.pages <= 0:
                raise ValidationError("Number of pages must be greater than zero.")