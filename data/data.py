class JointAttentionData:

    def __init__(self, glass_id, timestamp=None, index=None, run_length_output=None, hit_scan_output=None):
        self.glass_id = glass_id
        self.timestamp = timestamp
        self.index = index
        self.run_length_output = run_length_output
        self.hit_scan_output = hit_scan_output

    def update(self, timestamp, index, run_length_output, hit_scan_output):
        self.timestamp = timestamp
        self.index = index
        self.run_length_output = run_length_output
        self.hit_scan_output = hit_scan_output

    def __repr__(self):
        return str(self.__dict__)


class PupilEyeData:

    def __init__(self, glass_id, eye_id, timestamp=None, norm_pos=None, confidence=None):
        self.glass_id = glass_id
        self.eye_id = eye_id
        self.timestamp = timestamp
        self.norm_pos = norm_pos
        self.confidence = confidence

    def update(self, timestamp, norm_pos, confidence):
        self.timestamp = timestamp
        self.norm_pos = norm_pos
        self.confidence = confidence

    def __repr__(self):
        return str(self.__dict__)


class PupilWorldData:

    def __init__(self, glass_id, timestamp=None, index=None, frame=None):
        self.glass_id = glass_id
        self.index = index
        self.frame = frame
        self.timestamp = timestamp

    def update(self, timestamp, index, frame):
        self.timestamp = timestamp
        self.index = index
        self.frame = frame

    def __repr__(self):
        return str(self.__dict__)


