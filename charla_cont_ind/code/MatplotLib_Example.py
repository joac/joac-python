#!-*- coding: utf8 -*-

import sys
from PyQt4 import QtGui

from matplotlib.figure import Figure
from matplotlib.backends.backend_qt4agg \
    import FigureCanvasQTAgg as FigureCanvas
import psutil as p

MAXITERS = 12 

class CPUMonitor(FigureCanvas):

    def __init__(self):
        self.before = self.prepare_cpu_usage()
        self.fig = Figure()
        self.ax = self.fig.add_subplot(111)
        FigureCanvas.__init__(self, self.fig)
        self.ax.set_xlim(0,60)
        self.ax.set_ylim(0,100)
        self.ax.get_yaxis().grid(True)
        self.ax.set_autoscale_on(False)
        self.user, self.nice, self.sys, self.idle = [], [], [], []
        self.l_user, = self.ax.plot([], self.user, label='User %')
        self.l_nice, = self.ax.plot([], self.nice, label='Nice %')
        self.l_sys,  = self.ax.plot([], self.sys,  label='Sys %' )
        self.l_idle, = self.ax.plot([], self.idle, label='Idle %')
        self.ax.legend()
        self.fig.canvas.draw()
        self.n = 0
        self.timerEvent(None)
        self.timer = self.startTimer(500)
    
    def prepare_cpu_usage(self):
        
        t=p.cpu_times()

        if hasattr(t, 'nice'):
            return [t.user, t.nice, t.system, t.idle]
        else:
            return [t.user, 0, t.system, t.idle]

    def get_cpu_usage(self):
        now = self.prepare_cpu_usage()
        
        delta = [now[i] - self.before[i] for i in range(len(now))]
        
        total = sum(delta)
        self.before = now
        return [(100.0*dt)/total for dt in delta]

    def timerEvent(self, evt):
        result = self.get_cpu_usage()
        lista = ['user', 'nice', 'sys', 'idle']
        if len(self.user) >= MAXITERS:
            self.n +=1
        for number,field in enumerate(lista):
            a = getattr(self, field)
            if len(a) >= MAXITERS:
                a.pop(0)
                
            n=self.n
            a.append(result[number])
            field = 'l_%s' % field
            getattr(self, field).set_data(range(n, len(a)+n), a)
        self.ax.set_xlim(n, len(self.user) + n)
        self.fig.canvas.draw()


app = QtGui.QApplication(sys.argv)
widget = CPUMonitor()

widget.setWindowTitle("30 ultimos segundos de actividad del procesador")
widget.show()
sys.exit(app.exec_())
