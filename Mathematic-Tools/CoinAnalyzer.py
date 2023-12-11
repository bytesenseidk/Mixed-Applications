# Analyze total bought of crypto, the spending, coin prices & average, earnings and fees
import textwrap

class CoinAnalyzer(object):
    def __init__(self, amounts, prices, transfers, current_amount):
        self.amounts = amounts
        self.prices = prices
        self.transfers = transfers
        self.current_amount = current_amount

    def data_string(self):
        return textwrap.dedent(f"""
        Total Bought:   {round(self.total_bought(), 2)}
        Coin Average:   {round(self.coin_average(), 2)}
        Total Earning:  {round(self.earnings(), 2)}
        """)
    
    def __str__(self):
        return str(self.data_string())

    def total_transfered(self):
        amount = 0
        for buy in self.amounts:
            amount += buy
        return amount
    
    def total_bought(self):
        amount = self.total_transfered()
        amount -= self.spending()
        return amount

    def spending(self):
        amount = 0
        for sell in self.transfers:
            amount += sell
        return amount

    def coin_average(self):
        price = 0
        for _price in self.prices:
            price += _price
        return price / len(self.prices)
    
    def earnings(self):
        return self.current_amount - self.total_bought()
    

if __name__ == "__main__":
    amounts = [979.63, 5219.40, 830.67, 1547.73]
    prices = [0.91, 1.14, 1.32, 1.31]
    transfers = [499.83, 631.10, 999.38, 999.76]
    current_amount = 6100
    print(CoinAnalyzer(amounts, prices, transfers, current_amount))