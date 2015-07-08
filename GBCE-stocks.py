# This document contain source code for a recruitment test in JP Morgan
# This code works with python 2.7
# Description and author's remarks:
# 1. All classes are stored in single file, to reduce chance for human error during copying etc.
# 2. Brief description of every class is added
# 3. Python is not and never was my primary language
# Code written by Lukasz Biedak (github.com/lubiedak)

import random
import time
import datetime
import threading

transactions = []
stocks = [
{"Symbol": "TEA", "Type": 'C', "LD": 0,  "FD": 0,    "PV": 100, "Price": 100.0, "TrCo": 0}, #TrCo - Transactions counter
{"Symbol": "POP", "Type": 'C', "LD": 8,  "FD": 0,    "PV": 100, "Price": 120.0, "TrCo": 0},
{"Symbol": "ALE", "Type": 'C', "LD": 23, "FD": 0,    "PV": 60 , "Price": 360.0, "TrCo": 0},
{"Symbol": "GIN", "Type": 'P', "LD": 8,  "FD": 0.02, "PV": 100, "Price": 150.0, "TrCo": 0},
{"Symbol": "JOE", "Type": 'C', "LD": 13, "FD": 0,    "PV": 250, "Price": 200.0, "TrCo": 0}]

def GetStock(symbol):
    """Global function for retrieving stock from list"""
    return (i for i in stocks if i["Symbol"] == symbol).next()

class PriceUpdater:
    """Class responsible for updating price of a stock"""
    def updatePrice(self, transaction):
        if not any(t.stockSymbol == transaction.stockSymbol for t in transactions):
            self.firstTransactionForGivenStock(transaction)
        else:
            self.computePrice(transaction)
            
    def firstTransactionForGivenStock(self, transaction):
        stock = GetStock(transaction.stockSymbol)
        stock["Price"] = transaction.tradePrice
        stock["TrCo"] = transaction.quantity
        
    def computePrice(self, tr):
        stock = GetStock(tr.stockSymbol)
        #We modify existing price following formula given in test description
        stock["Price"] = (stock["Price"]*stock["TrCo"] + tr.tradePrice*tr.quantity)/(stock["TrCo"] + tr.quantity)
        stock["TrCo"] += tr.quantity

        
class Transaction:
    """Representation of transaction"""
    def __init__(self, stockSymbol, type, quantity, tradePrice):
        self.date = time.time()
        self.stockSymbol = stockSymbol
        self.type = type
        self.quantity = quantity
        self.tradePrice = tradePrice
    
    def __str__(self):
        st = datetime.datetime.fromtimestamp(self.date).strftime('%Y-%m-%d %H:%M:%S')
        
        return (st + "\t"
        + self.stockSymbol + "\t"
        + self.type + "\t"
        + str(self.quantity) + "\t"
        + str(self.tradePrice))
        

class TransactionsGenerator(threading.Thread):
    """Class responsible for generating transactions to make registering quicker"""
    def __init__(self, transactionsPerMinute, timeOfExecution):
        threading.Thread.__init__(self)
        self.daemon = True
        
        self.transactionsPerMinute = (transactionsPerMinute, 500)[transactionsPerMinute > 500]
        self.timeOfExecution = (timeOfExecution, 15)[timeOfExecution > 15]
        self.priceUpdater = PriceUpdater()
        
    def stopGenerating(self):
        self.running = False
    
    def run(self):
        start = time.time()
        self.running = True
        print("Starting transaction generator in background for " + str(self.timeOfExecution)
        + " minutes with " + str(self.transactionsPerMinute) + " transactions per minute.")
        while(self.running):
            transaction = self.generateRandomTransaction()
            
            self.priceUpdater.updatePrice(transaction)
            
            transactions.append(transaction)
            
            time.sleep(60.0/self.transactionsPerMinute)
            
            if (time.time()-start)/60 > self.timeOfExecution:
                self.running = False
        
    def generateRandomTransaction(self):
        symbol = stocks[random.randint(0, len(stocks)-1)]["Symbol"]
        type = ("Buy","Sell")[random.randint(0,1)==0]
        quantity = random.randint(1, 1000)
        
        #Generating transaction price
        actualPrice = GetStock(symbol)["Price"]
        sign = (-1,1)[type=="Buy"] #selling/buying is cheaper/pricey than actual stock price
        tradePrice = actualPrice + sign * actualPrice * 0.07 * random.random()
        
        return Transaction(symbol, type, quantity, tradePrice)
        

class MarketWatch:
    """Class responsible for computing and displaying market info"""
    def __init__(self):
        self.header = "Symbol\tPrice\tNo. Tr.\tDiv. Yield\tP/E Ratio"
    
    def presentData(self):
        print(self.header)
        for stock in stocks:
            dy = self.computeDividendYield(stock)
            pe = self.computePE(stock)
            line = (stock["Symbol"] + "\t"
            + ("%0.2f" % stock["Price"]) + "\t"
            + str(stock["TrCo"]) + "\t"
            + ("%0.5f" % dy) + "\t\t"
            + ("%0.2f" % pe))
            
            print line
        print("GBCE Index: " + str(self.computeIndex()))
        
    def computeIndex(self):
        index = 1.0
        for s in stocks:
            index*=s["Price"]
        return index**(1.0/len(stocks))
            
    def computeDividendYield(self, stock):
        if(stock["Type"] == 'C'):
            return float(stock["LD"])/stock["Price"]
        else:
            return stock["FD"]*stock["PV"]/stock["Price"]
    
    def computePE(self, stock):
        if stock["LD"] != 0:
            return stock["Price"]/stock["LD"]
        else:
            return 0


class UI:
    """Class responsible for interaction with user"""
    def __init__(self):
        self.menu = [
        "Buy stocks",
        "Sell stocks",
        "Start Transactions Generator",
        "Display Market Data",
        "Display All Transactions",
        "Quit"]
        
        self.mw = MarketWatch()
        self.priceUpdater = PriceUpdater()
        
    def displayMenu(self):
        i = 1
        print
        for line in self.menu:
            print(str(i) + ". " + line)
            i+=1
    
    def addTransaction(self, type):
        self.mw.presentData()
        symbol = ""
        q = 0
        price = 0
        
        correctChoice = False
        while(correctChoice==False):
            symbol = raw_input('Choose stock symbol you want to ' + type + ': ')
            if not any(s["Symbol"] == symbol for s in stocks):
                print("We don't have this type of stock. Try again.")
            else:
                correctChoice = True
                
        correctChoice = False
        while(correctChoice==False):
            try:
                q = int(raw_input('How many[1-1000] stocks you want to ' + type + ': '))
                if q<1 or q>1000:
                    print("Out of bounds [1-1000]")
                else:
                    correctChoice = True
            except(ValueError):
                print("This is not a number. Try again")
            
        correctChoice = False
        while(correctChoice==False):
            try:
                price = float(raw_input('How much a stock is worth for you : '))
                correctChoice = True
            except(ValueError):
                print("This is not a number. Try again")
        
        print("Transaction has been registered.")
        tr = Transaction(symbol,type,q,price)
        self.priceUpdater.updatePrice(tr)
        transactions.append(tr)
            
    def main(self):
        choice = 0
        while(choice!=len(self.menu)):
            self.displayMenu()
            correctChoice = False
            while(correctChoice==False):
                try:
                    choice = int(input('Choose one option: '))
                    correctChoice = True
                except(ValueError):
                    print("This is not a number")
                
            if(choice == 1):
                self.addTransaction("Buy")
            elif(choice==2):
                self.addTransaction("Sell")
            elif(choice==3):
                tg = TransactionsGenerator(100, 2)
                tg.start()
            elif(choice==4):
                self.mw.presentData()
            elif(choice==5):
                for tr in transactions:
                    print(str(tr))
            elif(choice==6):
                print "Bye, bye!\n"
                break
            else:
                print "No such option"
        

ui = UI()
ui.main()