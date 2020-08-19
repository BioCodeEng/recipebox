Author: Ally Engle

IMPORTANT NOTE: Use python3 manage.py <insert command.. My computer seems to be particular about using python3 for everything related to python 3.x.x.

Sources used (so far) for assistance and understanding(links included):
1. Kenzie Recipebox V.1, Forms, and Auth Demo by Joe!

Also:

2. Django Web Development with Python Introduction (https://pythonprogramming.net/django-web-development-python-tutorial/)
3. LinkedIn Learning: Become a Django Developer Learning Path(https://www.linkedin.com/learning/paths/become-a-django-developer)
4. Udemy: Python and Django Full Stack Web Developer Bootcamp by Jose Portilla (https://www.udemy.com/course/python-and-django-full-stack-web-developer-bootcamp/learn/lecture/4954484?start=15#overview)
5. Djangoproject: Writing your first Django app, part 4: (covers how to use HTTPresponseredirect which is useful in the login and logout parts of "authentication" assessment) (https://docs.djangoproject.com/en/3.1/intro/tutorial04/)
6. Djangoproject: Using the Django authentication system and decorators: @login-required (https://docs.djangoproject.com/en/3.1/topics/auth/default/) (https://docs.djangoproject.com/en/1.11/_modules/django/contrib/auth/decorators/)

Kenzie Django Auth Demo Notes
- [ ] 4:00 from Django.contrib.auth import login, logout, authenticate
- [ ] 5:00 from django.contrib.auth.models import User
- [ ] 5:45 User.objects.all()
- [ ] 6:15 authenticate(None, username=“ “, password=“ “)
    - [ ] None if it doesn’t authenticate
    - [ ] User if it does
- [ ] 7:15 Three things for authentications
    - [ ] Userform
    - [ ] Login_view
    - [ ] Logout_view
    - [ ] Urls
- [ ] 7:15 forms.py/LoginForm
- [ ] 10:00 views.py/login
- [ ] 11:30 views.py/LoginForm (still going through Kenzie Demo by Joe
- [ ] 14:15 Login_view view and url hooked up properly so that LoginForm page shows up
    - [ ] This far code from demo is used on top of initial init code!
- [ ] 14:30 Complete login_view function
