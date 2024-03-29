from jinja2 import Environment, FileSystemLoader
from os import sep

env = Environment(loader=FileSystemLoader(f"..{sep}templates"))


def render_and_save_template(template_name):

    template = env.get_template(template_name)
    rendered_content = template.render()

    # Save the rendered content to the specified file
    with open(f"..{sep}site{sep}" + template_name, "w", encoding="utf-8") as file:
        file.write(rendered_content)


## static pages from /templates to be rendered into /site

render_and_save_template("index.html")
render_and_save_template("people.html")
render_and_save_template("courses.html")
render_and_save_template("highlights.html")
render_and_save_template("404.html")
