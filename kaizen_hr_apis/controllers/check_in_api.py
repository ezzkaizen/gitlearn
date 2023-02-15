# -*- coding: utf-8 -*-
from odoo import fields, models, api
from odoo import http
from odoo.http import request
import json
import odoo.http as http
from odoo.http import Controller, request, route
from datetime import datetime


def format_time(time_str):
    return fields.datetime.strptime(time_str, '%m/%d/%Y %I:%M:%S')


class CheckInApi(http.Controller):

    @http.route('/check_in_api', type='json', auth='public', methods=["POST"])
    def check_in(self, **rec):
        print(rec)
        check_in = datetime.strptime(rec['check_in'], '%Y-%m-%d %H:%M:%S')
        # check_out = datetime.strptime(rec['check_out'], '%Y-%m-%d %H:%M:%S')
        print(rec)
        if rec:
            vals = {
                'employee_id': rec['employee_id'],
                'check_in': check_in if rec['check_in'] else "",
                # 'check_out': check_out if rec['check_out'] else False,
            }
            check_user = request.env['hr.attendance'].sudo().create(vals)
            print(check_user)
            args = {'success': True, 'message': 'Attendence Updated Successfully'}
            return args
        else:
            data = {'success': False, 'message': 'You Must Enter Check In And ID'}
            return data
