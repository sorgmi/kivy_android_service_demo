# Kivy android service and push notification example

Demo App which shows how to use push notifications and android services in your KivyMD App.

Features:
1. cross-platform application (Windows, Linux, Mac, Android, iOS) using [KivyMD](https://github.com/kivymd/KivyMD)
2. push notifications using [plyer](https://github.com/kivy/plyer)
3. Android background services using [pyjnius](https://github.com/kivy/pyjnius)

Screenshot 1            |  Screenshot 2
:-------------------------:|:-------------------------:
![](screenshots/p1.png)  |  ![](screenshots/p3.png)



# Run desktop version
```
pip install kivymd plyer
python main.py
```

# Build android app
**Option 1 using Docker (recommended):**
```
docker run --volume "$HOME/.buildozer":/home/user/.buildozer --volume "$PWD":/home/user/hostcwd kivy/buildozer android debug
```
The Android .apk is now inside the bin/ folder

**Option 2 building local (Ubuntu):**
```
sudo apt update

sudo apt install \
    autoconf \
    automake \
    build-essential \
    ccache \
    cmake \
    gettext \
    git \
    libffi-dev \
    libltdl-dev \
    libssl-dev \
    libtool \
    openjdk-13-jdk \
    patch \
    pkg-config \
    python3-pip \
    python3-setuptools \
    sudo \
    unzip \
    zip \
    zlib1g-dev
    
pip install --upgrade Cython==0.29.19 wheel pip virtualenv
pip install buildozer

buildozer android debug
```

# Build Desktop Binary (Windows, Linux, Mac)
```
pip install pyinstaller kivymd plyer
pyinstaller main.spec
```
On Windows binary can be found now at dist/main.exe