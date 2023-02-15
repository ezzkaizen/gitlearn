# -*- coding: utf-8 -*-
from odoo import fields, models, api
from odoo import http
from odoo.http import request
import json
import odoo.http as http
from odoo.http import Controller, request, route
from datetime import datetime
from odoo import models, fields, api, exceptions, _



def format_time(time_str):
    return fields.datetime.strptime(time_str, '%m/%d/%Y %I:%M:%S')


class CheckInOut(http.Controller):

    @http.route('/check_in_check_out', type='json', auth='public', methods=["POST"])
    def check_in_checkout(self,  employee_id):

        employee_id = request.env['hr.employee'].search([('id', '=', employee_id)])
        action_date = fields.Datetime.now()
        if employee_id.attendance_state != 'checked_in':
            vals = {
                'employee_id': employee_id.id,
                'check_in': action_date,
            }
            request.env['hr.attendance'].create(vals)
            args = {'status': True, 'message': 'Check in Successfully'}
            return args

        attendance = request.env['hr.attendance'].search([('employee_id', '=', employee_id.id), ('check_out', '=', False)],limit=1)
        if attendance:
            attendance.check_out = action_date
            args = {'status': True, 'message': 'Check Out Successfully'}
        else:
            args = {'status': False, 'message': 'you can checkout before checkin'}

        return args


