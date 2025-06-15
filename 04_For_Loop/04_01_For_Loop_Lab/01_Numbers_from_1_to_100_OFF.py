import time

with open('file_01.py', 'w') as f:
    for num in range(1, 101):
        f.write(f'print({num})\n')
        f.flush()  # Force write to disk
        # time.sleep(2)
