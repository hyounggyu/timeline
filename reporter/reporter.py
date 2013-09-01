from jinja2 import Environment, PackageLoader

if __name__ == '__main__':
  env = Environment(loader=PackageLoader('reporter', 'templates'))
  template = env.get_template('home.html')
  print template.render()
