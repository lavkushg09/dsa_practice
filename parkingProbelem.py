class ParkingSpace:
    def __init__(self, s_side, m_side, l_side):
        self.s_side = s_side
        self.m_side = m_side
        self.l_side = l_side

    def can_fit(self, vehicle_type):
        if vehicle_type == 'S':
            return self.s_side > 0
        elif vehicle_type == 'M':
            return self.m_side > 0
        elif vehicle_type == 'L':
            return self.l_side > 0
        return False
    
    def park_vehicle(self, vehicle_type):
        if self.can_fit(vehicle_type):
            if vehicle_type == 'S':
                self.s_side -= 1
            elif vehicle_type == 'M':
                self.m_side -= 1
            elif vehicle_type == 'L':
                self.l_side -= 1
            return True
        return False
    
    def check_is_empty(self, vehicle_type):
        if vehicle_type == 'S':
            return self.s_side == 0
        elif vehicle_type == 'M':
            return self.m_side == 0
        elif vehicle_type == 'L':
            return self.l_side == 0
        return True

    
    def leave_vehicle(self, vehicle_type):
        if not self.check_is_empty(vehicle_type):
            if vehicle_type == 'S':
                self.s_side += 1
            elif vehicle_type == 'M':
                self.m_side += 1
            elif vehicle_type == 'L':
                self.l_side += 1
            return True
        return False



if __name__ == "__main__":
    parking_space = ParkingSpace(2, 2, 1)
    print(parking_space.park_vehicle('S'))  # True
    print(parking_space.park_vehicle('M'))  # True
    print(parking_space.park_vehicle('L'))  # True
    print(parking_space.park_vehicle('L'))  # False
    print(parking_space.leave_vehicle('M')) # True
    print(parking_space.leave_vehicle('M')) # False
    print(parking_space.park_vehicle('M'))  # True