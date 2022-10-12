import os

def missingFrames(start, end):
    node = nuke.selectedNode()
    if node.Class() == 'Write':
        frameNum = node['file'].getValue().split('.')[-2]
        evalStr = node['file'].evaluate().rsplit('.', 2)
        seq = '%s.%s.%s'%(evalStr[0], frameNum, evalStr[-1])
        print(frameNum)
        print(evalStr)
        print(seq)

        frames = []
        for frame in range(start, end+1):
            file = seq%frame
            if not os.path.exists(file):
                frames.append(frame)

        nums = ""
        if frames:
            for frame in frames:
                if frame-1 in frames:
                    if frame-2 in frames:
                        nums = nums.replace(str(frame-1), str(frame))
                    else:
                        nums += '-%s'%frame
                else:
                    nums += ' %s'%frame

        return nums.strip()
