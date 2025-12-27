from odoo import models, fields

class Equipment(models.Model):
    _name = 'gearguard.equipment'
    _description = 'Equipment'

    name = fields.Char(string="Equipment Name", required=True)
    serial_number = fields.Char(string="Serial Number")
    maintenance_team = fields.Char(string="Maintenance Team")
