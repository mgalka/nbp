import datetime


class ExchangeRate:
    def __init__(self, currency, code, ask_rate, bid_rate):
        self.currency = currency
        self.code = code
        self.ask_rate = ask_rate
        self.bid_rate = bid_rate

    def __str__(self):
        return f'<{self.currency}({self.code})\t{self.bid_rate}' \
               f'\t{self.ask_rate}>'


class ExchangeRateTable:
    def __init__(self, name, effective_date, rates=None):
        self.name = name
        self.effective_date = datetime.datetime.strptime(effective_date, '%Y-%m-%d')
        self.rates = rates if rates is not None else []

    def add_rate(self, rate):
        self.rates.append(rate)

    def get_rate(self, code):
        for rate in self.rates:
            if rate.code == code:
                return rate

    def __getitem__(self, item):
        result = self.get_rate(item)
        if result is not None:
            return result
        else:
            raise KeyError(item)


def print_header(rate_table):
    print(f'Tabela: {rate_table.name}\tData: '
          f'{rate_table.effective_date}')
    print('Waluta\tSprz.\tKupno')


def print_content(rates):
    for rate in rates:
        print(f'{rate.currency}({rate.code})\t{rate.bid_rate}'
              f'\t{rate.ask_rate}')


def print_table(rate_table):
    print_header(rate_table)
    print_content(rate_table.rates)


if __name__ == '__main__':
    rate_table = ExchangeRateTable('C', '2020-11-10')
    rate_table.add_rate(ExchangeRate('dolar amerykański', 'USD', 3.9225, 4.0017))
    rate_table.add_rate(ExchangeRate('frank szwajcarski', 'CHF', 4.2838, 4.3704))
    rate_table.add_rate(ExchangeRate('jen japoński', 'JPY', 3.7483, 3.8241))
    print_table(rate_table)
    print(f"{rate_table['JPY']}")
    print(f"{rate_table['UNKNOWN']}")
