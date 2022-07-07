
class set:
    def __init__(self, abusolute_path="", turns=0):
        self.abusolute_path = abusolute_path
        self.turns = turns


class tunning_base:
    def __init__(self):
        self.TRAIN_SET = [set("", 1),
                          set("", 1),
                          set("", 1)]
        self.TEST_SET = [set("", 1),
                         set("", 1),
                         set("", 1)]

