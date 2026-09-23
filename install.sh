#!/bin/bash
echo "╔══╣ Setup: ROS2 Web Teleop (STARTING) ╠══╗"

sudo apt update

# System Environment
ENV="$(uname -m)"

# Install for Each Environment
if [[ ${ENV} == *"x86_64"* ]]; then
    wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
    sudo apt install -y ./google-chrome-stable_current_amd64.deb
    sudo rm google-chrome-stable_current_amd64.deb

sudo install -d -m 0755 /etc/apt/keyrings
wget -q https://packages.mozilla.org/apt/repo-signing-key.gpg -O- \
| sudo tee /etc/apt/keyrings/packages.mozilla.org.asc > /dev/null
gpg -n -q --import --import-options import-show \
/etc/apt/keyrings/packages.mozilla.org.asc
echo "deb [signed-by=/etc/apt/keyrings/packages.mozilla.org.asc] \
https://packages.mozilla.org/apt mozilla main" \
| sudo tee /etc/apt/sources.list.d/mozilla.list
echo '
Package: *
Pin: origin packages.mozilla.org
Pin-Priority: 1000
' | sudo tee /etc/apt/preferences.d/mozilla

else
    sudo rm -f /etc/apt/preferences.d/chromium-deb
    sudo tee /etc/apt/preferences.d/chromium-deb > /dev/null <<- 'EOF'
Package: chromium*
Pin: release o=LP-PPA-xtradeb-apps
Pin-Priority: 500

Package: chromium*
Pin: release o=Ubuntu*
Pin-Priority: -1
EOF
    sudo add-apt-repository -y ppa:xtradeb/apps
    sudo apt update
    sudo apt install -y chromium
fi

sudo apt install -y \
    sed \
    xdg-utils \
    firefox

pip3 install qrcode[pil] --break-system-packages
pip3 install websockets --break-system-packages
python3 -m pip install --break-system-packages \
    qrcode[pil]

echo "╚══╣ Setup: ROS2 Web Teleop (FINISHED) ╠══╝"