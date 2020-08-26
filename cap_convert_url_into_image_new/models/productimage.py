# -*- coding: utf-8 -*-
# Part of CAPTIVEA. Odoo 12 EE.

import asyncio
import concurrent.futures
from concurrent.futures import ThreadPoolExecutor
from odoo import fields
from odoo import models

class ProductImage(models.Model):
	_inherit = 'product.template'
	
	digits = fields.int(string='Custom Field')
	digits=3
	
	def my_function(self,line_id):
		line=self.env['product.template'].browse(line_id['id'])
		for x in range(1000):
			line['list_price']=x
		return(1)
	
	def complicated_task(self,my_action,list):
		results=[]
		outs=[]
		with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor: #was Process
			# for my_model, out in zip(recordset, executor.map(my_action, recordset)):
				# outs.append([my_model,out])
			futures = [executor.submit(my_action, el) for el in list]
		for future in concurrent.futures.as_completed(futures):
			# el=futures[future]
			# try:
			results.append(future.result())
			# except:
				# a=1
				# except Exception as exc:
				# print('%r generated an exception: %s' % (el)
		return(results)
			
		# return(outs)
		# results = []
        # with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
            # futures = [executor.submit(function, kwargs) for kwargs in recordset]
        # for future in concurrent.futures.as_completed(futures):
            # results.append(future.result())
        # return results
	
	# def complicated_task(self, function, recordset):
        # results = []
        # with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
            # futures = [executor.submit(function, kwargs) for kwargs in recordset]
        # for future in concurrent.futures.as_completed(futures):
            # results.append(future.result())
        # return results
		
# class Concurrent:

    # @staticmethod
    # def execute_concurrently(self, recordset):
        # results = []
        # with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
            # futures = [executor.submit(action, kwargs) for kwargs in recordset]
        # for future in concurrent.futures.as_completed(futures):
            # results.append(future.result())
        # return results