# -*- coding: utf-8 -*-

from odoo import models, fields, api
import time
import datetime

class UniversityProfessor(models.Model):
     _name = 'university.professor'
     f_name = fields.Char('First name')
     l_name = fields.Char('Last name')
     sexe = fields.Selection([('male','Male'),('female','Female')])
     identity_card = fields.Char('Identity card')
     address = fields.Text('Address')
     start_date= fields.Datetime( 'Start date')
     email = fields.Char()
     phone = fields.Char()
     active =fields.Boolean()

     department_id =fields.Many2one(comodel_name='university.department')
     subject_id =fields.Many2one(comodel_name="university.subject")

     classroom_ids =fields.Many2many(comodel_name='university.classroom',
                                     relation='prof_class_rel',
                                     column1='f_name',
                                     column2='name')

     @api.model
     def name_get(self):
          result =[]
          for prof in self:
               name ='[' +prof.department_id.name +']' + prof.f_name + ' ' + prof.l_name
               result.append((prof.id ,name))
          return result

     # ------------------------------------------------------------------------------------------------

     def send_mail(self):
         self.ensure_one()
         template_id =self.env.ref('university.email_template_prof').id
         ctx={
              'default_model':'university.professor',
              'default_res_id':self.id,
              'default_use_template':bool(template_id),
              'default_template_id': template_id,
              'default_composition_mode': 'comment',
              'email_to':self.email,
         }
         return{
              'type': 'ir.actions.act_window',
              'view_type':'form',
              'view_mode':'form',
              'res_model':'mail.compose.message',
              'target': 'new',
              'context': ctx,
         }
