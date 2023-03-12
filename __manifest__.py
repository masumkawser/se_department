# -*- coding: utf-8 -*-
{
    'name': "se_department",

    'summary': """
        This is smart-edu module for department 
        """,

    'description': """
        smart-edu department
    """,

    'author': "Md.Kawser ahamed",
    'website': "",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
            # security
        'security/ir.model.access.csv',
            # views
        'views/se_departmet_view.xml',
        'views/se_parent_view.xml',
        'views/se_department_menu.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
