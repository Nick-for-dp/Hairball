import time


class Record:
    def __init__(self,
                 pet,
                 user,
                 record_time,
                 type_flag,
                 address,
                 reward,
                 state_flag=1):
        # todo 自动生成id
        self.pet = pet
        self.user = user
        self.type_flag = type_flag
        # 0表示流浪宠物信息 1表示寻找宠物信息
        if type_flag == 1:
            self.lost_time = record_time
            self.report_time = None
        else:
            self.lost_time = None
            self.report_time = record_time
        self.address = address
        self.reward = reward
        self.state_flag = state_flag
        # 1表示还未找到宠物或流浪宠物未归家 0表示记录被删除 2表示找到宠物或流浪宠物归家
        self.state_flag = state_flag
        self.finish_time = None

    def set_state_flag(self, now_state_flag):
        assert now_state_flag in [0, 1, 2], "The input state flag is illegal"
        self.state_flag = now_state_flag
        if self.state_flag == 2:
            self.finish_time = time.strftime('%Y-%m-%d %H:%M', time.localtime(time.time()))
