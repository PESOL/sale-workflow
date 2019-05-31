from odoo import models, fields


class SaleCampaign(models.Model):
    _name = 'sale.campaign'

    name = fields.Char(
        string='Name',
        required=True)
    promotion_ids = fields.Many2many(
        comodel_name='sale.promotion',
        string='Promotions')
    start_date = fields.Date(
        string='Start Date')
    end_date = fields.Date(
        string='End Date')
    pricelist_ids = fields.Many2many(
        comodel_name='product.pricelist',
        string='Pricelists')
    active = fields.Boolean(
        string='Active',
        default=True)
