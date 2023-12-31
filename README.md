# TentaMaker

This Python package provides a system for building exams (tentor) at Chalmers.

Based on a pool of questions and solutions, the system generates exams both in
the form of PDF files for printing and PNG files for inclusion in online exam
systems such as Inspera or Canvas.

## Documentation

First, install the package by the following command:

    $ pip install tentamaker

Then, create a directory where you want to create and store the generated exams
and enter the directory, for example:

    $ mkdir exams
    $ cd exams

Then, run the following command to create the initial structure for your exams:

    $ init-exam

This will populate the current directory with a number of directories where the
output will be stored. This will also create a directory named `config`
containing the configuration of the exam.

To create an exam, you first need to build a pool of questions. Edit the file
`config/pool.tex` to build the pool of questions. Each question should be
entered in LaTeX in the following format

    % X.y.z
    Formulation of question.
    % Answer
    Solution to question.
    %

See the file `config/pool.tex` for examples of how to write questions and
solutions.

Each question has a label in the format `X.y.z` where `X` is a capital letter
(`A`, `B`, `C`, ...) denoting which part of the exam that the question belongs
to. The number `y` denotes the number of the question within the part `X` and
the number `z` denotes a variant of the question. Each question can have many
variants.

When generating exams, the *last variant* of each question is selected, unless
the randomization option is set (see below).

The next step is to edit the configuration file `conf/conf.toml` to set the title
of the course, the course code, name of examiner etc.

Once this is done, you may proceed to generate the exam by running the following
command:

    $ make-exam yyyy-mm-yy

Here, `yyyy-mm-yy` is the date of the exam. This will generate PDF files in the
directory `pdf` and snapshots of the questions in the directory `png`.

The command `make-exam` supports a number of optional command-line arguments
described below.

Add `--randomize` to randomize the selection of questions. The randomization
uses the seed specified in `conf/conf.toml`. If the seed is missing, the seed
will use a "non-deterministic" seed from the operating system.

Add `--verbose` to see more detailed output. This is useful for example if the
process hangs at "Building PDF file..." to see what might have gone wrong when
running LaTeX (pdflatex).

Add `--no-snapshots` to skip generation of PNG snapshots. This is useful during
the creation of an exam (not creating PNG files until the exam is final).

## Authors (in order of appearance)

* [Anders Logg](http://anders.logg.org)

## License

This project is licensed under the
[MIT license](https://opensource.org/licenses/MIT).

Copyright is held by the individual authors as listed at the top of
each source file.
