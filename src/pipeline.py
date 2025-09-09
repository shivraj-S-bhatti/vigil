import time
from rules import zscore_anomalies

def run_stream(df, thresh, on_alert, stop_flag):
    idx = 0
    while not stop_flag["stop"] and idx < len(df):
        window = df.iloc[:idx+1]["value"].tolist()
        if len(window) >= 50:
            hits = zscore_anomalies(window, thresh=thresh, window=min(200, len(window)//2))
            if hits and hits[-1] == idx:
                on_alert(f"[ALERT] {df.iloc[idx]['ts']} value={df.iloc[idx]['value']:.4f}")
        idx += 1
        time.sleep(0.02)  # ~50 Hz playback; tweak for demo
