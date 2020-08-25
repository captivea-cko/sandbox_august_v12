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
	def action(line_id):
		line=self.env['product.template'].browse(line_id['id'])
		for x in range(1000):
			line['list_price']=x
		return(1)
		
	# def complicated_task(self,recordset):
		# outs=[]
		# with concurrent.futures.ProcessPoolExecutor() as executor:
			# for model, out in zip(recordset, executor.map(action, recordset)):
				# outs.append([model,out])
		# return(outs)
	
	def complicated_task(self, function, recordset):
        results = []
        with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
            futures = [executor.submit(function, kwargs) for kwargs in recordset]
        for future in concurrent.futures.as_completed(futures):
            results.append(future.result())
        return results
		
class Concurrent:

    @staticmethod
    def execute_concurrently(self, recordset):
        results = []
        with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
            futures = [executor.submit(action, kwargs) for kwargs in recordset]
        for future in concurrent.futures.as_completed(futures):
            results.append(future.result())
        return results