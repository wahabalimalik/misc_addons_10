# -*- coding: utf-8 -*-
from odoo import http

# class WebsiteGlare(http.Controller):
#     @http.route('/website_glare/website_glare/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/website_glare/website_glare/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('website_glare.listing', {
#             'root': '/website_glare/website_glare',
#             'objects': http.request.env['website_glare.website_glare'].search([]),
#         })

#     @http.route('/website_glare/website_glare/objects/<model("website_glare.website_glare"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('website_glare.object', {
#             'object': obj
#         })