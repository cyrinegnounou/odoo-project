# -*- coding: utf-8 -*-

 from odoo import models, fields, api


 class UniversityProfessor(models.Model):
     _name = 'University.professor'
     f_name = fields.Char('First name')
     l_name = fields.Char('Last name')
     sexe = fields.Selection([('male','Male'),('female','Female')])
     identity_card = fields.Char('Identity card')
     address = fields.Text('Address')
     start_date= fields.DateTime( 'Start date')
     email = fields.Char()
     phone = fields.Char()
