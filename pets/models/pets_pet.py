from odoo import api, fields, models


class PetsPet(models.Model):
    _name = 'pets.pet'
    _inherit = ["image.mixin", "mail.thread"]
    _description = "Pet"

    name = fields.Char(required=True)
    official_name = fields.Char()
    date_of_birth = fields.Date()
    pet_type = fields.Selection(
        selection=[("cat", "Cat"), ("dog", "Dog")], required=True
    )
    sex = fields.Selection([("male", "Male"), ("female", "Female")], required=True)
    passport_number = fields.Char(string="Passport No.")

    vet_id = fields.Many2one("res.partner", "Veterinarian")
    move_ids = fields.One2many("account.move", "pet_id", "Invoices")
