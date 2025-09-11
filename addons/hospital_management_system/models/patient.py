from odoo import api, fields, models
from datetime import date
from odoo.exceptions import ValidationError

class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _description = 'Hospital Patient'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    name = fields.Char(string='Name' , required=True, defult='New', tracking=True)
    ref = fields.Char(string='Reference', required=True, help="Reference of the patient")
    date_of_birth = fields.Date(string='Date of Birth')
    age = fields.Integer(string='Age', tracking=True, compute='_compute_age')
    gender = fields.Selection([('male', 'Male'), ('female' , 'Female')], string= 'Gender', tracking=True, default='male')
    active = fields.Boolean(string='Active', default=True)

    _sql_constraints = [
        ('ref_uniq', 'unique(ref)', 'Reference must be unique')
    ]
    
    @api.constrains('age')
    def _check_valid_age(self):
        for rec in self:
            if rec.age < 1:
                raise ValidationError("Age is not valid")
            
    @api.depends('date_of_birth')      
    def _compute_age(self):
        for rec in self:
            today = date.today()
            if rec.date_of_birth:
                rec.age = today.year - rec.date_of_birth.year - ((today.month, today.day) < (rec.date_of_birth.month, rec.date_of_birth.day))
            else:
                rec.age = 0