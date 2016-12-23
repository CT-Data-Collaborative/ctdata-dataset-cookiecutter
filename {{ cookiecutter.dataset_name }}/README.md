{{ cookiecutter.dataset_name }}

{{ cookiecutter.description }}

## License MIT

## Getting Setup

We recommend approaching data processing as just another software development project. That means a few specific thing for us.

1. Version Control
2. Dedicated Environments
3. Automated Testing
4. Continuous Deployment


### Version control

We use git as our VCS. In most cases we can commit our full processing directory, but in cases where we are responsible for data suppression, we specifically exclude raw files from version control.


### Virtual Environments

Processing typically happens in either Python or R. However, testing is done with Python. We recommend setting up a virtual environment for managing any specific dependencies for testing a given dataset as follow:

`python3 -m venv /path/to/new/virtual/environment`

You can then install the requirements like so:

`pip install -r requirements.txt`

### Automated Testing

Testing relies on PyTest and a custom CTData PyTest plugin which is installed as a requirement dependency.

An example testing script is included in the `/tests` directory. Running `py.test` or `pytest` will execute this and other tests.

The basic testing suite makes a few assumptions about the form of the final dataset and uses the `metadata.yml` file to run a preset suite of tests. See our metadata spec repository for more details on how metadata should be written to facilitate testing and ingestion into CKAN.

If spot checks are provide in metadata, they will be automatically run as part of the basic testing suite. Spot checks should provide a series of keys corresponding to the factor level selections required to extract a single row from the final dataset. The value should also be provide, along with any required format conversions [NEED TO EXPAND].

In addition to spot checking, if the data processing does things like calculate percentages of a whole and there is an expectation that all subgroups are accounted for, it would be a good practice to extract subgroups and test that these percentages sum to 1 (or 100 depending on formatting).

### Deployment

We use travis-ci to automate publication of datasets to our CKAN installation. Deployment will only occur on the master branch and requires 100% testing success.
