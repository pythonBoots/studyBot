from polo import poloniex
import matplotlib.dates as mdates
import datetime

# converting date YY-MM-DD HH:MM:SS to epoch format


def date2epoch(date):
    year = int(date[:4])
    month = int(date[5:7])
    day = int(date[8:10])
    hour = int(date[11:13])
    minute = int(date[14:16])
    sec = int(date[17:19])
    num = mdates.date2num(datetime.datetime(year, month, day, hour, minute, sec))
    res = mdates.num2epoch(num)
    return res


def chartData(currPair, period, start, end):


    # initialization of Poloniex API
    initApi = poloniex('JR8ARSYK-EH5S20RD-3LGGHKSZ-FOZDDQSN',
                       '9ce33962e6f1f74212164c65a02f9425dbf810b53a52a5c041c0bfecaa33cf92840e9ae4d417633373a089c34234cbf44580d30260e3d38846c18cd2169e2133')

    # getting of data from poloniex in json  format and converting them to
    # list of dictionaries
    rawData = initApi.returnChartData(currPair, period,
                                      date2epoch(start),
                                      date2epoch(end))

    return rawData
