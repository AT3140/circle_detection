'''
Bounding Box Format: [llx,lly,urx,ury]
'''
import math

def getArea(boundingBox):
    return abs(boundingBox[0] - boundingBox[2]) * abs(boundingBox[1] - boundingBox[3])

def getBoundingBoxInclusiveOfPoint(boundingBox, xyProjectedCenter):
    retVal = boundingBox
    llx, lly, urx, ury = boundingBox[0], boundingBox[1], boundingBox[2], boundingBox[3]
    cx, cy = xyProjectedCenter[0], xyProjectedCenter[1]
    if(cx < llx):
        retVal[0] = cx
    elif(urx < cx):
        retVal[2] = cx
    if(cy < lly):
        retVal[1] = cy
    elif(ury < cy):
        retVal[3] = cy
    return retVal

def isCollinear(triplet):
    triplet = list(triplet)
    ax, ay = triplet[0][0], triplet[0][1]
    bx, by = triplet[1][0], triplet[1][1]
    cx, cy = triplet[2][0], triplet[2][1]
    D = 2 * ( ax * ( by - cy ) + bx * ( cy - ay ) + cx * ( ay - by ) )
    if(D == 0):
        return True
    else: return False

def getProjectedArc(triplet):
    triplet = list(triplet)
    ax, ay = triplet[0][0], triplet[0][1]
    bx, by = triplet[1][0], triplet[1][1]
    cx, cy = triplet[2][0], triplet[2][1]
    D = 2 * ( ax * ( by - cy ) + bx * ( cy - ay ) + cx * ( ay - by ) )
    Ux = ( math.pow(ax,2) + math.pow(ay,2) ) * ( by - cy ) + ( math.pow(bx,2) + math.pow(by,2) ) * ( cy - ay ) + ( math.pow(cx,2) + math.pow(cy,2) ) * (ay - by)
    Ux = Ux / D
    Uy = ( math.pow(ax,2) + math.pow(ay,2) ) * ( cx - bx ) + ( math.pow(bx,2) + math.pow(by,2) ) * ( ax - cx ) + ( math.pow(cx,2) + math.pow(cy,2) ) * (bx - ax)
    Uy = Uy / D
    r = math.sqrt( math.pow(ax - Ux, 2) + math.pow(ay - Uy, 2) )
    return (Ux,Uy), r 

def getNewPotentialCircle(triplet):
    xyProjectedCenter, radius = getProjectedArc(triplet) 
    x = xyProjectedCenter[0]
    y = xyProjectedCenter[1]
    boundingBox = [x,y,x,y]
    return [boundingBox, radius, triplet]

def detectPotentialCircles(xycoords, boundingBoxSizeLimit):
    potentialCircles = []
    currentPotentialCircle = []
    for i in range(len(xycoords)):
        p1 = xycoords[i % len(xycoords)]
        p2 = xycoords[(i + 1) % len(xycoords)]
        p3 = xycoords[(i + 2) % len(xycoords)]
        if(isCollinear({p1,p2,p3})):
            if(currentPotentialCircle):
                potentialCircles.append(currentPotentialCircle[:])
                currentPotentialCircle.clear()
        else:
            if(currentPotentialCircle):
                boundingBox = currentPotentialCircle[0][:]
                xyProjectedCenter, radius = getProjectedArc({p1,p2,p3}) 
                boundingBox = getBoundingBoxInclusiveOfPoint(boundingBox, xyProjectedCenter) 
                areaBoundingBox = getArea(boundingBox) 
                if(areaBoundingBox > boundingBoxSizeLimit): 
                    potentialCircles.append(currentPotentialCircle[:])
                    currentPotentialCircle = getNewPotentialCircle({p1, p2, p3})
                else:
                    currentPotentialCircle[0] = boundingBox
                    currentPotentialCircle[2].add(p3)
            else:
                currentPotentialCircle = getNewPotentialCircle({p1,p2,p3})
        
    if(currentPotentialCircle):
        potentialCircles.append(currentPotentialCircle[:])
    
    return potentialCircles

def stitchPotentialCircles(potentialCircles):
    return potentialCircles

def convertToCrpFormat(boundedCircles):
    circles = []
    for boundedCircle in boundedCircles:
        boundingBox = boundedCircle[0]
        center = [(boundingBox[0] + boundingBox[2]) / 2, (boundingBox[1] + boundingBox[3]) / 2]
        boundedCircle = [center, boundedCircle[1], boundedCircle[2]]
        circles.append(boundedCircle[:])
    return circles

def detect(xycords, linearError):
    boundingBoxSizeLimit = math.pow(linearError,2)
    print(f'Bounding Box Size : {round(boundingBoxSizeLimit,2)}')
    potentialCircles = detectPotentialCircles(xycords, boundingBoxSizeLimit)
    boundedCircles = stitchPotentialCircles(potentialCircles)
    circles = convertToCrpFormat(boundedCircles)
    return circles
