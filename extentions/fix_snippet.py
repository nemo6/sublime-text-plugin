import sublime
import sublime_plugin

class SnippetPostProcessListener( sublime_plugin.EventListener ):

	def on_post_text_command( self, view, command_name, args ):
		if command_name != "commit_completion":
			return
		view = sublime.active_window().active_view()
		view.run_command( "ysexruilnfhr" )

# snippet "\User\"
# regex:query.*snippet "\User\"

class ysexruilnfhr( sublime_plugin.TextCommand ):
	def run( self, edit ):
		selection = self.view.sel()[0]
		start = selection.begin()
		array = [
		"values().valueOf()",
		"valueOf()",
		"toString()",
		"join( \""
		"at(0",
		"length",
		]
		for x in array:
			offset_left = start - len(x)
			region = sublime.Region( offset_left , start )
			region_str = self.view.substr( region )
			print( x == "join(\"\")" )
			if region_str == x :
				if self.view.substr( sublime.Region( offset_left - 1 , offset_left ) ) != "." :
					view.insert( edit, offset_left , "." )
				else:
					pass
			else:
				pass
