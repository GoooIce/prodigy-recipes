from multiprocessing import Process
import os
import prodigy

def info(title, port):
    print(title)
    print(f"module name: {__name__}")
    print(f"parent process: {os.getppid()}")
    print(f"process id: {os.getpid()} \n")
    prodigy.serve(
        "ner.manual", 
        "gsr_is_protest",  # db
        "en_core_web_sm",
        "data/raw_github-issue-titles.jsonl", # input file
        port=port  # port
    )

def f(name, port):
    info("function f", port)
    print('hello', name)

if __name__ == '__main__':
    # info("main line")
    for i in range(3):
        p = Process(target=f, args=('bob', 9010+i))
        p.start()
    