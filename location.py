import pygame


def convertToPixel(num): #num is a list of two values, x and y
    x, y = 800, 800
    xunit=100
    yunit=100
    realx = (num[0] - 1) * xunit + (xunit / 2)  # x pixels
    realy = (8-num[1])*yunit+ (yunit/2)  # y pixels
    return [realx, realy]


def convertToNumber(num): #num is a list of two values, x and y
    x, y = 800, 800
    xunit=100
    yunit=100
    realx = int((num[0]/xunit)+1)
    realy = int(((y-num[1])/yunit)+1)
    return [realx, realy]
