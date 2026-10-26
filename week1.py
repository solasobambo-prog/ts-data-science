region = 'Lagos'            # str  - text, like a text cell
revenue = 1250000           # int  - whole numbers
growth_rate = 0.147         # float - decimals
is_active = True            # bool - TRUE/FALSE, exactly like Excel
 
print(region, revenue, growth_rate, is_active)
print(type(growth_rate))    # <class 'float'>

regions = ['Lagos', 'Abuja', 'Kano', 'Ibadan']   # a list
regions[0]        # 'Lagos'   - first item, index zero
regions[-1]       # 'Ibadan'  - last item, negative counts back
len(regions)      # 4
regions.append('Enugu')          # add to the end
 
sales_lookup = {'Lagos': 1250000, 'Abuja': 980000, 'Kano': 640000}
sales_lookup['Lagos']             # 1250000 - the VLOOKUP move
sales_lookup['Abuja'] = 1010000   # update a value
'Kano' in sales_lookup            # True - does the key exist?


rows = [
    {'region': 'Lagos', 'revenue': 1250000, 'units': 3100},
    {'region': 'Abuja', 'revenue': 980000,  'units': 2500},
    {'region': 'Kano',  'revenue': 640000,  'units': 1800},
]
rows[1]['region']          # 'Abuja' - row 1, column 'region'
rows[0]['revenue'] + rows[1]['revenue'] + rows[2]['revenue']

revenue = 980000
if revenue >= 1000000:
    tier = 'A'
elif revenue >= 700000:
    tier = 'B'
else:
    tier = 'C'
print(tier)              # 'B'
