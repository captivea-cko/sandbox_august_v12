# -*- coding: utf-8 -*-
# Part of CAPTIVEA. Odoo 12 EE.

import base64
import requests
from odoo import fields, models
class ProductImage(models.Model):
	_inherit = 'product.image'
	def convert_url_into_image(self,url):
		file=requests.get(url)
		
		img=base64.b64decode(file)
		return(img)
