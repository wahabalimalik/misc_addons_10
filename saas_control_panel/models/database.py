# -*- coding: utf-8 -*-

import re
import logging
from contextlib import closing

from odoo import models, fields, api
from odoo.tools.translate import _
import odoo
from odoo.service import db
from odoo.exceptions import ValidationError
from odoo import SUPERUSER_ID

DBNAME_PATTERN = '^[a-zA-Z0-9][a-zA-Z0-9_.-]+$'

_logger = logging.getLogger(__name__)

def exp_create_database(vals,country_code,lang,users_detail):
    _logger.info('Create database `%s`.', vals['name'])
    db._create_empty_database(vals['name'])
    _initialize_db(id,vals,country_code,lang,users_detail)
    return True

def _initialize_db(id,vals,country_code,lang,users_detail):
    try:
        dba = odoo.sql_db.db_connect(vals['name'])
        
        db_registory(vals,lang,dba)

        setup(dba,lang,country_code,users_detail,vals)

        
    except Exception, e:
        _logger.exception('CREATE DATABASE failed:')
        raise ValidationError(_('Database creation fails.'))

def db_registory(vals,lang,dba):
    
    with closing(dba.cursor()) as cr:
        odoo.modules.db.initialize(cr)
        odoo.tools.config['load_language'] = lang
        cr.commit()

    registry = odoo.modules.registry.Registry.new(vals['name'], vals['demo'], None, update_module=True)

def setup(dba,lang,country_code,users_detail,vals):
    with closing(dba.cursor()) as cr:
        env = odoo.api.Environment(cr, SUPERUSER_ID, {})

        if lang:
            language(env,lang)

        if country_code:
            country_codes(env,country_code)
        
        if users_detail:
            create_users(env,users_detail)
            create_groups(env,users_detail)

        if vals['apps']:
        	env['ir.config_parameter'].set_param('modules', vals['apps'][0][2])

        db_closing(lang,env,cr)

def language(env,lang):
    modules = env['ir.module.module'].search([('state', '=', 'installed')])
    modules.update_translations(lang)

def country_codes(env,country_code):
    countries = env['res.country'].search([('code', 'ilike', country_code)])
    if countries:
        env['res.company'].browse(1).country_id = countries[0]

def create_users(env,users_detail):
    
    for user in users_detail:
        login = user.name.replace(" ", "_")
        login = login.replace(".","")
        env['res.users'].create({
        	'name' : user.name,
			'login':  login.lower() + '@backoffice24.no',
			'lang' : user.lang,
			'image': user.image,
			'password' : '12345'
            # 'signature' : "<span data-o-mail-quote='1'>-- <br data-o-mail-quote='1'>+"user.name"</span>"
            })

def create_groups(env,users_detail):

	users_record = [rec.id for rec in env['res.users'].search([('id', '!=', 1)])]
	group_id = env.ref('my_control_panel.group_saas_manager')
	group = env['res.groups'].search([('id', '=', group_id.id)])
	for rec in users_record:
		group.users = [(4, rec)]

def db_closing(lang,env,cr):
	values = {'password': 'backoffice24', 'lang': lang}
	login = 'admin@backoffice24.no'
	if login:
		values['login'] = login
		emails = odoo.tools.email_split(login)
		if emails:
			values['email'] = emails[0]

	env.user.write(values)

	cr.execute('SELECT login, password FROM res_users ORDER BY login')
	cr.commit()

class SaasDatabase(models.Model):
    _name = 'saas.database'

    name = fields.Char('Database Name')
    business_name = fields.Many2one('res.partner', string = 'Business Name', domain = "[('is_company', '=', True)]")
    country = fields.Many2one('res.country')
    demo = fields.Boolean()
    inrollment_date = fields.Date('Inrollment Date',default=lambda self: fields.Datetime.now())
    expiry_date = fields.Date('Expiry Date')
    users = fields.Many2many('res.partner')
    apps = fields.Many2many('ir.module.module')

    @api.onchange('business_name')
    def _onchange_users(self):
    	if self.business_name:
    		return {'domain':{'users':[('parent_id','like',self.business_name.name)]}}

    def database_name_checking(self,patren,name):
    	if not re.match(patren, name):
    		raise ValidationError(_('Invalid database name. Only alphanumerical characters, underscore, hyphen and dot are allowed.'))

    def get_country_code(self,country_id):
        rec = self.env['res.country'].search([('id', '=', country_id)])
        return rec.code

    def users_detail(self,users_id):
        rec = self.env['res.partner'].search([('id', 'in', users_id)])
        return rec

    @api.model
    def create(self, vals):
    	self.database_name_checking(DBNAME_PATTERN, vals['name'])
        lang = 'en_US'
    	country_code = self.get_country_code(vals['country'])
        users_detail = self.users_detail(vals['users'][0][2])

        try:
            exp_create_database(vals,country_code,lang,users_detail)
            journal = super(SaasDatabase, self).create(vals)
            return journal

        except Exception, e:
        	error = "Database creation error: %s" % str(e) or repr(e)