# Nordic Microalgae - data layer and API

This GitHub repository contains:

- Source code and static data for the Nordic Microalgae data layer.
- Source code for the API.

More info: https://github.com/nordicmicroalgae/nordicmicroalgae-documentation

## How to run Flask (short intro)

- Clone nordicmicroalgae: git clone https://github.com/anloo/nordicmicroalgae.git
- Create virtual environment: virtualenv -p python3 ~/.virtualenvs/nordicmicroalgae
- Add the following to ~/.virtualenvs/nordicmicroalgae/bin/postactivate:
```
export DB_HOST='localhost'
export DB_NAME='nordicmicroalgae'
export DB_USER='nordicmicroalgae'
export DB_PASS='<replacewithpassword>'
```
- Activate virtual environment: source ~/.virtualenvs/nordicmicroalgae/bin/activate
- Source environment variables: source ~/.virtualenvs/nordicmicroalgae/bin/postactivate
- Change directory: cd nordicmicroalgae
- Install dependencies: pip install -r requirements.txt
- Launch development server: scripts/server
