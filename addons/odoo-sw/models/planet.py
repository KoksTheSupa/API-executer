# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ResPlanet(models.Model):
    _name = "res.planet"
    _description = "Planets"

    name = fields.Char(string="Name")
    diameter = fields.Integer(string="Diameter, km")
    rotation_period = fields.Integer(string="Rotation period, h")
    orbital_period = fields.Integer(string="Orbital period, h")
    population = fields.Char(string="population")
