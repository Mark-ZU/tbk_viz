import os
import sys

from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QCloseEvent
from PySide6.QtWidgets import QApplication, QLabel, QMainWindow
import PySide6QtAds as QtAds

class TestLabel(QLabel):
    def __init__(self, text, parent=None):
        super().__init__(text, parent)
        self.setWordWrap(True)
        # set center
        self.setAlignment(Qt.AlignCenter)

class MainWindow(QMainWindow):
    def __init__(self, title="My App", parent=None):
        super().__init__(parent)
        self.setWindowTitle(title)

        # create menu
        self.menuView = self.menuBar().addMenu("View")

        self.dock_manager = QtAds.CDockManager(self)
        
        dock_widget = QtAds.CDockWidget("Label 1")
        dock_widget.setWidget(TestLabel("Lorem ipsum dolor sit amet, consectetuer adipiscing elit. "))
        self.menuView.addAction(dock_widget.toggleViewAction())
        self.dock_manager.addDockWidget(QtAds.TopDockWidgetArea, dock_widget)

        dock_widget = QtAds.CDockWidget("Label 2")
        dock_widget.setWidget(TestLabel("Lorem ipsum dolor sit amet, consectetuer adipiscing elit. "))
        self.menuView.addAction(dock_widget.toggleViewAction())
        self.dock_manager.addDockWidget(QtAds.TopDockWidgetArea, dock_widget)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    w.resize(800,600)
    w.show()
    app.exec()