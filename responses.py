#!/usr/bin/env python
# coding: utf-8
"""
Displays responses and allows to assign actions
"""
# JN 2015-06-22
from __future__ import print_function, division, absolute_import
import sys
import os
import glob

from PyQt4 import QtCore as qc
from PyQt4 import QtGui as qg

import ui_response_viewer
from model import ResponseTableModel, RESP_STATE, CLUSTER_STATE
from tools import parse_name

DEBUG = False 

SCROLL_AREA_MIN_WIDTH = 50
TABLE_HEIGHT = 50


class GuiOverview(qg.QMainWindow, ui_response_viewer.Ui_MainWindow):
    """
    main window of channel overview program
    """
    def __init__(self, parent=None):
        super(GuiOverview, self).__init__(parent)
        self.setupUi(self)
        self.initialized = False
        self.pixmap = None

        self.channelmodel = ResponseTableModel()
        self.tableViewChannels.setModel(self.channelmodel)

        self.labelCurrentCh = qg.QLabel(self)
        self.labelCurrentCh.setMinimumWidth(200)
        self.statusBar().addWidget(self.labelCurrentCh)

        self.labelDirName = qg.QLabel(self)
        self.statusBar().addWidget(self.labelDirName)

        self.labelImage = qg.QLabel(self)
        # self.labelImageRight = qg.QLabel(self)

        for label in (self.labelImage,):  # self.labelImageRight):
            label.setSizePolicy(qg.QSizePolicy.Ignored, qg.QSizePolicy.Ignored)
            label.setScaledContents(True)

        self.scrollAreaImage.setWidget(self.labelImage)

        self.scrollAreaImage.setMinimumWidth(SCROLL_AREA_MIN_WIDTH)

        self.fit_w = True
        self.fit_h = True

        self.set_actions()

    def set_actions(self):
        self.tableViewChannels.selectionModel().\
            currentChanged.connect(self.item_action)
        self.actionInitialize_from_current_folder.\
            triggered.connect(self.init_from_cwd)

        self.actionSet_to_artifact.triggered.connect(self.set_artifact)
        self.actionSet_to_okay.triggered.connect(self.set_okay)
        self.actionSet_to_maybe.triggered.connect(self.set_candidate)
        self.actionSet_to_edit.triggered.connect(self.set_edit)
        self.actionSet_to_response.triggered.connect(self.set_response)
        self.actionSet_to_no_response.triggered.connect(self.set_noresponse)
        self.action_Save_classification_to_file.triggered.\
            connect(self.save_to_file)
        self.action_goto_next.triggered.connect(self.goto_next)

    def set_artifact(self):
        self.set_type(CLUSTER_STATE, 'A')

    def set_candidate(self):
        self.set_type(RESP_STATE, 'M')

    def set_edit(self):
        self.set_type(CLUSTER_STATE, 'E')

    def set_response(self):
        self.set_type(RESP_STATE, 'R')

    def set_noresponse(self):
        self.set_type(RESP_STATE, 'N')

    def set_okay(self):
        self.set_type(CLUSTER_STATE, 'O')

    def set_type(self, which_one, new_type):
        index = self.tableViewChannels.selectedIndexes()
        if index:
            self.channelmodel.set_type(index[0], which_one, new_type)
            self.tableViewChannels.selectionModel().\
                setCurrentIndex(index[0],
                                qg.QItemSelectionModel.Select |
                                qg.QItemSelectionModel.Current)

    def init_from_cwd(self):
        """
        helper
        """
        self.init_from_path(os.getcwd())

        # relayout
        top_visible = 50  # px
        vsizes = self.splitter.sizes()
        self.splitter.setSizes([top_visible,
                                sum(vsizes) - top_visible])

        # hsizes = self.splitter.sizes()
        # left_space = int(sum(hsizes) * .6)
        # self.splitter.setSizes([left_space, sum(hsizes) - left_space])

    def init_from_path(self, path):
        """
        read in channel information from a path
        """
        self.channelmodel.images = []
        self.labelDirName.setText(path)
        self.dirname_responses = os.path.join(path, 'responses')
        has_responses = os.path.isdir(self.dirname_responses)

        if not has_responses:
            print('No response folder found!')
            return

        else:
            img_names = glob.glob(os.path.join(self.dirname_responses,
                                               '*.png'))
        if DEBUG:
            img_names = img_names[:3]
        for img_name in sorted(img_names):

            info = parse_name(os.path.basename(img_name))
            image = qg.QPixmap(qg.QImage(img_name))
            row = [str(info['csc']), info['daytime'], str(info['gid']), 'O',
                   'N', image, os.path.basename(img_name)]
            self.channelmodel.add_row(row)

        self.channelmodel.reset()

        self.initialized = True

        self.set_sizes()

    def item_action(self, index=qc.QModelIndex(), prev=qc.QModelIndex()):
        """
        typical action is to show image
        """
        if not self.initialized:
            return

        self.pixmap = self.channelmodel.\
            get_image(index.row())
        if self.pixmap is not None:
            self.labelImage.setPixmap(self.pixmap)

        self.set_sizes()

        # set the status
        status = self.channelmodel.get_status(index.row(), RESP_STATE)
        self.labelCurrentCh.setText(status)

    def set_sizes(self, clicked='w'):
        """
        set image size
        """

        seq = [(self.labelImage, self.pixmap, self.scrollAreaImage)]

        for label, image, area in seq:
            if image is not None:

                if self.fit_h:
                    height = area.height()
                else:
                    height = image.height()

                if self.fit_w:
                    width = area.width()
                else:
                    width = image.width()

                label.resize(qc.QSize(width, height))

    def toggle(self, what):
        """
        toggle action for this channel
        """
        index = self.tableViewChannels.selectedIndexes()
        if index:
            self.channelmodel.toggle(index[0], what)
            self.tableViewChannels.selectionModel().\
                setCurrentIndex(index[0],
                                qg.QItemSelectionModel.Select |
                                qg.QItemSelectionModel.Current)

    def goto_next(self):
        self.goto(1)

    def goto_previous(self):
        self.goto(-1)

    def goto(self, shift):
        """
        go down one channel in table view
        """
        index = self.tableViewChannels.selectedIndexes()
        if index:
            row = index[0].row()
            col = index[0].column()
            if shift > 0:
                if row == len(self.channelmodel.images) - shift:
                    return
            elif shift < 0:
                if row < -shift:
                    return

            new_index = self.channelmodel.createIndex(row + shift, col)
            self.tableViewChannels.selectionModel().\
                setCurrentIndex(new_index,
                                qg.QItemSelectionModel.Select |
                                qg.QItemSelectionModel.Current)

    def save_to_file(self):
        """
        print out sort/extract channels
        """

        states = self.channelmodel.get_states()

        if not states:
            print('Not saving!')
            return

        out_fname = os.path.join(self.dirname_responses, 'states.csv')
        write = True

        if os.path.exists(out_fname):
            msgbox = qg.QMessageBox()
            msgbox.setText('Overwrite {} ?'.format(out_fname))
            msgbox.setStandardButtons(qg.QMessageBox.Yes | qg.QMessageBox.No)
            ret = msgbox.exec_()
            if ret == qg.QMessageBox.Yes:
                print('Overwriting ' + out_fname)
            else:
                write = False

        if write:
            from csv import writer as csvwriter
            with open(out_fname, 'wb') as csvfile:
                writer = csvwriter(csvfile)
                for row in states:
                    writer.writerow(row)


def main():
    APP = qg.QApplication(sys.argv)
    APP.setStyle('oxygen')
    WIN = GuiOverview()
    WIN.setWindowTitle('Response Viewer')
    WIN.showMaximized()
    APP.exec_()

if __name__ == "__main__":
    main()
