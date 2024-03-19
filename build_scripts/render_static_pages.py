from jinja2 import Environment, FileSystemLoader
from os import sep

env = Environment(loader=FileSystemLoader(f"..{sep}templates"))


def render_and_save_template(template_name, output_file_path):

    template = env.get_template(template_name)
    rendered_content = template.render()

    # Ensure the output directory exists
    # output_dir = os.path.dirname(output_file_path)
    # os.makedirs(output_dir, exist_ok=True)

    # Save the rendered content to the specified file
    with open(f"..{sep}site{sep}" + output_file_path, "w", encoding="utf-8") as file:
        file.write(rendered_content)


## static pages from /templates to be rendered into /site

render_and_save_template("home_page.html", "index.html")
render_and_save_template("faculty.html", "faculty.html")
