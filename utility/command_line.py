import sys

__version__ = "2.0.2"

class CommandLineSwitches:

	def parse(self, args):
		self.minMode=False
		self.develMode=False
		self.noSend=False

		if len(args)>1:
			for arg in args[1:]:
				if arg.lower()=="-version":
					print(f"RadioLog version {__version__}")
					sys.exit(0)
				if arg.lower()=="-devel":
					self.develMode=True
					print("Development mode enabled.")
				elif arg.lower()=="-min":
					self.minMode=True
					print("Minimum display size mode enabled.")
				elif arg.lower()=="-nosend":
					self.noSend=True
					print("Will not send any GET requests for this session.")
				else:
					print("ERROR Unrecognized command line switch: "+arg)
					print("USAGE: RadioLog [-version] [-devel] [-min] [-nosend]")
					sys.exit(1)
