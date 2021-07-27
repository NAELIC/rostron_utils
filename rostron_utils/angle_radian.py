import numpy as np
class AngleRadian():
    def angle_between(self, v_1, v_2):
            """Returns the angle in radians between vectors 'v1' and 'v2'"""
            v1_u = v_1 / np.linalg.norm(v_1) # unit vector
            v2_u = v_2 / np.linalg.norm(v_2) # unit vector
            sign = 1 if np.cross(v1_u, v2_u) > 0 else -1
            return sign * np.arccos(np.dot(v1_u, v2_u))