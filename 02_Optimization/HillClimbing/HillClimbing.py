import math
import random


def randThetaPhi():
    theta1 = random.randint(0, 360)
    theta2 = random.randint(0, 360)
    theta3 = random.randint(0, 360)
    phi1 = random.randint(0, 360)
    phi2 = random.randint(0, 360)
    phi3 = random.randint(0, 360)

    return [theta1, theta2, theta3, phi1, phi2, phi3]


def checkGain(currentPosition):

        theta1 = currentPosition[0]
        theta2 = currentPosition[1]
        theta3 = currentPosition[2]
        phi1 = currentPosition[3]
        phi2 = currentPosition[4]
        phi3 = currentPosition[5]
        s = "http://localhost:8080/antenna/simulate?phi1="+phi1+"&theta1="+theta1+"&phi2="+phi2+"&theta2="+theta2+"&phi3="+phi3+"&theta3="+theta3
        # NEED TO RETURN THE GAIN FROM S
        return s


def checkNeighbour(currentPosition):
    gain = checkGain(currentPosition)
    theta1 = currentPosition[0]
    theta2 = currentPosition[1]
    theta3 = currentPosition[2]
    phi1 = currentPosition[3]
    phi2 = currentPosition[4]
    phi3 = currentPosition[5]
    for i in range(20):
        theta1 = sumAngle(theta1)
        gain2 = checkGain(currentPosition)
        if gain2 > gain:
            gain = gain2
        theta1 = subAngle(theta1)
        gain2 = checkGain(currentPosition)
        if gain2 > gain:
            gain = gain2
    for i in range(20):
        theta2 = sumAngle(theta2)
        gain2 = checkGain(currentPosition)
        if gain2 > gain:
            gain = gain2
        theta2 = subAngle(theta2)
        gain2 = checkGain(currentPosition)
        if gain2 > gain:
            gain = gain2
    for i in range(20):
        theta3 = sumAngle(theta3)
        gain2 = checkGain(currentPosition)
        if gain2 > gain:
            gain = gain2
        theta3 = subAngle(theta3)
        gain2 = checkGain(currentPosition)
        if gain2 > gain:
            gain = gain2
    for i in range(20):
        phi1 = sumAngle(phi1)
        gain2 = checkGain(currentPosition)
        if gain2 > gain:
            gain = gain2
        phi1 = subAngle(phi1)
        gain2 = checkGain(currentPosition)
        if gain2 > gain:
            gain = gain2
    for i in range(20):
        phi2 = sumAngle(phi2)
        gain2 = checkGain(currentPosition)
        if gain2 > gain:
            gain = gain2
        phi2 = subAngle(phi2)
        gain2 = checkGain(currentPosition)
        if gain2 > gain:
            gain = gain2
    for i in range(20):
        phi3 = sumAngle(phi3)
        gain2 = checkGain(currentPosition)
        if gain2 > gain:
            gain = gain2
        phi3 = subAngle(phi3)
        gain2 = checkGain(currentPosition)
        if gain2 > gain:
            gain = gain2

    newPosition = [theta1, theta2, theta3, phi1, phi2, phi3]
    return newPosition

def sumAngle(angle):
    if angle < 360:
        return angle + 1
    else:
        return angle


def subAngle(angle):
    if angle > 0:
        return angle - 1
    else:
        return 0

def main:
    initPosition = randThetaPhi()


