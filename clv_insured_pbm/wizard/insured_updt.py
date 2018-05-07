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

import logging

from odoo import api, fields, models

_logger = logging.getLogger(__name__)


class InsuredUpdate(models.TransientModel):
    _inherit = 'clv.insured.updt'

    state = fields.Selection(
        [('draft', 'New'),
         ('processing', 'Processing'),
         ('active', 'Active'),
         ('suspended', 'Suspended'),
         ('cancelled', 'Cancelled'),
         ], string='State', default=False, readonly=False, required=False
    )
    state_selection = fields.Selection(
        [('set', 'Set'),
         ], string='State', default=False, readonly=False, required=False
    )

    insured_group_id = fields.Many2one(
        comodel_name='clv.insured_group',
        string='Insured Group'
    )
    insured_group_id_selection = fields.Selection(
        [('set', 'Set'),
         ('remove', 'Remove'),
         ], string='Insured Group', default=False, readonly=False, required=False
    )

    insurance_plan_id = fields.Many2one(
        comodel_name='clv.insurance_plan',
        string='Insurance Plan'
    )
    insurance_plan_id_selection = fields.Selection(
        [('set', 'Set'),
         ('remove', 'Remove'),
         ], string='Insurance Plan', default=False, readonly=False, required=False
    )

    @api.multi
    def do_insured_updt(self):
        self.ensure_one()

        super(InsuredUpdate, self).do_insured_updt()

        for insured in self.insured_ids:

            _logger.info(u'%s %s', '>>>>>', insured.name)

            if self.state_selection == 'set':
                insured.state = self.state
            if self.state_selection == 'remove':
                insured.state = False

            if self.insured_group_id_selection == 'set':
                insured.insured_group_id = self.insured_group_id
            if self.insured_group_id_selection == 'remove':
                insured.insured_group_id = False

            if self.insurance_plan_id_selection == 'set':
                insured.insurance_plan_id = self.insurance_plan_id
            if self.insurance_plan_id_selection == 'remove':
                insured.insurance_plan_id = False

        return True
