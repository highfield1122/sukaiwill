import time
def print_type_writer(msg):
    for s in msg:
        print(s,end='',flush=True)
        time.sleep(1)
def main():
    list='こんにちは'
    for s in list:
        print(s,end='',flush=True)
        time.sleep(1)
