# -*- coding: utf-8 -*-
# from odoo import http


# class Estate1(http.Controller):
#     @http.route('/estate1/estate1', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/estate1/estate1/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('estate1.listing', {
#             'root': '/estate1/estate1',
#             'objects': http.request.env['estate1.estate1'].search([]),
#         })

#     @http.route('/estate1/estate1/objects/<model("estate1.estate1"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('estate1.object', {
#             'object': obj
#         })

