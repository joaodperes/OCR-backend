from models.account import Account


class AccountManager:

    def authenticate(self, token: str) -> Account:

        return Account(
            id="00000000-0000-0000-0000-000000000001",
            account_name="Developer",
            token="DEVTOKEN"
        )


account_manager = AccountManager()