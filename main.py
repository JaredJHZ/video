import cv2



import os



filename = 'prueba.mp4'
frames_per_second = 60.0
res = '720p'



STD_DIMENSIONS =  {
    "480p": (640, 480),
    "720p": (1280, 720),
    "1080p": (1920, 1080),
    "4k": (3840, 2160),
}



VIDEO_TYPE = {
    'avi': cv2.VideoWriter_fourcc(*'XVID'),
    'mp4': cv2.VideoWriter_fourcc(*'XVID'),
}



def change_res(cap, width, height):
    cap.set(3, width)
    cap.set(4, height)



def get_dims(cap, res='1080p'):
    width, height = STD_DIMENSIONS["480p"]
    if res in STD_DIMENSIONS:
        width,height = STD_DIMENSIONS[res]
    change_res(cap, width, height)
    return width, height



def get_video_type(filename):
    filename, ext = os.path.splitext(filename)
    if ext in VIDEO_TYPE:
      return  VIDEO_TYPE[ext]
    return VIDEO_TYPE['avi']



def capture():
    cap = cv2.VideoCapture(0)
    #'http://192.168.0.5:8080/video')
    out = cv2.VideoWriter(filename, get_video_type(filename), 60, get_dims(cap, res))
    count = 0
    while(True):
      
        ret, frame = cap.read()
        out.write(frame)
        if ret:
            print(count)
            count += 1
            cv2.imwrite(os.path.join('./images', '%d.png') % count, frame)
        #checarSiSacoAlgo(frame)
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'): 
             break  
    cap.release()
    out.release()
    cv2.destroyAllWindows() 



if __name__ == "__main__":
    capture()



#def checarSiSacoAlgo(frame):
    ## analizando algo (Arturo)
    ## encontre algo (Jared)
    ## enviar video a s3 de prueba de que saco algo (Jared)
    ## mandar notiicacion con sns al supervisor (Obed)