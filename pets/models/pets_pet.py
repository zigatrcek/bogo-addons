from odoo import api, fields, models


class PetsPet(models.Model):
    _name = 'pets.pet'
    _inherit = ["image.mixin"]
    _description = "Pet"

    name = fields.Char(required=True)
    official_name = fields.Char()
    date_of_birth = fields.Date()
    pet_type = fields.Selection(
        selection=[("cat", "Cat"), ("dog", "Dog")], required=True
    )
    sex = fields.Selection([("male", "Male"), ("female", "Female")], required=True)
