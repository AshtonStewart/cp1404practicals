"""
Ashton Jack Stewart
Practical 07 - project class
"""


class Project:

    #S_D_P = Start_Date_Priority
    #C_E = Cost_Estimate
    #C_P = Completion_Percentage
    def __init__(self, name = "", S_D_P = "", C_E = float, priority = float, C_P = float):
        self.name = name
        self.S_D_P = S_D_P
        self.priority = priority
        self.C_E = C_E
        self.C_P = C_P

    def __str__(self):
        return f'{self.name}, start: {self.S_D_P}, priority: {self.priority}, estimate: ${self.C_E}'

    def is_completed(self):
        return self.C_P >= 100

    def to_line(self):
        return f"{self.name}\t{self.S_D_P}\t{self.priority}\t{self.C_E}\t{self.C_P}"
