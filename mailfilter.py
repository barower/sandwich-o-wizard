import subprocess

class Mailfilter:
    def __init__(self):
        self.__subject_filters = []

    def add_filter(self, string, script_on_detection):
        self.__subject_filters.append(SubjectFilter(string, script_on_detection))

    def get_filter_list(self):
        retstr = ""

        for inst in self.__subject_filters:
            retstr = retstr + " " +  inst.filterstring

        return retstr.strip()

    def do_filter(self, inputstr):
        for inst in self.__subject_filters:
            if inst.filterstring in inputstr:
                inst.set_script_pending()
                return True
        return False

    def run_pending_scripts(self):
        for inst in self.__subject_filters:
            inst.run_script()

class SubjectFilter:
    def __init__(self, string, script_on_detection):
        self.filterstring = string
        self.script = script_on_detection
        self.script_pending = False

    def set_script_pending(self):
        self.script_pending = True

    def run_script(self):
        if self.script_pending:
            subprocess.check_call(self.script.split())
            self.script_pending = False


if __name__ == "__main__":
    filt = Mailfilter()
    filt.add_filter("kanapki", "play /home/pi/Sounds/kanapkiv3.wav -q")
    filt.add_filter("slimak", "play /home/pi/Sounds/slimakv3.wav -q")
    filt.add_filter("ślimak", "play /home/pi/Sounds/slimakv3.wav -q")
    filt.add_filter("sushi", "play /home/pi/Sounds/sushiv3.wav -q")
    filt.add_filter("catering", "play /home/pi/Sounds/catering50v3.wav -q")

    filt.do_filter("ślimak")
    filt.do_filter("kanapki")

    filt.run_pending_scripts()

