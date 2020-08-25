# -*- coding: utf-8 -*-
# Part of CAPTIVEA. Odoo 12 EE.

import base64
from odoo import fields, models
class ProductImage(models.Model):
	_inherit = 'product.template'
	def complicated_task(line_id):
		line=self.env['product.template'].browse(line_id)
		for x in range(1000):
			line['list_price']=x
		return(1)