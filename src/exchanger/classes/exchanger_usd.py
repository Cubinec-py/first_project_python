import csv


def update_avaliable_csv(address, new_value):

    filepath = 'src/exchanger/const/available_currency.csv'
    row_num = address

    with open(filepath, 'r+t') as csvfile:
        reader = csv.reader(csvfile)
        lines = []

        for current_line in reader:
            if reader.line_num == row_num:
                current_line[1] = new_value
            lines.append(current_line)

        csvfile.seek(0)
        csv.writer(csvfile).writerows(lines)
        csvfile.truncate()


def print_result(a, result):
    return print(f'\nUNAVAILABLE, REQUIRED BALANCE {a.currency} {round(result, 2)}, AVAILABLE {a.available}\n')


class ExchangerUsd:

    def __init__(self, exchange, avaliables):
        self.exchanges = exchange
        self.avaliables = avaliables

    def exchanger_usd(self, exchange, avaliables, val):
        for i in exchange:
            for a in avaliables:
                if a.available >= (float(val[1]) // i.sale) and a.currency != val[0]:
                    result = float(val[1]) // i.sale
                    new_balance = float(a.available) - float(result)
                    update_avaliable_csv(address=3, new_value=f'{new_balance}')
                    print(f'\n{a.currency} {int(result)}, RATE {round(i.sale, 2)}\n')
                    break
                elif a.currency != val[0]:
                    result = float(val[1]) // i.sale
                    print_result(a, result)
                    break
