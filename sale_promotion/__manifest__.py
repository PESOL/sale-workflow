
# Copyright 2017 Pesol (<http://pesol.es>)
#                Angel Moya <angel.moya@pesol.es>
#                Antonio Rubio Lorente <antonio.rubio@pesol.es>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html)


{
    'name': 'Sale Promotion',
    'version': '12.0.1.0.0',
    'license': 'AGPL-3',
    'category': 'sale',
    'sequence': 1,
    'complexity': 'easy',
    'author': 'PESOL, Odoo Community Association (OCA)',
    'depends': [
        'sale_management',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/promotion_view.xml',
        'views/product_pricelist_view.xml',
        'views/product_template_view.xml',
        'views/campaign_view.xml',
        'views/sale_order_view.xml',
    ],
    'demo': [
        'demo/campaign_demo.xml',
        'demo/promotion_demo.xml',
    ],
    'installable': True,
}
