from datetime import datetime
from collections import OrderedDict

def log(s):
    print s

class TimerArray(object):
    def __init__(self):
        self.timers = OrderedDict()

    def click(self, timer_code, log_on_click=False, continue_where_stopped=False):
        if timer_code not in self.timers.keys():
            timer = Timer()
            self.timers[timer_code] = timer
            running = False
        else:
            timer = self.timers[timer_code]

        if not timer.running:
            timer.start_timer(continue_where_stopped)
        else:
            timer.stop_timer()
            if log_on_click:
                seconds = timer.get_current_reading()
                log('%s: %s seconds' % (timer_code, seconds))
    
    def __repr__(self):
        return str(self.timers)

class Timer(object):
    def __init__(self):
        self.running = False
        self.start_time = datetime.now()
        self.last_reading = 0
    
    def get_current_reading(self):
        if self.running:
            return (datetime.now() - self.start_time).seconds
        else:
            return self.last_reading
    
    def start_timer(self, continue_where_stopped=False):
        self.running = True
        if not continue_where_stopped:
            self.start_time = datetime.now()
        
    def stop_timer(self):
        self.last_reading = self.get_current_reading()
        self.running = False

    def __repr__(self):
        return 'running: %s, current_reading: %s' % (self.running, self.get_current_reading())
