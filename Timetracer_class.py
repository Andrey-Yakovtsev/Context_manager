from datetime import datetime
from Cook_book import dict_collector, starter


class MyTimeTracerManager:

    def __init__(self, log_path, encoding='utf-8'):
        self.log_file = open(log_path, 'a', encoding=encoding)
        self.name = self.__class__.__name__

    def __enter__(self):
        self.start = datetime.now()
        self.log_file.write(f'Старт функции {self.name}: {self.start}: \n')
        return self

    def write_trace_log(self, function):
        self.function = function
        self.function('reciepts_initial.txt')


    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            self.write_trace_log(f'error: {exc_val}')
        # self.write_trace_log('end')
        self.end = datetime.now()
        self.log_file.write(f'Конец функции {self.name}: {self.end}: \n')
        self.runtime = self.end - self.start
        self.log_file.write(f'Время работы функции {self.name}: {self.runtime}: \n')
        self.log_file.close()


if __name__ == '__main__':
    starter()
    with MyTimeTracerManager('my.log') as log:
        log.write_trace_log(dict_collector)

