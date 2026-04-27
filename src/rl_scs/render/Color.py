from enum import Enum

class Color(Enum):
    WHITE = (255, 255, 255)
    BAD_PINK = (255, 0, 255)
    YELLOW = (245, 200, 0)
    ORANGE = (200, 100, 0)
    RED = (200, 0, 0)
    DARK_RED = (90, 10, 25)
    BROWN = (90, 50, 0)
    DARK_GREEN = (60, 80, 40)
    GREEN = (45, 120, 5)
    LIGHT_BLUE = (40, 110, 230)
    BLUE = (0, 40, 90)
    BLACK = (0, 0, 0)
    LIGHT_BROWN = (143, 100, 46)

    def rgb(self):
        return self.value

    @staticmethod
    def str_to_rgb(color_str: str):
        # There must be a better way of doing this
        match color_str:
            case "green":
                rgb = Color.GREEN.rgb()
            case "dark_green":
                rgb = Color.DARK_GREEN.rgb()
            case "red":
                rgb = Color.RED.rgb()
            case "dark_red":
                rgb = Color.DARK_RED.rgb()
            case "blue":
                rgb = Color.BLUE.rgb()
            case "black":
                rgb = Color.BLACK.rgb()
            case "light_blue":
                rgb = Color.LIGHT_BLUE.rgb()
            case _:
                print("Unknown color choice.\nExiting")
                exit()

        return rgb