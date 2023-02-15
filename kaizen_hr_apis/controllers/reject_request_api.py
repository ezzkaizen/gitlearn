# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request


class GetRejectRequest(http.Controller):

    @http.route('/get_reject_request', type='json', auth='public', motheds=['GET'])
    def get_all_reject_request(self):
        reject = request.env['request.view'].sudo().search([('is_accept', '=', False)])
        rejected = []
        for rec in reject:
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
            rejected.append(vals)
        print(rejected)
        data = {'status': 200, 'response': rejected}
        return data
