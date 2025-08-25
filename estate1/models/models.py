# -*- coding: utf-8 -*-

from odoo import models, fields, api


class estate1(models.Model):
    _name = 'estate1.estate1'
    _description = 'estate1.estate1'

    name = fields.Char()
    value = fields.Integer()
    value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text()
    sale_person_id = fields.Many2one(
        "res.partner",
        string="Sale Person"
    )

    @api.depends('value')
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.value) / 100

class SalePerson(models.Model):
    _name = 'estate1.property.type'
    _description = 'Sele Person'

    name = fields.Char(string='Name', required=True)

