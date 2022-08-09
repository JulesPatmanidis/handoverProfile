set -ex
#BINDIR=`dirname $0`
#source $BINDIR/common.sh

cd /var/tmp

# Install dependencies
sudo apt update
sudo apt install -y software-properties-common lsb-release
sudo apt clean all
sudo apt-get -y install cmake libfftw3-dev libmbedtls-dev libboost-program-options-dev libconfig++-dev libsctp-dev

# Install ZMQ
sudo apt-get -y install libzmq3-dev
git clone https://github.com/zeromq/libzmq.git
cd libzmq
./autogen.sh
./configure
make
sudo make install
sudo ldconfig
cd ..

# Install CZMQ
git clone https://github.com/zeromq/czmq.git
cd czmq
./autogen.sh
./configure
make
sudo make install
sudo ldconfig
cd ..


# Install srsRAN
git clone https://github.com/srsRAN/srsRAN.git
cd srsRAN
git checkout release_21_10
mkdir build
cd build
cmake ../
make -j `nproc`
sudo make install
sudo ldconfig
#sudo srsran_install_configs.sh service
#cd /etc
#sudo mkdir srsran
#sudo cp /local/repository/etc/srsran/examples/* /etc/srsran/
#sudo cp /local/repository/etc/srsran/* /etc/srsran/



