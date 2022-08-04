"""Withdrawal Dialog."""

import sys
import questionary


def make_withdrawal(account):
    """Withdrawal Dialog."""

    # @TODO:  Use questionary to capture the withdrawal and set it equal to amount variable. Be sure that amount is a floating point number.
    withdrawal_amount = questionary.text("Enter amount you wish to withdraw:").ask()
    withdrawal_amount = float(withdrawal_amount)
    # @TODO:  Validates amount of withdrawal. If less than or equal to 0 system exits with error message.
    if withdrawal_amount <= 0:
        sys.exit("You entered invalid amount")
    # @TODO: Validates if withdrawal amount is less than or equal to account balance, processes withdrawal and returns account.
    # Else system exits with error messages indicating that the account is short of funds.
    elif withdrawal_amount < account["balance"]:
        account["balance"] -= withdrawal_amount
        print(f"Your withdraw is successful")
        return account
    else:
        sys.exit("Your account is short of funds")

        