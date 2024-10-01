import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QLabel, QPushButton,
    QWidget, QFrame, QHBoxLayout, QVBoxLayout
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from app.logic import *


class MainWindow(QMainWindow):
    def __init__(self, part: str, required: float):
        super().__init__()
        self.trees = all_trees_from_part(part, required)
        self.tree_index = 0
        self.setWindowTitle("Satisfactory Helper")
        self.setWindowIcon(QIcon("../images/satisfactory_icon.webp"))
        self.initUI(self.trees[self.tree_index])

    def show_stats(self, tree: list):
        stats = eval_tree(tree)

        stats_frame = QFrame(self)
        stats_frame.setStyleSheet(
            "border: 2px solid black;"
            "padding: 20px;"
            "border-radius: 10px;"
            "font-size: 16px;"
            "font-family: Arial;"
            "font-weight: Bold;"
        )

        stats_layout = QVBoxLayout(stats_frame)

        stats_label = QLabel(f"STATS")
        stats_label.setStyleSheet("border: None; font-size: 20px;")
        stats_label.setAlignment(Qt.AlignCenter)
        stats_layout.addWidget(stats_label)

        for stat in stats:
            stats_label = QLabel(f"{stat}: {stats[stat]}")
            stats_label.setStyleSheet("border: None;")
            stats_label.setAlignment(Qt.AlignCenter)
            stats_layout.addWidget(stats_label)

        stats_frame.adjustSize()
        return stats_frame

    def next_recipe_click(self):
        self.tree_index += 1
        self.initUI(self.trees[self.tree_index])

    def previous_recipe_click(self):
        self.tree_index -= 1
        self.initUI(self.trees[self.tree_index])

    def recipe_buttons(self) -> QFrame:
        buttons_frame = QFrame(self)
        buttons_layout = QHBoxLayout(buttons_frame)

        previous_recipe = QPushButton('<')
        if self.tree_index == 0:
            previous_recipe.setDisabled(True)
        else:
            previous_recipe.setDisabled(False)
        previous_recipe.clicked.connect(self.previous_recipe_click)
        buttons_layout.addWidget(previous_recipe)

        next_recipe = QPushButton('>')
        if self.tree_index == len(self.trees) - 1:
            next_recipe.setDisabled(True)
        else:
            next_recipe.setDisabled(False)
        next_recipe.clicked.connect(self.next_recipe_click)
        buttons_layout.addWidget(next_recipe)

        buttons_frame.adjustSize()
        return buttons_frame


    def create_input_box(self, outer_frame: QFrame, recipe_input: dict) -> QLabel:
        sub_label = QLabel(f"{recipe_input['part']}\n{recipe_input['required_per_minute']}", outer_frame)
        sub_label.setStyleSheet("border: None; background-color: hsl(167, 7%, 78%);")
        sub_label.setAlignment(Qt.AlignCenter)
        return sub_label

    def create_part_box(self, recipe: dict) -> QFrame:
        """
        Creates a Frame containing the top part and its inputs, so will print that to the UI when called
        :param recipe:
            The recipe for the top part
        :return:
            A QFrame containing the top part as a box and its inputs per minute
        """
        recipe_and_output = QFrame(self)

        outer_layout = QVBoxLayout(recipe_and_output)

        outputs_layout = QHBoxLayout()
        # add an arrow pointing to layer above
        arrow_label = QLabel("↑", self)  # Right arrow symbol
        arrow_label.setStyleSheet("font-size: 24px;")
        arrow_label.setAlignment(Qt.AlignCenter)
        outputs_layout.addWidget(arrow_label)

        if 'index' in recipe:
            info_layout = QVBoxLayout()
            # add info on outputs
            for info in ['output_per_minute', 'recipe_output_per_minute', 'machines_required', 'layer']:
                label = QLabel(f"{info}: {recipe[info]}", recipe_and_output)
                label.setStyleSheet("font-family: Arial; font-size: 14px; font-weight: Bold;")
                label.setAlignment(Qt.AlignCenter)
                info_layout.addWidget(label)
            outputs_layout.addLayout(info_layout)

        outer_layout.addLayout(outputs_layout)

        # top layer is the entire recipe
        this_recipe = QFrame(self)

        layout = QVBoxLayout(this_recipe)

        input_layout = QHBoxLayout()

        if 'index' in recipe:
            this_recipe.setStyleSheet(
                "border: 2px solid black;"
                "padding: 20px;"
                "border-radius: 10px;"
                "font-size: 16px;"
                "font-family: Arial;"
                "font-weight: Bold;"
            )
            # main_label are the output and the machine
            main_label = QLabel(f"{recipe['index']}\n{recipe['machine']}", this_recipe)
            main_label.setStyleSheet("border: None; padding: 20px;")
            main_label.setAlignment(Qt.AlignHCenter)
            layout.addWidget(main_label, alignment=Qt.AlignHCenter)

            for recipe_input in recipe['inputs']:
                sub_label = self.create_input_box(this_recipe, recipe_input)
                input_layout.addWidget(sub_label, alignment=Qt.AlignHCenter)

        else:
            this_recipe.setStyleSheet(
                "border: None;"
                "padding: 10px;"
                "border-radius: 10px;"
                "font-size: 16px;"
                "font-family: Arial;"
                "font-weight: Bold;"
            )
            input_layout.addWidget(self.create_input_box(this_recipe, recipe))

        layout.addLayout(input_layout)
        this_recipe.adjustSize()
        outer_layout.addWidget(this_recipe)
        return recipe_and_output

    def inputs_to_outputs(self, layer: list):
        inputs_outputs_frame = QFrame(self)

        # Create a complete layout for both outputs and inputs
        layout = QVBoxLayout(inputs_outputs_frame)

        # Add the output layer to the top
        layout.addWidget(self.create_part_box(layer[0]))

        if 'inputs' in layer[0]:
            # Create a horizontal layout for all the inputs
            inputs_layout = QHBoxLayout()

            for input_recipe in layer[1:]:
                inputs_layout.addWidget(self.inputs_to_outputs(input_recipe))

            layout.addLayout(inputs_layout)

        inputs_outputs_frame.adjustSize()
        return inputs_outputs_frame

    def initUI(self, tree: list):
        tree_ui = self.inputs_to_outputs(tree)

        # Create a central widget for the main window
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        # Create a layout for the central widget
        layout = QHBoxLayout(central_widget)

        # Add the final frame to the layout and align it to the center
        layout.addWidget(tree_ui, stretch=10, alignment=Qt.AlignCenter)

        stats_and_turn = QVBoxLayout()
        stats_ui = self.show_stats(tree)
        button_ui = self.recipe_buttons()
        stats_and_turn.addWidget(stats_ui, alignment=Qt.AlignTop)
        stats_and_turn.addWidget(button_ui, alignment=Qt.AlignBottom)

        layout.addLayout(stats_and_turn, stretch=1)



def main():
    app = QApplication(sys.argv)
    window = MainWindow('reinforced iron plate', 15)
    window.showMaximized()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
