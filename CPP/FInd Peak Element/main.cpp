class Solution {
public:
    int findPeakElement(vector<int>& nums) {
        int val;
        nums.push_back(round(pow(-2, 31)));
        if(nums.size()==1){val=0;}
        else{
            for(int i=1; i<nums.size()-1; i++){
                if(nums[i]>nums[i-1] && nums[i]>nums[i+1]){val=i;}
            }
        }
        return val;
    }
};
