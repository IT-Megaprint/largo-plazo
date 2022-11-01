# -*- coding: utf-8 -*-

from odoo import models, fields, api


class PosOrder(models.Model):
    _inherit = 'pos.order'

    @api.model
    def action_get_order_id(self, values):
        if values.get('server_id'):
            print(values.get('server_id')[0])
            pos_order = self.env['pos.order'].search(['|', ('id', '=', values['server_id'][0]), ('pos_reference', '=', values['order'])], limit=1)
        else:
            pos_order = self.env['pos.order'].search([('pos_reference', '=', values['order'])], limit=1)
        invoice_vals = self.env['account.move'].search_read(domain=[('invoice_origin', '=', pos_order.name)], fields=['firma_fel', 'serie_fel', 'numero_fel', 'date_fel'])
        return invoice_vals
