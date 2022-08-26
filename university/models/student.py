# -*- coding: utf-8 -*-

 from odoo import models, fields, api


 class UniversityStudent(models.Model):
     _name = 'University.student'
     f_name = fields.Char('First name')
     l_name = fields.Char('Last name')
     sexe = fields.Selection([('male','Male'),('female','Female')])
     identity_card = fields.Char('Identity card')
     address = fields.Text('Address')
     birthday = fields.DateTime( 'Birthday')
     registration_date = fields.Datetime('registration_date')
     email = fields.Char()
     phone = fields.Char()
