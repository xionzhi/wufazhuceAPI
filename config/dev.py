"""
@Time    : 2018-11-12 16:02:49
@Author  : xionzhi
@File    : dev.py
@Software: vscode
"""
import os
import logging.handlers


# # # # # # # # # # # # #
#     MYSQL CONFIG      #
# # # # # # # # # # # # #
DATABASE_DIALECT = 'mysql'
DATABASE_DRIVER = 'pymysql'
DATABASE_HOST = '127.0.0.1'
DATABASE_PASSWORD = '123456'
DATABASE_USER = 'root'
DATABASE_NAME = 'dbtmp'
DATABASE_PORT = 3306
DATABASE_CODE = 'utf8'

# # # # # # # # # # # # #
#     LOGGER FILE       #
# # # # # # # # # # # # #
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
log_file = base_dir + '/log/' + 'service.log'
handler = logging.handlers.TimedRotatingFileHandler(log_file, 'D', 1, 7)
fmt = '%(levelname)s %(asctime)s %(pathname)s [line:%(lineno)d] %(message)s'
formatter = logging.Formatter(fmt)
handler.setFormatter(formatter)

# # # # # # # # # # # # #
#    LOADING LOGGER     #
# # # # # # # # # # # # #
LOGGER = logging.getLogger(__name__)
LOGGER.addHandler(handler)
LOGGER.setLevel(logging.DEBUG)
