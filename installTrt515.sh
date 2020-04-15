sudo apt-get purge "libnvinfer*" && sudo apt-get purge "nv-tensorrt*"

sudo dpkg -i nv-tensorrt-repo-ubuntu1604-cuda9.0-trt5.1.5.0-ga-20190427_1-1_amd64.deb
sudo apt-key add /var/nv-tensorrt-repo-cuda9.0-trt5.1.5.0-ga-20190427/7fa2af80.pub

sudo apt-get install tensorrt
sudo dpkg -i cuda-license-9-0_9.0.176-1_amd64.deb
sudo dpkg -i cuda-cublas-9-0_9.0.176.4-1_amd64.deb
sudo dpkg -i cuda-cublas-dev-9-0_9.0.176.4-1_amd64.deb


sudo dpkg -i libcudnn7_7.6.0.64-1+cuda9.0_amd64.deb
sudo dpkg -i libcudnn7-dev_7.6.0.64-1+cuda9.0_amd64.deb
sudo dpkg -i libcudnn7-doc_7.6.0.64-1+cuda9.0_amd64.deb

sudo apt-get update
sudo apt-get install -y --no-install-recommends libnvinfer5=5.1.5-1+cuda9.0
sudo apt-get install -y --no-install-recommends libnvinfer-dev=5.1.5-1+cuda9.0
sudo apt-get install tensorrt
cd ..
./buildVisionProject.sh

