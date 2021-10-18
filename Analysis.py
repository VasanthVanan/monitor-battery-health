import numpy as np
import matplotlib.pyplot as plt

class LogReader:
    def __init__(self, file_path):
        self.file_path = file_path
    
    def read_lines(self):
        with open(self.file_path, "r") as file:
            lines = file.readlines()
        return lines
    
    def extract_percentages(self, lines):
        percentages = []
        for line in lines:
            percentage = int(line.split("%")[0][-2:])
            percentages.append(percentage)
        return percentages


class ChartPlotter:
    def __init__(self, data):
        self.data = data
    
    def plot_chart(self):
        plt.plot(self.data[-15:])
        plt.show()


if __name__ == "__main__":
    log_reader = LogReader("fiveMinjob.log") # swap file name (fiveMinjob / tenMinjob)
    lines = log_reader.read_lines()
    
    percentage_extractor = log_reader.extract_percentages(lines)
    
    chart_plotter = ChartPlotter(percentage_extractor)
    chart_plotter.plot_chart()
