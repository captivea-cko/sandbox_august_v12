# -*- coding: utf-8 -*-
# Part of CAPTIVEA. Odoo 12 EE.

import asyncio
import concurrent.futures
import matplotlib
import base64
from concurrent.futures import ThreadPoolExecutor
from odoo import fields,models


class ProductImage(models.Model):
	_inherit = 'product.template'

	
	def my_function(self,list):
		for line in list:
			line['list_price']+=100
		return(line['list_price'])