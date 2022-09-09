"""
カメラキャプチャテスト
"""
import sys
from pathlib import Path
from typing import List, Optional, Tuple

import cv2
import numpy as np

ROOT_PATH = Path(__file__).resolve().parent.parent
SRC_PATH = ROOT_PATH / "src"
sys.path.append(str(ROOT_PATH))
sys.path.append(str(SRC_PATH))

from . import settings

if __name__ == "__main__":

    cap = cv2.VideoCapture(0)   # キャプチャカメラ
    # cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('B', 'G', 'R', '3'))
    cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'))
    # cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('H', '2', '6', '4'))
    # cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('Y', 'U', 'Y', 'V'))
    jls_extract_var = cap
    jls_extract_var.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

    try:
        while True:
            ret, image_org = cap.read()
            if image_org is None:
                print("error")
                continue

            height, width = image_org.shape[:2]
            ratio = settings.CAMERA_IMG_SIZE / height
            image_org_resize = cv2.resize(
                                image_org,
                                None,
                                fx=ratio,
                                fy=ratio,
                                interpolation=cv2.INTER_LINEAR)

            if image_org_resize is None:
                continue

            cv2.imshow('カメラ映像', image_org_resize)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    except:
        import traceback
        traceback.print_exc()


    cap.release()
    cv2.destroyAllWindows()
