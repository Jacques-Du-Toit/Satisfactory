import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QLabel, QPushButton, QWidget, QHBoxLayout, QGridLayout, QFrame,
    QHBoxLayout, QVBoxLayout
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from app.logic import *


class MainWindow(QMainWindow):
    def __init__(self, tree):
        super().__init__()
        self.tree = tree
        self.setWindowTitle("Satisfactory Helper")
        self.setWindowIcon(QIcon("../images/satisfactory_icon.webp"))

        # top layer is the entire box
        top_layer = QFrame(self)
        top_layer.setStyleSheet(
            "border: 2px solid black;"
            "padding: 20px;"
            "border-radius: 10px;"
            "font-size: 16px;"
            "font-family: Arial;"
            "font-weight: Bold;"
        )

        layout = QVBoxLayout(top_layer)

        # main_label are the output and the machine
        main_label = QLabel(f"{tree[0]['index']}\n{tree[0]['machine']}", top_layer)
        main_label.setStyleSheet("border: None; padding: 20px;")
        main_label.setAlignment(Qt.AlignHCenter)

        layout.addWidget(main_label, alignment=Qt.AlignHCenter)

        input_layout = QHBoxLayout()
        for recipe_input in tree[0]['inputs']:
            sub_label = QLabel(f"{recipe_input['part']}\n{recipe_input['required_per_minute']}", top_layer)
            sub_label.setStyleSheet("border: None; background-color: hsl(167, 7%, 78%);")
            sub_label.setAlignment(Qt.AlignHCenter)
            input_layout.addWidget(sub_label, alignment=Qt.AlignHCenter)

        layout.addLayout(input_layout)

        top_layer.adjustSize()
        top_layer.move((self.width() - top_layer.width()) // 2, (self.height() - top_layer.height()) // 2)




def main():
    app = QApplication(sys.argv)
    tree = all_trees_from_part('reinforced iron plate', 5)[0]
    window = MainWindow(tree)
    window.showMaximized()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
