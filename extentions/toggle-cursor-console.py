import sublime
import sublime_plugin

# file : Default (Windows).sublime-keymap
# { "keys": ["ù"] , "command" : "is_console_open" }

cursor_in_console = False

class is_console_open( sublime_plugin.WindowCommand ):
	def run(self):
		global cursor_in_console
		view = self.window.active_view()
		panel = self.window.active_panel()
		is_console_open = (panel == "console")
		# print( "is_console_open" , is_console_open )
		# print( "cursor_in_console", cursor_in_console )
		if not is_console_open:
			print( "open console for the first time" )
			self.window.run_command( "show_panel" , { "panel": "console" } )
			cursor_in_console = True
			return
		# active_view = self.window.active_view()
		# console_view = self.window.find_output_panel("console")
		if cursor_in_console:
			print("focus_group")
			self.window.run_command( "focus_group", { "group": 0 } )
			cursor_in_console = False
		else:
			print("focus console")
			self.window.run_command( "show_panel", { "panel": "console" } )
			cursor_in_console = True

# in console :
# >> sublime.run_command("demo_sublime_app")
class demo_sublime_app( sublime_plugin.ApplicationCommand ):
	def run(self):
		print("hello")
