Polyclone is meant to be a lightweight replacement for the NCSA Polyglot server. Installation is simpler, but compatability is retained with the script format such that Polyglot scripts may be used by polyclone.

## Requirements ##

* Python 2.6+
* pip
* Virtualenv

## Installation ##

Check out the project:

    hg clone https://bitbucket.org/drexel/polyclone

Create a new virtual environtment for the project:

    virtualenv venv

Activate the virtual environment:

    . venv/bin/activate

Install the requirements:

    pip install -r requirements.txt

## Limitations ##

Unlike Polyglot, Polyclone cannot compose multiple transformations automatically. Also unlike Polyglot, Polyclone does not employ multiple servers, so all jobs must be processed on the same machine.

## Demonstration Site

A demonstration version of Polyclone is running at <http://polyglot.cci.drexel.edu/>
