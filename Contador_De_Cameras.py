import cv2

class ContadorCams(object):

    def __init__(self):
        self.aux = True
        self.cams = 0
        self.source = 0

#    def camsCounter(self, self.source):
    def camsCounter(self):

        while self.aux:
            cap = cv2.VideoCapture(self.source)
            if cap is None or not cap.isOpened():
                self.aux = False
                #print('Warning: unable to open video source: ', self.source)
            else:
                self.cams = self.cams + 1
                self.source = self.source + 1

            qntdCams = self.cams

        return self.cams

# =================================================================

if __name__ == "__main__":
    c1 = ContadorCams()
    qntdCams = c1.camsCounter()
    print("Há %d câmera(s) disponível." %(qntdCams))

#teste = ContadorCams()
#print(teste.camsCounter())

'''
import cv2

class ContadorCams(object):

    def __init__(self):
        self.aux = True
        self.cams = 0

    def camsCounter(self, source):
        cap = cv2.VideoCapture(source)
        if cap is None or not cap.isOpened():
            self.aux = False
            print('Warning: unable to open video source: ', source)
        else:
            self.cams = self.cams + 1

        return self.cams

# =================================================================

teste = ContadorCams()
print(teste.camsCounter(0))
'''

'''
t1 = teste()

while t1.aux:
    t1.testDevice(t1.cams)

print("\nExistem {} câmeras.\n".format(t1.cams))
'''