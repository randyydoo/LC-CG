class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        bank = set(bank)
        visited = set()
        q = collections.deque([startGene])
        c = 0

        while q:
            for _ in range(len(q)):
                gene = q.popleft()
                visited.add(gene)
                if gene == endGene:
                    return c
                for i in range(len(gene)):
                    for mut in ['A', 'C', 'G', 'T']:
                        temp_gene = gene[:i] + mut + gene[i+1:]
                        if temp_gene != gene and temp_gene not in visited and temp_gene in bank:
                            q.append(temp_gene)
            c += 1

        return -1
