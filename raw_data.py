# -*- encoding: utf-8 -*-

import threading
import time
import httplib2

import k_line
import config
import record


class RawData(object):
    """raw data define

    raw data is data from network
    """
    def __init__(self):
        self._raw_data = ""
        self._data = []
        self._http = None

    def fetch(self, url):
        """fetch data from network

        fetch data form network and parse it into list and simplified string.
        :rtype string
        :return string formatted raw data.
        :param url url the data store, real time data from network.

        """
        self._get(url)
        self._parse()

        return self._data

    def _get(self, url):
        # config.LOGGER.info(url)

        if self._http is None:
            self._http = httplib2.Http()

        headers = {
           'Connection': 'keep-alive'
        }
        resp, page = self._http.request(url, headers=headers)

        self._raw_data = unicode(page, 'gbk')
        config.LOGGER.info(self._raw_data)

    def _parse(self):
        data_list = self._raw_data.split('"')  # data_list is ('','','','')
        self._data = []
        rec = ''
        for i in range(len(data_list)-1):  # -1 is discard last ';'
            if i % 2 == 0:  # get code and put in record
                rec = data_list[i][-9:-1]
            else:  # data
                rec += ','
                rec += data_list[i]
                self._data.append(rec)


class RealData(threading.Thread):
    """Real Time Data Analyze

    Analyze Real Time Data, format the url and get record
    """
    def __init__(self, code):
        threading.Thread.__init__(self)
        self._code = code
        self._url = ""
        self._running = True
        self._kline = None
        self._kline5 = None

    def start_analyze(self):
        """Start Real Time Data Analyze

        Analyze Real Time Data, make the remote data fetch url, then start the thread to fetch and analyze.
        at the same time, write the raw data into the history file.
        """
        self._url = config.URL_PREFIX
        self._url += self._code
        self.start()

    def stop_analyze(self):
        """Stop Real Time Data Analyze

        Stop data analyze, quit the analyze thread and wait the thread quit.
        """
        self._running = False
        self.join()

    # @classmethod
    # def make_url(cls):
    #     code_list = stk_code.get_stk_code()
    #     url = config.URL_PREFIX
    #     for item in code_list:
    #         url += item
    #         url += ','
    #
    #     url = url[0:-1]  # del last ','
    #
    #     return url

    def run(self):
        self._kline = k_line.KLine1Min(self._code)
        self._kline5 = k_line.KLine5Min(self._code)
        remote_data = RawData()
        while self._running:
            raw_record = remote_data.fetch(self._url)  # fetch raw data
            rec = record.Record(raw_record[0])
            k = self._kline.get_kline(rec.get_data())
            self._kline.store(k)
            k5 = self._kline5.get_kline(k)
            self._kline5.store(k5)
            time.sleep(5)

        del self._kline
        self._kline = None
        del self._kline5
        self._kline5 = None


def analyze():
    real_time = RealData("sh000001")
    real_time.start_analyze()

    while True:
        s = raw_input("input quit to break analyze: ")
        if s == "quit":
            print "quit"
            break

    real_time.stop_analyze()

if __name__ == "__main__":
    analyze()
