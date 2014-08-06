import sublime, sublime_plugin
from .common import *

class SideBarNavigator(sublime_plugin.EventListener):
    def on_activated(self, view):
        window = sublime.active_window()
        window.run_command('reveal_in_side_bar')