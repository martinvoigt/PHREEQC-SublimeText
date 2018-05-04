import sublime
import sublime_plugin

import subprocess
import threading
import os

class PhreeqcCommand(sublime_plugin.WindowCommand):

    def run(self, kill=False):
        
        vars = self.window.extract_variables()
        args = ['c:\phreeqc\phreeqc.exe', vars['file_name'], vars['file_name']+'.out']

        self.window.run_command("exec", {"cmd": args})

        self.window.open_file(vars['file_name']+'.out')



#c:\\phreeqc\\phreeqc.exe \"$file\" \"$file\".out c:\\phreeqc\\database\\phreeqc.dat