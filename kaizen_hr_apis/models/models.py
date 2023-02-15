# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class kaizen_hr_apis(models.Model):
#     _name = 'kaizen_hr_apis.kaizen_hr_apis'
#     _description = 'kaizen_hr_apis.kaizen_hr_apis'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
