set -ex
#BINDIR=`dirname $0`
#source $BINDIR/common.sh

cd /var/tmp

# Install dependencies
sudo apt update
sudo apt install -y software-properties-common lsb-release
sudo apt clean all
sudo apt-get -y install cmake libfftw3-dev libmbedtls-dev libboost-program-options-dev libconfig++-dev libsctp-dev

# Install srsRAN
git clone https://github.com/srsRAN/srsRAN.git
cd srsRAN
# git checkout release_21_10 # Introduces probelm during config install!!
mkdir build
cd build
cmake ../
make -j `nproc`
sudo make install
sudo ldconfig
sudo srsran_install_configs.sh service
sudo cp /local/repository/etc/srsran/* /etc/srsran/