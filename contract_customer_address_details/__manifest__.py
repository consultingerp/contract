##############################################################################
#
#    Author: Oy Tawasta OS Technologies Ltd.
#    Copyright 2019 Oy Tawasta OS Technologies Ltd. (https://tawasta.fi)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program. If not, see http://www.gnu.org/licenses/agpl.html
#
##############################################################################

{
    "name": "Contract partner address details",
    "summary": "Add partner address details to contracts",
    "version": "12.0.1.0.0",
    "category": "Contract Management",
    "website": "https://github.com/Tawasta/contract",
    "author": "Tawasta",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": ["contract"],
    "data": [
        "views/account_analytic_account_view.xml",
        "views/account_analytic_search.xml",
    ],
}
