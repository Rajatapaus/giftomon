#breeding profitability calculator
#giftomon.io

#profitability % = how much more profitable
#breeding is conpared to buying from market.
#for example, 121% profitability means
#that for every GTO you spent breeding
#you win 1.21 GTO on avarage.

#donate if you like the project and want to buy me a beer!
#(or something else, it is really hot in here)
#0x8185ddf6d5a7c45e1a2542ceddef296295943f78

from collections import OrderedDict

#take account renting, True or False
breeding_rent = True

#gives simpler output
simple_output = False

#descending order
sort_output = True

#rounds to n decimals
#set to None if no rounding
#uses round_if function
rounding_decimals = 2
                            
rarity_costs = OrderedDict([
            #rarity     market_price,   breeding_rent_cost
            ('white',   [0.3,           0.1]),
            ('green',   [0.3,           0.1]),
            ('rare',    [7,             0.5]),
            ('epic',    [350,           10]),
            ('legend',  [3500,          120])
            ])

#for every pair, matching name must
#be found on rarity_costs
breeding_data = OrderedDict([
            #pair            #rare,     epic,   legend, cost_to_breed
            ('green_rare',   [0.171,    0.025,  0.003,  10]),
            ('rare_rare',    [0.269,    0.067,  0.008,  25]),
            ('rare_epic',    [0.392,    0.116,  0.015,  40]),
            ('epic_epic',    [0.723,    0.25,   0.027,  80]),
            ('epic_legend',  [0.62,     0.337,  0.043,  120]),
            ('legend_legend',[0.375,    0.555,  0.07,   200])
            ])

#pair, profit_percentage, breeding_total_cost, gains
outputs = []
for pair, droprates in breeding_data.items():
    #your breedings worth as GTO
    gains = ((droprates[0] * rarity_costs['rare'][0]) + (droprates[1] * rarity_costs['epic'][0])
        + (droprates[2] * rarity_costs['legend'][0]))

    breeding_cost = droprates[-1]

    if breeding_rent:
        rarities = pair.split('_')
        breeding_rent_cost = (rarity_costs[rarities[0]][1] + rarity_costs[rarities[1]][1])
        breeding_total_cost = breeding_rent_cost + breeding_cost
    else:
        breeding_total_cost = breeding_cost
    
    profit = gains - breeding_total_cost

    #profit percentage compared to your initial investment
    profit_percentage = (profit / breeding_total_cost) * 100
    
    #round two decimals
    #profit_percentage = round(profit_percentage, 2)

    outputs.append([pair, profit_percentage, breeding_total_cost, gains])

def round_if(n):
    if type(n) == float and rounding_decimals != None:
        return round(n, rounding_decimals)
    else:
        return n

if sort_output:
    output = outputs.sort(key=lambda x: x[1], reverse=True)
    #output = list(sorted(outputs, key=lambda x: x[2]))

for pair, profit_percentage, breeding_total_cost, gains in outputs:
    if simple_output:
        print(pair, str(round_if(profit_percentage)) + '%')
    else:
        print(pair)
        print('cost:', breeding_total_cost)
        print('return:', round_if(gains))
        print('profits:', str(round_if(profit_percentage)) + '%')
        print('')
