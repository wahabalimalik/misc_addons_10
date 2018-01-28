# -*- coding: utf-8 -*-
from odoo import http

# class WebsiteCustom(http.Controller):
#     @http.route('/website_custom/website_custom/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/website_custom/website_custom/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('website_custom.listing', {
#             'root': '/website_custom/website_custom',
#             'objects': http.request.env['website_custom.website_custom'].search([]),
#         })

#     @http.route('/website_custom/website_custom/objects/<model("website_custom.website_custom"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('website_custom.object', {
#             'object': obj
#         })