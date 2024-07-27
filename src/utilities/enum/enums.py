from enum import Enum

from decimal import Decimal


class TrainingType(Enum):
    TYPE_A = "Type A"
    TYPE_B = "Type B"
    TYPE_C = "Type C"
    TYPE_D = "Type D"
    TYPE_E = "Type E"


class Gender(Enum):
    MALE = "male"
    FEMALE = "female"


class ManGeb(Enum):
    f1 = Decimal("13.75")
    f2 = Decimal("5")
    f3 = Decimal("6.76")
    f4 = Decimal("66.5")


class WomanGeb(Enum):
    f1 = Decimal("9.56")
    f2 = Decimal("1.85")
    f3 = Decimal("4.68")
    f4 = Decimal("665")


class ActivityLevel(Enum):
    SEDENTARY = Decimal("1.2")
    LIGHTLY_ACTIVE = Decimal("1.375")
    MODERATELY_ACTIVE = Decimal("1.55")
    VERY_ACTIVE = Decimal("1.725")
    EXTREMELY_ACTIVE = Decimal("1.9")
