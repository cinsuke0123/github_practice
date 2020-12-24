#!-*-conding:utf-8-*-
import matplotlib.pyplot as plt
from abc import ABCMeta, abstractmethod
__all__ = ["lineplot", "scatter"]

# Graphクラスを継承しているクラスのplotメソッドのplotという名を統一
class Graph(metaclass = ABCMeta):
    @abstractmethod
    def plot(self):
        pass

class lineplot(Graph):

    def __init__(self, xlim, ylim, filename):
        self.xlim = xlim
        self.ylim = ylim
        self.filename = filename

    def plot(self, x, y):
        plt.grid()
        plt.plot(x, y)
        plt.xlim(self.xlim), plt.ylim(self.ylim)
        plt.savefig(self.filename)

class scatter(Graph):

    def __init__(self, xlim, ylim, filename):
        self.xlim = xlim
        self.ylim = ylim
        self.filename = filename

    def plot(self, x, y):
        plt.grid()
        plt.scatter(x, y)
        plt.xlim(self.xlim), plt.ylim(self.ylim)
        plt.savefig(self.filename)
