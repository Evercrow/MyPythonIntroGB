#Реализовать RLE алгоритм. реализовать модуль сжатия и восстановления данных.
#входные и выходные данные хранятся в отдельных текстовых файлах

# u_data = "1111111aaaaa21111222bbbbb2222222211"
# print(u_data)

#Модули ниже подходят для смешанных  цифро-буквенных строчек.
#За универсальность приходится платить низкой эффективностью сжатия,
#хотя удалось немножко выиграть, не кодируя одинарные символы.
#  
#двойные, как в википедии,непонятно как расшифровать. 
#Для декодера неясно, что такое в строке-шифре "аа" - ключ к обращению списка числа
#повторений, или же пропускаемая часть из двух символов, как одинарные? 

def EncodeRLE2(file_path):
	f = open(file_path, 'r')
	data = f.read()
	f.close()

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
	file_path = str(file_path)
	result_path = file_path[0:file_path.rfind('\\')+1]+'encoded_data.txt'
	from pathlib import Path
	f = open(Path(result_path), 'w')
	for i in range(len(run_lengths)-1):
		f.write(run_lengths[i]+" ")
	f.write(run_lengths[-1]+",")
	f.writelines(data_processed)
	f.close()
	# print("Initial data:") #для проверки в консоли раскомментить оба print блока
	# print(data)
	# print()
	print(f"Result written to '{result_path}")



def DecodeRLE2(file_path):
	f = open(file_path, 'r')
	enc_data = f.read()
	enc_string = enc_data[enc_data.find(',')+1:]
	run_data = enc_data[:enc_data.find(',')].split(" ")
	run_data = list(map(int,run_data))
	f.close()

	decoded = ""
	j = 0
	i = 0
	while i < len(enc_string):
		if enc_string[i] != enc_string[i+1]:
			decoded += enc_string[i]
		else:
			decoded +=enc_string[i]*run_data[j]
			j+=1
			i+=1
		i+=1 
	file_path = str(file_path)
	result_path = file_path[0:file_path.rfind('\\')+1]+'decoded_data.txt'
	
	from pathlib import Path
	f = open(Path(result_path), 'w')
	f.writelines(decoded)
	f.close()
	# print("Encoded data:")
	# print(enc_data)
	# print("Result:")	
	# print(decoded)
	print(f"Result written to '{result_path}")

from pathlib import Path

init_path = Path("Homework6/initial_data.txt")
EncodeRLE2(init_path)

enc_path = Path("Homework6\encoded_data.txt")
DecodeRLE2(enc_path)