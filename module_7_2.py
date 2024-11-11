
def custom_write(file_name, strings):
    strings_positions = {}
    line_number = 1
    file_wr = open(file_name, 'w+', encoding='Utf-8')
    for s in strings:
            line_byte = file_wr.tell()
            file_wr.write(f'{s}\n')
            strings_positions[(line_number, line_byte)] = s
            line_number += 1
    file_wr.close()
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