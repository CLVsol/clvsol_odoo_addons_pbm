# -*- coding: utf-8 -*-
###############################################################################
#
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
###############################################################################

from openerp import api, fields, models


class Insured(models.Model):
    _inherit = 'clv.insured'

    card_ids = fields.One2many(
        comodel_name='clv.card',
        inverse_name='insured_id',
        string='Cards'
    )
    count_cards = fields.Integer(
        string='Number of Cards',
        compute='_compute_count_cards',
        store=True
    )

    @api.depends('card_ids')
    def _compute_count_cards(self):
        for r in self:
            r.count_cards = len(r.card_ids)


class Card(models.Model):
    _inherit = "clv.card"

    insured_id = fields.Many2one(
        comodel_name='clv.insured',
        string='Insured',
        ondelete='restrict'
    )
    insured_code = fields.Char(
        string='Insured Code',
        related='insured_id.code',
        store=False
    )
    insured_alias = fields.Char(
        string='Insured Alias',
        related='insured_id.alias',
        store=False
    )
