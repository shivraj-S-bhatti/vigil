import pandas as pd

def load_time_series(path:str, ts_col:str=None, val_col:str=None):
    df = pd.read_csv(path)
    if ts_col is None: ts_col = df.columns[0]
    if val_col is None: val_col = df.columns[1]
    df[ts_col] = pd.to_datetime(df[ts_col], errors="coerce")
    df = df.dropna(subset=[ts_col, val_col])
    return df[[ts_col, val_col]].rename(columns={ts_col:"ts", val_col:"value"})
