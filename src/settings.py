import os, yaml, shutil, time, sys, math
from yaml import Loader, Dumper
import numpy as np
import pygame as pg
import pygame_gui as gui
from dataclasses import dataclass

ROW_COUNT = 6
COLUMN_COUNT = 7
SQUARESIZE = 100
DISPLAY_W, DISPLAY_H = COLUMN_COUNT * SQUARESIZE,  (ROW_COUNT + 1) * SQUARESIZE 
MENU_W, MENU_H = DISPLAY_W, DISPLAY_H + 100

MENU_RES = DISPLAY_W , 100
APP_CONFIG = dict()
CIRCLERADIUS = int(SQUARESIZE/2 - 5)
PLAYER = 0 
AI = 1

class Colors:
    Blue = (0, 0, 255)
    Red = (255, 0, 0)
    Green = (0, 255, 0)
    Black = (0, 0, 0)
    White = (255, 255, 255)
    Yellow = (255, 255, 0)
    DarkGrey = (36, 36, 36)
    Transparent = pg.Color(0,0,0,0)
    Orange = pg.Color(227, 178, 2, 255)


@dataclass
class Player:
    name: str = "Player X"
    color: Colors = Colors.Red
    score: int = 0


def load_config() -> dict:
    new_config = dict()
    with open(os.path.abspath(os.curdir)+"\\config\\config.yml", 'r') as f:
        content = yaml.load(f, Loader=Loader)
        for k, v in content.items():
            new_config[k] = v
    return new_config

def save_config(config):
    with open(os.path.abspath(os.curdir)+"\\config\\config.yml", 'w') as f:
        yaml.dump(config, f, Dumper=Dumper)

def create_board() -> np.ndarray:
    board = np.zeros((ROW_COUNT,COLUMN_COUNT))
    return board

