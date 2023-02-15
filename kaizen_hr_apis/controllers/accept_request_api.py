# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request


class GetAcceptRequest(http.Controller):

    @http.route('/get_accept_request', type='json', auth='public', motheds=['GET'])
    def get_all_accept_request(self):
        accept = request.env['request.view'].sudo().search([('is_accept', '=', True)])
        acceptance = []
        for rec in accept:
            vals = {
                'id': rec.id,
                'name': rec.name,
                'message': rec.message,
                'date': rec.date,
                'distance': rec.distance,
                'location': rec.location,
                'state': rec.state if rec.state else "",
                'is_accept': rec.is_accept,
                'check_type': rec.check_type if rec.check_type else "",

            }
            acceptance.append(vals)
        print(acceptance)
        data = {'status': 200, 'response': acceptance}
        return data
