# -*- coding: utf-8 -*-

from odoo import models, fields, api


class HRContractInherit(models.Model):
    _inherit = 'hr.contract'
    arabic_name = fields.Char(string="Name In Arabic", related='employee_id.arabic_name')
    employee_no = fields.Char(string="Employee Number", related='employee_id.employee_no')
    religion_id = fields.Many2one(comodel_name="employee.religion", string="Religion",
                                  related='employee_id.religion_id')
