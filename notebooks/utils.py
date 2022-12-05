import pandas as pd

def get_data(data_path='../data/MotorUniversal_2k_5kHz_SemNorm.xlsx'):
    data = pd.read_excel(data_path)
    columns = ['state'] + [f'current_{i}' for i in range(1, 1001)] + [f'volt_{i}' for i in range(1, 1001)]
    columns

    data.columns = columns

    return data