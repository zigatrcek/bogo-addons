from odoo import fields, models


class PetsSpecies(models.Model):
    _name = 'pets.species'
    _description = 'Species'

    name = fields.Char(required=True, translate=True)
    scientific_name = fields.Char()

