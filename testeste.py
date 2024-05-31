import pandas as pd

from datetime import date





#url = f'https://www.kayak.co.uk/flights/LGW-OPO/{departure_date}/{arrival_date}?sort=bestflight_a'

date = date.today()


list_data = [1,2,3,4,5,6,7,8,9,10]

df = pd.DataFrame(list_data)
df.to_csv(f'data{date}.csv', index=False)