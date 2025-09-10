{
    'name': 'Hospital Management',
    'version': '1.0.0',
    'category': 'Hospital',
    'author': 'Salma',
    'sequence': -100,
    'summary': 'hospital management system',
    'description': """Hospital Management System""",
    'depends': ['base','mail'],
'data': 
    [
    'security/ir.model.access.csv',
    'views/menu.xml',
    'views/patient_view.xml',
    'views/femail_patient_view.xml',
    'views/appointment_view.xml',
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3'
    }