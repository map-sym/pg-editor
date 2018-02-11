#! /usr/bin/python3

# author: Krzysztof Czarnecki
# email: czarnecki.krzysiek@gmail.com
# application: EMPER simulator
# brief: economic and strategic simulator
# opensource licence: GPL-3.0

class EmpNation:
    def __init__(self, name, conf):
        self.name = str(name)
        self.conf = conf
        
        if float(conf["acceptability"]) <= 0: raise ValueError("acceptability")
        if float(conf["productivity"]) <= 0: raise ValueError("productivity")        
        if float(conf["fertility"]) <= 0: raise ValueError("fertility")
        if float(conf["stability"]) <= 0: raise ValueError("stability")
        if float(conf["prowess"]) <= 0: raise ValueError("prowess")

    def get_config(self):
        return self.conf
