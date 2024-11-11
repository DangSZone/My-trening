strings_positions = {}
def custom_write(file_name, strings):

    line_number = 1
    file = open(file_name, encoding='Utf-8')
    file_lines = file.readlines()
    for s in strings:
        for f_s in file_lines:
            if s in f_s:
                break
            elif s not in f_s:
                continue
        else:
            file_wr = open(file_name, 'a', encoding='Utf-8')
            line_byte = file_wr.tell()
            file_wr.write(f'{s}\n')
            strings_positions[(line_number, line_byte)] = s
            line_number += 1
            file_wr.close()
    file.close()
    return strings_positions




info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)