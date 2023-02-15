# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
import json
from odoo import fields, models, api
import odoo.http as http
from odoo.http import Controller, request, route
import re
from datetime import datetime


def format_time(time_str):
    return fields.datetime.strptime(time_str, '%m/%d/%Y %I:%M:%S')


class CreateRequest(http.Controller):

    @http.route('/create_request', type='json', auth='public', methods=["POST"])
    def create_request(self, **rec):
        print("rec", rec)
        date = datetime.strptime(rec['date'], '%Y-%m-%d %H:%M:%S')
        print(date, 8888888888)
        if rec:
            vals = {
                'name': rec['name'],
                'message': rec['message'],
                'date': date if rec['date'] else False,
                'distance': rec['distance'],
                'location': rec['location'],
                'state': rec['state'],
                'is_accept': rec['is_accept'],
                'check_type': rec['check_type']
            }
            requests = request.env['request.view'].sudo().create(vals)
            print(requests)
            args = {'success': True, 'message': 'Request Created Success'}
            return args
        else:
            data = {'success': False, 'message': 'No Create Request'}
            return data
