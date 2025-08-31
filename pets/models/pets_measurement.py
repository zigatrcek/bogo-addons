from odoo import fields, models


class PetsMeasurement(models.Model):
    _name = "pets.measurement"
    _description = "Measurement"

    measurement_type = fields.Selection([("weight", "Weight"), ("size", "Size")], default='weight')
    pet_id = fields.Many2one('pets.pet')
    value = fields.Float()
    date = fields.Date(default=fields.Date.context_today)
    # TODO uom
