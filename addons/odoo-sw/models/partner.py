# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ResPartner(models.Model):
    _inherit = "res.partner"

    planet = fields.Many2one(
        comodel_name="res.planet",
        string="Planet",
    )
