# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request


class GetAllUsers(http.Controller):

    @http.route('/get_users', type='json', auth='public', motheds=['GET'])
    def get_all_users(self, rec):
        if rec:
            user = request.env['res.users'].sudo().search([('id', '=', rec)])
        else:
            user = request.env['res.users'].sudo().search([])
        users = []
        for rec in user:
            vals = {
                'id': rec.id,
                'name': rec.name,
                'login': rec.login,
                'phone_number': rec.phone_number,
            }
            users.append(vals)
        print(users)
        data = {'status': 200, 'response': users}
        return data
