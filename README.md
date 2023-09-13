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

    $ tentamaker-init

## Authors (in order of appearance)

* [Anders Logg](http://anders.logg.org)

## License

This project is licensed under the
[MIT license](https://opensource.org/licenses/MIT).

Copyright is held by the individual authors as listed at the top of
each source file.
