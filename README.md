# Redis-zada
Zadanie z 
1. Należy uruchomić dockera przy użyciu komendy: docker run -d --name some-redis -p 6379:6379 redis
2. Dla osób zaznajomionych z pythonem:
  a) Pobrać projekt i otworzyć go w IDE (Pycharm)
  b) Zainstalować requirements.txt
  c) Upewnić się, że docker jest uruchomiony na porcie 6379
  d) Uruchomić plik products_records.py. Zapełni on bazę danych paroma rekordami
  c) Uruchomić main.py czyli nasz główny serwer
  d) Jeżeli serwer jest uruchomiony to przy użyciu postmana alboo insomnie można wysyłać requesty pod endpoint
3. Dla osób bez znajomości pyhona:
  a) Pobrać projekt i otworzyć go w IDE (Pycharm)
  b) Otworzyć konsolę i wejść do folderu.
  c) Wywołać następujące komendy:
    python -m venv venv
    venv\Scripts\activate.bat
    python -m pip install -r requirements.txt
    python product_records.py
    python main.py
    d) Jeżeli serwer jest uruchomiony to przy użyciu postmana alboo insomnie można wysyłać requesty pod endpoint
    
