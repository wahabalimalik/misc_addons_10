# -*- coding: utf-8 -*-

import openerp.http as http
import odoo
from contextlib import closing
from odoo.tools.translate import _
from odoo.addons.web.controllers import main
from odoo.http import request

class Extension(main.Home):

    @http.route()
    def web_login(self, redirect=None, **kw):
        main.ensure_db()
        request.params['login_success'] = False
        if request.httprequest.method == 'GET' and redirect and request.session.uid:
            return http.redirect_with_hash(redirect)

        if not request.uid:
            request.uid = odoo.SUPERUSER_ID

        values = request.params.copy()
        try:
            values['databases'] = http.db_list()
        except odoo.exceptions.AccessDenied:
            values['databases'] = None

        if request.httprequest.method == 'POST':
            
            old_uid = request.uid
            database = 'Backoffice24'
            for db_name in odoo.service.db.list_dbs(force=False):
                db = odoo.sql_db.db_connect(db_name)
                with closing(db.cursor()) as cr:
                    cr.execute('SELECT login FROM res_users ORDER BY login')
                    rec = cr.fetchall()
                    if (request.params['login'],) in rec:
                        database = db_name
                        break
            odoo.tools.config['dbfilter'] = database

            username = request.params['login']
            uid = request.session.authenticate(database, username, request.params['password'])
            if uid is not False:
                request.params['login_success'] = True
                if not redirect:
                    redirect = '/web'
                return http.redirect_with_hash(redirect)
            request.uid = old_uid
            values['error'] = _("Wrong login/password")
        return request.render('web.login', values)
