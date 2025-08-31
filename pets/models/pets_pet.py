from odoo import api, fields, models


class PetsPet(models.Model):
    _name = 'pets.pet'
    _inherit = ["avatar.mixin", "mail.thread", "mail.activity.mixin"]
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

    weight_measurement_ids = fields.One2many(
        "pets.measurement", "pet_id", domain=[("measurement_type", "=", "weight")]
    )
    size_measurement_ids = fields.One2many(
        "pets.measurement", "pet_id", domain=[("measurement_type", "=", "size")]
    )
