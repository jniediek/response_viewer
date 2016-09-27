# coding: utf-8
"""
View Responses
"""
# JN 2015-06-22
from __future__ import division, print_function, absolute_import
from PyQt4 import QtCore as qc

NCOLS = 7
OBJECT, DAYTIME, GROUP, CLUSTER_STATE, RESP_STATE, IMAGE, FNAME = range(NCOLS)

CLUSTER_STATES = {'A': 'Artifact',
                  'O': 'Okay',
                  'E': 'Edit'}

RESP_STATES = {'M': 'Maybe',
               'R': 'Response',
               'N': 'No Response'}


class ResponseTableModel(qc.QAbstractTableModel):
    """
    Table of channels with properties such as extracted, sorted etc
    """
    def __init__(self):
        super(ResponseTableModel, self).__init__()
        self.images = []

    def rowCount(self, index=qc.QModelIndex()):
        return len(self.images)

    def columnCount(self, index=qc.QModelIndex()):
        return NCOLS - 2  # last cols: image, fname

    def data(self, index, role=qc.Qt.DisplayRole):
        if not (index.isValid() and
                0 <= index.row() < len(self.images)):
            return qc.QVariant()

        this_image = self.images[index.row()]
        col = index.column()

        if role == qc.Qt.DisplayRole:
            data = this_image[col]
            if col == CLUSTER_STATE:
                data = CLUSTER_STATES[data]
            if col == RESP_STATES:
                data = RESP_STATES[data]
            return qc.QVariant(data)

    def headerData(self, section, orientation, role=qc.Qt.DisplayRole):
        if role == qc.Qt.TextAlignmentRole:
            if orientation == qc.Qt.Horizontal:
                return qc.QVariant(int(qc.Qt.AlignLeft | qc.Qt.AlignVCenter))

        elif role == qc.Qt.DisplayRole:
            if orientation == qc.Qt.Horizontal:
                if section == OBJECT:
                    ret = 'Channel'
                elif section == DAYTIME:
                    ret = 'Daytime'
                elif section == GROUP:
                    ret = 'Group'
                elif section == CLUSTER_STATE:
                    ret = 'Cluster'
                elif section == RESP_STATE:
                    ret = 'Response'
                return qc.QVariant(ret)

            return qc.QVariant(int(section) + 1)

    def add_row(self, row):
        """
        simply add a channel to table
        """
        self.images.append(row)
        print('Added ' + row[0])

    def set_type(self, index, which_one, new_type):
        self.images[index.row()][which_one] = new_type
        self.reset()

    def get_image(self, row):
        """
        just return the image
        """
        return self.images[row][IMAGE]

    def get_status(self, row, which_one):
        """
        return a status row text
        """
        act = [self.images[row][which_one]]
        print(act)
        ret = self.images[row][OBJECT] + ' classification: ' + act[0]
        return ret

    def set_action(self, index, which_one, to_what):
        """
        set classification attribute
        """

        row = self.channels[index.row()]
        row[which_one] = to_what
        self.reset()

    def get_states(self):
        """
        return internal data
        """
        ret = []
        for row in self.images:
            retval = (row[FNAME], row[OBJECT], row[DAYTIME], row[GROUP],
                      row[CLUSTER_STATE], row[RESP_STATE])
            ret.append(retval)

        return ret
