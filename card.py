import os

from PIL.ImageQt import ImageQt
from PyQt6.QtGui import QPixmap

from gamedata import GameData
from PIL import Image


class Card():
    TILES_WIDTH = 64
    TILES_HEIGHT = 64

    def __init__(self, game_data: GameData, id: int, offset: int, data_hex: bytearray):
        self.offset = offset
        self.game_data = game_data
        self._data_hex = data_hex
        self._name = ""
        self._id = id
        self._top_value = 0
        self._down_value = 0
        self._left_value = 0
        self._right_value = 0
        self._type_int = 0
        self._type_str = ""
        self._power = 0
        self._image = 0
        print(self.game_data.card_data_json["card_info"])
        print(self._id)
        self.card_info = [x for x in self.game_data.card_data_json["card_info"] if x["id"] == self._id][0]
        self.__analyze_data()

    def __str__(self):
        return f"n°{self._id} {self._name} T:{self._top_value} D:{self._down_value} L:{self._left_value} R:{self._right_value} Type:{self._type_str} Power:{self._power}"

    def __repr__(self):
        return self.__str__()

    def __analyze_data(self):
        self._name = self.card_info["name"]
        self._top_value = self._data_hex[0]
        self._down_value = self._data_hex[1]
        self._left_value = self._data_hex[2]
        self._right_value = self._data_hex[3]
        self._type_value = self._data_hex[4]

        print(self._name)
        print(self._type_value)
        print(self._id)
        print(self.game_data.card_data_json["card_type"])
        print(self._type_value)
        self._type_str = [x["name"] for x in self.game_data.card_data_json["card_type"] if x["id"] == self._type_value][0]
        self._power = self._data_hex[5]

        self.__extract_tile()

    def get_top_value(self):
        return self._top_value

    def get_down_value(self):
        return self._down_value

    def get_left_value(self):
        return self._left_value

    def get_right_value(self):
        return self._right_value
    def get_image(self):
        return self._image

    def __extract_tile(self):
        # Open the image
        img = Image.open(os.path.join("Resources", "cards_00.png"))
        img_width, img_height = img.size

        # Calculate the number of tiles in both dimensions
        num_tiles_x = img_width // self.TILES_WIDTH
        num_tiles_y = img_height // self.TILES_HEIGHT
        tile_count = 0

        # Calculate the bounding box of the tile
        left = self.card_info["img_x"] * self.TILES_WIDTH
        upper = self.card_info["img_y"] * self.TILES_HEIGHT
        right = left + self.TILES_WIDTH
        lower = upper + self.TILES_HEIGHT
        # Extract the tile using cropping
        tile = img.crop((left, upper, right, lower))
        self._image = QPixmap.fromImage(ImageQt(tile))
        print(self._image)
