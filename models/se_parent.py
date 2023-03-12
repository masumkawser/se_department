from odoo import models, fields


class SeParentDepartment(models.Model):
    _name = 'se.parent'
    _description = 'Parent department'

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
    parentdepartment = fields.Char(
        string='Parent Department'
        # required=True
    )

    academicfaculty = fields.Char(
        string='Academic Faculty',
        required=True
    )

    active = fields.Boolean(
        string='Active',
        default=True)
    note = fields.Text(
        string='Note')
