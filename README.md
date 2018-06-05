[![Build Status](https://travis-ci.org/eduroom/eduroom-api.svg?branch=master)](https://travis-ci.org/eduroom/eduroom-api)
[![FOSSA Status](https://app.fossa.io/api/projects/git%2Bgithub.com%2Feduroom%2Feduroom-api.svg?type=shield)](https://app.fossa.io/projects/git%2Bgithub.com%2Feduroom%2Feduroom-api?ref=badge_shield)
#### License ####

Every code patch accepted in taiga codebase is licensed under [AGPL v3.0](http://www.gnu.org/licenses/agpl-3.0.html). You must be careful to not include any code that can not be licensed under this license.


[![FOSSA Status](https://app.fossa.io/api/projects/git%2Bgithub.com%2Feduroom%2Feduroom-api.svg?type=large)](https://app.fossa.io/projects/git%2Bgithub.com%2Feduroom%2Feduroom-api?ref=badge_large)

## Setup development environment ##

Just execute these commands in your virtualenv(wrapper):

```
pip install -r requirements.txt
python manage.py migrate --noinput
python manage.py loaddata initial_user
python manage.py loaddata initial_project_templates
python manage.py sample_data
```

**IMPORTANT: only runs with python 3.4+**

Initial auth data: admin/123123