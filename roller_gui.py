import sys
import random
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel, QPushButton,
                             QVBoxLayout, QHBoxLayout, QWidget, QSpinBox,
                             QComboBox, QMessageBox, QFileDialog, QLineEdit, QDialog)
from PyQt5.QtGui import QFont, QIcon, QPalette, QBrush, QPixmap
from PyQt5.QtCore import Qt


class DnDTracker(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('D&D Health, Mana, and Dice Roller')
        self.setGeometry(100, 100, 400, 300)

        # Font Settings
        font = QFont()
        font.setPointSize(25)

        # Health and Mana Widgets
        self.health_label = QLabel('Health:')
        self.health_label.setFont(font)
        self.health_spin = QSpinBox()
        self.health_spin.setFont(font)
        self.health_spin.setRange(0, 1000)
        self.health_spin.setValue(100)

        self.mana_label = QLabel('Mana:')
        self.mana_label.setFont(font)
        self.mana_spin = QSpinBox()
        self.mana_spin.setFont(font)
        self.mana_spin.setRange(0, 1000)
        self.mana_spin.setValue(50)

        # Character Name Widget
        self.character_name_label = QLabel('Character Name:')
        self.character_name_label.setFont(font)
        self.character_name_input = QLineEdit()
        self.character_name_input.setFont(font)

        # Dice Roller Widgets
        self.dice_label = QLabel('Select Die:')
        self.dice_label.setFont(font)
        self.dice_combo = QComboBox()
        self.dice_combo.setFont(font)
        self.dice_combo.addItems(['d4', 'd6', 'd8', 'd10', 'd12', 'd20', 'd100'])

        self.num_dice_label = QLabel('Number of Dice:')
        self.num_dice_label.setFont(font)
        self.num_dice_spin = QSpinBox()
        self.num_dice_spin.setFont(font)
        self.num_dice_spin.setRange(1, 10)

        self.roll_button = QPushButton('Roll Dice')
        self.roll_button.setFont(font)
        self.roll_button.setStyleSheet("background-color: lightblue; color: black;")
        self.roll_button.clicked.connect(self.roll_dice)

        # Settings Button
        self.settings_button = QPushButton('Settings')
        self.settings_button.setFont(QFont('Courier', 10))
        self.settings_button.setStyleSheet("background-color: black; color: lime; padding: 2px;")
        self.settings_button.setFixedSize(80, 30)
        self.settings_button.clicked.connect(self.open_settings_dialog)

        # Image Button
        self.image_button = QPushButton('Image')
        self.image_button.setFont(QFont('Courier', 10))
        self.image_button.setStyleSheet("background-color: gray; color: white; padding: 2px;")
        self.image_button.setFixedSize(80, 30)
        self.image_button.clicked.connect(self.open_image_dialog)

        # Layouts
        roll_button_layout = QHBoxLayout()
        roll_button_layout.addWidget(self.roll_button)
        roll_button_layout.addWidget(self.settings_button)
        roll_button_layout.addWidget(self.image_button)

        health_mana_layout = QHBoxLayout()
        health_mana_layout.addWidget(self.health_label)
        health_mana_layout.addWidget(self.health_spin)
        health_mana_layout.addWidget(self.mana_label)
        health_mana_layout.addWidget(self.mana_spin)

        character_name_layout = QHBoxLayout()
        character_name_layout.addWidget(self.character_name_label)
        character_name_layout.addWidget(self.character_name_input)

        dice_layout = QHBoxLayout()
        dice_layout.addWidget(self.dice_label)
        dice_layout.addWidget(self.dice_combo)
        dice_layout.addWidget(self.num_dice_label)
        dice_layout.addWidget(self.num_dice_spin)

        # Main Layout
        main_layout = QVBoxLayout()
        main_layout.addLayout(roll_button_layout)
        main_layout.addLayout(character_name_layout)
        main_layout.addLayout(health_mana_layout)
        main_layout.addLayout(dice_layout)

        # Set central widget
        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

    def roll_dice(self):
        die_type = self.dice_combo.currentText()
        num_dice = self.num_dice_spin.value()
        max_value = int(die_type[1:])

        rolls = [random.randint(1, max_value) for _ in range(num_dice)]
        result_text = f'You rolled {num_dice} {die_type}(s):\n' + '\n'.join(map(str, rolls))

        # Creating a custom message box with a larger font and animation-like effect
        msg_box = QMessageBox(self)
        msg_box.setWindowTitle('Dice Roll Result')
        msg_box.setText(result_text)
        result_font = QFont()
        result_font.setPointSize(35)
        msg_box.setFont(result_font)
        msg_box.setStyleSheet("background-color: #2e2e2e; color: #ffffff;")
        msg_box.exec_()

    def open_image_dialog(self):
        options, _ = QFileDialog.getOpenFileName(self, 'Select Background Image', '', 'Images (*.png *.jpg *.jpeg *.bmp)')
        if options:
            pixmap = QPixmap(options)
            palette = QPalette()
            palette.setBrush(QPalette.Window, QBrush(pixmap))
            self.setPalette(palette)

    def open_settings_dialog(self):
        settings_dialog = QDialog(self)
        settings_dialog.setWindowTitle('Settings')
        settings_dialog.setGeometry(150, 150, 300, 200)
        layout = QVBoxLayout()

        # Placeholder options
        placeholder_label = QLabel('Placeholder Option 1')
        placeholder_label.setFont(QFont('Arial', 15))
        layout.addWidget(placeholder_label)

        placeholder_label2 = QLabel('Placeholder Option 2')
        placeholder_label2.setFont(QFont('Arial', 15))
        layout.addWidget(placeholder_label2)

        settings_dialog.setLayout(layout)
        settings_dialog.exec_()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    tracker = DnDTracker()
    tracker.show()
    sys.exit(app.exec_())
