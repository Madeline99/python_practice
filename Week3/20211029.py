import cv2

img = cv2.imread("E:\钟静\pythonProject\Week3\image\1.png",cv2.IMREAD_COLOR)  # 读入图片
cv2.imshow("image", img)  # 显示图片
cv2.waitKey(0)  # 等待键盘输入，参数为0表示无限等待。不调用waitkey的话，窗口一闪即逝，看不到图片
cv2.destroyAllWindows()  # 关闭所有窗口
