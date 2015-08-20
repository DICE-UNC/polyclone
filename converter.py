#Copyright 2014 Drexel Univeristy
from os import path
import subprocess as sp
from scanner import command_map, scriptdir
from tempfile import mkdtemp
from shutil import rmtree

def do_conversion(filepath, target_ext):
  work_dir = path.split(filepath)[0]
  filename = path.split(filepath)[1]
  base_filename = path.splitext(filename)[0]
  source_ext = path.splitext(filename)[1]
  if not source_ext:
    return 'can''t determine source file format'
  source_ext = source_ext[1:]

  scriptname = command_map.get(source_ext + ':' + target_ext)
  if not scriptname:
    return 'no conversion available from ' + source_ext + ' to ' + target_ext

  command = path.join(scriptdir, scriptname) + " " + base_filename + "." + source_ext + " " + base_filename + "." + target_ext + " " + source_ext + " " + target_ext;
  p = sp.Popen([command, ], stdout=sp.PIPE, stderr=sp.PIPE, shell=True, cwd=work_dir)
  streamdata = p.communicate()
  rc = p.returncode

  if(rc == 0):
    if not path.isfile(path.join(work_dir, 'file.' + target_ext)):
      return 'Conversion didn''t yield expected target file'
    else:
      return True
  else:
    errmsg = 'ERROR processing ' + scriptname + '\n'
    errmsg += 'Return Code ' + str(rc) + '\n'
    if streamdata[0] <> None and len(streamdata[0]):
      errmsg += '<br />\nOUT:<br />\n' + streamdata[0] + '\n'
    if streamdata[1] <> None and len(streamdata[1]):
      errmsg += '<br />\nERR:<br />\n' + streamdata[1] + '\n'
    return errmsg

def get_work_dir():
  return mkdtemp(prefix='pconv-')

def clean_work_dir(path):
  rmtree(path)
