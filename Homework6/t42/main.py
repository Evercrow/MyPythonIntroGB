#Реализовать RLE алгоритм. реализовать модуль сжатия и восстановления данных.
#входные и выходные данные хранятся в отдельных текстовых файлах
# Пример входной строки:
# u_data = "1111111aaaaa21111222bbbbb2222222211"
# print(u_data)

#Модули ниже подходят для смешанных  цифро-буквенных строчек.
#За универсальность приходится платить низкой эффективностью сжатия,
#хотя удалось немножко выиграть, не кодируя одинарные символы.
#  
#двойные, как в википедии(где 1 и 2 не пишутся в массив длин повторов),непонятно как расшифровать. 
# Как понять декодеру: в строке-шифре "AA" - ключ к обращению списка числа
#повторений, или же пропускаемая часть из двух символов, как одинарные? 

#функция считывания строки из файла по названию файла
def FileAccess(file_name):
	from pathlib import Path
	file_path = Path(str(Path(__file__).parent.resolve())+"\\"+file_name)
	f = open(file_path, 'r', encoding="utf-8")
	f_data = f.read()
	f.close()
	return f_data


def EncodeRLE2(initial,mode = 's'):
	if mode == 'f':
		data = FileAccess(initial)
	elif mode == 's': 
		data = initial
	else : return print("input proper read-mode, 'f' for filename, 's' or nothing for string")
	run_start =""
	count = 1
	data_processed = ""
	run_lengths = []
	for place in range(len(data)+1):
		is_end = place== len(data)
		if run_start != data[place-int(is_end)] or is_end:
			if count >1:
				data_processed += run_start*2
				run_lengths.append(str(count))
				count = 1
			else : 
				data_processed += run_start*(count)
				count = 1
			run_start = data[place-int(is_end)]
		else : count +=1	

	from pathlib import Path
	end_path = str(Path(__file__).parent.resolve()) + '\encoded_data.txt'
	f = open(Path(end_path), 'w',encoding="utf-8")
	for i in range(len(run_lengths)-1):
		f.write(run_lengths[i]+" ")
	f.write(run_lengths[-1]+",")
	f.writelines(data_processed)
	f.close()
	# print("Initial data:") #для проверки в консоли раскомментить оба print блока
	# print(data)
	# print()
	print(f"Result written to {end_path}")



def DecodeRLE2(initial,mode = 'f'):
	if mode == 'f':
		enc_data = FileAccess(initial)
	elif mode == 's': 
		enc_data = initial
	else : return print("input proper read-mode, 'f' or nothing for filename, 's' for string")

	enc_string = enc_data[enc_data.find(',')+1:] 
	run_data = list(map(int,enc_data[:enc_data.find(',')].split(" ")))
	
	decoded = ""
	j = 0
	i = 0
	is_end = False
	while i < len(enc_string)-1:
		is_end = i== len(enc_string)
		if enc_string[i] != enc_string[i+1-int(is_end)] :
			decoded += enc_string[i]
		else:
			decoded +=enc_string[i]*run_data[j]
			j+=1
			i+=1
		i+=1	 
	
	from pathlib import Path
	result_path = str(Path(__file__).parent.resolve()) + '\decoded_data.txt'
	f = open(Path(result_path), 'w',encoding="utf-8")
	f.writelines(decoded)
	f.close()
	# print("Encoded data:")
	# print(enc_data)
	# print("Result:")	
	# print(decoded)
	print(f"Result written to '{result_path}")

#вызов сжимателя, по умолчанию обрабатывает входную строку 
# example = 'GGG11111ЮЮЮ444456'
# EncodeRLE2(example, 'a')
# при указании 'f' будет искать файл с названием, указанным в строке.
init_path = "initial_data.txt"
EncodeRLE2(init_path, 'f')

#вызов декодера
#по умолчанию считывает по пути, указанному строкой
enc_path = "encoded_data.txt"
DecodeRLE2(enc_path)
