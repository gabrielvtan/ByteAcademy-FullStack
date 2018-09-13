#!/usr/bin/env python3

def currency_converter(amount):
    penny = 0.01
    nickel = 0.05
    dime = 0.10
    quarter = 0.25
    oneDollar = 1.00
    fiveDollar = 5.00
    tenDollar = 10.00
    twentyDollar = 20.00
    fiftyDollar = 50.00
    hundredDollar = 100.00

    hundred_need = float(amount//100)
    fifty_need = float((amount%100)//50)
    twenty_need = float(((amount%100)%50)//20)
    ten_need = float((((amount%100)%50)%20)//10)
    five_need = float(((((amount%100)%50)%20)%10)//5)
    one_need = float((((((amount%100)%50)%20)%10)%5)//1)
    quarter_need = float(((((((amount%100)%50)%20)%10)%5)%1)//0.25)
    dime_need = float((((((((amount%100)%50)%20)%10)%5)%1)%0.25)//0.10)
    nickel_need = float(((((((((amount%100)%50)%20)%10)%5)%1)%0.25)%0.10)//0.05)
    penny_need = float((((((((((amount%100)%50)%20)%10)%5)%1)%0.25)%0.10)%0.05)//0.01)

    print('hundreds needed: {}'.format(hundred_need))
    print('fifty needed: {}'.format(fifty_need))
    print('twenty needed: {}'.format(twenty_need))
    print('ten needed: {}'.format(ten_need))
    print('five needed: {}'.format(five_need))
    print('one needed: {}'.format(one_need))
    print('quarter needed: {}'.format(quarter_need))
    print('dime needed: {}'.format(dime_need))
    print('nickel needed: {}'.format(nickel_need))
    print('penny needed: {}'.format(penny_need))

if __name__ == "__main__":
    currency_converter(float(input("How much money are you converting? ")))
