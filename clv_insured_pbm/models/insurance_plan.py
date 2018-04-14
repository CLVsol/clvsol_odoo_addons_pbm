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

from odoo import api, fields, models


class InsurancePlan(models.Model):
    _inherit = 'clv.insurance_plan'

    insured_ids = fields.One2many(
        comodel_name='clv.insured',
        inverse_name='insurance_plan_id',
        string='Insureds'
    )
    count_insureds = fields.Integer(
        string='Number of Insureds',
        compute='_compute_count_insureds',
        store=True
    )

    @api.depends('insured_ids')
    def _compute_count_insureds(self):
        for r in self:
            r.count_insureds = len(r.insured_ids)


class Insured(models.Model):
    _inherit = 'clv.insured'

    insurance_plan_id = fields.Many2one(
        comodel_name='clv.insurance_plan',
        string='Insurance Plan',
        ondelete='restrict'
    )
