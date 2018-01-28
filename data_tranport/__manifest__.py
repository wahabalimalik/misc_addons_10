# -*- coding: utf-8 -*-
{
    'name': "data_tranport",

    'summary': """
        When liston any new event call the killbill api and send data""",

    'description': """
        When liston any new event call the killbill api and send data
    """,

    'author': "Wahab Ali Malik",
    'website': "http://www.yourcompany.com",
    'category': 'Generic Modules',
    'data': [
        'views/ext.xml',
    ],
    'version': '0.1',
    'depends': ['base','account','component_event'],
}