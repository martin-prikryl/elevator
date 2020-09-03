#!/usr/bin/python3
'''
Elevator OOD
'''
from enum import Enum, auto
from typing import List

class ElevatorDirection(Enum):
    '''
    Direction of moving elevator
    '''
    UP = auto()
    DOWN = auto()

class Elevator:
    '''
    Elevator inside the set
    It's expected that every Elevator must be inside some ElevatorSet.
    '''
    def __init__(self, floors: List(int)):
        self.floors = floors[:]
        self.door = Door()
        self.requested_floors = set()
        self.buttons = {}
        for floor in self.floors:
            self.buttons[floor] = InsideButton(self, floor)
        self.direction = None

    def request_floor(self, floor: int):
        '''Add floor to request list'''
        self.requested_floors.add(floor)

    def get_button(self, floor: int) -> InsideButton:
        '''Access InsideButton class'''
        return 

class ElevatorSet:
    '''Set of elevators'''
    def __init__(self):
        self.elevators = []

    def add_elevator(self, elevator: Elevator):
        '''Add elevator to set'''
        self.elevators.append(elevator)

    def get_elevator(self, number: int) -> Elevator:
        '''Access Elevator object'''
        return self.elevators[number]

class InsideButton:
    '''
    Button inside elevator cabin
    '''
    def __init__(self, elevator: Elevator, floor: int):
        self.elevator = elevator
        self.floor = floor

    def press(self):
        '''Press the button'''
        self.elevator.request_floor(self.floor)

class DoorStatus(Enum):
    '''
    Door status - opening and closing skipped for simplicity
    '''
    OPEN = auto()
    CLOSED = auto()

class Door:
    '''
    Cabin door - floor doors skipped for simplicity
    '''
    def __init__(self):
        self.status = DoorStatus.CLOSED

    def open(self):
        '''Open door'''
        self.status = DoorStatus.OPEN

    def close(self):
        '''Close door'''
        self.status = DoorStatus.CLOSED

    def get_status(self):
        '''Get door status'''
        return self.status
