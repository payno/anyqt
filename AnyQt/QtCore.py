from . import _api

__all__ = [
    'QAbstractAnimation',
    'QAbstractEventDispatcher',
    'QAbstractItemModel',
    'QAbstractListModel',
    'QAbstractNativeEventFilter',
    'QAbstractProxyModel',
    'QAbstractState',
    'QAbstractTableModel',
    'QAbstractTransition',
    'QAnimationGroup',
    'QBasicTimer',
    'QBitArray',
    'QBuffer',
    'QByteArray',
    'QByteArrayMatcher',
    'QChildEvent',
    'QCollator',
    'QCollatorSortKey',
    'QCommandLineOption',
    'QCommandLineParser',
    'QCoreApplication',
    'QCryptographicHash',
    'QDataStream',
    'QDate',
    'QDateTime',
    'QDir',
    'QDirIterator',
    'QDynamicPropertyChangeEvent',
    'QEasingCurve',
    'QElapsedTimer',
    'QEvent',
    'QEventLoop',
    'QEventLoopLocker',
    'QEventTransition',
    'QFile',
    'QFileDevice',
    'QFileInfo',
    'QFileSelector',
    'QFileSystemWatcher',
    'QFinalState',
    'QGenericArgument',
    'QGenericReturnArgument',
    'QHistoryState',
    'QIODevice',
    'QIdentityProxyModel',
    'QItemSelection',
    'QItemSelectionModel',
    'QItemSelectionRange',
    'QJsonDocument',
    'QJsonParseError',
    'QJsonValue',
    'QLibrary',
    'QLibraryInfo',
    'QLine',
    'QLineF',
    'QLocale',
    'QLockFile',
    'QMargins',
    'QMarginsF',
    'QMessageAuthenticationCode',
    'QMessageLogContext',
    'QMessageLogger',
    'QMetaClassInfo',
    'QMetaEnum',
    'QMetaMethod',
    'QMetaObject',
    'QMetaProperty',
    'QMetaType',
    'QMimeData',
    'QMimeDatabase',
    'QMimeType',
    'QModelIndex',
    'QMutex',
    'QMutexLocker',
    'QObject',
    'QObjectCleanupHandler',
    'QParallelAnimationGroup',
    'QPauseAnimation',
    'QPersistentModelIndex',
    'QPluginLoader',
    'QPoint',
    'QPointF',
    'QProcess',
    'QProcessEnvironment',
    'QPropertyAnimation',
    'QReadLocker',
    'QReadWriteLock',
    'QRect',
    'QRectF',
    'QRegExp',
    'QRegularExpression',
    'QRegularExpressionMatch',
    'QRegularExpressionMatchIterator',
    'QResource',
    'QRunnable',
    'QSaveFile',
    'QSemaphore',
    'QSequentialAnimationGroup',
    'QSettings',
    'QSharedMemory',
    'QSignalBlocker',
    'QSignalMapper',
    'QSignalTransition',
    'QSize',
    'QSizeF',
    'QSocketNotifier',
    'QSortFilterProxyModel',
    'QStandardPaths',
    'QState',
    'QStateMachine',
    'QStorageInfo',
    'QStringListModel',
    'QSysInfo',
    'QSystemSemaphore',
    'QT_TRANSLATE_NOOP',
    'QT_TR_NOOP',
    'QT_TR_NOOP_UTF8',
    'QT_VERSION',
    'QT_VERSION_STR',
    'QTemporaryDir',
    'QTemporaryFile',
    'QTextBoundaryFinder',
    'QTextCodec',
    'QTextDecoder',
    'QTextEncoder',
    'QTextStream',
    'QTextStreamManipulator',
    'QThread',
    'QThreadPool',
    'QTime',
    'QTimeLine',
    'QTimeZone',
    'QTimer',
    'QTimerEvent',
    'QTranslator',
    'QUrl',
    'QUrlQuery',
    'QUuid',
    'QVariant',
    'QVariantAnimation',
    'QWaitCondition',
    'QWriteLocker',
    'QXmlStreamAttribute',
    'QXmlStreamAttributes',
    'QXmlStreamEntityDeclaration',
    'QXmlStreamEntityResolver',
    'QXmlStreamNamespaceDeclaration',
    'QXmlStreamNotationDeclaration',
    'QXmlStreamReader',
    'QXmlStreamWriter',
    'Q_ARG',
    'Q_CLASSINFO',
    'Q_ENUMS',
    'Q_FLAGS',
    'Q_RETURN_ARG',
    'Qt',
    'QtCriticalMsg',
    'QtDebugMsg',
    'QtFatalMsg',
    'QtInfoMsg',
    'QtMsgType',
    'QtSystemMsg',
    'QtWarningMsg',
    'bin_',
    'bom',
    'center',
    'dec',
    'endl',
    'fixed',
    'flush',
    'forcepoint',
    'forcesign',
    'hex_',
    'left',
    'lowercasebase',
    'lowercasedigits',
    'noforcepoint',
    'noforcesign',
    'noshowbase',
    'oct_',
    'qAbs',
    'qAddPostRoutine',
    'qAddPreRoutine',
    'qChecksum',
    'qCompress',
    'qCritical',
    'qDebug',
    'qErrnoWarning',
    'qFatal',
    'qFloatDistance',
    'qFormatLogMessage',
    'qFuzzyCompare',
    'qInf',
    'qInstallMessageHandler',
    'qIsFinite',
    'qIsInf',
    'qIsNaN',
    'qIsNull',
    'qQNaN',
    'qRegisterResourceData',
    'qRemovePostRoutine',
    'qRound',
    'qRound64',
    'qSNaN',
    'qSetFieldWidth',
    'qSetMessagePattern',
    'qSetPadChar',
    'qSetRealNumberPrecision',
    'qSharedBuild',
    'qUncompress',
    'qUnregisterResourceData',
    'qVersion',
    'qWarning',
    'qrand',
    'qsrand',
    'reset',
    'right',
    'scientific',
    'showbase',
    'uppercasebase',
    'uppercasedigits',
    'ws'
]

if _api.USED_API == _api.QT_API_PYQT5:
    from PyQt5 import QtCore as _QtCore
    globals().update(
        {name: getattr(_QtCore, name) for name in __all__}
    )

    Signal = _QtCore.pyqtSignal
    Slot = _QtCore.pyqtSlot
    Property = _QtCore.pyqtProperty
    del _QtCore

elif _api.USED_API == _api.QT_API_PYQT4:
    from PyQt4 import QtCore as _QtCore, QtGui as _QtGui
    __missing__ = [
        'QAbstractNativeEventFilter',
        'QCollator',
        'QCollatorSortKey',
        'QCommandLineOption',
        'QCommandLineParser',
        'QEventLoopLocker',
        'QFileDevice',
        'QFileSelector',
        'QJsonDocument',
        'QJsonParseError',
        'QJsonValue',
        'QLockFile',
        'QMarginsF',
        'QMessageAuthenticationCode',
        'QMessageLogContext',
        'QMessageLogger',
        'QMimeDatabase',
        'QMimeType',
        'QRegularExpression',
        'QRegularExpressionMatch',
        'QRegularExpressionMatchIterator',
        'QSaveFile',
        'QSignalBlocker',
        'QStandardPaths',
        'QStorageInfo',
        'QTemporaryDir',
        'QTimeZone',
        'QUrlQuery',
        'QtInfoMsg',
        'qAddPreRoutine',
        'qFloatDistance',
        'qFormatLogMessage',
        'qInstallMessageHandler',
        'qSetMessagePattern'
    ]
    globals().update(
        {name: getattr(_QtCore, name) for name in __all__
         if hasattr(_QtCore, name)}
    )

    Signal = _QtCore.pyqtSignal
    Slot = _QtCore.pyqtSlot
    Property = _QtCore.pyqtProperty

    QAbstractProxyModel = _QtGui.QAbstractProxyModel
    QIdentityProxyModel = _QtGui.QIdentityProxyModel
    QItemSelection = _QtGui.QItemSelection
    QItemSelectionModel = _QtGui.QItemSelectionModel
    QItemSelectionRange = _QtGui.QItemSelectionRange
    QSortFilterProxyModel = _QtGui.QSortFilterProxyModel
    QStringListModel = _QtGui.QStringListModel
    del _QtCore, _QtGui

elif _api.USED_API == _api.QT_API_PYSIDE:
    from PySide import QtCore as _QtCore, QtGui as _QtGui
    __missing__ = [
        'QAbstractNativeEventFilter',
        'QCollator',
        'QCollatorSortKey',
        'QCommandLineOption',
        'QCommandLineParser',
        'QEventLoopLocker',
        'QFileDevice',
        'QFileSelector',
        'QJsonDocument',
        'QJsonParseError',
        'QJsonValue',
        'QLibrary',
        'QLockFile',
        'QMarginsF',
        'QMessageAuthenticationCode',
        'QMessageLogContext',
        'QMessageLogger',
        'QMetaType',
        'QMimeDatabase',
        'QMimeType',
        'QObjectCleanupHandler',
        'QRegularExpression',
        'QRegularExpressionMatch',
        'QRegularExpressionMatchIterator',
        'QSaveFile',
        'QSharedMemory',
        'QSignalBlocker',
        'QStandardPaths',
        'QStorageInfo',
        'QTemporaryDir',
        'QTimeZone',
        'QUrlQuery',
        'QVariant',
        'Q_ARG',
        'Q_CLASSINFO',
        'Q_ENUMS',
        'Q_FLAGS',
        'Q_RETURN_ARG',
        'QtInfoMsg',
        'bin_',
        'bom',
        'center',
        'dec',
        'endl',
        'fixed',
        'flush',
        'forcepoint',
        'forcesign',
        'hex_',
        'left',
        'lowercasebase',
        'lowercasedigits',
        'noforcepoint',
        'noforcesign',
        'noshowbase',
        'oct_',
        'qAddPreRoutine',
        'qCompress',
        'qErrnoWarning',
        'qFloatDistance',
        'qFormatLogMessage',
        'qInf',
        'qInstallMessageHandler',
        'qQNaN',
        'qRemovePostRoutine',
        'qRound64',
        'qSNaN',
        'qSetFieldWidth',
        'qSetMessagePattern',
        'qSetPadChar',
        'qSetRealNumberPrecision',
        'qSharedBuild',
        'qUncompress',
        'reset',
        'right',
        'scientific',
        'showbase',
        'uppercasebase',
        'uppercasedigits',
        'ws'
    ]
    globals().update(
        {name: getattr(_QtCore, name) for name in __all__
         if hasattr(_QtCore, name)}
    )
    __all__ = sorted(set(__all__) - set(__missing__))
    QAbstractProxyModel = _QtGui.QAbstractProxyModel
    QIdentityProxyModel = _QtGui.QIdentityProxyModel
    QItemSelection = _QtGui.QItemSelection
    QItemSelectionModel = _QtGui.QItemSelectionModel
    QItemSelectionRange = _QtGui.QItemSelectionRange
    QSortFilterProxyModel = _QtGui.QSortFilterProxyModel
    QStringListModel = _QtGui.QStringListModel

    _major, _minor, _micro = tuple(map(int, _QtCore.qVersion().split(".")))
    QT_VERSION = (_major << 16) + (_minor << 8) + _micro
    QT_VERSION_STR = "{}.{}.{}".format(_major, _minor, _micro)

    del _QtCore, _QtGui, _major, _minor, _micro
