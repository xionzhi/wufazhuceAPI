"""
@Time    : 2018-11-12 16:02:49
@Author  : xionzhi
@File    : runserver.py
@Software: vscode
"""
from service import app


if __name__ == '__main__':
    app.run(port=8080, debug=True)
