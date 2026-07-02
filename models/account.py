from dataclasses import dataclass


@dataclass
class Account:
    id: str
    account_name: str
    token: str

    real_name: str = ""
    email: str = ""

    has_email: bool = False
    is_activated: bool = True

    is_admin: bool = False
    is_guest: bool = False