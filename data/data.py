class JointAttentionData:

    def __init__(self, glass_id, timestamp, index, run_length_output, hit_scan_output):
        self.glass_id = glass_id
        self.timestamp = timestamp
        self.index = index
        self.run_length_output = run_length_output
        self.hit_scan_output = hit_scan_output

    def __repr__(self):
        return str(self.__dict__)


class PupilEyeData:

    def __init__(self, glass_id, timestamp, eye_id, norm_pos, confidence):
        self.glass_id = glass_id
        self.eye_id = eye_id
        self.norm_pos = norm_pos
        self.confidence = confidence
        self.timestamp = timestamp

    def __repr__(self):
        return str(self.__dict__)


class PupilWorldData:

    def __init__(self, glass_id, timestamp, index, frame):
        self.glass_id = glass_id
        self.index = index
        self.frame = frame
        self.timestamp = timestamp

    def __repr__(self):
        return str(self.__dict__)


