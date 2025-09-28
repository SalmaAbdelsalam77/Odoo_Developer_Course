from odoo import api, fields, models
from datetime import datetime
from odoo.exceptions import ValidationError

class HospitalAppointmentHistory(models.Model):
    _name = 'hospital.appointment.history'
    _description = 'Hospital Appointment History'
    _rec_name = 'patient_id'
    
    patient_id = fields.Many2one('hospital.patient', string='Patient', required=True, tracking=True)
    appointment_id = fields.Many2one('hospital.appointment')
    old_state = fields.Char()
    new_state = fields.Char()