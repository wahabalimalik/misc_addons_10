# -*- coding: utf-8 -*-

from odoo import http
import json
from bs4 import BeautifulSoup
import requests
import datetime


class KillBill(http.Controller):
	@http.route('/web/broker/', type='http', auth="none", methods=['POST'],cors="*", csrf=False)
	def broker_demo(self, **kw):
		return"""<?xml version="1.0" encoding="UTF-8"?>
		<mpesaBroker xmlns="http://infowise.co.tz/broker/" version="2.0">
		<response>
		<conversationID>fd2052b5-beb3-4598-b23a-420fa1fa52ba</conversationID>
		<originatorConversationID>eef8deb8-bed763b7564308</originatorConversationID>
		<transactionID>485757</transactionID>
		<serviceID>1094</serviceID>
		<responseCode>0</responseCode>
		<responseDesc>Received</responseDesc>
		<serviceStatus>Success</serviceStatus>
		</response>
		</mpesaBroker>
				"""

	@http.route('/web/isopesademo/', type='http', auth="none", methods=['POST'],cors="*", csrf=False)
	def iso_demo(self, **kw):
		return"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
		<return>
		<field39>00</field39>
		<field48>[ amount|Pay option|bill type]</field48>
		<field54>NULL </field54>
		</return>
				"""

	@http.route('/web/killbill/', type='json', auth="none", methods=['POST'],cors="*", csrf=False)
	def listoner(self, **kw):
		# max_date = datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%S.000Z')
		# min_date = (datetime.datetime.now() - datetime.timedelta(minutes=3)).strftime('%Y-%m-%dT%H:%M:%S.000Z')
		# print max_date
		# print min_date
		# get_headers = {
		#     'Accept': 'application/json',
		#     'X-Killbill-ApiKey': 'vunoo',
		#     'X-Killbill-ApiSecret': 'vunoo',
		#     }

		# records = http.request.env['res.partner'].sudo().search([])
		# print records
		# for record in records:
		# 	if record.killbill_id:
		# 		params = (
		# 		    ('accountId', '%s' %(record.killbill_id)),
		# 		    ('withHistory', 'true'),
		# 		    ('minDate', '%s' %(min_date)),
		# 		    ('maxDate', '%s' %(max_date)),
		# 		    ('withInProcessing', 'false'),
		# 		    ('withBusEvents', 'true'),
		# 		    ('withNotifications', 'false'),
		# 		)

		# 		r = requests.get('http://13.95.148.150:8080/1.0/kb/admin/queues', headers=get_headers, params=params, auth=('admin', 'password'))

		# 		if r.json().has_key('busEvents'):
		# 			for x in range(0,len(r.json()['busEvents'])):
		# 				if r.json()['busEvents'][x]['className'] == "org.killbill.billing.invoice.api.DefaultInvoicePaymentInfoEvent":
		# 					inv_records = http.request.env['account.invoice'].search([
		# 						('partner_id','=',record.id),
		# 						('kb_invoice_id','=',r.json()['busEvents'][x]['event']['invoiceId'])
		# 					])
		# 					inv = inv_records

		# 					rr = http.request.env['account.payment']
		# 					ch= rr.search([('communication','=',inv.number)])
		# 					if not ch:
		# 						rr.create({
		# 							'communication' : inv.number,
		# 							'journal_id' : 5,
		# 							'currency_id' : 3,
		# 							'partner_id' : inv.partner_id.id,
		# 							'payment_method_id' : 1,
		# 							'payment_date' : str(datetime.datetime.now().strftime('%Y-%m-%d')),
		# 							'payment_difference_handling' : 'open',
		# 							'company_id' : 1,
		# 							'state' : 'draft',
		# 							'name' : 'Draft Payment',
		# 							'partner_type' : 'customer',
		# 							'amount' : inv.amount_total_signed,
		# 							'payment_type' : 'inbound',
		# 							'check_amount_in_words' : http.request.env['account.payment']._get_check_amount_in_words(inv.amount_total_signed),
		# 						})

		# 					nw = rr.search([('communication','=',inv.number)])
		# 					nw.post()				

		# print http.request.params
		return json.dumps({"result":"Success"}) 
		#curl -i -X POST -H "Content-Type: application/json" -d '{"params": {"name":"prakashsharma","email":"prakashsharmacs24@gmail.com","phone":"+917859884833"}}' 'http://localhost:8069/web/killbill/'

	@http.route('/web/mpasa/', type='http', auth="none", methods=['POST'],cors="*", csrf=False)
	def mpassa(self, **kw):
		xml = str(kw)
		spId = xml[xml.find('<spId>')+6: xml.find('</spId>')]
		spPassword = xml[xml.find('<spPassword>')+12: xml.find('</spPassword>')]
		timestamp = xml[xml.find('<timestamp>')+11: xml.find('</timestamp>')]
		amount = xml[xml.find('<amount>')+8: xml.find('</amount>')]
		commandID = xml[xml.find('<commandID>')+11: xml.find('</commandID>')]
		initiator = xml[xml.find('<initiator>')+11: xml.find('</initiator>')]
		conversationID = xml[xml.find('<conversationID>')+16: xml.find('</conversationID>')]
		originatorConversationID = xml[xml.find('<originatorConversationID>')+26: xml.find('</originatorConversationID>')]
		recipient = xml[xml.find('<recipient>')+11: xml.find('</recipient>')]
		mpesaReceipt = xml[xml.find('<mpesaReceipt>')+14: xml.find('</mpesaReceipt>')]
		transactionDate = xml[xml.find('<transactionDate>')+17: xml.find('</transactionDate>')]
		accountReference = xml[xml.find('<accountReference>')+18: xml.find('</accountReference>')]
		transactionID = xml[xml.find('<transactionID>')+15: xml.find('</transactionID>')]
		resultURL = xml[xml.find('<resultURL>')+11: xml.find('</resultURL>')]

		http.request.env['m.pesa'].sudo().create({
			'spId' : spId,
			'spPassword' : spPassword,
			'timestamp' : timestamp,
			'amount' : amount,
			'commandID' : commandID,
			'initiator' : initiator,
			'conversationID' : conversationID,
			'originatorConversationID' : originatorConversationID,
			'recipient' : recipient,
			'mpesaReceipt' : mpesaReceipt,
			'transactionDate' : transactionDate,
			'accountReference' : accountReference,
			'transactionID' : transactionID,
			'resultURL' : resultURL,
			'killbill_callable' : True,
			})
		return """<?xml version="1.0" encoding="UTF-8"?>
		<mpesaBroker xmlns="http://infowise.co.tz/broker/" version="2.0">
		<response>
		<conversationID>%s</conversationID>
		<originatorConversationID>%s</originatorConversationID>
		<transactionID>%s</transactionID>
		<serviceID>1094</serviceID>
		<responseCode>0</responseCode>
		<responseDesc>Received</responseDesc>
		<serviceStatus>Success</serviceStatus>
		</response>
		</mpesaBroker>""" %(
			conversationID,
			originatorConversationID,
			transactionID)

		# curl -i -X POST -d '<mpesaBroker xmlns="http://infowise.co.tz/broker/" version="2.0"><request><serviceProvider><spId>999999</spId><spPassword>encryptedPassword0</spPassword><timestamp>20141026092954</timestamp></serviceProvider><transaction><amount>60025.0</amount><commandID>BuyGoodsOnline</commandID><initiator>255754296979</initiator><conversationID>fd2052b5-beb3-4598-b23a-420fa1fa52ba</conversationID><originatorConversationID>eef8deb8-be7b-43</originatorConversationID><recipient>999999</recipient><mpesaReceipt>X-AJ213</mpesaReceipt><transactionDate>2014-10-26 09:29:54+0300</transactionDate><accountReference>94</accountReference><transactionID>94</transactionID></transaction><resultURL>https://12.34.56.78:18443/broker/c2b/callback</resultURL></request></mpesaBroker>' 'http://localhost:8069/web/mpasa/'

	@http.route('/web/tigopesa/', type='http', auth="none", methods=['POST'],cors="*", csrf=False)
	def tigopesa(self, **kw):
		# convert data receive from request to string
		xml = str(kw)
		# Declare all variables which are expected to be recevie in tigopesa request
		TYPE,TXNID,MSISDN,AMOUNT,COMPANYNAME,CUSTOMERREFERENCEID,TYPE_enq,TXNID_enq,COMPANYNAME_enq = '','','','','','','','','',
		# recieving data for bill payment request
		if '<TYPE>SYNC_BILLPAY_REQUEST</TYPE>' in xml:
			TYPE = xml[xml.find('<TYPE>')+6: xml.find('</TYPE>')]
			TXNID = xml[xml.find('<TXNID>')+7: xml.find('</TXNID>')]
			MSISDN = xml[xml.find('<MSISDN>')+8: xml.find('</MSISDN>')]
			AMOUNT = xml[xml.find('<AMOUNT>')+8: xml.find('</AMOUNT>')]
			COMPANYNAME = xml[xml.find('<COMPANYNAME>')+13: xml.find('</COMPANYNAME>')]
			CUSTOMERREFERENCEID = xml[xml.find('<CUSTOMERREFERENCEID>')+21: xml.find('</CUSTOMERREFERENCEID>')]
		# recieving data for bill payment enquiry request
		elif '<TYPE>SYNC_ENQUIRY</TYPE>' in xml:
			TYPE_enq = xml[xml.find('<TYPE>')+6: xml.find('</TYPE>')]
			TXNID_enq = xml[xml.find('<TXNID>')+7: xml.find('</TXNID>')]
			COMPANYNAME_enq = xml[xml.find('<COMPANYNAME>')+13: xml.find('</COMPANYNAME>')]
		# save all data recieved in to database for recording and tracking purposes
		http.request.env['tigo.pesa'].sudo().create({
			'TYPE' : TYPE,
			'TXNID' : TXNID,
			'MSISDN' : MSISDN,
			'AMOUNT' : AMOUNT,
			'COMPANYNAME' : COMPANYNAME,
			'CUSTOMERREFERENCEID' : CUSTOMERREFERENCEID,
			'TYPE_enq' : TYPE_enq,
			'TXNID_enq' : TXNID_enq,
			'COMPANYNAME_enq' : COMPANYNAME_enq,
			'killbill_callable' : True,
			})
		#  Authentication from killbill process start below

		record = http.request.env['tigo.pesa'].search([('killbill_callable','=', 'True')])
		params = (
			('withItems', 'false'),
			('withChildrenItems', 'false'),
			('audit', 'NONE'),
			)
		get_headers = {
		    'Accept': 'application/json',
		    'X-Killbill-ApiKey': 'vunoo',
		    'X-Killbill-ApiSecret': 'vunoo',
		    }
			
		for  rec in record:
			callback_respose = ''
			url = 'http://13.95.148.150:8080/1.0/kb/invoices/%s' %(rec.CUSTOMERREFERENCEID)

			r = requests.get(url, headers=get_headers, params=params, auth=('admin', 'password'))
			if r.json().has_key("className"):
				if r.json()['className'] == "org.killbill.billing.invoice.api.InvoiceApiException":
					_logger.warn(r.json()['message'])
					callback_respose = 'error010'
			elif r.json().has_key("invoiceId"):
				if r.json()['amount'] == rec.amount:
					callback_respose = 'errror000'
				else:
					callback_respose = 'error012'
		return """<?xml version="1.0"?>
		<!DOCTYPE COMMAND PUBLIC "-//Ocam//DTD XML Command 1.0//EN" "xml/command.dtd">
		<COMMAND>
		<TYPE>SYNC_BILLPAY_RESPONSE</TYPE>
		<TXNID>BP140218.1240.B01530</TXNID>
		<REFID>000217605331</REFID>
		<RESULT>TS</RESULT>
		<ERRORCODE>%s</ERRORCODE>
		<ERRORDESC/>
		<MSISDN>0714405395</MSISDN>
		<FLAG>Y</FLAG>
		<CONTENT>message_content.</CONTENT>
		</COMMAND>""" %(callback_respose)

		# curl -i -X POST -d '<mpesaBroker xmlns="http://infowise.co.tz/broker/" version="2.0"><request><serviceProvider><spId>999999</spId><spPassword>encryptedPassword0</spPassword><timestamp>20141026092954</timestamp></serviceProvider><transaction><amount>60025.0</amount><commandID>BuyGoodsOnline</commandID><initiator>255754296979</initiator><conversationID>fd2052b5-beb3-4598-b23a-420fa1fa52ba</conversationID><originatorConversationID>eef8deb8-be7b-43</originatorConversationID><recipient>999999</recipient><mpesaReceipt>X-AJ213</mpesaReceipt><transactionDate>2014-10-26 09:29:54+0300</transactionDate><accountReference>94</accountReference><transactionID>94</transactionID></transaction><resultURL>https://12.34.56.78:18443/broker/c2b/callback</resultURL></request></mpesaBroker>' 'http://localhost:8069/web/mpasa/'

	@http.route('/web/isopesa/', type='http', auth="none", methods=['POST'],cors="*", csrf=False)
	def isopesa(self, **kw):

		##############################################################
		# curl -i -X POST -d '<message>
		#  <isomsg>
		#  <field id="1" value="0200" />
		#  <field id="2" value="6834010000000200" />
		#  <field id="3" value="680000" />
		#  <field id="4" value="5000" />
		#  <field id="11" value="456987" />
		#  <field id="12" value="125000" />
		#  <field id="13" value="0402" />
		#  <field id="32" value="10000000002" />
		#  <field id="37" value="785632159235" />
		#  <field id="49" value="TZS" />
		#  <field id="59" value="uat1, 1094184598105347820" /><field id="98" value="255678999555 " />
		#  <field id="99" value="73052185" />
		#  <field id="102" value="0150000011111" />
		#  </isomsg>
		# </message> ' 'http://localhost:8069/web/isopesa/'
		###############################################################

		# convert data receive from request to string
		
		xml = str(kw)
		xml = xml[1:-1]
		soup = BeautifulSoup(xml, 'lxml')
		
		field_id_1  = [stat['value'] for stat in soup.find_all("field") if stat['id'] == '']
		field_id_2  = [stat['value'] for stat in soup.find_all("field") if stat['id'] == '2']
		field_id_3  = [stat['value'] for stat in soup.find_all("field") if stat['id'] == '3']
		field_id_11 = [stat['value'] for stat in soup.find_all("field") if stat['id'] == '11'] 
		field_id_12 = [stat['value'] for stat in soup.find_all("field") if stat['id'] == '12']
		field_id_13 = [stat['value'] for stat in soup.find_all("field") if stat['id'] == '13']
		field_id_32 = [stat['value'] for stat in soup.find_all("field") if stat['id'] == '32']
		field_id_37 = [stat['value'] for stat in soup.find_all("field") if stat['id'] == '37']
		field_id_49 = [stat['value'] for stat in soup.find_all("field") if stat['id'] == '49']
		field_id_59 = [stat['value'] for stat in soup.find_all("field") if stat['id'] == '59']
		field_id_98 = [stat['value'] for stat in soup.find_all("field") if stat['id'] == '98']
		field_id_99 = [stat['value'] for stat in soup.find_all("field") if stat['id'] == '99']

		# save all data recieved in to database for recording and tracking purposes
		http.request.env['iso.pesa'].sudo().create({
			'field_id_1' : field_id_1[0] if field_id_1[0] else '',
			'field_id_2' : field_id_2[0] if field_id_2[0] else '',
			'field_id_3' : field_id_3[0] if field_id_3[0] else '',
			'field_id_11' : field_id_11[0] if field_id_11[0] else '',
			'field_id_12' : field_id_12[0] if field_id_12[0] else '',
			'field_id_13' : field_id_13[0] if field_id_13[0] else '',
			'field_id_32' : field_id_32[0] if field_id_32[0] else '',
			'field_id_37' : field_id_37[0] if field_id_37[0] else '',
			'field_id_49' : field_id_49[0] if field_id_49[0] else '',
			'field_id_59' : field_id_59[0] if field_id_59[0] else '',
			'field_id_98' : field_id_98[0] if field_id_98[0] else '',
			'field_id_99' : field_id_99[0] if field_id_99[0] else '',
			'killbill_callable' : True,
			})
		# First return to constomer in every case.
		return """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<return>
<field39>00</field39>
<field48>[ amount|Pay option|bill type]</field48>
<field54>NULL </field54>
</return>"""