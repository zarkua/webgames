import subprocess
import glob
import os

# Константы параметров громкости
LOUDNESS_TARGET = -16  # Integrated Loudness (I)
TRUE_PEAK = -1         # True Peak (TP)
LOUDNESS_RANGE = 16    # Loudness Range (LRA)

# Определение папок
folders = {
    'Tier_1': {'q': 10, 'ar': 44100},
    'Tier_2': {'q': 7, 'ar': 32100},
    'Tier_3': {'q': 5, 'ar': 32100},
    'Tier_4': {'q': 5, 'ar': 22050},
    'Tier_5': {'ac': 1, 'q': 3, 'ar': 16000},
}
final_folder = 'Final'

# Создание папки Final, если она не существует
if not os.path.exists(final_folder):
    os.makedirs(final_folder)

# Функция для получения размера файла
def get_file_size(path):
    return os.path.getsize(path)

# Функция для расчета процентного изменения размера
def calculate_percentage_change(original, new):
    change = ((new - original) / original) * 100
    return round(change, 2)

# Суммарные размеры файлов до и после конвертации
total_original_size = 0
total_converted_size = 0

# Обработка файлов в каждой папке
for folder, params in folders.items():
    for file_path in glob.glob(f'{folder}/*.*'):
        original_size = get_file_size(file_path)
        total_original_size += original_size
        file_name = os.path.splitext(os.path.basename(file_path))[0]
        output_path = f'{final_folder}/{file_name}.ogg'

        command = [
            'ffmpeg', '-loglevel', 'error', '-i', file_path, 
            '-c:a', 'libvorbis', '-filter:a', 
            f'loudnorm=I={LOUDNESS_TARGET}:TP={TRUE_PEAK}:LRA={LOUDNESS_RANGE}'
        ]
        if 'ac' in params:
            command += ['-ac', str(params['ac'])]
        command += ['-q:a', str(params['q']), '-ar', str(params['ar']), output_path]

        subprocess.run(command)

        # Получение и сравнение размера конвертированного файла
        converted_size = get_file_size(output_path)
        total_converted_size += converted_size
        percentage_change = calculate_percentage_change(original_size, converted_size)

        print(f'{file_name}: Размер файла изменен на {percentage_change}%')

# Расчет и вывод общих результатов
total_original_size_mb = total_original_size / (1024 * 1024)
total_converted_size_mb = total_converted_size / (1024 * 1024)
total_size_reduction = total_original_size_mb - total_converted_size_mb

print(f'\nОбщий результат:')
print(f'Общий размер до конвертации: {total_original_size_mb:.2f} МБ')
print(f'Общий размер после конвертации: {total_converted_size_mb:.2f} МБ')
print(f'Общее уменьшение размера: {total_size_reduction:.2f} МБ')

print('done.')
