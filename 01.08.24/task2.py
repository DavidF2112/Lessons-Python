def validate_card_number(card_number):
    if not isinstance(card_number, str):
        return False
    
    parts = card_number.split('-')
    if len(parts) != 4 or any(len(part) != 4 for part in parts):
        return False

    if not all(part.isdigit() for part in parts):
        return False
    
    full_number = ''.join(parts)

    def luhn_checksum(card_number):
        def digits_of(n):
            return [int(d) for d in str(n)]
        digits = digits_of(card_number)
        odd_digits = digits[-1::-2]
        even_digits = digits[-2::-2]
        checksum = sum(odd_digits)
        for d in even_digits:
            checksum += sum(digits_of(d * 2))
        return checksum % 10

    return luhn_checksum(full_number) == 0


print(validate_card_number("1234-5678-9012-3456"))
print(validate_card_number("4539-1488-0343-6467")) 