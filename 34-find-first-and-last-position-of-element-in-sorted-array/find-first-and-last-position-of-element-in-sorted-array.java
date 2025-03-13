class Solution {
    public int[] searchRange(int[] nums, int target) {
        int[] ans = {-1, -1};
        // check for first occurrence of target first
        int start = search(nums,target,true);
        int end = search(nums,target,false);
        ans[0] = start;
        ans[1] = end;
        return ans;
    }
    // this function just returns the index value of target
    int search(int[] nums,int target,boolean firstStartIndex){
        int ans = -1;
        int start = 0;
        int end = nums.length - 1;

        while (start <= end){
            // start + (end - start) / 2 might be possible that value excedes the interger capacity
            int mid = (start+end)/2;
            if(target > nums[mid]){
                start = mid +1;
            }
            else if (target < nums[mid]){
                end = mid -1;
            }
            else{
                // potential ans found
                ans = mid;
                if(firstStartIndex){
                    end = mid - 1;
                }
                else {
                    start = mid + 1;
                }
            }
        }
        return ans;
    }
}