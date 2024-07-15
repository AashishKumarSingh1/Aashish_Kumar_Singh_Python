import heapq
class Solution:
    def furthestBuilding(self, heights: list[int], bricks: int, ladders: int) -> int:
        used_bricks = []
        heapq.heapify(used_bricks) 
        
        for i in range(len(heights) - 1):
            diff = heights[i + 1] - heights[i]
            
            if diff > 0:
                heapq.heappush(used_bricks, diff)
                
                if len(used_bricks) > ladders:
                    min_bricks = heapq.heappop(used_bricks)
                    bricks -= min_bricks
                    
                    if bricks < 0:
                        return i 
                    
        return len(heights) - 1 