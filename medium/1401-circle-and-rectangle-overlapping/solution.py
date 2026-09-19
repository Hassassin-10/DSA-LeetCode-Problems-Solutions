class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        # Find the closest point (closestX, closestY) on the rectangle to the circle's center
        closestX = max(x1, min(xCenter, x2))
        closestY = max(y1, min(yCenter, y2))
        
        # Calculate the squared distance between the circle's center and this closest point
        dx = closestX - xCenter
        dy = closestY - yCenter
        
        # Check if the squared distance is within the squared radius
        return (dx * dx + dy * dy) <= (radius * radius)