# Django(DRF) Template

#### Running locally
- Clone project and create virtual environment `python3 -m venv <venv_name>` and activate it `source venv/bin/activate`
- Install requirements `pip3 install -r requirements.txt `
- Copy `.env.example` to `.env` and update according to requirement.
- Run server `python manage.py runserver --settings=config.settings.local`


#### Running unit tests
- `python manage.py test --keepdb --settings=config.settings.test`

#### Running parallel unit tests:
This is not supported in windows. But for linux and macos use:
- `python manage.py test --parallel --keepdb --settings=config.settings.test`

#### Note: 
You can provide environment variable as well to map settings.

Example:

    - Unix Bash Shell:
        export DJANGO_SETTINGS_MODULE=config.settings.local

    - Window Shell:
        set DJANGO_SETTINGS_MODULE=config.settings.local
