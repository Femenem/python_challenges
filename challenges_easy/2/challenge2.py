#!usr/bin/python3
import os, sys

bitcoinValue = 242
bitcoinsNeeded = input("How many bitcoins do you want? ")
bitcoinsNeeded = float(bitcoinsNeeded)
total = bitcoinValue*bitcoinsNeeded
print("You need ",int(total)," in dollars to get this many")