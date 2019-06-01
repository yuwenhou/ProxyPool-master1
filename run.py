from proxypool.api import app
from proxypool.schedule import Schedule

def main():

    s = Schedule() #运行调度器
    s.run()
    app.run() #运行一个api接口，flask




if __name__ == '__main__':
    main()

