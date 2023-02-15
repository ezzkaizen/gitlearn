from odoo import http
from odoo.http import request


class GetCheckOutRequest(http.Controller):

    @http.route('/get_check_out_request', type='json', auth='public', motheds=['GET'])
    def get_out_request(self):
        request_out = request.env['request.view'].sudo().search([('check_type', '=', 'check_out')])
        Check_Out = []
        for rec in request_out:
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
            Check_Out.append(vals)
        print(Check_Out)
        data = {'status': 200, 'response': Check_Out}
        return data
