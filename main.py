from src.settings import *
from src.Game import Game
from src.Menu import MainMenu, IngameMenu, OptionMenu, NameMenu

BASE_DIR = os.path.dirname(__file__)


class MainApp:
    def __init__(self) -> None:
        pg.init()
        self.screen = pg.display.set_mode((DISPLAY_W, DISPLAY_H))
        pg.display.set_caption(f"{APP_CONFIG['name']} - PyGame")
        self.load_files()
        self.manager = gui.UIManager((DISPLAY_W, DISPLAY_H), os.path.abspath(os.curdir)+"\\config\\theme.json")
        self.player1 = None
        self.player2 = None
        
        self.menu = MainMenu(self.manager)
        self.option_menu = OptionMenu(self.manager)
        self.name_menu = None
        self.ingame_menu = None
        
        self.game = Game()
        self.clock = pg.time.Clock()

    def load_files(self):
        self.bg_img = pg.image.load(
            os.path.join(BASE_DIR + "\\assets\\img\\", "bg.jpg")
        ).convert_alpha()
        self.bg_img = pg.transform.scale(self.bg_img, (DISPLAY_W, DISPLAY_H))

    def setup_players(self, p1name, p2name):
        self.player1 = Player(p1name, Colors.Red)
        self.player2 = Player(p2name, Colors.Yellow)

    def draw_board(self):
        # Draw default black
        for c in range(COLUMN_COUNT):
            for r in range(ROW_COUNT):
                pg.draw.rect(self.screen, Colors.Blue, (c * SQUARESIZE, r * SQUARESIZE + SQUARESIZE, SQUARESIZE, SQUARESIZE))        
                pg.draw.circle(self.screen, Colors.Transparent, (int(c * SQUARESIZE + SQUARESIZE / 2), int(r * SQUARESIZE + SQUARESIZE + SQUARESIZE/2)), CIRCLERADIUS)
        
        # Draw Player chips
        for c in range(COLUMN_COUNT):
            for r in range(ROW_COUNT):
                if self.game.board[r][c] == 1:
                    pg.draw.circle(self.screen, self.player1.color, (int(c * SQUARESIZE + SQUARESIZE / 2), DISPLAY_H+ SQUARESIZE - int(r * SQUARESIZE + SQUARESIZE + SQUARESIZE/2) -1), CIRCLERADIUS)
                elif self.game.board[r][c] == 2:
                    pg.draw.circle(self.screen, self.player2.color, (int(c * SQUARESIZE + SQUARESIZE / 2), DISPLAY_H +SQUARESIZE   - int(r * SQUARESIZE + SQUARESIZE + SQUARESIZE/2)-1), CIRCLERADIUS)

    def draw_game(self):
        # self.screen.fill(Colors.DarkGrey)
        self.screen.blit(self.bg_img, (0, 0))
        self.screen.fill(Colors.DarkGrey, rect=(0, 0, *MENU_RES))
        self.draw_board()

    def play_game(self):
        self.game.reset_game()
        self.ingame_menu = IngameMenu(self.manager, self.player1, self.player2)
        posx = None
        self.ingame_menu.create_menu()
        while not self.game.gameover:
            time_delta = self.clock.tick(APP_CONFIG['FPS']) / 1000.0
            self.draw_game()
            

            if posx: 
                # show move preview
                if self.game.turn == PLAYER:      
                    pg.draw.circle(self.screen, self.player1.color, (posx, int(SQUARESIZE/2 +SQUARESIZE)), CIRCLERADIUS)
                else:
                    pg.draw.circle(self.screen, self.player2.color, (posx, int(SQUARESIZE/2 +SQUARESIZE)), CIRCLERADIUS)

            for e in pg.event.get():
                if e.type == pg.QUIT:
                    self.game.gameover = True
                    pg.quit()
                    sys.exit()
                elif (e.type == pg.KEYUP and e.key == pg.K_ESCAPE):
                    self.game.gameover = True
                    self.show_mainmenu()
                
                if e.type == pg.MOUSEMOTION:
                    posx = e.pos[0]
                # handle clicks
                elif e.type == pg.MOUSEBUTTONDOWN:
                    posx = e.pos[0]
                    col = math.floor(posx/SQUARESIZE)
                    if self.game.turn == PLAYER:
                        if self.game.is_valid_location(self.game.board, col):
                            row = self.game.get_next_open_row(self.game.board, col)
                            self.game.drop_piece(self.game.board, row, col, 1)
                            self.draw_board()
                            self.manager.draw_ui(self.screen)
                            pg.display.flip()
                            if self.game.winning_move(self.game.board, 1):
                                print("[!] Player 1 Wins!")
                                self.player1.score += 1
                                time.sleep(2)
                                self.game.gameover = True
                                self.play_game()
                        else:
                            continue
                    elif self.game.turn == 1:
                        if self.game.is_valid_location(self.game.board, col):
                            row = self.game.get_next_open_row(self.game.board, col)
                            self.game.drop_piece(self.game.board, row, col, 2)
                            self.draw_board()
                            self.manager.draw_ui(self.screen)
                            pg.display.flip()

                            if self.game.winning_move(self.game.board, 2):
                                print("[!] Player 2 Wins!")
                                self.player2.score += 1
                                time.sleep(2)
                                self.game.gameover = True
                                self.play_game()
                        else:
                            continue

                    self.manager.process_events(e)
                    self.game.turn += 1
                    self.game.turn = self.game.turn % 2

                    self.game.print_board(self.game.board)

                    self.ingame_menu.update(self.game.turn)
         
            
            self.manager.update(time_delta)           
            self.manager.draw_ui(self.screen)

            self.clock.tick(APP_CONFIG['FPS'])
            pg.display.update()
    
    def show_namemenu(self):
        on_menu = True
        self.name_menu = NameMenu(self.manager)
        self.name_menu.create_menu()
        while on_menu:
            time_delta = self.clock.tick(APP_CONFIG['FPS']) / 1000.0

            for e in pg.event.get():
                if e.type == pg.QUIT:
                    on_menu = False
                    pg.quit()
                    sys.exit()
                elif e.type == pg.KEYUP and e.key == pg.K_ESCAPE:
                    on_menu = False
                    self.show_mainmenu()

                if e.type == gui.UI_BUTTON_PRESSED:
                    if e.ui_element == self.name_menu.set_name_btn:
                        p1 = self.name_menu.p1_name_input.text
                        p2 = self.name_menu.p2_name_input.text
                        if p1 == "" or p2 == "":
                            print("[x] Namen nicht gesetzt")
                            continue
                        else:
                            on_menu = False
                            self.setup_players(p1, p2)
                            self.play_game()
                    if e.ui_element == self.name_menu.exit_name_btn:
                        on_menu = False
                        self.show_mainmenu()
                        

                self.manager.process_events(e)


            self.screen.blit(self.bg_img, (0, 0))
            #self.screen.fill(Colors.White, rect=(0, 0, *MENU_RES))
            self.manager.draw_ui(self.screen)
            
            self.manager.update(time_delta)
            self.clock.tick(APP_CONFIG['FPS'])
            pg.display.update()

    def show_mainmenu(self):
        on_menu = True
        self.menu.create_menu()
        while on_menu:
            time_delta = self.clock.tick(APP_CONFIG['FPS']) / 1000.0

            for e in pg.event.get():
                if e.type == pg.QUIT:
                    on_menu = False
                    pg.quit()
                    sys.exit()
                elif e.type == pg.KEYUP and e.key == pg.K_ESCAPE:
                    on_menu = False
                    pg.quit()

                # Button events
                elif e.type == gui.UI_BUTTON_PRESSED:
                    if e.ui_element == self.menu.exit_btn:
                        on_menu = False
                        pg.quit()
                    if e.ui_element == self.menu.play_btn:
                        on_menu = False
                        self.show_namemenu()
                    if e.ui_element == self.menu.option_btn:
                        print("[!] Option button clicked.")
                        on_menu = False
                        self.show_options()
                self.manager.process_events(e)
            
            self.screen.blit(self.bg_img, (0, 0))
            #self.screen.fill(Colors.White, rect=(0, 0, *MENU_RES))
            self.manager.draw_ui(self.screen)
            
            self.manager.update(time_delta)
            self.clock.tick(APP_CONFIG['FPS'])
            pg.display.update()

    def show_options(self):
        on_option = True
        self.option_menu.create_menu()
        while on_option:
            time_delta = self.clock.tick(APP_CONFIG['FPS']) / 1000.0

            for e in pg.event.get():
                if e.type == pg.QUIT or (e.type == pg.KEYUP and e.key == pg.K_ESCAPE):
                    on_option = False
                    self.show_mainmenu()

                self.manager.process_events(e)
            
            self.screen.blit(self.bg_img, (0, 0))
            #self.screen.fill(Colors.White, rect=(0, 0, *MENU_RES))
            self.manager.draw_ui(self.screen)
            
            self.manager.update(time_delta)
            self.clock.tick(APP_CONFIG['FPS'])
            pg.display.update()

if __name__ == "__main__":
    print("\n[!] Starting Game...")
    APP_CONFIG = load_config()
    app = MainApp()
    try:
        app.show_mainmenu()
    except KeyboardInterrupt:
        print("\n[!] User keyboard exit")
    except Exception as e:
        print("[x] Error:", e)
    finally:
        print("[!] Exit Game")
        sys.exit(0)