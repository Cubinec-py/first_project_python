from exchanger.classes.exchanger_final import ExchangerFinal


def run_exchanger():

    while True:
        start.greeting()
        val = input('Please, make your choice: ')
        valid_val = val.upper().split()
        try:
            if valid_val[0] == 'COURSE':
                start.print_exchange_status(start.exchanges, start.avaliables, valid_val[1])

            elif valid_val[0] == 'EXCHANGE':
                start.exchanger(start.exchanges, start.avaliables, valid_val[1:3])

            elif valid_val[0] == 'STOP':
                print('\nSERVICE STOPPED')
                break
            else:
                print('\nPlease, write right command!\n')

        except IndexError:
            print('\nError, please, write right command!\n')


if __name__ == '__main__':
    start = ExchangerFinal()
    run_exchanger()