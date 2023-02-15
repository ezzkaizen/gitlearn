from odoo import http
from odoo.http import request


class GetOthersRequest(http.Controller):

    @http.route('/get_others_request', type='json', auth='public', motheds=['GET'])
    def get_other_request(self):
        other = request.env['request.view'].sudo().search(
            [('check_type', '!=', 'check_in'), ('check_type', '!=', 'check_out')])
        other_request = []
        for rec in other:
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
            other_request.append(vals)
        print(other_request)
        data = {'status': 200, 'response': other_request}
        return data
