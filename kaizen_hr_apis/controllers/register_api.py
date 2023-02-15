# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request


class RegisterApi(http.Controller):

    @http.route('/register_api', type='json', auth='public', methods=["POST"])
    def register_user(self, **rec):
        print(rec,555555555555555555555)
        if rec['name'].strip() and rec['login'].strip() and rec['phone_number'].strip() and rec['password'].strip():
            vals = {
                'name': rec['name'],
                'login': rec['login'],
                'password': rec['password'],
                'phone_number': rec['phone_number'],
                'groups_id': [(6, 0, [request.env.ref('base.group_public').id])],
            }
            new_user = request.env['res.users'].sudo().create(vals)
            print("new_user", new_user)
            args = {'success': True, 'message': 'Success'}
            return args
        else:
            data = {'success': False, 'message': 'No Register Created'}
            return data
