## Flask app with CI integration

![Github Actions](https://github.com/bergpb/flask-ci/workflows/Github%20Actions/badge.svg)
[![CircleCI](https://circleci.com/gh/bergpb/flask-ci.svg?style=svg)](https://circleci.com/gh/bergpb/flask-ci)
[![Build Status](https://travis-ci.com/bergpb/flask-ci.svg?branch=master)](https://travis-ci.com/bergpb/flask-ci)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/164ef7868a6d440daa33708eb6e82a77)](https://www.codacy.com/app/bergpb/flask-ci?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=bergpb/flask-ci&amp;utm_campaign=Badge_Grade)
[![Codacy Badge](https://api.codacy.com/project/badge/Coverage/164ef7868a6d440daa33708eb6e82a77)](https://www.codacy.com/app/bergpb/flask-ci?utm_source=github.com&utm_medium=referral&utm_content=bergpb/flask-ci&utm_campaign=Badge_Coverage)
[![codecov](https://codecov.io/gh/bergpb/flask-ci/branch/master/graph/badge.svg)](https://codecov.io/gh/bergpb/flask-ci)
[![Coverage Status](https://coveralls.io/repos/github/bergpb/flask-ci/badge.svg?branch=master)](https://coveralls.io/github/bergpb/flask-ci?branch=master)

### A simple Flask app with continuous integration config (Jenkins, Travis, CircleCI, Codacy and Coveralls)



Running app:
1.  Install dependencies: ```pipenv install```
2.  Start flask app: ```flask run```

Running tests (with tox):
1.  Install dependencies: ```pipenv install```
2.  Running all tests and coverage: ```tox```

Running tests (with make):
1.  Running tests: ```make test```
2.  Run Coverage: ```make coverage```
