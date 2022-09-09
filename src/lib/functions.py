import numpy as np
import matplotlib.pyplot as plt

def tanh(x: np.ndarray):
    """
    フィルターの重みを計算する
        -∞ ⇒ -1
        0 ⇒ 0
        +∞ ⇒ 1
    """
    return np.tanh(x)


def stanh(x: np.ndarray):
    """
    フィルターの重みを計算する
        -∞ ⇒ 0
        0  ⇒ 0.5
        +∞ ⇒ 1
    """
    return (np.tanh(x) + 1) / 2


def dtanh(x: np.ndarray):
    """
    フィルターの重みを計算する
        -∞ ⇒ 0
        0  ⇒  1
        +∞ ⇒ 0
    """
    return 1 - np.abs(np.tanh(x))


def create_filter(target_min, target_max, output, alpha=30, reverse=True):
    """
    target_min : ぼかす深度範囲の最小値
    target_max : ぼかす深度範囲の最大値
    output : 深度（numpy変換後）
    alpha : targetの範囲と範囲外の境界のぼかし具合 alphaがでかいほど境界がボケる
    reverse : ぼかす領域、ぼかさない領域を反転する
    """
    # ===========================================
    # ぼかし加減フィルタの作成
    # minを0、maxを0に補正した深度の値を
    # scaled hyperbolic tangentで変換し、min - max を行うことで、
    # minからmaxの範囲は0に近似、その範囲外は1に近似するよう変換する
    # ===========================================
    # ぼかし加減フィルタ(10で割っているのは、なだらかな数値分布にするため)
    stanh_filter_blur_min = stanh((output / alpha) - (target_min / alpha))
    stanh_filter_blur_max = stanh((output / alpha) - (target_max / alpha))

    diff_stanh_filter_blur = stanh_filter_blur_min - stanh_filter_blur_max
    # ぼかしをかける領域を反転させる
    if reverse:
        diff_stanh_filter_blur = np.abs(1-diff_stanh_filter_blur)
    # 画像の次元と同じになるよう変換
    filter_blur = np.stack(
        [diff_stanh_filter_blur, diff_stanh_filter_blur, diff_stanh_filter_blur], axis=2)

    # フィルタの数値分布画像(1000倍しているのは、画像として差分を強調するため)
    sm = plt.cm.ScalarMappable(cmap=None)
    img_filter_blur = sm.to_rgba(diff_stanh_filter_blur * 1000, bytes=True)[:, :, :3]
    return filter_blur, img_filter_blur


