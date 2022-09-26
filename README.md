# FastAPI template

 

## Project requirements

### 

- [Python 3.10.7](https://www.python.org/downloads/release/python-3107/)
- pip package 22.2.2
- FastAPI 0.82.0
- uvicorn 0.18.3
- pylint 2.15.2
- sqlalchemy 1.4.41

To start the project run 

1. Installing FastAPI

```
pip install fastapi
```

1. Installing Uvicorn

```
pip install "uvicorn[standard]"
```

1. Create the virtual environment  run 

```
python -m venv env
```

1. Activate the virtual env created

```
source ./env/bin/activate
```

Related links:

[Here](https://fastapi.tiangolo.com/contributing/#developing) 👈

1. To install all requirements \(dependencies\) from requirements.txt file you'll need to run 

```
$ pip install -r path/to/requirements.txt
```

**NOTE:** every new dependency added to the project need to be included into requirements.txt file

Related links:

[Here](https://note.nkmk.me/en/python-pip-install-requirements/) 👈

1. To run the project and start uvicorn server

```
uvicorn main:app --reload
```

**NOTE:** If you need to see the swagger documentation go to **/docs** endpoint in the browser

## Pylint 

## What is Pylint?

Pylint is a static code analyser for Python 2 or 3. The latest version supports Python 3.7.2 and above.

Pylint analyses your code without actually running it. It checks for errors, enforces a coding standard, looks for code smells, and can make suggestions about how the code could be refactored.

Documentation for further information

[Here](https://pylint.pycqa.org/en/latest/) 👈

## How to use it?

Every time that you need to check your code you need to run the following command:

```
pylint <filename> || pylint <foldername>
```

Pylint Rules

The pylint rules are defined in the .pylintrc file located in the root of the project.

.pylintrc example

[Here](https://www.codeac.io/documentation/pylint-configuration.html) 👈

Pylint rate your code and evaluate it in a range from 0 to 10 \(0 = too bad 👎, 10 = too good👍\)

**NOTE**: Each commit will be accepted with the evaluation of a 10, otherwise the CI/CD will fail.

## Python variables names

Rules for Python variables:

A variable name must start with a letter or the underscore character

A variable name cannot start with a number

A variable name can only contain alpha\-numeric characters and underscores \(A\-z, 0\-9, and \_ \)

Variable names are case\-sensitive \(age, Age and AGE are three different variables\)

Example: 

```
#Legal variable names:
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

#Illegal variable names:
2myvar = "John"
my-var = "John"
my var = "John"
```

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

FastAPI \-\> domain services \-\> database

DDD \-\> domain driven design for python \- clean architecture

TDD \-\> test driven development

Project structure and configuration

    Dependencies

        Development environment \(within the project\)

         \- ENVs ensure that the development environment is the same for all \(same version of python\)

         \- requirements.txt == package.json

         \- Pylint \-\- CI/CD

         \- Prettier \(I don't know if it's prettier or other\), we need to force a code style

    Code

        \- Python design patterns

            \- separate the infra layer from the business layer from the data layer

    Tests

        \- First you do the test, then you do TDD coding

        \- 95% coverage

        \- unit tests \- test a small unit of code \(all external services are mocks\)

        \- integration tests \- integrate several layers of the service \(i.e., a repository with the database, call an endpoint through fastAPI\)

        \- load tests...

    Pipelines

        \- integration with gitlab \+ GCP

