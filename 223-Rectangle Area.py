class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        x = (min(G, C) - max(A, E)) if min(G, C) > max(A, E) else 0
        y = (min(D, H) - max(B, F)) if min(D, H) > max(B, F) else 0
        return (D - B) * (C - A) + (G -E) * (H - F) - x * y

solution = Solution()
print(solution.computeArea(-3, 0, 3, 4, 0, -1, 9, 2))