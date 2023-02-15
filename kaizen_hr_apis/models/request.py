# -*- coding: utf-8 -*-

from odoo import api, fields, models
from datetime import date, datetime, time, timedelta


class RequestView(models.Model):
    _name = "request.view"

    name = fields.Char(string="Name", required=False, )
    message = fields.Text(string="Message", required=False, )
    date = fields.Datetime(string="Date", required=False, )
    # time = fields.Datetime(string="Time", required=False, )
    distance = fields.Char(string="Distance", required=False, )
    state = fields.Selection(string="Status", selection=[('in_progress', 'In Progress'), ('done', 'Done'), ],
                             default='in_progress', )
    location = fields.Char(string="Location", required=False, )
    is_accept = fields.Boolean(string="Is Accept", )
    check_type = fields.Selection(string="Check Type",
                                  selection=[('check_in', 'Check In'), ('check_out', 'Check Out'), ])
