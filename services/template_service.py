from jinja2 import Environment, PackageLoader, select_autoescape

env = Environment(
    loader=PackageLoader('autodoc', 'templates'),
    autoescape=select_autoescape(['html', 'xml', 'md'])  # 'md' is added to the list
)

def get_template(name):
    return env.get_template(f"{name}.j2")  # assuming your templates have .j2 extension
