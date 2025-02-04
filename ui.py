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
        self.server_windows = None
        self.stat_window = None
    
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
        self.server_windows = curses.newwin(7, 36, 7, 30)
        self.stat_window = curses.newwin(9, 36, 15, 30)
    
    def draw_main(self):
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

    def draw_and_handle(self):
        if self.dimensions_changed():
            self.update_dimension()
            self.update_window_dimensions()

        curses.curs_set(0)
        self.screen.timeout(100)  # Set a timeout for getch to avoid blocking

        while True:
            self.draw_main()  # Draw the main window

            key = self.screen.getch()  # Non-blocking getch

            if key == curses.KEY_UP and self.current_selection > 0:
                self.current_selection -= 1
            elif key == curses.KEY_DOWN and self.current_selection < 8:  # Adjust based on your menu length
                self.current_selection += 1
            elif key == curses.KEY_ENTER or key in [10, 13]:
                if self.current_selection == 8: break
            elif key == ord('q'):  # Press 'q' to exit
                break