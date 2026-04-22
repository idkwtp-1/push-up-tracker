import json
import os
from datetime import datetime

class DataManager:
    def __init__(self, data_file='pushup_data.json'):
        self.data_file = data_file
        self.data = self.load_data()

    def load_data(self):
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r') as f:
                    return json.load(f)
            except:
                pass
        return {
            'target_minutes': 30,
            'pushup_count': 0,
            'sound_enabled': True,
            'autostart_enabled': False,
            'pushup_history': [],
            'video_index': 0,
            'fastest_100_time': None
        }

    def save_data(self, **kwargs):
        self.data.update(kwargs)
        with open(self.data_file, 'w') as f:
            json.dump(self.data, f, indent=4)

    def get(self, key, default=None):
        return self.data.get(key, default)

    def set(self, key, value):
        self.data[key] = value
        self.save_data()

    def reset_progress(self):
        self.data['pushup_count'] = 0
        self.save_data()

    def get_next_video_index(self):
        idx = self.data.get('video_index', 0)
        new_idx = (idx + 1) % 3
        self.set('video_index', new_idx)
        return idx

    def update_fastest_100_time(self, time_seconds):
        current = self.data.get('fastest_100_time')
        if current is None or time_seconds < current:
            self.set('fastest_100_time', time_seconds)
