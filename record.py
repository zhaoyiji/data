INDEX_MAP = {'code': 0,
             'name': 1,
             'open': 2,
             'closed': 3,
             'now': 4,
             'high': 5,
             'low': 6,
             'buy_bid': 7,
             'sell_bid': 8,
             'volume': 9,
             'amount': 10,
             'buy_1_amount': 11,
             'buy_1': 12,
             'buy_2_amount': 13,
             'buy_2': 14,
             'buy_3_amount': 15,
             'buy_3': 16,
             'buy_4_amount': 17,
             'buy_4': 18,
             'buy_5_amount': 19,
             'buy_5': 20,
             'sell_1_amount': 21,
             'sell_1': 22,
             'sell_2_amount': 23,
             'sell_2': 24,
             'sell_3_amount': 25,
             'sell_3': 26,
             'sell_4_amount': 27,
             'sell_4': 28,
             'sell_5_amount': 29,
             'sell_5': 30,
             'date': 31,
             'time': 32,
             }


class Record(object):
    """Record object

    Record is a onetime get data from RawData.
    Record is a line in dat file.
    """
    def __init__(self, data):
        self._data_string = ''
        self._data = []
        self._parse(data)

    def _parse(self, data):
        """dump string formatted data into list formatted data.

        dump string formatted data into list.
        return stk name
        :rtype: no
        :param data: string formatted data
        """
        self._data_string = data
        self._data = data.split(',')

    def get_value(self, name):
        """Get specified value by name.

        :rtype: string
        :param name: string formatted key.
        """
        return self._data[INDEX_MAP[name]]

    def get_data_string(self):
        """Get String Formatted data.

        Get String Formatted completed record data.
        """
        return self._data_string

    def get_data(self):
        """Get List Formatted data.

        Get List Formatted completed record data.
        :rtype list
        """
        return self._data

    def get_code(self):
        """Get Code.

        Get stk Code.
        :rtype string
        """
        return self._data[0]
