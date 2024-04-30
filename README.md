# POC4Auth
## Proof Of Concept 4Auth

🇺🇦🇺🇦 Реалізація підтвердження Email-адреси користувача, з використанням WebSocket, при якій інформація про успіх підтвердження з'являється на початковій сторінці (там де користувач вводив адресу), а посилання з підтвердження автоматично закривається.

🇺🇸🇬🇧 Implementation of user Email address verification, using WebSocket, where the information about the successful verification appears on the initial page (where the user entered the address), and the verification link automatically closes.


## How to run
0. Prerequisites
- [Resend](https://resend.com/home) API token
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

6. Open the following url in your browser
[http://localhost:8000/](http://127.0.0.1:8000/)

