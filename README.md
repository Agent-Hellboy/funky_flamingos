# funky flamingos

A repo with various authentication-related functionalities

### Usage instructions

+ Install the dependencies listed in requirements.txt or alternatively, use [pipenv](#pipenv-usage-instructions)
+ Run `python manage.py runserver 5757` (you can replace 5757 with some other port)
+ Visit http://localhost:5757/users
+ To use GitHub login, add a client ID and client secret to `funky_flamnigos/.env`,
  and visit http://localhost:5757/users/register
+ The callback URL for GitHub must be http://localhost:5757/users/github_login


### Pipenv usage instructions

+ Install pipenv using `pip install pipenv` and run `pipenv shell` to activate the environment.
<<<<<<< HEAD
+ Run `pipenv install` to install all the dependencies and pipenv should automatically install them for you.
=======
+ Run `pipenv install` to install all the dependencies and pipenv should install them for you.
>>>>>>> 3c7210920dd8ae92c75a129f9c4a6498d6f96af1
