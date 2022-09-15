# Программа для передачи файлов на голографический вентилятор

## Использование

Запустить готовый бинарный файл `main.exe`, находящийся в папке
`/dist`

```bash
.\main.exe -v -f [НАЗВАНИЕ_ФАЙЛА]
```

Либо запустить исполняемый файл main.py

```bash
python .\main.py -v -f [НАЗВАНИЕ_ФАЙЛА]
```

Пример использования

```bash
.\main.exe -v -f movie.avi -a 192.168.1.1 -u anon -p pass
```

Передаст на ftp-сервер файл `movie.avi` по адресу `192.168.1.1` от указанного пользователя с паролем

## Полный список опций

```bash
optional arguments:
  -h, --help            show this help message and exit
  -f FILENAME, --file FILENAME
                        Файл, который необходимо передать
  -a ADDRESS, --address ADDRESS
                        ip адрес для передачи
  -u USERNAME, --user USERNAME
                        Пользователь ftp сервера
  -p PASSWORD, --password PASSWORD
                        Пароль пользователя
  -v, --verbouse        Вывод процесса работы в консоль
```

## Cоздание билда вручную

Установить `pyinstaller`

```bash
pip install -r .\req.txt
```

Или 

```bash
pip install pyinstaller
```

После чего

```bash
pyinstaller --onefile .\main.py
```