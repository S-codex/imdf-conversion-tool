from enum import Enum


class RestrictionCategEnum(Enum, str):
    EMPLOYEESONLY = "employeesonly"
    RESTRICTED = "restricted"