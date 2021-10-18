from datetime import datetime, date
import re

class TextColor:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class BannerPrinter:
    def __init__(self):
        pass
    
    def print_banner(self):
        print(TextColor.OKCYAN + "    __  ___            _ __                __          __  __                 " + TextColor.ENDC)
        print(TextColor.OKCYAN + "   /  |/  /___  ____  (_) /_____  _____   / /_  ____ _/ /_/ /____  _______  __" + TextColor.ENDC)
        print(TextColor.OKGREEN + "  / /|_/ / __ \/ __ \/ / __/ __ \/ ___/  / __ \/ __ `/ __/ __/ _ \/ ___/ / / /" + TextColor.ENDC)
        print(TextColor.WARNING + " / /  / / /_/ / / / / / /_/ /_/ / /     / /_/ / /_/ / /_/ /_/  __/ /  / /_/ / " + TextColor.ENDC)
        print(TextColor.OKCYAN + "/_/  /_/\____/_/ /_/_/\__/\____/_/     /_.___/\__,_/\__/\__/\___/_/   \__, /  " + TextColor.ENDC)
        print(TextColor.OKCYAN + "                                                                     /____/   " + TextColor.ENDC)

class LogParser:
    def __init__(self, log_file):
        self.log_file = log_file

    def read_content(self):
        with open(self.log_file, 'r') as f:
            return f.read()

    def read_lines(self):
        with open(self.log_file, 'r') as f:
            return f.readlines()

class BatteryAnalyzer:
    def __init__(self, text, lines):
        self.text = text
        self.lines = lines

    def analyze_battery(self):
        compare = int(re.findall(r'\d+', self.lines[2])[0])
        battery_percentage = []
        log_date = []

        for i in self.text:
            if compare == int(i[-3:]):
                log_date.append((datetime.strptime(i.strip()[:11], "%d-%b-%Y"), i.strip()[:11]))
                battery_percentage.append(int(i[-3:].strip()))
                compare = compare - 1

        today_date = datetime.strptime(date.today().strftime("%d-%b-%Y"), "%d-%b-%Y")

        return battery_percentage, log_date, compare, today_date

class BatteryPrinter:
    def __init__(self, battery_percentage, log_date, compare, today_date):
        self.battery_percentage = battery_percentage
        self.log_date = log_date
        self.compare = compare
        self.today_date = today_date

    def print_battery_info(self):
        print("-------------------------------------")
        print("   Date     Capacity     Elapsed Days")
        print("-------------------------------------")

        for i in range(len(self.battery_percentage)):
            if len(self.battery_percentage) - 1 > i:
                if i == 0:
                    print(self.log_date[i][1] + "\t" + str(self.battery_percentage[i]) + "\t   -start-")
                else:
                     print(self.log_date[i][1] + "\t" + str(self.battery_percentage[i]) + "\t   " + str(
                        (self.log_date[i][0] - self.log_date[i - 1][0]))[:-9])

        print("---Today" + "---\t" + str(self.compare + 1) + "\t   " + str((self.today_date - self.log_date[-2][0]))[:-9])

class BatteryStatusAnalyzer:
    def __init__(self, log_file):
        self.log_parser = LogParser(log_file)
        self.banner_printer = BannerPrinter()
        self.battery_analyzer = None
        self.battery_printer = None

    def analyze_battery_status(self):
        content = self.log_parser.read_content()
        lines = self.log_parser.read_lines()
        text = str(content).split("%")[:-1]

        try:
            self.battery_analyzer = BatteryAnalyzer(text, lines)
            battery_percentage, log_date, compare, today_date = self.battery_analyzer.analyze_battery()

            self.banner_printer.print_banner()

            self.battery_printer = BatteryPrinter(battery_percentage, log_date, compare, today_date)
            self.battery_printer.print_battery_info()

        except IndexError:
            print(TextColor.FAIL + "Error: Please run this script after few months of use." + TextColor.ENDC)

if __name__ == "__main__":
     log_file = 'cycleStatus.log'
     analyzer = BatteryStatusAnalyzer(log_file)
     analyzer.analyze_battery_status()

