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
