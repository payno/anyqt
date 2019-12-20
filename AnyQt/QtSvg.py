from . import _api

if _api.USED_API == _api.QT_API_PYQT5:
    from PyQt5.QtSvg import *
elif _api.USED_API == _api.QT_API_PYSIDE2:
    from PySide2.QtSvg import *
