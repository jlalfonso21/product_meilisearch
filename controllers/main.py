# -*- coding: utf-8 -*-

from odoo import _, http
from odoo.addons.website_sale.controllers.main import WebsiteSale
from odoo.http import request
from odoo.exceptions import ValidationError


class ProductMeiliSearch(WebsiteSale):

    def __init__(self):
        self.meili_server_address = None
        self.meili_server_api_key = None
        self.meili_product_index = None
        super().__init__()
    
    def _prepare_meili_search_args(self):
        if not self.meili_server_address:
            self.meili_server_address = request.env['ir.config_parameter'].sudo().get_param('msearch.service.url') or False 
            if not self.meili_server_address:
                raise ValidationError("Cant't get meilisearch server address from database.")

        if not self.meili_server_api_key:
            self.meili_server_api_key = request.env['ir.config_parameter'].sudo().get_param('msearch.service.apikey') or False 

        if not self.meili_product_index:
            self.meili_product_index = request.env['ir.config_parameter'].sudo().get_param('msearch.service.product.index') or 'products' 
            if not self.meili_product_index:
                raise ValidationError("Cant't get meilisearch server products index from database.")

    @http.route('/shop/products/autocomplete', type='json', auth='public', website=True)
    def products_autocomplete(self, term, options={}, **kwargs):
        self._prepare_meili_search_args()
        
        res = super(ProductMeiliSearch, self).products_autocomplete(term, options, **kwargs)
        
        return res

