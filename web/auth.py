import json

from managers.account_manager import account_manager


def handle(handler):

    account = account_manager.authenticate("dummy")

    handler.send_response(200)
    handler.send_header("Content-Type", "application/json")
    handler.end_headers()

    handler.wfile.write(json.dumps({
        "Id": account.id,
        "AccountName": account.account_name,
        "Token": account.token,
        "RealName": account.real_name,
        "Email": account.email,
        "HasEmail": account.has_email,
        "IsActivated": account.is_activated,
        "IsAdmin": account.is_admin,
        "IsGuest": account.is_guest
    }).encode())