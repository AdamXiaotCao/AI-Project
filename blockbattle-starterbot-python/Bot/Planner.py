from Bot.Strategies.RandomStrategy import RandomStrategy
from Bot.Strategies.OurStrategy import OurStrategy

def create(strategyType, game, coefficients):
    switcher = {
        "random": RandomStrategy(game),
        "my": OurStrategy(game, coefficients)
    }

    strategy = switcher.get(strategyType.lower())

    return Planner(strategy)

class Planner:
    def __init__(self, strategy):
        self._strategy = strategy

    def makeMove(self):
        return self._strategy.choose()
