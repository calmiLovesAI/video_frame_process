import cv2
import os
import shutil

# 视频存储路径
video_path = ""
# 输出视频文件保存路径
video_save_path = ""
# 存储已经读取的帧图片的临时路径
frame_save_path = ""


def process_frame(frame):
    return frame


if __name__ == '__main__':
    # 创建临时文件夹
    if not os.path.exists(frame_save_path):
        os.mkdir(frame_save_path)
    
    video_capture_1 = cv2.VideoCapture(video_path)
    frame_counter = 0
    while True:
        ret, frame = video_capture_1.read()
        if ret:
            frame_counter += 1
            # 存储每一帧的图片
            cv2.imwrite(frame_save_path + "frame_%d.jpg"%(frame_counter), frame)
            if frame_counter % 50 == 0:
                print("====================>Storing frame: %d<=================="%(frame_counter))
        else:
            break

    # 读取视频
    video_capture_2 = cv2.VideoCapture(video_path)
    # 码率
    fps = video_capture_2.get(cv2.CAP_PROP_FPS)
    # 帧尺寸
    frame_size = (int(video_capture_2.get(cv2.CAP_PROP_FRAME_WIDTH)), int(video_capture_2.get(cv2.CAP_PROP_FRAME_HEIGHT)))
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    video_writer = cv2.VideoWriter(video_save_path, fourcc, fps, frame_size)
    num_of_frame = 0    # 帧数
    while True:
        sucess, frame = video_capture_2.read()
        if sucess:
            num_of_frame += 1
            # 对每一帧图片进行处理
            new_frame = process_frame(cv2.imread(frame))

            # 写入帧
            print("===================>Writing frame: %d<=================="%(num_of_frame))
            video_writer.write(new_frame)
        else:
            print("Completed the video frame writing!")
            break
    
    shutil.rmtree(frame_save_path)
    