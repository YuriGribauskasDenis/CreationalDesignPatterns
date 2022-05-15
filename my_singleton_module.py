from pathlib import Path

path = ''

def set_path(new_path):
    global path
    path = new_path

def log_to_path(text):
    global path
    try:
        with open(path, 'a') as f:
            f.write(f'{text}\n')
    except IOError:
        print('set correct path')

if __name__ == "__main__":
    set_path(r'C:\tmp\python_tut_practice\patterns\log0.txt')
    log_to_path('hello')
    set_path(r'C:\tmp\python_tut_practice\patterns\log1.txt')
    log_to_path('i know you')
    set_path(r'C:\tmp\python_tut_practice\patterns\log0.txt')
    log_to_path('i am your friend')