import os
from pydub import AudioSegment
import time


def convert_mp3_to_wav(input_file, output_file):
    audio = AudioSegment.from_mp3(input_file)
    audio.export(output_file, format='wav')


def get_answer(question):
    result = ''
    while result != 'y' and result != 'n':
        print(f'{question} (y/n): ', end='')
        result = input().lower()
    return result


def sleep_and_exit():
    print('잠시 후 프로그램이 종료됩니다.')
    time.sleep(1)
    exit(0)


print('Himchan mp3 to wav Converter (1.0.0)')
print('contact@juhwijung.com\n')
print('이 exe 파일이 위치한 폴더의 모든 mp3 파일을 wav로 변환합니다.')
print('결과물은 result 폴더에 저장됩니다.')
print('원본은 유지되고 별도의 폴더에 저장하므로 안전합니다.')

if get_answer('변환을 시작합니까?') == 'n':
    sleep_and_exit()

current_directory = os.getcwd()
result_folder = os.path.join(current_directory, 'result')
mp3_files = [file for file in os.listdir(current_directory) if file.endswith('.mp3')]

if len(mp3_files) == 0:
    print('mp3 파일이 존재하지 않습니다.')
    sleep_and_exit()

if not os.path.exists(result_folder):
    os.mkdir(result_folder)

for mp3_file in mp3_files:
    wav_file = mp3_file.replace('.mp3', '.wav')
    wav_file_path = os.path.join(result_folder, wav_file)
    if os.path.exists(wav_file_path):
        print(f'경고: 이미 {wav_file}가 존재합니다.')
        if get_answer('이 파일을 덮어씌울까요?') == 'n':
            print(f'{wav_file}을 건너뜁니다.')
            continue
        print(f'{wav_file}을 덮어씁니다.')
    convert_mp3_to_wav(mp3_file, wav_file_path)
    print(f'{mp3_file}를 변환하여 {wav_file_path}에 저장되었습니다.')

print('모든 파일을 변환했습니다.')
print(f'결과물이 {result_folder}에 저장되었습니다.')
sleep_and_exit()

