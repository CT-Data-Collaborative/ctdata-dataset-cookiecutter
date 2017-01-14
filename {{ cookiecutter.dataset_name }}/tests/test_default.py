import pytest

##################################################################
#
# Basic testing script for {{ cookiecutter.dataset_name }}
# Created by {{ cookiecutter.author_name }}
# On {{ cookiecutter.creation_date }}
#
##################################################################

{% if cookiecutter.dataset_geography == 'Town' %}
def test_towns(towns, geographies):
    assert set([x['Town'] for x in towns]) == set(geographies)
{% elif cookiecutter.dataset_geography == 'County' %}
def test_counties(counties, geographies):
    assert set([x['County'] for x in counties]) == set(geographies)
{% else %}
{% endif %}

def test_dataset_row_counts(rowcount):
    assert rowcount.actual == rowcount.expected

def test_spotcheck_testing(spotcheck_results):
    for check in spotcheck_results:
        assert check.expected == check.actual

def test_geography_count(geographies, geography_units_count):
    assert len(geographies) == geography_units_count