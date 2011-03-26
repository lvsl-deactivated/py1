# coding: utf-8

import jinja2
import os


def main():
    curr_dir = os.path.dirname(os.path.abspath(__file__))
    fs_loader = jinja2.FileSystemLoader([curr_dir], encoding='utf-8')
    env = jinja2.Environment(loader=fs_loader)

    tmpl = env.get_template('jinja_tmpl.html')
    ctx = {'name': 'test'}

    return tmpl.render(ctx)


if __name__ == "__main__":
    print main()
