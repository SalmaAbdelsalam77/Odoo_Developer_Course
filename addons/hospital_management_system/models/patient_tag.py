from odoo import api, fields, models
from odoo.exceptions import ValidationError

class patientTag(models.Model):
    _name ="patient.tag"
    _descirption =  "Patient Tag"
    
    name = fields.Char(string = "Name", required=True)
    active = fields.Boolean(string="Active",default=True) 
    color = fields.Integer(string="Color")  
    color_2 = fields.Char(sring="Color 2")