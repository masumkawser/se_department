from odoo import models,fields

class SeDepartment(models.Model):
    _name='se.department'
    _description='department'

    name = fields.Char(
        string='DepartmentName',
        required=True
    )
    
    code = fields.Char(
        string='Code',
        required=True
    )
    departmentlogo = fields.Binary(
        string='DepartmentLogo',
        
    )
    parentdepartment = fields.Char(
        string='Parent department',
        required=True
    )
    
    academicfaculty =fields.Char(
        string='Academic Faculty',
        required=True
    )
    
    # active=fields.Boolean(string='Active',default=True)