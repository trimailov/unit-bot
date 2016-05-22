import pytest

from unit_bot.finder import Finder


text_data = [
    ('1.2 kmh',               [('1.2', ' ', 'kmh', 'kmh', '', '')]),
    ('1.2 kph',               [('1.2', ' ', 'kph', 'kph', '', '')]),
    ('1.2 kmh, 62mph',        [('1.2', ' ', 'kmh', 'kmh', '', ''),
                               ('62', '', 'mph', '', '', 'mph')]),
    ('62, 6.2m/s',            [('6.2', '', 'm/s', '', 'm/s', '')]),
    ('.2    km/h',            [('.2', ' ', 'km/h', 'km/h', '', '')]),
    ('bla bla bla \n .9mi/h', [('.9', '', 'mi/h', '', '', 'mi/h')]),
    ('2014 bla bla bla',      []),
]


@pytest.mark.parametrize('text, result', text_data)
def test_find_units(text, result):
    # test various pieces of text and verify that units are found
    f = Finder(text)
    assert f.find_units() == result


convertion_data = [
    ('1.2 kmh',               {'1.2 kmh': ['0.333333 m/s', '0.75 mph']}),
    ('1.2 kmh, 62mph',        {'1.2 kmh': ['0.333333 m/s', '0.75 mph'],
                               '62 mph':  ['99.2 km/h', '27.5556 m/s']}),
    ('62, 6.2m/s',            {'6.2 m/s': ['22.32 km/h', '13.95 mph']}),
    ('.2    km/h',            {'.2 km/h': ['0.0555556 m/s', '0.125 mph']}),
    ('bla bla bla \n .9mi/h', {'.9 mi/h': ['1.44 km/h', '0.4 m/s']}),
]


@pytest.mark.parametrize('text, result', convertion_data)
def test_convert_units(text, result):
    # test various pieces of text and verify that correct conversions are made
    f = Finder(text)
    assert f.convert_units() == result


message_data = [
    ('1.2 kmh', "/u/unit-conversion-bot have found such values: `1.2 kmh`.\n\n1.2 kmh is: 0.333333 m/s or 0.75 mph\n"),
    ('1.2 kmh, 62mph', "/u/unit-conversion-bot have found such values: `1.2 kmh`, `62 mph`.\n\n1.2 kmh is: 0.333333 m/s or 0.75 mph\n\n\n62 mph is: 99.2 km/h or 27.5556 m/s\n"),
]


@pytest.mark.parametrize('text, result', message_data)
def test_generate_message(text, result):
    # test various pieces of text and verify that correct conversions are made
    f = Finder(text)
    assert f.generate_conversion_message() == result
