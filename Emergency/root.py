from enum import Enum
class EmergencyType(str, Enum):
    MEDICAL ="medical"
    FIRE ="fire"
    CRIME="crime"
    OTHER="other"
class StatusManagement(str, Enum):
    REPORTED="reported"
    DISPATCHED="dispatched"
    ON_SCENE="on_scene"
    RESOLVED="resolved"
    CLOSED="closed"
    
    