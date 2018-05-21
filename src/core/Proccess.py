import os
import psutil

class ProcessTool:
    def getProcessInfo(self):
        processes = list()
        with os.popen('top -b -n 1') as fd:
            counter = 0
            for line in fd:
                if counter < 7:
                    counter += 1
                    continue
                processes.append(self.processParser(line))
        return processes

    def processParser(self,inputStr):
        process = dict()
        inputConv = inputStr.split(" ")
        inputConv1 = list()
        for item in inputConv:
            if not (str(item).find(" ") >= 0) and item != "":
                inputConv1.append(item.split("\n")[0])
        process["pid"] = inputConv1[0]
        process["user"] = inputConv1[1]
        process['cpu'] = inputConv1[8]
        process['mem'] = inputConv1[9]
        process['name'] = inputConv1[11]
        return process

    def killProcess(self,pid):
        print("pid:"+str(pid))
        if psutil.pid_exists(pid):
            p = psutil.Process(pid)
            p.kill()
            print("kill:"+str(pid))




if __name__ == '__main__':
    tool = ProcessTool()
    tool.getProcessInfo()
