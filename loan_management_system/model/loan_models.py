# -*- coding: utf-8 -*-

from odoo import models, fields, api

class LoanAmount(models.Model):
    _name = 'loan.amount'

    name = fields.Float('Amount')
    description = fields.Text('Description')
    w_type = fields.Selection([('debit','Debit'),('credit','Credit')],default='debit',string="Wallet Type")
    date = fields.Date('Trans Date')

class LoanLoan(models.Model):
    _name = 'loan.loan'

    loan_type = fields.Selection([('flexible','Flexible'),('concrete','Concrete')],default='flexible',string="Loan Type")
    name = fields.Char('Account Number')
    description = fields.Text('Description')
    amount = fields.Float()
    balance = fields.Float()
    customer = fields.Many2one('res.partner')
    agent = fields.Many2one('res.users')
    date_release = fields.Date('Release Date')
    date_payment = fields.Date('Payment Date')
    loan_status = fields.Selection([('pending','Pending'),('paid','Paid')],default='pending',string="Loan Status")

class LoanDashboard(models.Model):
    _name = 'loan.dashboard'

    name = fields.Char()