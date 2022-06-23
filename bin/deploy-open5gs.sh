set -ex
BINDIR=`dirname $0`
source $BINDIR/common.sh

sudo apt update
sudo apt install -y software-properties-common
sudo add-apt-repository -y ppa:open5gs/latest
sudo apt update
sudo apt install -y open5gs
sudo cp /local/repository/etc/open5gs/* /etc/open5gs/
sudo systemctl restart open5gs-mmed
sudo systemctl restart open5gs-sgwud

#TODO: find a better method for adding subscriber info
cd $SRCDIR
wget https://raw.githubusercontent.com/open5gs/open5gs/main/misc/db/open5gs-dbctl
chmod +x open5gs-dbctl
./open5gs-dbctl add 208930000000001 3f3f473f2f3fd0943f3f3f3f097c6862 e9be7fb89bb01978e67972ca8580079e  # IMSI,K,OPC
./open5gs-dbctl type 208930000000001 1  # APN type IPV4

