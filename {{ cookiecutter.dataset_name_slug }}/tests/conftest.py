import pytest
import datapackage


{% if cookiecutter.dataset_geography == 'Town' %}
@pytest.fixture
def towns():
    """Load our town list datapackage"""
    dp = datapackage.DataPackage('https://raw.githubusercontent.com/CT-Data-Collaborative/ct-town-list/master/datapackage.json')
    return dp.resources[0].data

{% elif cookiecutter.dataset_geography == 'County' %}
@pytest.fixture
def counties():
    """Load our county list datapackage"""
    dp = datapackage.DataPackage('https://raw.githubusercontent.com/scuerda/ct-county-list/master/datapackage.json')
    return dp.resources[0].data

{% else %}
{% endif %}
