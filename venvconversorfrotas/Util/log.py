import logging
import configparser
from Util.base import Base as base

cfg = configparser.ConfigParser()
cfg.read(r'C:\Users\Equiplano\PycharmProjects\conversorFrotas\cfg.ini')
class Log:

    def log(self, msg, filename='log', level=logging.INFO):
        dir = cfg['DEFAULT']['DiretorioArquivosLog']
        dir = base().create_dir(dir)
        logging.basicConfig(filename=str(dir) + filename + '.txt', format='%(asctime)s - %(levelname)s - %(message)s', level=level)
        logging.log(level, msg)

        return dir