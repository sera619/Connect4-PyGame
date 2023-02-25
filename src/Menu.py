from src.settings import *


class MainMenu:
    def __init__(self, manager: gui.UIManager) -> None:
        self.manager = manager
        self.play_btn = None
        self.option_btn = None
        self.exit_btn = None
        self.header_text = None
        self.version_text = None
    
    def clear_screen(self):
        self.manager.clear_and_reset()

    def create_menu(self):
        self.clear_screen()
        self.play_btn = None
        self.option_btn = None
        self.exit_btn = None
        self.header_text = None
        self.version_text = None
        self.header_text = gui.elements.UILabel(
            relative_rect=pg.Rect(
                (DISPLAY_W * 0.50) - 400, (DISPLAY_H * 0.15) - 25, 800, 100
            ),
            text="Connect 4",
            manager=self.manager,
        )

        self.play_btn = gui.elements.UIButton(
            relative_rect=pg.Rect(
                ((DISPLAY_W // 2) - 150,( DISPLAY_H * .5)- 40),
                (300, 80)),
            text="Start Game",
            manager=self.manager
            )

        self.option_btn = gui.elements.UIButton(
            relative_rect=pg.Rect(
                ((DISPLAY_W // 2) - 150,( DISPLAY_H * .65)- 40),
                (300, 80)),
            text="Options",
            manager=self.manager
            )

        self.exit_btn = gui.elements.UIButton(
            relative_rect=pg.Rect(
                ((DISPLAY_W // 2) - 150,( DISPLAY_H * .8)- 40),
                (300, 80)),
            text="Exit",
            manager=self.manager
            )

        self.version_text = gui.elements.UILabel(
            relative_rect=pg.Rect(
                ((DISPLAY_W // 2)- 300, (DISPLAY_H * .95) - 50),
            (600, 100)),
            text="Versiontext",
            manager=self.manager,
            object_id=gui.core.ObjectID("#versionlabel"),
            )

class NameMenu:
    def __init__(self, manager: gui.UIManager) -> None:
        self.manager = manager
        self.p1_name_input = None
        self.p2_name_input = None
        self.set_name_btn = None        
        self.namemenu_header = None

    def create_menu(self):
        self.manager.clear_and_reset()
        self.namemenu_header = gui.elements.UILabel(
            relative_rect=pg.Rect(
                (DISPLAY_W * 0.50) - 400, (DISPLAY_H * 0.15) - 50, 800, 100
            ),
            text="New Game",
            manager=self.manager,
            object_id=gui.core.ObjectID('#subtitlelabel')
        )

        self.p1_name_input = gui.elements.UITextEntryLine(
            relative_rect=pg.Rect(
                (DISPLAY_W * 0.5) - 200, (DISPLAY_H * 0.425) - 50, 400, 80
            ),
            placeholder_text="Enter Player 1 Name...",
            manager=self.manager,
        )

        self.p2_name_input = gui.elements.UITextEntryLine(
            relative_rect=pg.Rect(
                (DISPLAY_W * 0.50) - 200, (DISPLAY_H * 0.575) - 50, 400, 80
            ),
            placeholder_text="Enter Player 2 Name...",
            manager=self.manager,
        )

        self.set_name_btn = gui.elements.UIButton(
            relative_rect=pg.Rect(
                ((DISPLAY_W // 3) - 100,( DISPLAY_H * .8)- 40),
                (200, 80)),
            text="Start",
            manager=self.manager
            )

        self.exit_name_btn = gui.elements.UIButton(
            relative_rect=pg.Rect(
                ((DISPLAY_W) - 350,( DISPLAY_H * .8)- 40),
                (200, 80)),
            text="Exit",
            manager=self.manager
            )
    
class OptionMenu:
    def __init__(self, manager: gui.UIManager) -> None:
        self.manager = manager
        self.option_header = None
        self.option1_label = None
        self.option2_label = None
        self.option3_label = None
        self.version_label = None

    def create_menu(self):
        self.manager.clear_and_reset()
        self.option_header = gui.elements.UILabel(
            relative_rect=pg.Rect(
                (DISPLAY_W * 0.50) - 400, (DISPLAY_H * 0.15) - 50, 800, 100
            ),
            text="Options",
            manager=self.manager,
            object_id=gui.core.ObjectID('#subtitlelabel')
        )

        # self.option1_label = gui.elements.UILabel(
        #     relative_rect=pg.Rect(

        #     )
        # )
        # self.option2_label = None
        # self.option3_label = None
        self.version_text = gui.elements.UILabel(
            relative_rect=pg.Rect(
                ((DISPLAY_W // 2)- 300, (DISPLAY_H * .95) - 50),
            (600, 100)),
            text="Versiontext",
            manager=self.manager,
            object_id=gui.core.ObjectID("#versionlabel"),
            )
 
class IngameMenu:
    def __init__(self, manager: gui.UIManager, p1: Player, p2: Player) -> None:
        self.manager = manager
        self.p1 = p1
        self.p2 = p2
        self.player1name_label = None
        self.player2name_label = None
        self.player1score_label = None
        self.player2score_label= None

    def update(self, turn):
        self.manager.clear_and_reset()
        self.player1name_label = None
        self.player2name_label = None
        if turn == 0:
            self.player1name_label = gui.elements.UILabel(
                relative_rect=pg.Rect(
                    ((DISPLAY_W * 0.25) - 150, (DISPLAY_H * 0.025) - 50, 
                    300, 100)
                ),
                text=f"{self.p1.name}",
                manager=self.manager,
                object_id=gui.core.ObjectID('#activeplayerlabel')
            )

            self.player2name_label = gui.elements.UILabel(
                relative_rect=pg.Rect(
                    ((DISPLAY_W * 0.25) - 150, (DISPLAY_H * 0.075) - 50, 
                    300, 100)
                ),
                text=f"{self.p2.name}",
                manager=self.manager,
                object_id=gui.core.ObjectID('#scoreitemlabel')
            )

        elif turn == 1:
            self.player1name_label = gui.elements.UILabel(
                relative_rect=pg.Rect(
                    ((DISPLAY_W * 0.25) - 150, (DISPLAY_H * 0.025) - 50,
                     300, 100)
                ),
                text=f"{self.p1.name}",
                manager=self.manager,
                object_id=gui.core.ObjectID('#scoreitemlabel')
            )

            self.player2name_label = gui.elements.UILabel(
                relative_rect=pg.Rect(
                    ((DISPLAY_W * 0.25) - 150, (DISPLAY_H * 0.075) - 50,
                     300, 100)
                ),
                text=f"{self.p2.name}",
                manager=self.manager,
                object_id=gui.core.ObjectID('#activeplayerlabel')

            )
        self.player1score_label = gui.elements.UILabel(
            relative_rect=pg.Rect(
                ((DISPLAY_W * 0.525) - 150, (DISPLAY_H * 0.025) - 50,
                300, 100)
            ),
            text=f"Score: {self.p1.score}",
            manager=self.manager,
            object_id=gui.core.ObjectID('#scoreitemlabel')
        )

        self.player2score_label = gui.elements.UILabel(
            relative_rect=pg.Rect(
                ((DISPLAY_W * 0.525) - 150, (DISPLAY_H * 0.075) - 50,
                 300, 100)
            ),
            text=f"Score: {self.p2.score}",
            manager=self.manager,
            object_id=gui.core.ObjectID('#scoreitemlabel')

        )


    def create_menu(self):
        self.manager.clear_and_reset()
        self.player1name_label = None
        self.player2name_label = None
        self.player1score_label = None
        self.player2score_label= None
        self.player1name_label = gui.elements.UILabel(
            relative_rect=pg.Rect(
                (DISPLAY_W * 0.25) - 150, (DISPLAY_H * 0.025) - 50, 300, 100
            ),
            text=f"{self.p1.name}",
            manager=self.manager,
            object_id=gui.core.ObjectID('#activeplayerlabel')
        )

        self.player2name_label = gui.elements.UILabel(
            relative_rect=pg.Rect(
                (DISPLAY_W * 0.25) - 150, (DISPLAY_H * 0.075) - 50, 300, 100
            ),
            text=f"{self.p2.name}",
            manager=self.manager,
            object_id=gui.core.ObjectID('#scoreitemlabel')
        )

        self.player1score_label = gui.elements.UILabel(
            relative_rect=pg.Rect(
                (DISPLAY_W * 0.525) - 150, (DISPLAY_H * 0.025) - 50, 300, 100
            ),
            text=f"Score: {self.p1.score}",
            manager=self.manager,
            object_id=gui.core.ObjectID('#scoreitemlabel')
        )

        self.player2score_label = gui.elements.UILabel(
            relative_rect=pg.Rect(
                (DISPLAY_W * 0.525) - 150, (DISPLAY_H * 0.075) - 50, 300, 100
            ),
            text=f"Score: {self.p2.score}",
            manager=self.manager,
            object_id=gui.core.ObjectID('#scoreitemlabel')

        )



