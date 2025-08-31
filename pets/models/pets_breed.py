from odoo import fields, models


class PetsBreed(models.Model):
    _name = 'pets.breed'
    _description = 'Breed'

    name = fields.Char(required=True, translate=True)
    species_id = fields.Many2one('pets.species')
