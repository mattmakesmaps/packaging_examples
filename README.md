# README

Source: [https://python-packaging.readthedocs.io/en/latest/index.html]()

Experiment using packages, relative imports, cmd utils.

To install:

1. clone repo: [https://github.com/mattmakesmaps/packaging_examples]()
2. drop into `virtualenv`
3. `cd` into `packaging_examples` directory.
4. run `pip install -e .` to install in developer mode.
5. run `python setup.py test` to execute tests

**NOTE:** Re-running `pip install -e .` will just uninstall and re-install
the package.

```bash
packaging_examples
├── bin # Dir for command line scripts
│   └── say-script.py # Command Line Util; absolute import of `dumbpack` package.
├── dumbpack
│   ├── __init__.py # Relative import `test` module and it's `sayHello()` function.
│   ├── tests # Dir for tests
│   │   ├── __init__.py # Creates package for tests to live
│   │   ├── test_text.py # Module containing some example tests
│   ├── text.py # Module containing `sayHello()` function.
├── MANIFEST.in
├── README.md
└── setup.py
```

