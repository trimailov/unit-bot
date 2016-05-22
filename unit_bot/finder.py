from collections import namedtuple
import re

from unit_bot import creds


class Finder(object):
    def __init__(self, text):
        self.text = text
        self.units = self.find_units()

        self.conversion_table = {
            'kmh': self.convert_kmh,
            'km/h': self.convert_kmh,
            'm/s': self.convert_mps,
            'mph': self.convert_mph,
            'mi/h': self.convert_mph
        }

    def build_regex(self):
        NUMBER = "(\d+\.?\d*|\.\d+)"

        SPEED_KM = "(kmh|km/h)"
        SPEED_MTR = "(m/s)"
        SPEED_MILE = "(mph|mi/h)"

        REGEXP = "%s(\s)*(%s|%s|%s)" % (
            NUMBER, SPEED_KM, SPEED_MTR, SPEED_MILE
        )
        return REGEXP

    def find_units(self):
        return re.findall(self.build_regex(), self.text)

    def convert_units(self):
        units = self.units
        conversion_dict = {}
        if units:
            Unit = namedtuple('Unit', 'value ws units')

            for unit in units:
                u = Unit._make(unit[:3])
                # get conversion function according to type of units
                conversion_func = self.conversion_table[u.units]
                original_value = '{} {}'.format(u.value, u.units)
                conversion_dict[original_value] = conversion_func(u.value)

        return conversion_dict

    def convert_kmh(self, unit_value):
        kmh = float(unit_value)
        mps = kmh / 3.6
        mph = kmh / 1.6
        return ['{:g} m/s'.format(mps), '{:g} mph'.format(mph)]

    def convert_mps(self, unit_value):
        mps = float(unit_value)
        kmh = mps * 3.6
        mph = kmh / 1.6
        return ['{:g} km/h'.format(kmh), '{:g} mph'.format(mph)]

    def convert_mph(self, unit_value):
        mph = float(unit_value)
        kmh = mph * 1.6
        mps = kmh / 3.6
        return ['{:g} km/h'.format(kmh), '{:g} m/s'.format(mps)]

    def generate_conversion_message(self):
        converted_units = self.convert_units()

        intro_text = "/u/{username} have found such values: `{units}`.".format(
            username=creds.USERNAME,
            units='`, `'.join(sorted(converted_units.keys())),
        )
        converted_values_lines = []
        converted_values = sorted(converted_units.items())
        for key, value in converted_values:
            converted_values_lines.append(
                '{} is: {} or {}\n'.format(key, value[0], value[1])
            )
        message = "{intro}\n\n{converted_values}".format(
            intro=intro_text,
            converted_values='\n\n'.join(converted_values_lines)
        )
        return message
