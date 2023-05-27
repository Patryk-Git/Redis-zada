# Redis-zada
Zadanie z 
1. Należy uruchomić dockera przy użyciu komendy: docker run -d --name some-redis -p 6379:6379 redis
2. Dla osób zaznajomionych z pythonem:<br />
  a) Pobrać projekt i otworzyć go w IDE (Pycharm)<br />
  b) Zainstalować requirements.txt<br />
  c) Upewnić się, że docker jest uruchomiony na porcie 6379<br />
  d) Uruchomić plik products_records.py. Zapełni on bazę danych paroma rekordami<br />
  c) Uruchomić main.py czyli nasz główny serwer<br />
  d) Jeżeli serwer jest uruchomiony to przy użyciu postmana alboo insomnie można wysyłać requesty pod endpoint<br />
3. Dla osób bez znajomości pyhona:<br />
  a) Pobrać projekt i otworzyć go w IDE (Pycharm)<br />
  b) Otworzyć konsolę i wejść do folderu.<br />
  c) Wywołać następujące komendy:<br />
    python -m venv venv<br />
    venv\Scripts\activate.bat<br />
    python -m pip install -r requirements.txt<br />
    python product_records.py<br />
    python main.py<br />
    d) Jeżeli serwer jest uruchomiony to przy użyciu postmana alboo insomnie można wysyłać requesty pod endpoint<br />
    
