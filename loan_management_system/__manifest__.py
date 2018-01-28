# -*- coding: utf-8 -*-
{
    'name': "Loan Management System",

    'description': """
App to manage load system
======================================

A comprihensive app to manage and keep track of loan and its recovery.And deduction in case of installments
    """,
    'author': "Wahab Ali Malik",
    'website': "http://www.glareerp.com",
    'version': '0.1',
    'depends': ['base'],
    'data': [
        'views/loan_template.xml',
    ],
    'qweb': [
        "static/src/xml/sales_team_dashboard.xml",
    ],
    'css': ['static/src/css/sales_team.css'],
}