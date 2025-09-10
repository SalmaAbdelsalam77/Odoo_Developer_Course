from odoo import api, fields, models
from odoo.exceptions import ValidationError

class HospitalAppointment(models.Model):
    _name = 'hospital.appointment'
    _description = 'Hospital Appointment'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'patient_id'
    
    patient_id = fields.Many2one('hospital.patient', string='Patient', required=True, tracking=True)
    ref = fields.Char(string='Reference', required=True)
    gender = fields.Selection(related='patient_id.gender')
    appointment_time = fields.Datetime(string='Appointment Time', required=True, tracking=True, default=fields.Datetime.now)
    booking_date = fields.Date(string='Booking Date', required=True, tracking=True, default=fields.Date.today)
    prescription = fields.Html(string='Prescription')
    priority = fields.Selection([
        ('0', 'Low'), 
        ('1', 'Medium'), 
        ('2', 'High'), 
        ('3', 'Very High')], string= 'Priority', select=True)
    
    state = fields.Selection([
        ('draft', 'Draft'), 
        ('in_consultation', 'In Consultation'), 
        ('done', 'Done'), 
        ('cancel', 'Cancelled')], string= 'Status', default='draft', tracking=True, required=True)
    
    @api.onchange('patient_id')
    def _onchange_(self):
        self.ref = self.patient_id.ref 
        
    def action_test(self):
        print("Test Button Clicked")
        return{
            'effect': {
                'fadeout': 'slow',
                'message': 'Test Button Clicked',
                'type' : 'rainbow_man'
            }
        }