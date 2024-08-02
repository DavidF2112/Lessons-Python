def validate_login(login):
    if len(login) < 2 or len(login) > 10:
        return False
    if not login.isalnum():
        return False
    return True


