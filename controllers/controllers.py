# -*- coding: utf-8 -*-
# from odoo import http


# class Librery(http.Controller):
#     @http.route('/librery/librery/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/librery/librery/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('librery.listing', {
#             'root': '/librery/librery',
#             'objects': http.request.env['librery.librery'].search([]),
#         })

#     @http.route('/librery/librery/objects/<model("librery.librery"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('librery.object', {
#             'object': obj
#         })
