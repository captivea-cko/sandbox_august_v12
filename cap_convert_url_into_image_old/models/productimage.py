# -*- coding: utf-8 -*-
# Part of CAPTIVEA. Odoo 12 EE.

import base64
from odoo import fields, models
class ProductImage(models.Model):
	_inherit = 'product.image'
	def convert_url_into_image(url, **kw):
		img=base64.b64decode(url)
		return(img)