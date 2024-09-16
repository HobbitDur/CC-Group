import os

from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QSpinBox, QLabel, QHBoxLayout

from card import Card
from PIL import Image


class CardWidget(QWidget):

    def __init__(self, card: Card):
        QWidget.__init__(self)
        self.card = card
        self.__main_layout = QHBoxLayout()
        self.setLayout(self.__main_layout)

        self.__left_value_widget = QSpinBox()
        self.__left_value_widget.setValue(self.card.get_left_value())
        self.__right_value_widget = QSpinBox()
        self.__right_value_widget.setValue(self.card.get_right_value())
        self.__down_value_widget = QSpinBox()
        self.__down_value_widget.setValue(self.card.get_down_value())
        self.__top_value_widget = QSpinBox()
        self.__top_value_widget.setValue(self.card.get_top_value())

        self.__card_image_location_drawer = QLabel()
        self.__card_image_location_drawer.setPixmap(self.card.get_image())

        self.__left_layout = QVBoxLayout()
        self.__middle_layout = QVBoxLayout()
        self.__right_layout = QVBoxLayout()
        self.__text_layout = QVBoxLayout()
        self.__main_layout.addLayout(self.__left_layout)
        self.__main_layout.addLayout(self.__middle_layout)
        self.__main_layout.addLayout(self.__right_layout)
        self.__main_layout.addLayout(self.__text_layout)
        self.__main_layout.addStretch(1)

        self.__left_layout.addStretch(1)
        self.__left_layout.addWidget(self.__left_value_widget)
        self.__left_layout.addStretch(1)

        self.__middle_layout.addStretch(1)
        self.__middle_layout.addWidget(self.__top_value_widget)
        self.__middle_layout.addWidget(self.__card_image_location_drawer)
        self.__middle_layout.addWidget(self.__down_value_widget)
        self.__middle_layout.addStretch(1)

        self.__right_layout.addStretch(1)
        self.__right_layout.addWidget(self.__right_value_widget)
        self.__right_layout.addStretch(1)
