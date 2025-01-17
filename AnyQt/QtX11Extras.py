from . import _api

__all__ = ["QX11Info"]

if _api.USED_API == _api.QT_API_PYQT5:
    from PyQt5.QtX11Extras import *
elif _api.USED_API == _api.QT_API_PYSIDE2:
    from PySide2.QtX11Extras import *
