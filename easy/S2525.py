class Solution:
    def categorizeBox(self, length: int, width: int, height: int, mass: int) -> str:
        
        
        is_bulky = (
            length >= 10**4 or 
            width >= 10**4 or 
            height >= 10**4 or 
            (length * width * height) >= 10**9
        )
        
        # Check if the box is Heavy
        is_heavy = mass >= 100
        
        # Categorize based on the booleans
        if is_bulky and is_heavy:
            return "Both"
        elif is_bulky:
            return "Bulky"
        elif is_heavy:
            return "Heavy"
        else:
            return "Neither"