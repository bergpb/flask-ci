## Flask app with CI integration.

![Travis (.org)](https://img.shields.io/travis/bergpb/flask-ci-test.svg)
[![codecov](https://codecov.io/gh/bergpb/flask-ci-test/branch/master/graph/badge.svg)](https://codecov.io/gh/bergpb/flask-ci-test)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/a0759b8c0a1d411291aad485408ba1c0)](https://www.codacy.com/app/bergpb/flask-ci-test?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=bergpb/flask-ci-test&amp;utm_campaign=Badge_Grade)


#### A simple Flask app with continuous integration config (Travis and CircleCI).


1. Install dependencies: ```pipenv install```
2. Running tests: ```pytest -v```
3. Run Coverage: ```coverage run app.py```
4. Show report: ```coverage report```
5. Create html page from report: ```coverage html```
6. Run project with: ```flask run```