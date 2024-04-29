# POC4Auth
## Proof Of Concept 4Auth

Реалізація підтвердження Email-адреси користувача, з використанням WebSocket, при якій інформація про успіх підтвердження з'являється на початковій сторінці (там де користувач вводив адресу), а посилання з підтвердження автоматично закривається.

## How to run
0. Prerequisites
- Resend API token
- Python 3

1. Clone project
```shell
git clone https://github.com/Igor4er/poc4auth
cd poc4auth
```

2. (Optional) Create and activate venv
```shell
python -m venv venv
.\venv\Scripts\activate
```
Unix:
```shell
python3 -m venv venv
source ./venv/bin/activate
```

3. Install requirements
```shell
pip install -r requirements.txt
```

4. Create .env file and fill it (see `.env.dist`)
```shell
cp .env.dist .env
```

5. Run using following command
```shell
python ./src/main.py
```
