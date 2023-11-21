class TimeMap:

    def __init__(self):
        self.dic = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.dic.keys():
            self.dic[key].append([value, timestamp])
        else:
            self.dic[key] = [[value, timestamp]]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.dic:
            return ""
        left, right = 0, len(self.dic[key]) - 1
        while left <= right:
            curr = (right + left) // 2
            if self.dic[key][curr][1] == timestamp:
                return self.dic[key][curr][0]
            elif self.dic[key][curr][1] < timestamp:
                left = curr + 1
            else:
                right = curr - 1
        if right >= 0:
            return self.dic[key][right][0]
        return ""

