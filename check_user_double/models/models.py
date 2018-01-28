# -*- coding: utf-8 -*-

from odoo import models, api, _
import openerp.http as http
import odoo
from contextlib import closing
from odoo.exceptions import ValidationError

class ResUsersExt(models.Model):
    _inherit = 'res.users'

    @api.constrains('login')
    def _check_login_duplications(self):
    	for db_name in http.db_list():
        	db = odoo.sql_db.db_connect(db_name)
        	with closing(db.cursor()) as cr:
        		cr.execute('SELECT login FROM res_users ORDER BY login')
        		rec = cr.fetchall()
        		if (self.login,) in rec:
        			raise ValidationError(_('This email already exist.Try some other one'))