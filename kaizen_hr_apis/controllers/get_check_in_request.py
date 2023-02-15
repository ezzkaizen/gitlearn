from odoo import http
from odoo.http import request


class GetCheckInRequest(http.Controller):

    @http.route('/get_check_in_request', type='json', auth='public', motheds=['GET'])
    def get_in_request(self):
        request_in = request.env['request.view'].sudo().search([('check_type', '=', 'check_in')])
        Check_In = []
        for rec in request_in:
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
            Check_In.append(vals)
        print(Check_In)
        data = {'status': 200, 'response': Check_In}
        return data
