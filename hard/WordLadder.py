class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        length = len(beginWord)
        graph = collections.defaultdict(list)
        wordList.append(beginWord)

        for word in wordList:
            for j in range(length):
                temp = word[:j] + '.' + word[j+1:]
                graph[temp].append(word)
        c = 1 
        q = deque([beginWord])
        visited = set()

        while q:
            for i in range(len(q)):
                c_word = q.popleft()
                visited.add(c_word)
                if c_word == endWord:
                    return c
                for j in range(length):
                    temp = c_word[:j] + '.' + c_word[j+1:]
                    if temp in graph:
                        for word in graph[temp]:
                            if word not in visited:
                                q.append(word)
            c += 1
        return 0
