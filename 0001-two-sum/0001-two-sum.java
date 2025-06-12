class Solution {
    public int[] twoSum(int[] nums, int target) {
        // int n = nums.length;
        // Map<Integer, Integer> map = new HashMap<>();
        // int[] result = new int[2];
        // for(int i = 0 ; i < n ; i++){
        //     int val = target - nums[i];
        //     if(map.containsKey(val)){
        //         result[0] = map.get(val);
        //         result[1] = i;
        //     }
        //     map.put(nums[i], i);
        // }
        // return result;
        for(int i=0;i <nums.length-1;i++){
            for(int j=i+1;j < nums.length;j++){  
                if(nums[i]+nums[j]==target){
                    return new int[] {i, j};
                }
            }
        }
        return null;
    }
}