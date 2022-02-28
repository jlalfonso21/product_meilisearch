# -*- coding: utf-8 -*-
# from odoo import http


# class ProductMeilisearch(http.Controller):
#     @http.route('/product_meilisearch/product_meilisearch/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/product_meilisearch/product_meilisearch/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('product_meilisearch.listing', {
#             'root': '/product_meilisearch/product_meilisearch',
#             'objects': http.request.env['product_meilisearch.product_meilisearch'].search([]),
#         })

#     @http.route('/product_meilisearch/product_meilisearch/objects/<model("product_meilisearch.product_meilisearch"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('product_meilisearch.object', {
#             'object': obj
#         })
