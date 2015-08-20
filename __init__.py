#Copyright 2014 Drexel Univeristy
from converter import do_conversion, get_work_dir, clean_work_dir
from scanner import all_target_extensions, conversion_dict
from test import run_tests
from flask import Flask, request, redirect, url_for, stream_with_context, request, Response, send_from_directory, jsonify, g
from os import path, makedirs
import json
from jinja2 import Environment, FileSystemLoader

templatepath = path.join(path.dirname(__file__), 'templates')
env = Environment(loader=FileSystemLoader(templatepath))

app = Flask(__name__)

def after_this_request(func):
  if not hasattr(g, 'call_after_request'):
    g.call_after_request = []
  g.call_after_request.append(func)
  return func

@app.after_request
def per_request_callbacks(response):
  for func in getattr(g, 'call_after_request', ()):
    response = func(response)
  return response

@app.route('/', methods=['GET'])
def show_form():
  template = env.get_template('main.html')
  return template.render(jsonmap=json.dumps(conversion_dict), all_ext = all_target_extensions)

@app.route('/test', methods=['GET'])
def test_results():
  return jsonify(run_tests())

@app.route('/', methods=['POST'])
def process_form():
  if not 'output_format' in request.form:
    return 'no destination format specified', 400
  target_format = request.form['output_format']
  target_format = target_format.strip()
  
  if not 'file' in request.files:
    return 'file not found in POST', 400
  file = request.files['file']
  file_base_name = path.splitext(file.filename)[0]
  source_format = path.splitext(file.filename)[1][1:]

  tmp_path = get_work_dir()

  @after_this_request
  def delete_work_dir(response):
    clean_work_dir(tmp_path)
    return response

  filepath = path.join(tmp_path, 'file.' + source_format)
  file.save(filepath)
  result = do_conversion(filepath, target_format)
  if result <> True:
    return result, 500

  resp = send_from_directory(tmp_path, 'file.' + target_format)
  resp.headers['Content-Disposition'] = 'attachment; filename=' + file_base_name + '.' + target_format
  return resp

if __name__ == '__main__':
  app.run(threaded = True, host='0.0.0.0', debug=True)

