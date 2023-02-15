# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request


class GetEmployeeDetails(http.Controller):

    @http.route('/get_all_employee', type='json', auth='public', motheds=['GET'])
    def get_employee_details(self, rec):
        if rec:
            employee = request.env['hr.employee'].sudo().search([('id', '=', rec)])
        else:
            employee = request.env['hr.employee'].sudo().search([])
        employees = []
        for rec in employee:
            if employee:
                vals = {
                    'id': rec.id,
                    'name': rec.name,
                    'mobile_phone': rec.mobile_phone if rec.mobile_phone else "",
                    'department_id': rec.department_id.id if rec.department_id.id else "",
                    'work_email': rec.work_email if rec.work_email else "",
                    'parent_id': rec.parent_id.id if rec.parent_id.id else "",
                    'coach_id': rec.coach_id.id if rec.coach_id.id else "",
                    'address_id': rec.address_id.id,
                    'work_location_id': rec.work_location_id.id if rec.work_location_id.id else "",
                    'gender': rec.gender if rec.gender else "",
                    'country_id': rec.country_id.id if rec.country_id.id else "",
                    'birthday': rec.birthday if rec.birthday else "",
                }
                employees.append(vals)
        print(employees)
        data = {'status': 200, 'response': employees}
        return data
