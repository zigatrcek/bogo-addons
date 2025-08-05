from odoo import fields, models


class AccountMove(models.Model):
    _inherit = 'account.move'

    pet_id = fields.Many2one('pets.pet')
