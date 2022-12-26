import pyrosim.pyrosim as pyrosim
pyrosim.Start_SDF("boxes.sdf")
NumX = 5
NumY = 5
x = 0
lengthInit = 1
widthInit = 1
heightInit = 1
for idxX in range(NumX):
    y = 0
    for idxY in range(NumY):
        idx = 0
        length = lengthInit 
        width = widthInit
        height = heightInit
        z = 0.5
        while idx < 10:
            pyrosim.Send_Cube(name= f'Box{idx+1}{idxX}{idxY}', pos=[x,y,z] , size=[length,width,height])
            z = z + height
            height = 0.9*height
            width = 0.9*width
            length = 0.9*length
            idx = idx + 1
            print(idx)
        y = y + widthInit
    x = x +  lengthInit
pyrosim.End()