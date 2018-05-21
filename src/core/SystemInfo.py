
class SystemInfo:
    ''' 获取Linux系统主机名称 '''
    def getHostname(self):
        with open('/proc/version') as fd:
            hostname = "unkown"
            for line in fd:
                hostname = line.split("(")[0]
        return {'hostname':hostname}
    def getGccVersion(self):
        gccVersion = "unkown"
        with open('/proc/version') as fd:
            for line in fd:
                gccVersion = line.split("(gcc")[1]
                gccVersion = gccVersion.split("#")[0]
        return {'gccVersion':gccVersion}

    ''' 获取Linux系统的版本信息 '''
    def getOsVersion(self):
        osver = "unkown"
        with open('/etc/issue') as fd:
            for line in fd:
                osver = line.split('\\n')[0]
                break
        return {'osver':osver}

    ''' 获取CPU的型号和CPU的核心数 '''
    def getCpu(self):
        num = 0
        with open('/proc/cpuinfo') as fd:
            for line in fd:
                if line.startswith('processor'):
                    num += 1
                if line.startswith('model name'):
                    cpu_model = line.split(':')[1].strip().split()
                    cpu_model = cpu_model[0] + ' ' + cpu_model[2]  + ' ' + cpu_model[-1]
        return {'cpu_num':num, 'cpu_model':cpu_model}