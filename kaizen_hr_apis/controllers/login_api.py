# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request


class LoginApi(http.Controller):
    @http.route('/login_api', type='json', auth="none", methods=["POST"])
    def test_login(self, db, login, password, base_location=None):
        request.session.authenticate(db, login, password)
        return request.env['ir.http'].session_info()