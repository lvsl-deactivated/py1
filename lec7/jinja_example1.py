# coding: utf-8

import jinja2

def main():
    tmpl = jinja2.Template('Hello {{name}}!')
    print tmpl.render(name='Rango')

if __name__ == "__main__":
    main()
