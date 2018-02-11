import pygame
import Square
import bishopBase
import king
import knight
import pawn
import pygame
import queen
import rook
import threaten


def inCheck(piece, list_of_pieices):
    if threaten.isThreatened(piece, list_of_pieices):
        return True
    else:
        return False


def inCheckmate(turn, list_of_pieces):
    for i in list_of_pieces:
        if i.team == turn and i.type == "KING" and threaten.isThreatened(i, list_of_pieces):
            if i.validMoves == []:  # no squares for king to move to
                # get the piece(s) attacking and find if it/they is/are threatened
                threatlist = threaten.threats(i)
                if len(threatlist) > 1:  # double check(mate)
                    return True
                elif len(threaten.threats(threatlist[0])) > 0:  # there is at least one way to capture the attacker
                    return False
                else:  # king can't move, one attacker, no way to capture (i.e. must block)
                    threat = threatlist[0]
                    blocksquares = []
                    if threat.type == "KNIGHT":
                        return True
                    elif threat.type == "PAWN":
                        return True
                    elif threat.type == "BISHOP":
                        xdiff = threat.x - i.x
                        ydiff = threat.y - i.y
                        xvals = []
                        yvals = []
                        if xdiff > 0:
                            for j in range(1, xdiff):
                                xvals = xvals + (i.x + j)
                        if xdiff < 0:
                            for j in range(1, abs(xdiff)):
                                xvals = xvals + (i.x - j)
                        if ydiff > 0:
                            for j in range(1, ydiff):
                                yvals = yvals + (i.x + j)
                        if ydiff < 0:
                            for j in range(1, abs(ydiff)):
                                yvals = yvals + (i.x - j)
                        for k in range(len(xvals)):
                            blocksquares = blocksquares + (xvals[k], yvals[k])
                        for l in list_of_pieces:
                            if l.team == turn and l.type != "KING":
                                for m in blocksquares:
                                    for n in l.validMoves():
                                        if m == n:  # if a potential block square is a valid move for a friendly piece
                                            return False
                                        else:
                                            return True
                    elif threat.type == "ROOK" or threat.type == "QUEEN":
                        xdiff = threat.x - i.x
                        ydiff = threat.y - i.y
                        xvals = []
                        yvals = []
                        if xdiff > 0:
                            for j in range(1, xdiff):
                                xvals = xvals + (i.x + j)
                        if xdiff < 0:
                            for j in range(1, abs(xdiff)):
                                xvals = xvals + (i.x - j)
                        if xdiff == 0:
                            for j in range(1, abs(ydiff)):
                                xvals = xvals + (i.x)
                        if ydiff > 0:
                            for j in range(1, ydiff):
                                yvals = yvals + (i.x + j)
                        if ydiff < 0:
                            for j in range(1, abs(ydiff)):
                                yvals = yvals + (i.x - j)
                        if ydiff == 0:
                            for j in range(1, abs(xdiff)):
                                yvals = yvals + (i.y)
                        for k in range(len(xvals)):
                            blocksquares = blocksquares + (xvals[k], yvals[k])
                        for l in list_of_pieces:
                            if l.team == turn and l.type != "KING":
                                for m in blocksquares:
                                    for n in l.validMoves():
                                        if m == n:  # if a potential block square is a valid move for a friendly piece
                                            return False
                                        else:
                                            return True
