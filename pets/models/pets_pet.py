from odoo import api, fields, models


class PetsPet(models.Model):
    _name = 'pets.pet'
    
    name = fields.Char()
    official_name = fields.Char()
    date_of_birth = fields.Date()
    pet_type = fields.Selection(selection=[
        ('cat', 'Cat'),
        ('dog', 'Dog')
    ])
    