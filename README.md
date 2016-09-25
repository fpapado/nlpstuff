# nlpstuff
Here's where I deposit various NLP-related scripts, inspired by topics in my Postgraduate course.
They might be useful to students taking an NLP class with little programming
experience (such as those coming from a linguistics background), and want to
see how to implement popular algorithms using simple Python constructs.

Issues, comments, and pull requests are most welcome!

## Python Version
Currently using Python 3, but since there's nothing specific apart from print()
statements, I'll make a best effort to add Python 2 versions of each script.

## Dependencies
There are currently no hard dependencies, as the aim is to use simple
constructs.
Should there be any dependencies (numpy might be one), they will be managed via
virtual environments.
[You can find more information on virtualenv
here](http://docs.python-guide.org/en/latest/dev/virtualenvs/)

If you want to to test virtualenv out with some simple dev dependencies (that
install the really neat [ptpython interpreter
interface](https://github.com/jonathanslenders/ptpython)) do this:

```shell
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Prints and logs
There is probably going to be a lot of printing / logging in these scripts, as
most of them aim to demonstrate steps in an algorithm.
It might be a good idea to make them optional (e.g. by a default kwargs) in the
future.
