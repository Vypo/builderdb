from sitetree.utils import tree, item

sitetrees = (
    tree('accounts', items=[
        item('Sign Up', 'account_signup', access_guest=True),
        item('Log In', 'account_login', access_guest=True),
        item('Log Out', 'account_logout', access_loggedin=True),
    ]),
)
