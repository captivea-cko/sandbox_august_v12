# -*- coding: utf-8 -*-
# Part of CAPTIVEA. Odoo 12 EE.

import base64
import concurrent.futures
import matplotlib.pyplot as plt
from odoo import fields, models
class ProductImage(models.Model):
	_inherit = 'product.template'
	# def complicated_task(self,line_id):
		# line=self.env['product.template'].browse(line_id)
		# for x in range(1000):
			# line['list_price']=x
		# return(1)
	def complicated_task(self,action,recordset):
		outs=[]
		with concurrent.futures.ProcessPoolExecutor() as executor:
			for model, out in zip(recordset, executor.map(action, recordset)):
				outs.append([model,out])
		return(outs)