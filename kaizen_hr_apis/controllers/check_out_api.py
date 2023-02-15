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


class CheckOutApi(http.Controller):

    @http.route('/check_out_api', type='json', auth='public', methods=["POST"])
    def check_in(self, **rec):
        check_out = datetime.strptime(rec['check_out'], '%Y-%m-%d %H:%M:%S')
        # check_in = datetime.strptime(rec['check_in'], '%Y-%m-%d %H:%M:%S')
        # check_in = datetime.strptime(rec['check_in'], '%Y-%m-%d %H:%M:%S')
        # attendance = request.env['hr.attendance'].search([('employee_id', '=', self.id), ('check_out', '=', False)])
        # print(attendance)
        # if attendance:
        #     attendance.check_out = check_out
        # action_date = fields.Datetime.now()
        #
        # if self.attendance_state != 'checked_in':
        #     vals = {
        #         'employee_id': self.id,
        #         'check_in': action_date,
        #     }
        #     return self.env['hr.attendance'].create(vals)
        # attendance = self.env['hr.attendance'].search([('employee_id', '=', self.id), ('check_out', '=', False)],
        #                                               limit=1)
        # if attendance:
        #     attendance.check_out = action_date
        # else:
        #     raise exceptions.UserError(
        #         _('Cannot perform check out on %(empl_name)s, could not find corresponding check in. '
        #           'Your attendances have probably been modified manually by human resources.') % {
        #             'empl_name': self.sudo().name, })
        # return attendance
        # attendence_check_in = request.env['hr.attendance'].sudo().search(
        #     [('check_out', '=', False), ('check_in', '!=', False)])
        # print(attendence_check_in, 1111111111111111111)
        if rec:
            print(rec)
            vals = {
                'employee_id': rec['employee_id'],
                # 'check_in': check_in if check_in else False,
                'check_out': check_out if check_out else False,
            }
            check_user = request.env['hr.attendance'].sudo().create(vals)
            print(check_user, 11111111111111111)
            args = {'success': True, 'message': 'Check Out Attendence Updated Successfully'}
            return args
        else:
            data = {'success': False, 'message': 'You Must Enter Check In And ID'}
            return data



        # if rec['employee_id']:
        #     vals = {
        #         'check_in': check_in,
        #     }
        #     new = request.env['hr.attendance'].sudo().create(vals)
        #     print(new)
        #     if rec['employee_id'] and rec['check_in']:
        #         vals = {
        #             'check_out': check_out
        #         }
        #         new.append(vals)
        # else:
        #     data = {'success': False, 'message': 'You Must Enter Check In And ID'}
        #     return data


