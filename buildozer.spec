name: Build TACHY APK

on:
  push:
    branches: [ main ]
  workflow_dispatch:

jobs:
  build:
    runs-on: ubuntu-22.04

    steps:
      - uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.10'

      - name: Install system dependencies
        run: |
          sudo apt update
          sudo apt install -y openjdk-17-jdk git zip unzip wget \
          build-essential autoconf libtool pkg-config \
          zlib1g-dev libncurses5-dev libncursesw5-dev libtinfo5 \
          cmake libffi-dev libssl-dev tar

      - name: Install Buildozer
        run: |
          pip install --upgrade pip
          pip install cython==0.29.36 buildozer setuptools wheel

      # 🔥 FORCE FULL ANDROID SDK INSTALL (REAL FIX)
      - name: Install Android SDK (FULL)
        run: |
          mkdir -p $HOME/android-sdk
          cd $HOME/android-sdk

          wget https://dl.google.com/android/repository/commandlinetools-linux-11076708_latest.zip -O sdk.zip
          unzip sdk.zip

          mkdir -p cmdline-tools/latest
          mv cmdline-tools/* cmdline-tools/latest/ || true

          export ANDROID_SDK_ROOT=$HOME/android-sdk
          export PATH=$ANDROID_SDK_ROOT/cmdline-tools/latest/bin:$PATH

          yes | sdkmanager --licenses

          sdkmanager \
            "platform-tools" \
            "platforms;android-33" \
            "build-tools;33.0.2"

      - name: Build APK
        run: |
          export ANDROID_SDK_ROOT=$HOME/android-sdk
          export PATH=$ANDROID_SDK_ROOT/platform-tools:$PATH
          buildozer android debug

      - uses: actions/upload-artifact@v4
        with:
          name: tachy-apk
          path: bin/*.apk
