# -*- coding: utf-8 -*-
{
    'name': "Odoo REST API",

    'summary': """
        Odoo REST API""",

    'description': """
        Odoo REST API
    """,

    'author': "easonwu",
    'website': "https://github.com/easonwy/odoo-rest-api",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/17.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Technical',
    'version': '0.2',
    'license': 'MIT',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],

    "application": True,
    "installable": True,
    "auto_install": False,

    'external_dependencies': {
        'python': ['pypeg2']
    }
}