#Copyright 2014 Drexel Univeristy
from converter import do_conversion, get_work_dir, clean_work_dir
from scanner import command_map, conversion_dict, scan_tests, testdir
from os import path
import shutil
from pprint import pprint

def run_tests():
  passed = []
  failed = []
  commands = command_map.copy()
  for filename in scan_tests():
    testpath = path.join(testdir, filename)
    source_ext = path.splitext(filename)[1][1:]
    if not source_ext in conversion_dict:
      print('no conversions for test file ' + filename)
      continue
    for target_ext in conversion_dict[source_ext]:
      print('test conversion ' + filename + ' to ' + target_ext)
      work_dir = get_work_dir()
      sourcefile = path.join(work_dir, 'file.' + source_ext)
      shutil.copyfile(testpath, sourcefile)
      result = do_conversion(sourcefile, target_ext)
      conversionpath = source_ext + ':' + target_ext
      command = commands.pop(conversionpath)
      if result == True:
        passed.append(conversionpath + ':' + command)
      else:
        failed.append((conversionpath + ':' + command, result))
      clean_work_dir(work_dir)
  untested = []
  return {
    'passed': passed,
    'failed': failed,
    'untested': list(commands.keys())
  }

if __name__ == '__main__':
  pprint(run_tests())

