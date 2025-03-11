from math import floor, ceil

class Formatter:
    def __init__(self):
        pass

    def format_temperature(number):
        number_string = str(number)

        if (len(number_string)) > 0:
            try:
                parts = number_string.split('.')
                decimal_part = parts[1]
            except Exception:
                decimal_part = 0

            if (int(decimal_part) < 50):
                return floor(number)
            elif (int(decimal_part) > 50):
                return ceil(number)
        else:
            return None
