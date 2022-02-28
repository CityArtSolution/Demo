# -*- coding: utf-8 -*-

from odoo import models, fields, api
from dateutil.relativedelta import relativedelta


class HREmployeeInherit(models.Model):
    _inherit = 'hr.employee'
    arabic_name = fields.Char(string="Name In Arabic")
    employee_no = fields.Char(string="Employee Number")
    passport_end_date = fields.Date(string="Passport End Date")
    passport_attachment = fields.Binary(string="Passport Attachment")
    identification_no_date_end = fields.Date(string="Identification End Date")
    identification_no_attachment = fields.Binary(string="Identification Attachment")
    age = fields.Integer(string="Age", compute='get_employee_age')
    work_owner = fields.Char(string="Work Owner")
    work_owner_no = fields.Char(string="Work Owner Phone Number")
    employee_type_x = fields.Selection(string="Employee Type",
                                     selection=[('official', 'Official'), ('contractor', 'Contractor'),
                                                ('freelance', 'Freelance')])
    family_ids = fields.One2many(comodel_name="employee.family", inverse_name="employee_id")
    religion_id = fields.Many2one(comodel_name="employee.religion", string="Religion", required=False, )
    accommodation_start_date = fields.Date(string="Accommodation Start Date")
    accommodation_end_date = fields.Date(string="Accommodation End Date")
    visa_no = fields.Char(string="Visa Number")
    visa_end_date = fields.Date(string="Visa End Date")
    accommodation_job = fields.Char(string="Job in Accommodation")

    @api.depends('birthday')
    def get_employee_age(self):
        for rec in self:
            rec.age = 0
            if rec.birthday:
                current_date = fields.Date.from_string(fields.date.today())
                birthday = fields.Date.from_string(rec.birthday)
                diff = relativedelta(current_date, birthday)
                rec.age = diff.years


class EmployeeFamilyMembers(models.Model):
    _name = 'employee.family'
    _rec_name = 'name'
    name = fields.Char(string="Name", required=True)
    gender = fields.Selection(string="Gender", selection=[('male', 'Male'), ('female', 'Female')], required=True)
    birthday = fields.Date(string="Birthday")
    age = fields.Integer(string="Age", compute='get_employee_age')
    employee_id = fields.Many2one(comodel_name="hr.employee")

    @api.depends('birthday')
    def get_employee_age(self):
        for rec in self:
            rec.age = 0
            if rec.birthday:
                current_date = fields.Date.from_string(fields.date.today())
                birthday = fields.Date.from_string(rec.birthday)
                diff = relativedelta(current_date, birthday)
                rec.age = diff.years


class EmployeeReligion(models.Model):
    _name = 'employee.religion'
    _rec_name = 'name'
    name = fields.Char()
