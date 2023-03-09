# -*- coding: utf-8 -*-
# from odoo import http


# class SeDepartment(http.Controller):
#     @http.route('/se_department/se_department', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/se_department/se_department/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('se_department.listing', {
#             'root': '/se_department/se_department',
#             'objects': http.request.env['se_department.se_department'].search([]),
#         })

#     @http.route('/se_department/se_department/objects/<model("se_department.se_department"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('se_department.object', {
#             'object': obj
#         })
