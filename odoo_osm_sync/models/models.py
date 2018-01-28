# -*- coding: utf-8 -*-

from odoo import models, fields, api,_
from odoo.exceptions import UserError, ValidationError

class OsmBuildingData(models.Model):
	_name = 'osm.build'

	bus_ids = fields.Integer()
	street = fields.Char()
	name = fields.Char()
	building = fields.Char()
	levels = fields.Integer()
	material = fields.Char()
	shop = fields.Char()
	types = fields.Char()
	amenity = fields.Char()
	info_data = fields.One2many('info.data', 'info_id')


class InfoData(models.Model):
	_name = 'info.data'

	types = fields.Char()
	bus_ids = fields.Char()
	lat = fields.Char()
	lon = fields.Char()
	name = fields.Char()
	shop = fields.Char()
	amenity = fields.Char()
	owner = fields.Char()
	tenant = fields.Char()

	info_id = fields.Many2one('osm.build',ondelete='cascade')
	
		
		

class osm_build_own(models.Model):
    _name = 'build.own'

    name = fields.Char('Owner Name')
    vrn = fields.Integer('VRN')
    accessed = fields.Boolean('Accessed')
    branch = fields.Char('Branch')
    tin = fields.Char('TIN')
    efd = fields.Char('EFD')
    valued = fields.Char('Valued')
    citizen = fields.Boolean()
    tenants = fields.One2many('build.tnt','tnt_id')
    tax = fields.Float()

class osm_build_tnt(models.Model):
    _name = 'build.tnt'
    name = fields.Char()
    tnt_id = fields.Many2one('build.own')
    citizen = fields.Boolean()
    rent = fields.Integer()