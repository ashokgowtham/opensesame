import sublime, sublime_plugin
sidebarVisible = True
class SideBarNavigator(sublime_plugin.EventListener):
    def on_activated(self, view):
        window = sublime.active_window()
        global sidebarVisible
        if sidebarVisible:
            window.run_command('reveal_in_side_bar')

    def on_window_command(self, window, command_name, args):
        if command_name == "toggle_side_bar":
            global sidebarVisible
            sidebarVisible = not sidebarVisible