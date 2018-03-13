from .config import cfg
from lib.utils.cython_nms import nms_new as cython_nms
# from lib.utils.gpu_nms import gpu_nms

def nms(dets, thresh):
    if dets.shape[0] == 0:
        return []
    if cfg.USE_GPU_NMS:
        return gpu_nms(dets, thresh, device_id=cfg.GPU_ID)
    else:
        return cython_nms(dets, thresh)
