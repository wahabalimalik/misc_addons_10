# -*- coding: utf-8 -*-
{
    'name': "website_custom",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Wahab Ali Malik",
    'website': "http://www.placeholder.com",
    'category': 'Website',
    'version': '0.1',
    'depends': ['website'],
    'data': [
        # 'security/ir.model.access.csv',
        'views/custom_snipit.xml',
        'views/templates.xml',
        'views/views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}