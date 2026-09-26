
# Ctrl+'/ù : view.run_command("pz1r5hqxnxve")
# transform "foo = x => x" to "function foo(x){ return x }"

class pz1r5hqxnxve( sublime_plugin.TextCommand ):
	def run( self , edit ):
		global view
		view = self.view
		selection = self.view.sel()[0]
		text_selection = self.view.substr( selection )
		reformatted_text = re.sub( r"([\w_]+)\u0020*=\u0020*\((a)\)\u0020*=>", r"function \1 (\2)", text_selection )

		# date_text = "Today's date is 02-09-2024 and yesterday was 01-09-2024."
		# date_pattern = r"(\d{2})-(\d{2})-(\d{4})"
		# reformatted_text = re.sub(date_pattern, r"\3-\2-\1", date_text)
		print(reformatted_text)

		self.view.replace( edit, selection , reformatted_text )
