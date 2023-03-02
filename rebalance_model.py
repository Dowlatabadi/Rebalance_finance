from matplotlib import pyplot as plt
import random
# algo base 152$

price_perc_change=100*[-1]
price_perc_change+=500*[.1]
print("sum is : ",100+sum(price_perc_change))
chart_generated=False
prices=[]
def invest_ret():
    random.shuffle(price_perc_change)
    start_price=22000
    global chart_generated
    initial_amount=100
    s1=initial_amount/2
    mins1=s1
    s2=initial_amount/2
#    s0 no rebalance
    s01=initial_amount
    s02=s1
#    print(s1,s2)
    y=0
    for x in price_perc_change:
        s2+=s2*(x/100)
        s02+=s02*(x/100)
        s01+=s01*(x/100)
        if not chart_generated:
            prices.append(s01)
        #rebalance
        if True:#s2>s1:
            mins1=min(s1,mins1)
            s1=(s2+s1)/2
            s2=s1
#        print(s1,s2)
#        print(s01,s02)
     #   print(s1+s2)
    if not chart_generated:
        chart_generated=True
    return (s1+s2,s02+(initial_amount/2),s01,mins1)

s=0
s0=0
s1=0
min1=0
tests=10000
for i in range(tests):
    s+=invest_ret()[0]
    s0+=invest_ret()[1]
    s1+=invest_ret()[2]
    min1+=invest_ret()[3]


print("half exposure + rebalance (avg) ",s/tests)
print("half exposure compound    (avg) ",s0/tests)
print("full exposure compound    (avg) ",s1/tests)
print("min usdt rebalance strategy: ",min1/tests)
plt.plot(prices)
plt.show()
