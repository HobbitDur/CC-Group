import os

from PyQt6.QtCore import QSize
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QScrollArea, QFileDialog, QPushButton, QHBoxLayout

from card import Card
from cardwidget import CardWidget
from gamedata import GameData


class CCGroupWidget(QWidget):

    def __init__(self, icon_path='Resources'):
        QWidget.__init__(self)

        # Window management
        self.window_layout = QVBoxLayout()
        self.setLayout(self.window_layout)
        self.scroll_widget = QWidget()
        self.scroll_area = QScrollArea()
        self.window_layout.addWidget(self.scroll_area)
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setWidget(self.scroll_widget)
        self.__layout_main = QVBoxLayout()
        self.scroll_widget.setLayout(self.__layout_main)
        self.setWindowTitle("CC Group")
        self.setMinimumSize(1080, 720)
        self.setWindowIcon(QIcon(os.path.join(icon_path, 'icon.ico')))


        self.file_dialog = QFileDialog()
        self.file_dialog_button = QPushButton()
        self.file_dialog_button.setIcon(QIcon(os.path.join(icon_path, 'folder.png')))
        self.file_dialog_button.setIconSize(QSize(30, 30))
        self.file_dialog_button.setFixedSize(40, 40)
        self.file_dialog_button.setToolTip("Open data file")
        self.file_dialog_button.clicked.connect(self.__load_file)


        self.layout_top = QHBoxLayout()
        self.layout_top.addWidget(self.file_dialog_button)

        self.current_file_data = bytearray()
        self.game_data = GameData()
        self.game_data.load_card_data(os.path.join("Resources", "card.txt"))
        self.game_data.load_card_type_data(os.path.join("Resources", "card_type.txt"))
        self.game_data.load_card_json_data(os.path.join("Resources", "card.json"))

        #self.layout_main.addLayout(self.layout_top)
        #self.layout_main.addLayout(self.layout_translation_lines)
        #self.layout_main.addStretch(1)
        self.__card_widget_list = []
        self.init()

    def init(self):
        self.__load_file()

    def __load_file(self, file_to_load: str = ""):
        file_to_load = os.path.join("OriginalFiles", "FF8_EN.exe")  # For developing faster
        print(f"File to load: {file_to_load}")
        if not file_to_load:
            file_to_load = self.file_dialog.getOpenFileName(parent=self, caption="Find file", filter="*",
                                                            directory=os.getcwd())[0]
        if file_to_load:
            self.file_loaded = file_to_load

        with open(self.file_loaded, "rb") as in_file:
            while el := in_file.read(1):
                self.current_file_data.extend(el)

        card_data_size = 8
        nb_card = 109
        general_offset = 0x400000
        menu_offset = 0x796508
        minigame_offset = 0x874D00
        list_card = []
        id = 0
        for card_data_index in range(menu_offset, menu_offset+nb_card*card_data_size, card_data_size):
            new_card = Card(self.game_data, id, menu_offset+card_data_index, self.current_file_data[card_data_index: card_data_index+card_data_size])
            list_card.append(new_card)
            id +=1

        for card in list_card:
            self.__card_widget_list.append(CardWidget(card))
            self.__layout_main.addWidget(self.__card_widget_list[-1])





