# Copyright 2014 Vypo
#
# message   f=sitetrees.py&n=140ca0881fac3423
# sha256    489f20b0a830e9b98df2cab606828508be8c8eceba95d015bd8db8501c3bb09b
#
# This file is part of BuilderDB.
#
# BuilderDB is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# BuilderDB is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with BuilderDB.  If not, see <http://www.gnu.org/licenses/>.
from sitetree.utils import tree, item

sitetrees = (
    tree('accounts', items=[
        item('Sign Up', 'account_signup', access_guest=True),
        item('Log In', 'account_login', access_guest=True),
        item('Password Reset', 'account_reset_password', in_menu=False, in_sitetree=False, children=[
            item('Sent', 'account_reset_password_done', in_menu=False, in_sitetree=False),
            item('Reset', 'account_reset_password_from_key', in_menu=False, in_sitetree=False), # TODO: Fix this so that it works
            item('Done', 'account_reset_password_from_key_done', in_menu=False, in_sitetree=False),
        ]),
        item('{{ user.username }}', 'accounts_index', access_loggedin=True, children=[
            item('Change Password', 'account_change_password', access_loggedin=True, in_menu=False),
            item('Account Inactive', 'account_inactive', access_loggedin=True, in_menu=False, in_sitetree=False),
            item('Email Addresses', 'account_email', access_loggedin=True, in_menu=False, in_sitetree=False, children=[
                item('Confirm', 'account_email_confirm confirmation.key', access_loggedin=True, in_menu=False, in_sitetree=False),
            ]),
        ]),
        item('Log Out', 'account_logout', access_loggedin=True),
    ]),
)
