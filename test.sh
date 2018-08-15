#!/usr/bin/env bash

set -e

lilypond-book --output=out --pdf test.lytex
cd out/
pdflatex test
evince test.pdf
