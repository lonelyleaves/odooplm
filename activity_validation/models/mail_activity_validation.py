# -*- coding: utf-8 -*-
##############################################################################
#
#    OmniaSolutions, ERP-PLM-CAD Open Source Solutions
#    Copyright (C) 2011-2019 https://OmniaSolutions.website
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this prograIf not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
'''
Created on Nov 16, 2019

@author: mboscolo
'''
import logging
import datetime
from odoo import models
from odoo import fields
from odoo import api
from odoo import _
from odoo.exceptions import UserError
from datetime import timedelta
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT


class MailActivityValidation(models.Model):
    _name = "mail.activity.validation"

    _desctiption = "This object perform the validation managed by user"

    mail_activity_type_id = fields.Many2one('mail.activity.type', string="Activity Type")

    user_ids = fields.One2many('res.users', 'mail_activity_validation_id',
                              string='Validation user involved')

    group_ids = fields.One2many('res.groups', 'mail_activity_validation_id',
                               string='Validation Groups',
                               help="""All the user related to this group will be added as Validation user""")

    response = fields.Selection([('ready', 'Ready'),
                                 ('accepted', 'Accepted'),
                                 ('rejected', 'Rejected')], string="Response")
