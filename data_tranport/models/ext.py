# -*- coding: utf-8 -*-

from odoo import models, fields, api
import requests
import datetime
from time import strftime
import logging

_logger = logging.getLogger(__name__)

get_headers = {
    'Accept': 'application/json',
    'X-Killbill-ApiKey': 'vunoo',
    'X-Killbill-ApiSecret': 'vunoo',
    }

class ResPartnerExt(models.Model):
	_inherit = 'res.partner'
	
	killbill_id = fields.Char('KillBill ID')

class AccInvExt(models.Model):
	_inherit = 'account.invoice'
	
	killbill_id = fields.Char('Control Number')
	kb_invoice_id = fields.Char("Invoice Id")

class Tigopesa(models.Model):
	_name = 'tigo.pesa'
	
	TYPE = fields.Char()
	TXNID = fields.Char()
	MSISDN = fields.Char()
	AMOUNT = fields.Char()
	COMPANYNAME = fields.Char()
	CUSTOMERREFERENCEID = fields.Char()
	TYPE_enq = fields.Char()
	TXNID_enq = fields.Char()
	COMPANYNAME_enq = fields.Char()
	killbill_callable = fields.Boolean()

class Isopesa(models.Model):
	_name = 'iso.pesa'
	field_id_1 = fields.Char()
	field_id_2 = fields.Char()
	field_id_3 = fields.Char()
	field_id_11 = fields.Char()
	field_id_12 = fields.Char()
	field_id_13 = fields.Char()
	field_id_32 = fields.Char()
	field_id_37 = fields.Char()
	field_id_49 = fields.Char()
	field_id_59 = fields.Char()
	field_id_98 = fields.Char()
	field_id_99 = fields.Char()
	killbill_callable = fields.Boolean()

	@api.model
	def up_request(self):
		record = self.env['iso.pesa'].search([('killbill_callable','=', 'True')])
		
		params = (
			('withItems', 'false'),
			('withChildrenItems', 'false'),
			('audit', 'NONE'),
			)

		headers = {'Content-Type': 'application/xml'}
			
		for  rec in record:
			callback_respose = None
			url = 'http://13.95.148.150:8080/1.0/kb/invoices/%s' %(rec.field_id_37)

			r = requests.get(url, headers=get_headers, params=params, auth=('admin', 'password'))
			if r.json().has_key("className"):
				if r.json()['className'] == "org.killbill.billing.invoice.api.InvoiceApiException":
					_logger.warn(r.json()['message'])
					callback_respose = 999
			elif r.json().has_key("invoiceId"):
				if r.json()['amount'] == rec.amount:
					callback_respose = 0
				else:
					callback_respose = 999

			xml = """<message>
			<isomsg>
			<field id="1" value="0200" />
			<field id="2" value="6834010000000200" />
			<field id="3" value="670000" />
			<field id="11" value="456987" />
			<field id="12" value="125000" />
			<field id="13" value="0402" />
			<field id="32" value="10000000002" />
			<field id="37" value="785632159235" />
			<field id="49" value="TZS" />
			<field id="59” value="uat1, 1094184598105347820" />
			<field id="98” value="255678999555" />
			<field id="99” value="73052185" />
			</isomsg>
			</message>"""

class MpesaFinal(models.Model):
	_name = 'm.pesa_final'

	conversationID = fields.Char()
	originatorConversationID = fields.Char()
	transactionID = fields.Char()
	serviceID = fields.Char()
	responseCode = fields.Char()
	responseDesc = fields.Char()
	serviceStatus = fields.Char()

class Mpesa(models.Model):
	_name = 'm.pesa'
	
	spId = fields.Char()
	spPassword = fields.Char()
	timestamp = fields.Char()
	amount = fields.Float()
	commandID = fields.Char()
	initiator = fields.Char()
	conversationID = fields.Char()
	originatorConversationID = fields.Char()
	recipient = fields.Char()
	mpesaReceipt = fields.Char()
	transactionDate = fields.Char()
	accountReference = fields.Char()
	transactionID = fields.Char()
	resultURL = fields.Char()
	killbill_callable = fields.Boolean()

	@api.model
	def up_request(self):
		record = self.env['m.pesa'].search([('killbill_callable','=', 'True')])
		
		params = (
			('withItems', 'false'),
			('withChildrenItems', 'false'),
			('audit', 'NONE'),
			)

		headers = {'Content-Type': 'application/xml'}
			
		for  rec in record:
			callback_respose = None
			url = 'http://13.95.148.150:8080/1.0/kb/invoices/%s' %(rec.transactionID)

			r = requests.get(url, headers=get_headers, params=params, auth=('admin', 'password'))
			if r.json().has_key("className"):
				if r.json()['className'] == "org.killbill.billing.invoice.api.InvoiceApiException":
					_logger.warn(r.json()['message'])
					callback_respose = 999
			elif r.json().has_key("invoiceId"):
				if r.json()['amount'] == rec.amount:
					callback_respose = 0
				else:
					callback_respose = 999

			xml = """<?xml version="1.0" encoding="UTF-8"?>
	<mpesaBroker xmlns="http://infowise.co.tz/broker/" version="2.0">
		<result>
			<serviceProvider>
				<spId>999999</spId>
				<spPassword>encryptedPassword0</spPassword>
				<timestamp>20141026092954</timestamp>
			</serviceProvider>
			<transaction>
				<resultType>Completed</resultType>
				<resultCode>%s</resultCode>
				<resultDesc>Success</resultDesc>
				<serviceReceipt>123456-2344</serviceReceipt>
				<serviceDate>2014-10-26 09:29:54+0300</serviceDate>
				<serviceID>1234</serviceID>
				<originatorConversationID>eef8deb8-be7b-43f1-a66</originatorConversationID>
				<conversationID>3ebafc33-70d8-4645-bb47-ab909efffda5</conversationID>
				<transactionID>485757</transactionID>
				<initiator>999999</initiator>
				<initiatorPassword>encryptedPassword1</initiatorPassword>
			</transaction>
		</result>
	</mpesaBroker>""" %(callback_respose)


			# rec.resultURL
			r = requests.post(
				'http://localhost:8069/web/broker/', #dummy url of broker for final callback
				headers=headers,
				data=xml
				)
			conversationID = r.text[r.text.find('<conversationID>') +16:r.text.find('</conversationID>')]
			originatorConversationID = r.text[r.text.find('<originatorConversationID>') + 26:r.text.find('</originatorConversationID>')]
			transactionID = r.text[r.text.find('<transactionID>') +15:r.text.find('</transactionID>')]
			serviceID = r.text[r.text.find('<serviceID>') +11:r.text.find('</serviceID>')]
			responseCode = r.text[r.text.find('<responseCode>') +14:r.text.find('</responseCode>')]
			responseDesc = r.text[r.text.find('<responseDesc>') +14:r.text.find('</responseDesc>')]
			serviceStatus = r.text[r.text.find('<serviceStatus>') +15:r.text.find('</serviceStatus>')]
			self.env['m.pesa_final'].create({
				'conversationID' : conversationID,
				'originatorConversationID' : originatorConversationID,
				'transactionID' : transactionID,
				'serviceID' : serviceID,
				'responseCode' : responseCode,
				'responseDesc' : responseDesc,
				'serviceStatus' : serviceStatus
				})

			rec.write({
				'killbill_callable' : False
				})

class KillBill(models.Model):
	
	_name = 'kill.bill'

	@api.model
	def fetch_kill_bill(self):
		max_date = datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%S.000Z')
		min_date = (datetime.datetime.now() - datetime.timedelta(minutes=3)).strftime('%Y-%m-%dT%H:%M:%S.000Z')

		records = self.env['res.partner'].search([])
		for record in records:
			if record.killbill_id:
				params = (
				    ('accountId', '%s' %(record.killbill_id)),
				    ('withHistory', 'true'),
				    ('minDate', '%s' %(min_date)),
				    ('maxDate', '%s' %(max_date)),
				    ('withInProcessing', 'false'),
				    ('withBusEvents', 'true'),
				    ('withNotifications', 'false'),
				)

				r = requests.get('http://13.95.148.150:8080/1.0/kb/admin/queues', headers=get_headers, params=params, auth=('admin', 'password'))

				if r.json().has_key('busEvents'):
					for x in range(0,len(r.json()['busEvents'])):
						if r.json()['busEvents'][x]['className'] == "org.killbill.billing.invoice.api.DefaultInvoicePaymentInfoEvent":
							inv_records = self.env['account.invoice'].search([
								('partner_id','=',record.id),
								('kb_invoice_id','=',r.json()['busEvents'][x]['event']['invoiceId'])
							])
							inv = inv_records

							rr = self.env['account.payment']
							ch= rr.search([('communication','=',inv.number)])
							if not ch:
								rr.create({
									'communication' : inv.number,
									'journal_id' : 5,
									'currency_id' : 3,
									'partner_id' : inv.partner_id.id,
									'payment_method_id' : 1,
									'payment_date' : str(datetime.datetime.now().strftime('%Y-%m-%d')),
									'payment_difference_handling' : 'open',
									'company_id' : 1,
									'state' : 'draft',
									'name' : 'Draft Payment',
									'partner_type' : 'customer',
									'amount' : inv.amount_total_signed,
									'payment_type' : 'inbound',
									'check_amount_in_words' : self.env['account.payment']._get_check_amount_in_words(inv.amount_total_signed),
								})

							nw = rr.search([('communication','=',inv.number)])
							nw.post()					