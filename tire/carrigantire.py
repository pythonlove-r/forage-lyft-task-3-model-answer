from tire.tire import Battery
from utils import add_years_to_date


class CarriganTire(Battery):
    def __init__(self, num1, num2,num3,num4):
        self.num1 = num1
        self.num2 = num2
        self.num3 = num3
        self.num4 = num4


    def needs_service(self):  
        if num1<0.9&num2<0.9&num3<0.9&num4<0.9
            return False
        else:
            return True
