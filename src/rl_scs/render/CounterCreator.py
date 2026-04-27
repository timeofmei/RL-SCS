from ..utils.package_utils import get_package_root
from .Color import Color
from .fonts import FONT_SANS
import pygame

class CounterCreator:

    def __init__(self):
        self.package_root = get_package_root()
        return
    
    def create_counter_from_scratch(self, image_name, unit_stats, unit_type, color_str=None, color_rgb=None):
        #pygame.init()

        if color_rgb is not None:
            image_color = color_rgb
        elif color_str is not None:
            image_color = Color.str_to_rgb(color_str)
        else:
            print("You must either give a color_str(\"blue\") or color_rgb((50,23,246)) argument.\nExiting")
            exit()

        image_path = str(self.package_root / "assets" / f"{image_name}.jpg")        

        #### BACKGROUND ####
        unit_image = pygame.Surface((800, 800))
        unit_image.fill(image_color)


        #### SYMBOL ####
        unit_symbol_position = (220, 150)
        unit_symbol_dimensions = (360, 200)

        unit_symbol_rect = pygame.draw.rect(
            unit_image,
            Color.BLACK.rgb(),
            [unit_symbol_position, unit_symbol_dimensions],
            16
        )
        symbol_center = unit_symbol_rect.center

        match unit_type:
            case "infantary":
                line_thickness = 8
                margin = line_thickness // 2

                top_left = (unit_symbol_rect.topleft[0]+margin, unit_symbol_rect.topleft[1]+margin)
                top_right = (unit_symbol_rect.topright[0]-margin, unit_symbol_rect.topright[1]+margin)
                bottom_left = (unit_symbol_rect.bottomleft[0]+margin, unit_symbol_rect.bottomleft[1]-margin)
                bottom_right = (unit_symbol_rect.bottomright[0]-margin, unit_symbol_rect.bottomright[1]-margin)
                # We needed to make the lines shorter by a certain margin so that they dont overflow outside the rectangle
                pygame.draw.line(unit_image, Color.BLACK.rgb(), top_left, bottom_right, line_thickness)
                pygame.draw.line(unit_image, Color.BLACK.rgb(), top_right, bottom_left, line_thickness)

            case "mechanized":
                line_thickness = 8
                elipse_dims = ( unit_symbol_dimensions[0]*0.6, unit_symbol_dimensions[1]*0.6)
                elipse_rect = pygame.Rect((0,0), elipse_dims)
                elipse_rect.center = symbol_center
                pygame.draw.ellipse(unit_image, Color.BLACK.rgb(), elipse_rect, line_thickness)

            case _:
                print("Unregonized type.\nExiting")
                exit()


        #### STATS ####
        unit_stats_position = (140, 450)
        unit_stats_dimensions = (520, 220)

        (attack, defense, movement) = unit_stats

        stats_area_rect = pygame.draw.rect(unit_image, Color.YELLOW.rgb(), [unit_stats_position, unit_stats_dimensions])
        stats_area_w = stats_area_rect.width
        stats_area_h = stats_area_rect.height

        stats_text = str(attack) + " - "  + str(defense) + " - "  + str(movement)
        stats_font = pygame.font.SysFont(FONT_SANS, 200)
        stats_surface = stats_font.render(stats_text, True, Color.BLACK.rgb())
        stats_surface = pygame.transform.scale(stats_surface, (0.75*stats_area_w, 1.1*stats_area_h))
        stats_rect = stats_surface.get_rect(center=stats_area_rect.center)
        stats_rect.y += 30
        unit_image.blit(stats_surface, stats_rect)     
    
        pygame.image.save(unit_image, image_path)
        #pygame.quit()
        return image_path
    
    def create_counter_from_base_image(self, image_name, base_unit_choice, unit_stats):
        #pygame.init()
        
        green_image_path = str(self.package_root / "assets" / "base_images" / "green_unit.jpg")
        red_image_path = str(self.package_root / "assets" / "base_images" / "red_unit.jpg")
        blue_image_path = str(self.package_root / "assets" / "base_images" / "blue_unit.jpg")

        (attack, defense, movement) = unit_stats

        match base_unit_choice:
            case "green":
                raw_image_path = green_image_path
                rectangle_position = (48, 338)
                rectangle_dims = (540, 225)
            case "red":
                raw_image_path = red_image_path
                rectangle_position = (45, 365)
                rectangle_dims = (584, 244)
            case "blue":
                print("blue base image not implemented yet.")
                raw_image_path = red_image_path
                rectangle_position = (45, 365)
                rectangle_dims = (584, 244)

            case _:
                print("Unknown image choice.\nExiting")
                exit()
            

        raw_image = pygame.image.load(raw_image_path)
        (width, height) = raw_image.get_size()

        stats_area_rect = pygame.draw.rect(raw_image, Color.YELLOW.rgb(), [rectangle_position, rectangle_dims])
        stats_area_w = stats_area_rect.width
        stats_area_h = stats_area_rect.height

        stats_text = str(attack) + " - "  + str(defense) + " - "  + str(movement)
        stats_font = pygame.font.SysFont(FONT_SANS, 200)
        stats_surface = stats_font.render(stats_text, True, Color.BLACK.rgb())
        stats_surface = pygame.transform.scale(stats_surface, (0.75*stats_area_w, 1.1*stats_area_h))
        stats_rect = stats_surface.get_rect(center=stats_area_rect.center)
        stats_rect.y += 30
        raw_image.blit(stats_surface, stats_rect)
        
        final_image = raw_image.copy()
        image_path = str(self.package_root / "assets" / f"{image_name}.jpg")
        pygame.image.save(final_image, image_path)  
        #pygame.quit()
        return image_path

    def add_border(self, color_str, source_path, dest_path=""):
        #pygame.init()
        border_color = Color.str_to_rgb(color_str)

        if dest_path == "":
            dest_path = source_path

        final_image = pygame.image.load(source_path)

        (width, height) = final_image.get_size()
        border_thickness = int(0.04 * height)
        pygame.draw.rect(final_image, border_color, [0, 0, width, height], border_thickness)

        pygame.image.save(final_image, dest_path) 
        #pygame.quit()
        return dest_path
