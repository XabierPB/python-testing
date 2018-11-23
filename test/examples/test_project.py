from hypothesis.strategies import characters, text, builds
from hypothesis import given
from unicodedata import category
from hypothesis.extra.datetime import datetimes
from functions.examples.project import Project
from hypothesis.strategies import composite
from hypothesis import assume


names = text(
    characters(max_codepoint=1000, blacklist_categories=('Cc', 'Cs')), min_size=1)\
    .map(lambda s: s.strip())\
    .filter(lambda s: len(s) > 0)
names.example()

project_date = datetimes(timezones=('UTC',), min_year=2000, max_year=2100)
project_date.example()

projects = builds(Project, name=names, start=project_date, end=project_date)
projects.example()

# Projects can start after they end when we use builds this way. One way to fix this would be to use filter():
projects = builds(Project, name=names, start=project_date, end=project_date).filter(lambda p: p.start < p.end)
projects.example()


@given(names)
def test_names_match_our_requirements(name):
    assert len(name) > 0
    assert name == name.strip()
    for c in name:
        assert 1 <= ord(c) <= 1000
        assert category(c) not in ('Cc', 'Cs')


@given(project_date)
def test_dates_are_in_the_right_range(date):
    assert 2000 <= date.year <= 2100
    assert date.tzinfo._tzname == 'UTC'


@composite
def projects(draw):
    name = draw(names)
    date1 = draw(project_date)
    date2 = draw(project_date)
    assume(date1 != date2)
    start = min(date1, date2)
    end = max(date1, date2)

    return Project(name, start, end)


@given(projects())
def test_projects_end_after_they_started(project):
    assert project.start < project.end




