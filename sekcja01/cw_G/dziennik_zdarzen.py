import logging


# konfiguracja loggera
def utworz_logger_plikowy(nazwa_pliku):
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.WARNING)

    file_handler = logging.FileHandler(nazwa_pliku)
    format_komunikatow = '{asctime} : {levelname:8} : {name} : {message}'
    formatter = logging.Formatter(format_komunikatow, style='{', datefmt='%Y-%m-%d %H:%M:%S')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    return logger


if __name__ == '__main__':
    dziennik = utworz_logger_plikowy('dziennik.log')

    # użycie loggera
    dziennik.debug('TESTOWANIE DZIAŁANIA LOGGERA...')
    dziennik.info('Do tego miejsca wszystko działa OK...')
    dziennik.warning('Coś jest nie tak...')
    dziennik.error('Opcja nie działa, ale możemy kontynuować...')
    dziennik.critical('Błąd krytyczny - kończymy działanie...')
