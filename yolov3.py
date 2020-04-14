import network as nn
from config import config
import argparse
ratio=1
def darknet_unit(filters):
    nn.conv(1,filters,1,1,1,'leaky')
    nn.conv(1,filters*2,3,1,1,'leaky')
    nn.shortcut(-3,'linear')

def darknet_block(filters,n):
    nn.conv(1,filters*2,3,2,1,'leaky')
    for i in range(1,n+1):
        darknet_unit(filters)
                
def darknet53():
    nn.conv(1,32,3,1,1,'leaky')
    darknet_block(32*ratio,1)
    darknet_block(64*ratio,2)
    darknet_block(128*ratio,8)
    darknet_block(256*ratio,8)
    darknet_block(512*ratio,4)
    
def detection_moudle(filters):
    nn.conv(1,filters,1,1,1,'leaky')
    nn.conv(1,filters*2,3,1,1,'leaky')
    nn.conv(1,filters,1,1,1,'leaky')
    nn.conv(1,filters*2,3,1,1,'leaky')
    nn.conv(1,filters,1,1,1,'leaky')
    nn.conv(1,filters*2,3,1,1,'leaky')
    nn.conv('null',config.num/config.layer_num*(config.num_class+5),1,1,1,'linear')
    return config.net_id

def Fuse(filters,layer_id):
    nn.route(-4)
    nn.conv(1,filters,1,1,1,'leaky')
    #nn.upsample(2)
    nn.deconv('null',filters,2,2,0,'linear')
    nn.route('-1, '+str(layer_id))

def get_yolo():
    darknet53()
    
    detection_moudle(512*ratio)
    nn.yolo(mask =config.mask1,anchors =config.anchors,classes=config.num_class,num=config.num,jitter=config.jitter,ignore_thresh =config.ignore_thresh,truth_thresh =config.truth_thresh,random=config.random)
    
    Fuse(256*ratio,61)  
    detection_moudle(256*ratio)
    nn.yolo(mask =config.mask2,anchors =config.anchors,classes=config.num_class,num=config.num,jitter=config.jitter,ignore_thresh =config.ignore_thresh,truth_thresh =config.truth_thresh,random=config.random)
    
    Fuse(128*ratio,36)   
    detection_moudle(128*ratio)
    nn.yolo(mask =config.mask3,anchors =config.anchors,classes=config.num_class,num=config.num,jitter=config.jitter,ignore_thresh =config.ignore_thresh,truth_thresh =config.truth_thresh,random=config.random)


def write_cfg(result_name):
    fout=open(result_name,'w+')
    fout.writelines(config.file_line)
    fout.close()
def parse_args():
    parser = argparse.ArgumentParser(description='get yolo .cfg files')
    # general
    parser.add_argument('--type', help='train or test', default='train', type=str)
    args = parser.parse_args()
    return args

def main():
    nn.write_setting('train')
    get_yolo()
    write_cfg('yolov3_'+config.model_name+'_'+'train'+'.cfg')
    nn.write_setting('test')
    get_yolo()
    write_cfg('yolov3_'+config.model_name+'_'+'test'+'.cfg')

if __name__ == '__main__':
    main()