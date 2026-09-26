# SCOPE START : add_space_in_parenthesis =>

# in : class add_scope_function in : def is_line_empty
def selection_to_range_region_2( sublime_region ):
	line_range = list( range( sublime_region.begin() , sublime_region.end() ) )
	# return list( map( lambda x : sublime.Region( x , x + 1 ) , line_range ) )
	return list(map( lambda x : { "text" : view.substr(x) , "cell_region" : sublime.Region( x , x + 1 ) } , line_range ))

class add_space_in_parenthesis( sublime_plugin.TextCommand ):

	def run(self,edit):
		global view
		view = self.view
		# selection = view.sel()[-1]
		# start = selection.begin()
		point = self.view.sel()[0].begin()

		print( "" )

		line_number = find_line_number( self.view , point )
		line_selection = get_line_selection( line_number )

		a = sublime.Region( line_selection.begin() , point )
		b = sublime.Region( point , line_selection.end() )

		char_array_a = selection_to_range_region_2( a )
		char_array_a.reverse()
		char_array_b = selection_to_range_region_2( b )

		open_parenthesis = None

		close_parenthesis = None

		level = 0
		for index, x in enumerate( char_array_a ):
			if( x["text"] == ")" ):
				level += 1
			if( x["text"] == "(" ):
				open_parenthesis = x["cell_region"]
				break
			if( x["text"] == "(" ):
				level -= 1

		level = 0
		for index, x in enumerate( char_array_b ):
			if( x["text"] == "(" ):
				level += 1
			if( x["text"] == ")" and level == 0 ):
				close_parenthesis = x["cell_region"]
				break
			if( x["text"] == ")" ):
				level -= 1

		check_close_space = self.view.substr( sublime.Region( close_parenthesis.begin() - 1 , close_parenthesis.begin() ) )

		check_open_space = self.view.substr( sublime.Region( open_parenthesis.end() , open_parenthesis.end() + 1 ) )

		print( [ check_close_space ] )

		print( [ check_open_space ] )

		if check_close_space != " " :

			self.view.insert( edit , close_parenthesis.begin() , " " )

		if check_open_space != " " :

			self.view.insert( edit , open_parenthesis.end() , " " )

# SCOPE END : add_space_in_parenthesis <=
