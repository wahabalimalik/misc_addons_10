# -*- coding: utf-8 -*-
from odoo import http

# class OdooOsmSync(http.Controller):
#     @http.route('/odoo_osm_sync/odoo_osm_sync/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/odoo_osm_sync/odoo_osm_sync/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('odoo_osm_sync.listing', {
#             'root': '/odoo_osm_sync/odoo_osm_sync',
#             'objects': http.request.env['odoo_osm_sync.odoo_osm_sync'].search([]),
#         })

#     @http.route('/odoo_osm_sync/odoo_osm_sync/objects/<model("odoo_osm_sync.odoo_osm_sync"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('odoo_osm_sync.object', {
#             'object': obj
#         })