# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'temporalpthreshsourcettest1006.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

from PThresholdTemporalSourceTTest import PThresholdTempSourceTTest

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(730, 491)
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 160, 331, 221))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.ROI = QtWidgets.QLineEdit(self.layoutWidget)
        self.ROI.setObjectName("ROI")
        self.gridLayout_2.addWidget(self.ROI, 5, 1, 1, 1)
        self.ROILabel = QtWidgets.QLabel(self.layoutWidget)
        self.ROILabel.setObjectName("ROILabel")
        self.gridLayout_2.addWidget(self.ROILabel, 5, 0, 1, 1)
        self.MinimumTempLabel = QtWidgets.QLabel(self.layoutWidget)
        self.MinimumTempLabel.setObjectName("MinimumTempLabel")
        self.gridLayout_2.addWidget(self.MinimumTempLabel, 4, 0, 1, 1)
        self.tailComboBox = QtWidgets.QComboBox(self.layoutWidget)
        self.tailComboBox.setObjectName("tailComboBox")
        self.tailComboBox.addItem("")
        self.tailComboBox.addItem("")
        self.tailComboBox.addItem("")
        self.tailComboBox.addItem("")
        self.gridLayout_2.addWidget(self.tailComboBox, 6, 1, 1, 1)
        self.MinTempCluster = QtWidgets.QLineEdit(self.layoutWidget)
        self.MinTempCluster.setObjectName("MinTempCluster")
        self.gridLayout_2.addWidget(self.MinTempCluster, 4, 1, 1, 1)
        self.Condition1 = QtWidgets.QLineEdit(self.layoutWidget)
        self.Condition1.setAutoFillBackground(False)
        self.Condition1.setObjectName("Condition1")
        self.gridLayout_2.addWidget(self.Condition1, 0, 1, 1, 1)
        self.TailLabel = QtWidgets.QLabel(self.layoutWidget)
        self.TailLabel.setObjectName("TailLabel")
        self.gridLayout_2.addWidget(self.TailLabel, 6, 0, 1, 1)
        self.Condition1Label = QtWidgets.QLabel(self.layoutWidget)
        self.Condition1Label.setObjectName("Condition1Label")
        self.gridLayout_2.addWidget(self.Condition1Label, 0, 0, 1, 1)
        self.Prestimulus = QtWidgets.QLineEdit(self.layoutWidget)
        self.Prestimulus.setObjectName("Prestimulus")
        self.gridLayout_2.addWidget(self.Prestimulus, 3, 1, 1, 1)
        self.PrestimLabel = QtWidgets.QLabel(self.layoutWidget)
        self.PrestimLabel.setObjectName("PrestimLabel")
        self.gridLayout_2.addWidget(self.PrestimLabel, 3, 0, 1, 1)
        self.StartTime = QtWidgets.QLineEdit(self.layoutWidget)
        self.StartTime.setMaxLength(1000)
        self.StartTime.setObjectName("StartTime")
        self.gridLayout_2.addWidget(self.StartTime, 2, 1, 1, 1)
        self.FindROI = QtWidgets.QPushButton(self.layoutWidget)
        self.FindROI.setObjectName("FindROI")
        self.gridLayout_2.addWidget(self.FindROI, 5, 2, 1, 1)
        self.StartTimelabel = QtWidgets.QLabel(self.layoutWidget)
        self.StartTimelabel.setObjectName("StartTimelabel")
        self.gridLayout_2.addWidget(self.StartTimelabel, 2, 0, 1, 1)
        self.BadSubjects = QtWidgets.QLineEdit(self.layoutWidget)
        self.BadSubjects.setAutoFillBackground(False)
        self.BadSubjects.setObjectName("BadSubjects")
        self.gridLayout_2.addWidget(self.BadSubjects, 1, 1, 1, 1)
        self.BadSubjectsLabel = QtWidgets.QLabel(self.layoutWidget)
        self.BadSubjectsLabel.setObjectName("BadSubjectsLabel")
        self.gridLayout_2.addWidget(self.BadSubjectsLabel, 1, 0, 1, 1)
        self.layoutWidget1 = QtWidgets.QWidget(Form)
        self.layoutWidget1.setGeometry(QtCore.QRect(340, 160, 292, 151))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.layoutWidget1)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.PthreshVal = QtWidgets.QLineEdit(self.layoutWidget1)
        self.PthreshVal.setObjectName("PthreshVal")
        self.gridLayout_3.addWidget(self.PthreshVal, 2, 1, 1, 1)
        self.EndTimeLabel = QtWidgets.QLabel(self.layoutWidget1)
        self.EndTimeLabel.setObjectName("EndTimeLabel")
        self.gridLayout_3.addWidget(self.EndTimeLabel, 1, 0, 1, 1)
        self.Condition2 = QtWidgets.QLineEdit(self.layoutWidget1)
        self.Condition2.setObjectName("Condition2")
        self.gridLayout_3.addWidget(self.Condition2, 0, 1, 1, 1)
        self.Condition2Label = QtWidgets.QLabel(self.layoutWidget1)
        self.Condition2Label.setObjectName("Condition2Label")
        self.gridLayout_3.addWidget(self.Condition2Label, 0, 0, 1, 1)
        self.MAXFDR = QtWidgets.QLineEdit(self.layoutWidget1)
        self.MAXFDR.setObjectName("MAXFDR")
        self.gridLayout_3.addWidget(self.MAXFDR, 3, 1, 1, 1)
        self.PtreshLabel = QtWidgets.QLabel(self.layoutWidget1)
        self.PtreshLabel.setObjectName("PtreshLabel")
        self.gridLayout_3.addWidget(self.PtreshLabel, 2, 0, 1, 1)
        self.NumberPermutaiton = QtWidgets.QLineEdit(self.layoutWidget1)
        self.NumberPermutaiton.setObjectName("NumberPermutaiton")
        self.gridLayout_3.addWidget(self.NumberPermutaiton, 4, 1, 1, 1)
        self.MAxFDRLabel = QtWidgets.QLabel(self.layoutWidget1)
        self.MAxFDRLabel.setObjectName("MAxFDRLabel")
        self.gridLayout_3.addWidget(self.MAxFDRLabel, 3, 0, 1, 1)
        self.NumberPermLabel = QtWidgets.QLabel(self.layoutWidget1)
        self.NumberPermLabel.setObjectName("NumberPermLabel")
        self.gridLayout_3.addWidget(self.NumberPermLabel, 4, 0, 1, 1)
        self.EndTime = QtWidgets.QLineEdit(self.layoutWidget1)
        self.EndTime.setObjectName("EndTime")
        self.gridLayout_3.addWidget(self.EndTime, 1, 1, 1, 1)
        self.layoutWidget2 = QtWidgets.QWidget(Form)
        self.layoutWidget2.setGeometry(QtCore.QRect(10, 80, 271, 62))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.layoutWidget2)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.ProjecTRoot = QtWidgets.QLineEdit(self.layoutWidget2)
        self.ProjecTRoot.setObjectName("ProjecTRoot")
        self.gridLayout.addWidget(self.ProjecTRoot, 0, 0, 1, 1)
        self.FindpushButton = QtWidgets.QPushButton(self.layoutWidget2)
        self.FindpushButton.setObjectName("FindpushButton")
        self.gridLayout.addWidget(self.FindpushButton, 0, 1, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout, 0, 1, 1, 1)
        self.ProjectRoot = QtWidgets.QLabel(self.layoutWidget2)
        self.ProjectRoot.setObjectName("ProjectRoot")
        self.gridLayout_4.addWidget(self.ProjectRoot, 0, 0, 1, 1)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 0, 481, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.cancel = QtWidgets.QPushButton(Form)
        self.cancel.setGeometry(QtCore.QRect(330, 380, 169, 32))
        self.cancel.setObjectName("cancel")
        self.Ok = QtWidgets.QPushButton(Form)
        self.Ok.setGeometry(QtCore.QRect(500, 380, 126, 32))
        self.Ok.setObjectName("Ok")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(10, 140, 261, 23))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.layoutWidget.raise_()
        self.layoutWidget.raise_()
        self.layoutWidget.raise_()
        self.BadSubjectsLabel.raise_()
        self.BadSubjects.raise_()
        self.BadSubjects.raise_()
        self.ProjectRoot.raise_()
        self.label.raise_()
        self.cancel.raise_()
        self.Ok.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.cancel.clicked.connect(self.close)

        Rootdirectory = self.FindpushButton.clicked.connect(self.FindFolder)

        self.Ok.clicked.connect(self.RunAnalysis)
        Form.setTabOrder(self.ProjecTRoot, self.FindpushButton)
        Form.setTabOrder(self.FindpushButton, self.Condition1)
        Form.setTabOrder(self.Condition1, self.Condition2)
        Form.setTabOrder(self.Condition2, self.StartTime)
        Form.setTabOrder(self.StartTime, self.EndTime)
        Form.setTabOrder(self.EndTime, self.Prestimulus)
        Form.setTabOrder(self.Prestimulus, self.PthreshVal)
        Form.setTabOrder(self.PthreshVal, self.MinTempCluster)
        Form.setTabOrder(self.MinTempCluster, self.MAXFDR)
        Form.setTabOrder(self.MAXFDR, self.tailComboBox)
        Form.setTabOrder(self.tailComboBox, self.NumberPermutaiton)



    def FindFolder(self):

        directory = QtWidgets.QFileDialog.getExistingDirectory(self, "Find Files",
        QtCore.QDir.currentPath())


        self.ProjecTRoot.setText(directory)
        return directory
    ##### record all data entered in the form and pass it to the ttest function
    def RunAnalysis(self):
        condition1Name = self.Condition1.text()

        condition2Name = self.Condition2.text()
        startTime = self.StartTime.text()
        endTime = self.EndTime.text()
        presTim = self.Prestimulus.text()
        PThresh = self.PthreshVal.text()
        minTemporalCluster = self.MinTempCluster.text()
        maxFDR = self.MAXFDR.text()
        numPerm = self.NumberPermutaiton.text()
        anlsysTail = self.tailComboBox.currentData()
        ROI = self.ROI.text()
        root = self.ProjecTRoot.text()
        PThresholdTempSourceTTest(root, condition1Name, condition2Name,startTime,endTime, presTim,PThresh,minTemporalCluster, numPerm, anlsysTail, ROI)

        #if condition1Name == "" or condition2Name == "":
        #    QtWidgets.QMessageBox.information(self, "Empty Field",
        #    "Please enter all the required information in the form .")
        #return

        #pass all values to t-test function


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Permutation Test For a Temporal t-test analysis"))
        Form.setToolTip(_translate("Form", "PThreshold T-test for Temporal Data"))
        self.ROI.setToolTip(_translate("Form", "Please enter the prestimulus interval"))
        self.ROILabel.setText(_translate("Form", "ROI"))
        self.MinimumTempLabel.setText(_translate("Form", "Minimum Temporal Cluster"))
        self.tailComboBox.setItemText(0, _translate("Form", "Please choose an option"))
        self.tailComboBox.setItemText(1, _translate("Form", "Both"))
        self.tailComboBox.setItemText(2, _translate("Form", "Left tail"))
        self.tailComboBox.setItemText(3, _translate("Form", "Right Tail"))
        self.MinTempCluster.setToolTip(_translate("Form", "Please enter the prestimulus interval"))
        self.Condition1.setToolTip(_translate("Form", "Please enter the first condition\'s name"))
        self.TailLabel.setText(_translate("Form", "Tail"))
        self.Condition1Label.setText(_translate("Form", "Condition 1 :"))
        self.Prestimulus.setToolTip(_translate("Form", "Please enter the prestimulus interval"))
        self.PrestimLabel.setText(_translate("Form", "Prestimulus"))
        self.StartTime.setToolTip(_translate("Form", "Enter the start time"))
        self.StartTime.setInputMask(_translate("Form", "0"))
        self.FindROI.setText(_translate("Form", "find"))
        self.StartTimelabel.setText(_translate("Form", "Start Time:"))
        self.BadSubjects.setToolTip(_translate("Form", "Please enter the first condition\'s name"))
        self.BadSubjectsLabel.setText(_translate("Form", "BadSubjects"))
        self.PthreshVal.setToolTip(_translate("Form", "Please Enter the PThreshold value"))
        self.EndTimeLabel.setText(_translate("Form", "End Time"))
        self.Condition2.setToolTip(_translate("Form", "Please enter the first condition\'s name"))
        self.Condition2Label.setText(_translate("Form", "Condition 2:"))
        self.MAXFDR.setToolTip(_translate("Form", "Please enter the prestimulus interval"))
        self.PtreshLabel.setText(_translate("Form", "P_value threshold"))
        self.NumberPermutaiton.setToolTip(_translate("Form", "Please enter the prestimulus interval"))
        self.MAxFDRLabel.setText(_translate("Form", "Max FDR Rate"))
        self.NumberPermLabel.setText(_translate("Form", "Number Of Permutations"))
        self.EndTime.setToolTip(_translate("Form", "enter the ending time "))
        self.FindpushButton.setText(_translate("Form", "find"))
        self.ProjectRoot.setText(_translate("Form", "Project Root :"))
        self.label.setText(_translate("Form", "Temporal only T-test Analysis for source data "))
        self.cancel.setText(_translate("Form", "Cancel"))
        self.Ok.setText(_translate("Form", "Run Analysis"))

