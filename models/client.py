from odoo import models, fields


class Client(models.Model):
    _name='client'
    _description = "Client "
    _inherits = {'owner': 'owner_id'}

    owner_id = fields.Many2one('owner', required=True, ondelete='cascade')

