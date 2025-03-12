class Solution {
public:
    int findNumbers(vector<int>& nums) {
        int count = 0;
        
        for (int num : nums) {
            int digitCount = 0;
            int temp = num;
            
            // Count the number of digits
            while (temp != 0) {
                digitCount++;
                temp /= 10;
            }
            
            // Check if the number of digits is even
            if (digitCount % 2 == 0) {
                count++;
            }
        }
        return count;
    }
};
