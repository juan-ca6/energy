import requests

def save_df(latitude,longitude):
    parameters = ['T2M','T10M','WD10M','WS10M','QV10M','RH2M','CLOUD_AMT','CLOUD_AMT_NIGHT','RHOA']
    parameters_subset = ','.join(parameters[:20])
    
    community = 'RE'

    start = '20200101'
    end = '20240601'

    url = f'https://power.larc.nasa.gov/api/temporal/daily/point?parameters={parameters_subset}&community={community}&longitude={longitude}&latitude={latitude}&start={start}&end={end}&format=CSV'

    response = requests.get(url)

    data = response.text
    data_parts = data.split('-END HEADER-')

    actual_data = data_parts[1].strip()

    path = f'.csv'

    with open(path, 'w') as f:
        f.write(actual_data)
