# License MIT (https://opensource.org/licenses/MIT).
# Copyright 2015-2017 Ivan Yelizariev <https://it-projects.info/team/yelizariev>
# Copyright 2016 Juan José Scarafía <https://github.com/jjscarafia>
# Copyright 2016 manawi <https://github.com/manawi>
# Copyright 2016 Florent Thomas <https://github.com/flotho>
# Copyright 2017 Kolushov Alexandr <https://github.com/KolushovAlexandr>

from odoo.addons.website_sale.controllers.main import WebsiteSale
from odoo.http import request


class Controller(WebsiteSale):
    def checkout_redirection(self, order):
        res = super().checkout_redirection(order=order)
        order = request.website.with_context(request.context).sale_get_order()
        if not all(
            [
                line.product_uom_qty <= line.product_id.virtual_available
                for line in order.order_line
                if not line.is_delivery
            ]
        ):
            return request.redirect("/shop/cart")

        return res
