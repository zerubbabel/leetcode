#
# @lc app=leetcode.cn id=1603 lang=python3
#
# [1603] 设计停车系统
#

# @lc code=start
class ParkingSystem:
    loc=[0]*4
    def __init__(self, big: int, medium: int, small: int):
        self.loc[1]=big
        self.loc[2]=medium
        self.loc[3]=small

    def addCar(self, carType: int) -> bool:
        if self.loc[carType]>0:
            self.loc[carType]-=1
            return True
        return False
        


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)
# @lc code=end

