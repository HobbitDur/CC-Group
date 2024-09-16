import os

from PIL.ImageQt import ImageQt
from PyQt6.QtGui import QPixmap

from gamedata import GameData
from PIL import Image


class Card():
    TILES_WIDTH = 64
    TILES_WIDTH_EL = 128
    TILES_HEIGHT = 64
    TILES_HEIGHT_EL = 128

    def __init__(self, game_data: GameData, id: int, offset: int, data_hex: bytearray, remaster=False):
        self.offset = offset
        self.game_data = game_data
        self._name = ""
        self._id = id
        self.top_value = 0
        self.down_value = 0
        self.left_value = 0
        self.right_value = 0
        self._elem_int = 0
        self._elem_str = ""
        self.power_value = 0
        self._image = 0
        self.card_info = [x for x in self.game_data.card_data_json["card_info"] if x["id"] == self._id][0]
        self.card_el_info = {}
        self.__analyze_data(remaster, data_hex)

    def __str__(self):
        return f"n°{self._id} {self._name} T:{self.top_value} D:{self.down_value} L:{self.left_value} R:{self.right_value} Type:{self._elem_str} Power:{self.power_value}"

    def __repr__(self):
        return self.__str__()

    def __analyze_data(self, remaster, data_hex):
        self._name = self.card_info["name"]
        self.top_value = data_hex[0]
        self.down_value = data_hex[1]
        self.left_value = data_hex[2]
        self.right_value = data_hex[3]
        self._elem_int = data_hex[4]
        self.__set_elemental_str()
        self.power_value = data_hex[5]
        self.card_el_info = [x for x in self.game_data.card_data_json['card_type'] if x["id"] == self._elem_int][0]
        if remaster:
            self._image = self.card_info["img_remaster"]
        else:
            self._image = self.card_info["img"]

    def get_image(self):
        return self._image

    def get_name(self):
        return self._name

    def get_type_int(self):
        return self._elem_int

    def get_id(self):
        return self._id

    def __set_elemental_str(self):
        self._elem_str = [x["name"] for x in self.game_data.card_data_json["card_type"] if x["id"] == self._elem_int][0]

    def set_elemental(self, elem_id: int):
        self._elem_int = elem_id
        self.__set_elemental_str()

    def change_remaster_image(self, remaster):
        if remaster:
            self._image = self.card_info['img_remaster']
        else:
            self._image = self.card_info['img']
