#!/usr/bin/env python3

from jinja2 import Template
import os
import random
import subprocess


def create_file():
    notes = ["c'", "d'", "e'", "f'", "g'", "a'", "b'", "c''", "d''", "e''", "f''", "g''"]
    random.shuffle(notes)
    questions = []
    for note in notes:
        snippet_template = Template(open('templates/snippet.template').read())
        question = snippet_template.render(treble_note = note, base_note = "")
        print('question:\n', question)
        questions.append(question)

    template = Template(open('templates/template.lytex').read())
    output = template.render(questions = questions)
    open('out.lytex', 'w').write(output)

def build():
    subprocess.check_call(['lilypond-book', '--output=out', '--pdf', 'out.lytex'])
    os.chdir('out')
    subprocess.check_call(['pdflatex', 'out.tex'])


def main():
    create_file()
    build()

if __name__ == '__main__':
    main()
