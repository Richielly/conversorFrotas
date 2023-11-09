import logging
import configparser
from Util.base import Base as base
import os
from datetime import datetime
cfg = configparser.ConfigParser()
cfg.read('cfg.ini')
class Log:
    def log(self, line='?', msg='?', filename='geral'):
        log_dir = cfg['DEFAULT']['DiretorioArquivosLog']
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)
        log_file = os.path.join(log_dir, filename + '_log.txt')
        try:
            now = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
            log_time = f"[{now}] Linha: [{line}] {msg}"

            if os.path.exists(log_file):
                mode = 'a'
            else:
                mode = 'w'

            with open(log_file, mode) as file:
                file.write(log_time + '\n')
        except Exception as e:
            return str(e)


