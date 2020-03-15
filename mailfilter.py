import os

class Mailfilter:
    def __init__(self):
        self.__filterinstances = []

    def add_filter(self, string, script_on_detection):
        self.__filterinstances.append(Filterinstance(string, script_on_detection))

    def get_filter_list(self):
        retstr = ""

        for inst in self.__filterinstances:
            retstr = retstr + " " +  inst.filterstring

        return retstr.strip()

    def do_filter(self, inputstr):
        for inst in self.__filterinstances:
            if inst.filterstring in inputstr:
                inst.set_script_pending()
                return True
        return False

    def run_pending_scripts(self):
        for inst in self.__filterinstances:
            inst.run_script()

class Filterinstance:
    def __init__(self, string, script_on_detection):
        self.filterstring = string
        self.script = script_on_detection
        self.script_pending = False

    def set_script_pending(self):
        self.script_pending = True

    def run_script(self):
        if self.script_pending:
            os.system(self.script)
            self.script_pending = False


if __name__ == "__main__":
    filt = Mailfilter()
    filt.add_filter("kanapki", "~/Sounds/playsound.sh kanapki")
    filt.add_filter("slimak", "~/Sounds/playsound.sh slimak")
    filt.add_filter("ślimak", "~/Sounds/playsound.sh slimak")
    filt.add_filter("sushi", "~/Sounds/playsound.sh sushi")
    filt.add_filter("catering", "~/Sounds/playsound.sh catering50")

    filt.do_filter("ślimak")
    filt.do_filter("kanapki")

    filt.run_pending_scripts()

