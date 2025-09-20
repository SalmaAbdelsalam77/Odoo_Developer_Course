from odoo import api, fields, models
from datetime import datetime
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
    is_late = fields.Boolean(tracking=True, compute= '_check_appointment_time')
    booking_date = fields.Date(string='Booking Date', required=True, tracking=True, default=fields.Date.today)
    prescription = fields.Html(string='Prescription')
    doctor_id = fields.Many2one('res.users', string='Doctor', tracking= True)
    pharmacy_line_ids = fields.One2many('appointment.pharmacy.lines','appointment_id', string= 'Pharmacy Lines')
    hide_sales_price = fields.Boolean(string="Hide Sales Price", default=False)
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
    def _onchange_patient_id(self):
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
        
    def action_in_consultation(self):
        for rec in self:
            rec.state = 'in_consultation'
        
    def action_draft(self):
        for rec in self:
            rec.state = 'draft'
        
    def action_done(self):
        for rec in self:
            rec.state = 'done'
        
    def action_cancel(self):
        for rec in self:
            rec.state = 'cancel'
                
    def _check_appointment_time(self):
            now = fields.Datetime.now()
            for rec in self.search([]):
                if rec.appointment_time < now:
                    rec.is_late = True
                else:
                    rec.is_late = False

            
            
            
class AppointmentPharmacyLines(models.Model):
    _name = "appointment.pharmacy.lines"
    _description = "Appointment Pharmacy Lines"
    
    product_id = fields.Many2one('product.product', required = True)
    price_unit = fields.Float(related ='product_id.list_price')
    quantity = fields.Integer(string = 'Quantity', default = 1)
    appointment_id = fields.Many2one('hospital.appointment' , string= 'Appointment')