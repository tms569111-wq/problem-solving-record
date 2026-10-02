from collections import deque
def solution(begin, target, words):
    word_set = set(words)
    if target not in word_set:
        return 0
    def bfs():
        already = set()
        q = deque([(begin, 0)])
        already.add(begin)
        while q:
            now, count = q.popleft()
            for i in range(len(begin)):
                for j in 'abcdefghijklmnopqrstuvwxyz':
                    new_str = now[0:i] + j + now[i + 1:]
                    if new_str in already:
                        continue
                    if new_str not in word_set:
                        continue
                    if new_str == target:
                        return count + 1
                    q.append((new_str, count + 1))
                    already.add(new_str)
    return bfs()
  