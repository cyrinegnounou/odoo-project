# -*- coding: utf-8 -*-
from odoo.exceptions import UserError
from odoo import api, fields, models, tools, _
from datetime import time, datetime

from odoo.odoo.exceptions import ValidationError


class UniversityStudent(models.Model):
     _name = 'university.student'
     # _rec_name='f_name'

     f_name = fields.Char('First name')
     l_name = fields.Char('Last name')
     sexe = fields.Selection([('male','Male'),('female','Female')])
     identity_card = fields.Char('Identity card')
     address = fields.Text('Address')
     birthday = fields.Datetime( 'Birthday')
     registration_date = fields.Datetime('registration_date')
     email = fields.Char()
     phone = fields.Char()


     state= fields.Selection([('l1' ,'level 1'),('l2','level 2'),('l3','level 3'),('finished','finished')])

     department_id = fields.Many2one(comodel_name='university.department')
     classroom_id = fields.Many2one(comodel_name='university.classroom')

     subject_ids = fields.Many2many(related='classroom_id.subject_ids')

     @api.model
     def name_get(self):
          result =[]
          for student in self:
               name = '[' +student.classroom_id.classroom_name +']' + student.f_name + ' ' + student.l_name
               result.append((student.id ,name))
          return result




     @api.onchange('registration_date','birthday')
     def check_date(self):
          print('hhhhhhhhhhhhhhhhh')
          if self.birthday > self.registration_date:
               print('hhh')
               raise UserError(_('The birthday must be inferior than tha registration date !'))

     # ---------------------------------------------------------------------------------------------------------

     def next_level(self):
          if self.state == False:
               self.write({'state': 'l1'})
          elif self.state =='l1':
               self.write({'state':'l2'})
          elif self.state =='l2':
               self.write({'state':'l3'})
          elif self.state =='l3':
               self.write({'state': 'finished'})
          elif self.state == 'finished':
               raise UserError (_('this student has finished his courses'))