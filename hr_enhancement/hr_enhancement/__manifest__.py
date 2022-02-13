# -*- coding: utf-8 -*-
{
    'name': "HR Enhancement",
    'author': "Cityart",
    'category': 'HR',
    'version': '0.1',
    # any module necessary for this one to work correctly
    'depends': ['base', 'hr', 'hr_contract'],
    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/contract_inherit.xml',
        'views/employee_inherit.xml'
    ],
}
