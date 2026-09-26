import sublime
import sublime_plugin

panel_array = [ "find" , "find_in_files" , "replace", "console" ]

panel_active = False

demo_active = False

console_active = False

demo_counter = 0

last = ""

"""

  // Default (Windows).sublime-keymap

	{
		"keys": ["alt+1"],
		"command": "demo"
	},

	{
		"keys": ["ctrl+f"],
		"command": "show_panel",
		"args": {
			"panel": "find",
			"toggle": true,
			"regex" : false
		},
	},

	{
		"keys": ["alt+2"],
		"command": "show_panel",
		"args": {
			"panel": "find",
			"in_selection": true,
			// "regex": false,
			"toggle": true,
		}
	},

	/*{
		"keys": ["alt+1"],
		"command": "show_panel",
		"args": {
			"panel": "find_in_files",
			"regex": true,
			"toggle": true,
		}
	},*/

"""

class demo( sublime_plugin.WindowCommand ):
	def run(self,start=None):
		global demo_active
		global panel_active
		global demo_counter
		demo_counter += 1
		# print( 0 )
		# print( "WindowCommand" )
		if panel_active == False and demo_active == False and console_active == False :
			demo_active = True
			panel_active = True
			sublime.active_window().run_command( "show_panel",
			{
				"panel": "find",
				"regex": True,
				"toggle": True,
			})
		elif panel_active and demo_active and console_active == False :
			demo_active = False
			panel_active = False
			sublime.active_window().run_command( "show_panel",
			{
				"panel": "find",
				"regex": True,
				"toggle": True,
			})
		elif panel_active and not demo_active :
			sublime.active_window().run_command( "toggle_regex" )

class DetectRegexIconClickListener( sublime_plugin.EventListener ):
	def on_post_window_command( self, window, command_name, args ):
		# window = sublime.active_window()
		global last
		global panel_active
		global demo_active
		global demo_counter

		view = window.active_view()
		panel_name = window.active_panel()
		panel_name = str( panel_name )
		# print( { "command_name": command_name } )

		if command_name == "hide_panel" :
			demo_active = False
			demo_counter = 0
			panel_active = False
			last = ""

		if command_name == "show_panel" :

			if panel_name in panel_array :
				last = panel_name

				if ( panel_name == "console" ):
					console_active = True
					print( { "demo_counter" : demo_counter , "demo_active" : demo_active, "panel_active": panel_active } )

				if( panel_name != "console" ):
					demo_counter += 1
					print( "panel open" , panel_name )
					panel_active = True

				if( demo_counter >= 3 ):
					demo_active = False
					demo_counter = 0

				# if demo_active :
				# 	demo_active = False
				# print( "panel open" , panel_name )

			if panel_name == "None" :

				if( last != "console" ):
					print( "panel close" , last )
					print( "" )
					panel_active = False

				if( last == "console" ):
					console_active = False
					panel_active = False

				demo_active = False
				demo_counter = 0
				last = ""
				# sublime.active_window().run_command( "toggle_regex" )
				# sublime.active_window().run_command( "hide_panel" , { panel:"find_in_files" , "regex": False } )
				# sublime.active_window().run_command( "hide_panel" , { panel:"replace" , "regex": False } )

#
