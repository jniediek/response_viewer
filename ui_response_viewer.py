# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'responses.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(793, 555)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.splitter = QtGui.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.tableViewChannels = QtGui.QTableView(self.splitter)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableViewChannels.sizePolicy().hasHeightForWidth())
        self.tableViewChannels.setSizePolicy(sizePolicy)
        self.tableViewChannels.setFrameShape(QtGui.QFrame.Box)
        self.tableViewChannels.setAlternatingRowColors(True)
        self.tableViewChannels.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.tableViewChannels.setSortingEnabled(True)
        self.tableViewChannels.setObjectName(_fromUtf8("tableViewChannels"))
        self.layoutWidget = QtGui.QWidget(self.splitter)
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.scrollAreaImage = QtGui.QScrollArea(self.layoutWidget)
        self.scrollAreaImage.setFrameShape(QtGui.QFrame.NoFrame)
        self.scrollAreaImage.setFrameShadow(QtGui.QFrame.Sunken)
        self.scrollAreaImage.setWidgetResizable(False)
        self.scrollAreaImage.setObjectName(_fromUtf8("scrollAreaImage"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 57, 599))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Ignored, QtGui.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy)
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.scrollAreaImage.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollAreaImage)
        self.verticalLayout_2.addWidget(self.splitter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 793, 19))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuActions = QtGui.QMenu(self.menubar)
        self.menuActions.setObjectName(_fromUtf8("menuActions"))
        self.menu_Options = QtGui.QMenu(self.menubar)
        self.menu_Options.setObjectName(_fromUtf8("menu_Options"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionInitialize_from_current_folder = QtGui.QAction(MainWindow)
        self.actionInitialize_from_current_folder.setObjectName(_fromUtf8("actionInitialize_from_current_folder"))
        self.actionSet_to_artifact = QtGui.QAction(MainWindow)
        self.actionSet_to_artifact.setObjectName(_fromUtf8("actionSet_to_artifact"))
        self.actionSet_to_maybe = QtGui.QAction(MainWindow)
        self.actionSet_to_maybe.setObjectName(_fromUtf8("actionSet_to_maybe"))
        self.actionSet_to_edit = QtGui.QAction(MainWindow)
        self.actionSet_to_edit.setObjectName(_fromUtf8("actionSet_to_edit"))
        self.actionSet_to_response = QtGui.QAction(MainWindow)
        self.actionSet_to_response.setObjectName(_fromUtf8("actionSet_to_response"))
        self.action_Fit_image_size = QtGui.QAction(MainWindow)
        self.action_Fit_image_size.setCheckable(True)
        self.action_Fit_image_size.setObjectName(_fromUtf8("action_Fit_image_size"))
        self.action_Save_classification_to_file = QtGui.QAction(MainWindow)
        self.action_Save_classification_to_file.setObjectName(_fromUtf8("action_Save_classification_to_file"))
        self.actionSet_to_no_response = QtGui.QAction(MainWindow)
        self.actionSet_to_no_response.setObjectName(_fromUtf8("actionSet_to_no_response"))
        self.actionSet_to_okay = QtGui.QAction(MainWindow)
        self.actionSet_to_okay.setObjectName(_fromUtf8("actionSet_to_okay"))
        self.action_goto_next = QtGui.QAction(MainWindow)
        self.action_goto_next.setObjectName(_fromUtf8("action_goto_next"))
        self.menuActions.addAction(self.actionInitialize_from_current_folder)
        self.menuActions.addSeparator()
        self.menuActions.addAction(self.actionSet_to_okay)
        self.menuActions.addAction(self.actionSet_to_edit)
        self.menuActions.addAction(self.actionSet_to_artifact)
        self.menuActions.addSeparator()
        self.menuActions.addAction(self.actionSet_to_response)
        self.menuActions.addAction(self.actionSet_to_maybe)
        self.menuActions.addAction(self.actionSet_to_no_response)
        self.menuActions.addSeparator()
        self.menuActions.addAction(self.action_Save_classification_to_file)
        self.menuActions.addAction(self.action_goto_next)
        self.menu_Options.addAction(self.action_Fit_image_size)
        self.menubar.addAction(self.menuActions.menuAction())
        self.menubar.addAction(self.menu_Options.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.menuActions.setTitle(_translate("MainWindow", "&Actions", None))
        self.menu_Options.setTitle(_translate("MainWindow", "&Options", None))
        self.actionInitialize_from_current_folder.setText(_translate("MainWindow", "&Initialize from current folder", None))
        self.actionInitialize_from_current_folder.setShortcut(_translate("MainWindow", "Ctrl+I", None))
        self.actionSet_to_artifact.setText(_translate("MainWindow", "Set to \'&artifact\'", None))
        self.actionSet_to_artifact.setShortcut(_translate("MainWindow", "A", None))
        self.actionSet_to_maybe.setText(_translate("MainWindow", "Set to \'&maybe response\'", None))
        self.actionSet_to_maybe.setShortcut(_translate("MainWindow", "M", None))
        self.actionSet_to_edit.setText(_translate("MainWindow", "Set to \'needs &edit\'", None))
        self.actionSet_to_edit.setShortcut(_translate("MainWindow", "E", None))
        self.actionSet_to_response.setText(_translate("MainWindow", "Set to \'&response\'", None))
        self.actionSet_to_response.setShortcut(_translate("MainWindow", "R", None))
        self.action_Fit_image_size.setText(_translate("MainWindow", "&Fit image size", None))
        self.action_Save_classification_to_file.setText(_translate("MainWindow", "&Save classification to file", None))
        self.action_Save_classification_to_file.setShortcut(_translate("MainWindow", "Ctrl+S", None))
        self.actionSet_to_no_response.setText(_translate("MainWindow", "Set to \'&no response\'", None))
        self.actionSet_to_no_response.setShortcut(_translate("MainWindow", "N", None))
        self.actionSet_to_okay.setText(_translate("MainWindow", "Set to &okay", None))
        self.actionSet_to_okay.setShortcut(_translate("MainWindow", "O", None))
        self.action_goto_next.setText(_translate("MainWindow", "Move to next row", None))
        self.action_goto_next.setShortcut(_translate("MainWindow", "Space", None))

