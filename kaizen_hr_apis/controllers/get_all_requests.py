# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request


class GetAllRequests(http.Controller):

    @http.route('/get_all_request', type='json', auth='public', motheds=['GET'])
    def get_all_requests(self, rec):
        if rec:
            req = request.env['request.view'].sudo().search([('id', '=', rec)])
        else:
            req = request.env['request.view'].sudo().search([])
        requests = []
        for rec in req:
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
            requests.append(vals)
        print(requests)
        data = {'status': 200, 'response': requests}
        return data
