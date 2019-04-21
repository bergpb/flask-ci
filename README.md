## Flask app with CI integration

[![Build Status](https://travis-ci.com/bergpb/flask-ci.svg?branch=master)](https://travis-ci.com/bergpb/flask-ci)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/164ef7868a6d440daa33708eb6e82a77)](https://www.codacy.com/app/bergpb/flask-ci?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=bergpb/flask-ci&amp;utm_campaign=Badge_Grade)
[![Codacy Badge](https://api.codacy.com/project/badge/Coverage/164ef7868a6d440daa33708eb6e82a77)](https://www.codacy.com/app/bergpb/flask-ci?utm_source=github.com&utm_medium=referral&utm_content=bergpb/flask-ci&utm_campaign=Badge_Coverage)
[![codecov](https://codecov.io/gh/bergpb/flask-ci/branch/master/graph/badge.svg)](https://codecov.io/gh/bergpb/flask-ci)

### A simple Flask app with continuous integration config (Travis and CircleCI)

Installing and running:
1.  Install dependencies: ```pipenv install```
2.  Running all tests and coverage: ```tox```

Or command by command:
1.  Running tests: ```pytest -v```
2.  Run Coverage: ```coverage run app.py```
3.  Show report: ```coverage report```
4.  Create html page from report: ```coverage html```
