import cv2 
from util import classify

class Camera:
    def __init__(self,save_path='',img_extn='.jpg'):
        self.save_path=save_path
        self.detect_frame=None
        self.frame_pred=None
        self.img_extn=img_extn
        self.cnt=0
        self.cmds={'s':'save image','d':'detect frame','q':'end camera stream'}

    def get_cmds(self):
        return self.cmds

    def save_img(self):
        cv2.imwrite(self.save_path+'/'+self.frame_pred+str(self.cnt)+self.img_extn,self.detect_frame)
        self.cnt+=1
        print('Image saved!')

    def classify_img(self):
        print('Detecting...')
        self.frame_pred=classify(frame=self.detect_frame)
        cv2.imshow(f'Prediction: {self.frame_pred}',self.detect_frame)
        print(f'Prediction: {self.frame_pred}')

    def start_capture(self):
        vid = cv2.VideoCapture(0) 

        while(True): 
            _,frame = vid.read() 
            cv2.imshow('live camera', frame)
            if cv2.getWindowProperty(f'Prediction: {self.frame_pred}',cv2.WND_PROP_VISIBLE)<1:
                self.frame_pred=None
                self.detect_frame=None
            if cv2.waitKey(1) & 0xFF == ord('d'):
                if self.detect_frame is None:
                    self.detect_frame=frame
                    self.classify_img()
                else:
                    print('Error -- please close previous detection before attempting new one.')
            if cv2.waitKey(1) & 0xFF == ord('s'):
                if self.detect_frame is not None:
                    self.save_img()
                else:
                    print('Error -- no frame is detected; must detect a specific frame to save.')
            if cv2.waitKey(1) & 0xFF == ord('q'): 
                vid.release() 
                cv2.destroyAllWindows() 
                return

