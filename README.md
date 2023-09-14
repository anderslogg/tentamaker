# TentaMaker

This Python package provides a system for building exams (tentor) at Chalmers.

Based on a pool of questions and solutions, the system generates exams both in
the form of PDF files for printing and PNG files for inclusion in online exam
systems such as Inspera or Canvas.

## Documentation

First, install the package by the following command:

    $ pip install .

Then, create a directory where you want to create and store the generated exams
and enter the directory, for example:

    $ mkdir exams
    $ cd exams

Then, run the following command to create the initial structure for your exams:

    $ init-exam

Then, do this:

    $ make-exam yyyy-mm-yy

Where `yyyy-mm-yy` is the date of the exam,

The command `make-exam` supports the follow optional command-line arguments:

Add `--verbose` to see more detailed output. This is useful for example if the
process hangs at "Building PDF file..." to see what might have gone wrong when
running LaTeX (pdflatex).

Add `--randomize` to randomize the selection of questions.

Add `--no-snapshots` to skip generation of PNG snapshots. This is useful during
the creation of an exam (not creating PNG files until the exam is final).

## Authors (in order of appearance)

* [Anders Logg](http://anders.logg.org)

## License

This project is licensed under the
[MIT license](https://opensource.org/licenses/MIT).

Copyright is held by the individual authors as listed at the top of
each source file.
