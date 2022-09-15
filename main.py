"""
Консольное приложение для передачи файлов на 
галографический вентилятор 
"""
import ftplib
import argparse
import os

class Logger():
	active = True
	def __init__(self) -> None:
		pass

	def log(self, message):
		if self.active:
			print(message)

parser = argparse.ArgumentParser()

parser.add_argument("-f", "--file", dest="filename",
	help="Файл, который необходимо передать",
	required=True)

parser.add_argument("-a", "--address", dest="address",
	help="ip адрес для передачи",
	default="192.168.1.1")

parser.add_argument("-u", "--user", dest="username",
	help="Пользователь ftp сервера",
	default="anon")

parser.add_argument("-p", "--password", dest="password",
	help="Пароль пользователя",
	default="anon")

parser.add_argument("-v", "--verbouse", dest="verb",
	help='Вывод процесса работы в консоль',
	action='store_true')

args = parser.parse_args()


logger = Logger()

if not args.verb:
	logger.active = False

try:
	session = ftplib.FTP(args.address, args.username, args.password)

except OSError as err:
	logger.log('Произошла ошибка при подключении, проверьте правильность адреса')
	exit(0)

except Exception as err:
	logger.log('Неудалось подключится. Провертье правильность введённых данных')
	exit(0)

else: 

	logger.log('Чтение указанного файла...')
	if not os.path.exists(args.filename):
		logger.log('Указанный файл не найден или не существует')
		exit(0)

	with open(args.filename, 'rb') as file:
		logger.log('Передача файла...')

		try:
			result = session.storbinary('STOR ' + os.path.basename(args.filename), file)

		except Exception as err:
			logger.log(f'При передаче файла произошла ошибка: {err}')
			exit(0)

		else: 
			logger.log('Передача файла успешно завершена.')

		session.quit()

exit(1)