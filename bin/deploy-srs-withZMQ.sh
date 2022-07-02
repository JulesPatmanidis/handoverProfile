#set -ex
#BINDIR=`dirname $0`
# source $BINDIR/common.sh
SRCDIR=/var/tmp

cd /var/tmp

# Install dependencies
sudo apt update
sudo apt install -y software-properties-common lsb-release
sudo apt clean all
sudo apt-get install cmake libfftw3-dev libmbedtls-dev libboost-program-options-dev libconfig++-dev libsctp-dev

## Install ZMQ
#git clone https://github.com/zeromq/libzmq.git
#cd libzmq
#./autogen.sh
#./configure
#make
#sudo make install
#sudo ldconfig
#cd ..
#
## Install CZMQ
#git clone https://github.com/zeromq/czmq.git
#cd czmq
#./autogen.sh
#./configure
#make
#sudo make install
#sudo ldconfig
#cd ..
#
#
## Install srsRAN
#git clone https://github.com/srsRAN/srsRAN.git
#cd srsRAN
#mkdir build
#cd build
#cmake ../
#make
#sudo make install
#srsran_install_configs.sh user
#sudo ldconfig




