# -*- coding: utf-8 -*-

 from odoo import models, fields, api


 class UniversityDepartment(models.Model):
     _name = 'University.departement'

     name = fields.Char()
     code =fields.Char()