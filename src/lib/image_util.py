import cv2
import numpy as np
import matplotlib.pyplot as plt

def create_heatmap(filter_blur: np.ndarray):
    """
    ヒートマップの作成
    """
    # フィルタの数値分布画像(1000倍しているのは、画像として差分を強調するため)
    _filter_blur = filter_blur.copy()
    _filter_blur[0,0] = 1
    _filter_blur[0,1] = 0
    sm = plt.cm.ScalarMappable(cmap=None)
    img_filter_blur = sm.to_rgba(diff_stanh_filter_blur * 1000, bytes=True)[:, :, :3]
    return


def put_text(img, text, pos=(10, 20)):
    """
    img : 入力画像
    text : 表示文字列
    pos : 表示位置
    """
    FONTSCALE = 0.7
    THICKNESS = 2
    TEXT_COLOR = (255, 255, 255)
    FONTFACE = cv2.FONT_HERSHEY_SIMPLEX

    flame = 5
    text_color_bg = (0,0,0)
    # ===========================================
    # 画面表示文字
    # ===========================================
    x, y = pos
    text_size, _ = cv2.getTextSize(text, FONTFACE, FONTSCALE, THICKNESS)
    text_w, text_h = text_size
    cv2.rectangle(img, (pos[0]-flame,pos[1]-flame), (x + text_w + flame, y + text_h + flame), text_color_bg, -1)
    cv2.putText(img,
                text=text,
                org=(x, int(y + text_h + FONTSCALE - 1)),
                fontFace=FONTFACE,
                fontScale=FONTSCALE,
                color=TEXT_COLOR,
                thickness=THICKNESS)

    return img
