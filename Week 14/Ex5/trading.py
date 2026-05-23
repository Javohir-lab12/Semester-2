from abc import ABC, abstractmethod

class TradingStrategy(ABC):
    @abstractmethod
    def decide(self, price):
        pass

class BuyLowStrategy(TradingStrategy):
    def __init__(self, threshold):
        self.threshold = threshold
    def decide(self, price):
        return 'BUY' if self.threshold > price else 'HOLD'
    
class SellHighStrategy(TradingStrategy):
    def __init__(self, threshold):
        self.threshold = threshold
    def decide(self, price):
        return 'SELL' if self.threshold > price else 'HOLD'
    
class AlwaysHoldStrategy(TradingStrategy):
    def decide(self, price):
        return 'HOLD'
    
class Observer(ABC):
    @abstractmethod
    def update(price):
        pass

class Trader(Observer):
    def __init__(self, name, strategy: TradingStrategy):
        self.name = name
        self.strategy = strategy
    def update(self, price):
        action = self.strategy.decide(price)
        print(f'{self.name}: {action} at {price}')
    
class PriceLogger(Observer):
    def __init__(self):
        self.history = []
    def update(self, price):
        self.history.append(price)
        print(f'📒 Logger: recorded ${price}(total: {len(self.history)})')

class Stock:
    def __init__(self, symbol):
        self.symbol = symbol
        self.observers = []
    def subscribe(self, observer: Observer):
        self.observers.append(observer)
    def unsubscribe(self, observer: Observer):
        self.observers.remove(observer)
    def set_price(self, price):
        print(f'📊 <symbol>: ${price}')
        for observer in self.observers:
            observer.update(price)

apple = Stock("AAPL")

apple.subscribe(Trader("Alisher", BuyLowStrategy(100)))
apple.subscribe(Trader("Sevara",  SellHighStrategy(150)))
apple.subscribe(Trader("Aziz",    AlwaysHoldStrategy()))
apple.subscribe(PriceLogger())

for price in [120, 90, 160, 140]:
    apple.set_price(price)