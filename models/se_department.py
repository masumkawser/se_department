from odoo import models, fields


class SeDepartment(models.Model):
    _name = 'se.department'
    _description = 'department'

    name = fields.Char(
        string='Department Name',
        required=True
    )

    code = fields.Char(
        string='Code',
        required=True
    )
    departmentlogo = fields.Binary(
        string='Department Logo',

    )

    parentdepartment_id = fields.Many2one(
        'se.parent', string='Parent Department')
    # (
    #     string='Parent Department',
    #     required=True
    # )

    academicfaculty = fields.Char(
        string='Academic Faculty',
        required=True
    )

    active = fields.Boolean(
        string='Active',
        default=True)
    note = fields.Text(
        string='Note')
