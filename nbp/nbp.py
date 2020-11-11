import datetime as d


class ExchangeRate:
    def __init__(self, currency, sell_rate, buy_rate, ratio=1):
        self.currency = currency
        self.sell_rate = sell_rate
        self.buy_rate = buy_rate
        self.ratio = ratio


class ExchangeRateTable:
    def __init__(self, name, publish_date, rates=None):
        self.name = name
        self.publish_date = d.datetime.strptime(publish_date, '%Y-%m-%d')
        self.rates = []

    def add_rate(self, rate):
        self.rates.append(rate)

    def get_rate(self, currency):
        for rate in self.rates:
            if rate.currency == currency:
                return rate


def print_header(rate_table):
    print(f'Tabela: {rate_table.name}\tData publikacji: '
          f'{rate_table.publish_date.date()}')
    print('Waluta\tSprz.\tKupno')


def print_content(rates):
    for rate in rates:
        print(f'{rate.ratio} {rate.currency}\t{rate.buy_rate}'
              f'\t{rate.sell_rate}')


def print_table(rate_table):
    print_header(rate_table)
    print_content(rate_table.rates)


if __name__ == '__main__':
    rate_table = ExchangeRateTable('C', '2020-11-10')
    rate_table.add_rate(ExchangeRate('USD', 3.9225, 4.0017))
    rate_table.add_rate(ExchangeRate('CHF', 4.2838, 4.3704))
    rate_table.add_rate(ExchangeRate('JPY', 3.7483, 3.8241, ratio=100))
    print_table(rate_table)
