def validate_email(email):
    if "@" not in email or "." not in email:
        return False
    

    local, domain = email.split("@")
    if len(domain.split(".")) < 2:
        return False

    if not domain.replace(".", "").isalnum():
        return False

    if not (local and domain):
        return False


    if not local[0].isalnum():
        return False


    previous_char = ""
    for char in local:
        if not (char.isalnum() or char in "_-"):
            return False
        if char == "-" and previous_char == "-":
            return False
        previous_char = char

    return True


