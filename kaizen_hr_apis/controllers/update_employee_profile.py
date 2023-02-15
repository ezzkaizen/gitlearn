from odoo import fields, models, api
from odoo import http
from odoo.http import request
import json
import odoo.http as http
from odoo.http import Controller, request, route


class UpdateEmployeeProfile(http.Controller):
    @http.route('/update_employee_profile', type='json', auth='public', methods=["PATCH"])
    def update_customer(self, **rec):
        print("rec...", rec)
        employee_data = request.env['hr.employee'].sudo().browse(rec['rec'])
        if employee_data:
            employee_data.sudo().write(
                {'name': rec.get('name'), 'mobile_phone': rec.get('mobile_phone'), 'work_email': rec.get('work_email'),
                 'parent_id': rec.get('parent_id'),
                 'coach_id': rec.get('coach_id'), 'address_id': rec.get('address_id'),
                 'work_location_id': rec.get('work_location_id'), 'gender': rec.get('gender'),
                 'country_id': rec.get('country_id')})
            print(employee_data)
            args = {'success': True, 'message': 'Employee Data Updated'}
            return args
        else:
            data = {'success': False, 'message': 'No Data Updated'}
            return data
