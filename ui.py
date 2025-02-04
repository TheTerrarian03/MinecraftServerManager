import curses
import time

class MainMenu:
    def __init__(self, screen: curses.window):
        self.current_selection = 0
        self.screen = screen

        # screen dimensions
        self.screen_height = -1
        self.screen_width = -1

        # subwindows
        self.main_window = None
        self.playit_window = None
        self.server_window = None
        self.stat_window = None

        # temp vars for status
        self.playit_online = False
        self.server1_online = False
    
    def dimensions_changed(self):
        height, width = self.screen.getmaxyx()
        if self.screen_height != height or self.screen_width != width:
            return True
        return False

    def update_dimension(self):
        self.screen_height, self.screen_width = self.screen.getmaxyx()

    def update_window_dimensions(self):
        self.main_window = curses.newwin(19, 30, 0, 0)
        self.playit_window = curses.newwin(6, 36, 0, 30)
        self.server_window = curses.newwin(7, 36, 6, 30)
        self.stat_window = curses.newwin(9, 36, 13, 30)
    
    def draw_main(self):
        self.main_window.clear()
        self.main_window.border(0)

        self.main_window.addstr(2, 9, "[Services]")
        self.main_window.addstr(3, 5, "Manage A Server", curses.A_REVERSE if self.current_selection == 0 else curses.A_NORMAL)
        self.main_window.addstr(4, 5, "Manage Playit", curses.A_REVERSE if self.current_selection == 1 else curses.A_NORMAL)
        self.main_window.addstr(5, 5, "Manage Stop All", curses.A_REVERSE if self.current_selection == 2 else curses.A_NORMAL)
        self.main_window.addstr(6, 5, "Manage (Re)Start All", curses.A_REVERSE if self.current_selection == 3 else curses.A_NORMAL)

        self.main_window.addstr(8, 9, "[Config]")
        self.main_window.addstr(9, 5, "Save Config", curses.A_REVERSE if self.current_selection == 4 else curses.A_NORMAL)
        self.main_window.addstr(10, 5, "Load Config", curses.A_REVERSE if self.current_selection == 5 else curses.A_NORMAL)

        self.main_window.addstr(12, 9, "[System]")
        self.main_window.addstr(13, 5, "Write Services", curses.A_REVERSE if self.current_selection == 6 else curses.A_NORMAL)
        self.main_window.addstr(14, 5, "Auto-load Services", curses.A_REVERSE if self.current_selection == 7 else curses.A_NORMAL)

        self.main_window.addstr(16, 9, "Quit", curses.A_REVERSE if self.current_selection == 8 else curses.A_NORMAL)

        self.main_window.refresh()

    def draw_playit(self):
        self.playit_window.clear()
        self.playit_window.border(0)

        self.playit_window.addstr(2, 2, f"Playit.gg - {"Online" if self.playit_online else "Offline"}")
        self.playit_window.addstr(3, 2, "> writing-cir.gl.joinmc.link")

        self.playit_window.refresh()
    
    def draw_server(self):
        self.server_window.clear()
        self.server_window.border(0)

        self.server_window.addstr(2, 2, "\"Server 1\"")
        self.server_window.addstr(3, 2, "Port 25565")
        self.server_window.addstr(4, 2, "\"writing-cir.gl.joinmc.link\"")

        self.server_window.refresh()

    def draw_stats(self):
        self.stat_window.clear()
        self.stat_window.border(0)

        self.stat_window.addstr(2, 14, "[Memory]")
        self.stat_window.addstr(3, 4, "▓▓▓▓▓▓▓▓▒░░░░░░░░░░░░░░░░░░░")
        
        self.stat_window.addstr(5, 16, "[CPU]")
        self.stat_window.addstr(6, 4, "▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒░░░░░░░░")

        self.stat_window.refresh()

    def draw_and_handle(self):
        if self.dimensions_changed():
            self.update_dimension()
            self.update_window_dimensions()

        curses.curs_set(0)
        self.screen.timeout(100)  # Set a timeout for getch to avoid blocking

        while True:
            self.draw_main()  # Draw the main window
            self.draw_playit()
            self.draw_server()
            self.draw_stats()

            key = self.screen.getch()  # Non-blocking getch

            if key == curses.KEY_UP and self.current_selection > 0:
                self.current_selection -= 1
            elif key == curses.KEY_DOWN and self.current_selection < 8:  # Adjust based on your menu length
                self.current_selection += 1
            elif key == curses.KEY_ENTER or key in [10, 13]:
                match self.current_selection:
                    case 8: break
                    case 3: 
                        self.playit_online = True
                    case 2: 
                        self.playit_online = False
            elif key == ord('q'):  # Press 'q' to exit
                break