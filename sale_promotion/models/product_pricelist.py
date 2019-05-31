from odoo import models, fields, api


class Pricelist(models.Model):
    _inherit = "product.pricelist"

    campaign_ids = fields.Many2many(
        comodel_name='sale.campaign',
        string='Campaigns')

    @api.model
    def get_promotions(self):
        promotions = self.env['sale.promotion']
        today = fields.Date.from_string(fields.Date.today())
        campaigns = self.campaign_ids.filtered(
            lambda c: (not c.start_date or fields.Date.from_string(
                c.start_date) < today) and
            (not c.end_date or fields.Date.from_string(
                c.end_date) > today))
        for campaign in campaigns:
            promotions = promotions + campaign.promotion_ids.filtered(
                lambda p: (not p.start_date or fields.Date.from_string(
                    p.start_date) < today) and
                (not p.end_date or fields.Date.from_string(
                    p.end_date) > today))
        return promotions
