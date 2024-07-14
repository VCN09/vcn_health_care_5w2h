class Tarefa:
    def __init__(self, what, why, wher, whe, who, how, how_much, priority, statu):
        self.what = what
        self.why = why
        self.wher = wher
        self.whe = whe
        self.who = who
        self.how = how
        self.how_much = how_much
        self.priority = priority
        self.statu = statu

    def __str__(self):
        return f"What: {self.what} | Why: {self.why} | Wher: {self.wher} | Whe: {self.whe} | Who: {self.who} | " \
               f"How: {self.how} | How Much: {self.how_much} | Priority: {self.priority} | Statu: {self.statu}"
