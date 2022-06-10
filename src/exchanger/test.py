from exchanger.classes.exchanger_final import ExchangerFinal


def run_exchanger():
    while True:
        start.greeting()
        val = input('Please, make your choice: ')
        valid_val = val.upper().split()
        try:
            if valid_val[0] == 'COURSE':
                start.print_exchange_status(start.exchanges, start.avaliables, valid_val[1])
                break
            elif valid_val[0] == 'EXCHANGE':
                start.test(start.exchanges, start.avaliables, valid_val[1:3])
                break
            elif valid_val[0] == 'STOP':
                print('\nSERVICE STOPPED')
                break
        except IndexError:
            print('\nPlease, write right command!\n')
            start.print_choice()


if __name__ == '__main__':
    start = ExchangerFinal()
    run_exchanger()



    @staticmethod
    def print_choice():
        print('If you want to see USD to UAH, print "course usd".',
              'If you want to see UAH to USD, print "course uah".', sep='\n')

    @staticmethod
    def print_exchange_variant():
        print('To exchange USD to UAH print "EXCHANGE USD ... ".',
              'To exchange UAH to USD print "EXCHANGE UAH ... ".', sep='\n')