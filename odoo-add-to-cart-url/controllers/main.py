# -*- coding: utf-8 -*-
# URL Format: https://your-instance.com/add_to_cart_by_url?product_id=1&quantity=2
from odoo import http
from odoo.http import request
from odoo.addons.website_sale.controllers.main import WebsiteSale

class AddByUrlController(WebsiteSale):

    @http.route(['/add_to_cart_by_url'], type='http', auth='public', website=True, csrf=False)
    def add_to_cart(self, product_id, quantity, **kwargs):
        # Parse product_id and quantity
        product_id = int(product_id)
        quantity = int(quantity)

        # Get the sale order (cart) or create a new one
        sale_order = request.website.sale_get_order(force_create=1)

        # Add the product to the cart
        sale_order._cart_update(
            product_id=product_id,
            add_qty=quantity,
        )
        
        return request.redirect('/shop/cart')

