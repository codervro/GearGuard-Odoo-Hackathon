from odoo import models, fields

class MaintenanceRequest(models.Model):
    _name = 'gearguard.request'
    _description = 'Maintenance Request'

    subject = fields.Char(string="Issue", required=True)
    equipment_id = fields.Many2one('gearguard.equipment', string="Equipment")
    technician = fields.Char(string="Assigned Technician")

    state = fields.Selection([
        ('new', 'New'),
        ('progress', 'In Progress'),
        ('done', 'Repaired')
    ], default='new', string="Status")
