from collections import namedtuple
import re


class Finder(object):
    def __init__(self, text):
        self.text = text

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
        units = self.find_units()
        if units:
            Unit = namedtuple('Unit', 'value ws units')
            convertion_answer = []
            unit_values_found = []

            for unit in units:
                u = Unit._make(unit[:3])
                # get conversion function according to type of units
                func = self.conversion_table[u.units]
                convertion_answer.append(func(u.value))
                unit_values_found.append('{} {}'.format(u.value, u.units))

            intro_text = "`{username}` have found such values: `{units}`.".format(
                username=creds.USERNAME,
                units='`, `'.join(unit_values_found),
            )
            convertion_answer.insert(0, intro_text)
            return '\n\n---\n\n'.join(convertion_answer)

    def convert_kmh(self, unit_value):
        kmh = float(unit_value)
        mps = kmh / 3.6
        mph = kmh / 1.6

        answer = '%g km/h, converts to:\n\n%g m/s,\n\n%g mph.' % (
            kmh, mps, mph
        )
        print(answer)
        return answer

    def convert_mps(self, unit_value):
        mps = float(unit_value)
        kmh = mps * 3.6
        mph = kmh / 1.6

        answer = '%g m/s, converts to:\n\n%g km/h,\n\n%g mph.' % (
            mps, kmh, mph
        )
        print(answer)
        return answer

    def convert_mph(self, unit_value):
        mph = float(unit_value)
        kmh = mph * 1.6
        mps = kmh / 3.6

        answer = '%g mph, converts to:\n\n%g km/h,\n\n%g m/s.' % (
            mph, kmh, mps
        )
        print(answer)
        return answer
