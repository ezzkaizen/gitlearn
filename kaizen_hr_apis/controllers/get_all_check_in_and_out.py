# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request


class GetAllUsersCheck(http.Controller):

    @http.route('/get_all_check', type='json', auth='public', motheds=['GET'])
    def get_all_attend(self, rec):
        if rec:
            attend = request.env['hr.attendance'].sudo().search([('id', '=', rec)])
        else:
            attend = request.env['hr.attendance'].sudo().search([])
        attends = []
        for rec in attend:
            vals = {
                'id': rec.id,
                'employee_id': rec.employee_id.name,
                'check_in': rec.check_in,
                'check_out': rec.check_out,
                'worked_hours': rec.worked_hours,
            }
            attends.append(vals)
        print(attends)
        data = {'status': 200, 'response': attends}
        return data
