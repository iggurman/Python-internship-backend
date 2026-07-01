class CricketPlayer:
    def __init__(self, runs, matches):
        self.__runs = runs
        self.__matches = matches

    def add_runs(self, runs):
        self.__runs += runs

    def add_match(self):
        self.__matches += 1

    def batting_average(self):
        if self.__matches == 0:
            return 0
        return self.__runs / self.__matches


c = CricketPlayer(500, 10)

print(c.batting_average())

c.add_runs(100)
c.add_match()

print(c.batting_average())