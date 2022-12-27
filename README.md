# VALFE08 ( Vishwa's Android Log File Extractor )

VALFE08 (Vishwa's Android Log File Extractor) is a utility tool, which enables users to acquire forensic data from android devices in a simpler manner.

It is a CLI-based utility tool that uses [Python](https://www.python.org/) and [ADB](https://developer.android.com/studio/command-line/adb) to extract relevant forensic log files from an android device.

## How to use

_Note:_
**VALFE08 is not ready for production yet** and it is only tested on Windows as of now.

<!-- _Note:_
 Please read the DISCLAIMER before using the tool. -->

Prepackaged binary for Windows is available in the releases section if you are interested (checksum are provided as well for the executables). However, I will happy if you test it out on your device and help with the project.

### Requirements

The following are required to run the source code/VALFE08,

1. Python 3.11.1 and PIP 22.3.1
2. ADB

ADB is necessary for VALFE08 to work. Download and Install ADB from the [official source](https://developer.android.com/studio/releases/platform-tools#downloads) and the same to the system path.

VALFE08 also requires the target android device to be connected via USB in debugging mode. For this to work, one needs to enable USB debugging and accept the correct RSA Fingerprint prompted on the android device, to validate the connection. You can read more about enabling USB Debugging in your android device [here](https://developer.android.com/studio/debug/dev-options#enable).

_Note:_
Enabling USB debugging may vary from device to device, please have a glance at your device manufacturer's device manual to know more.

Please see [requirements](https://github.com/code-reaper08/VALFE08/blob/main/requirements.txt) for additional packages to install.

nstead of manually installing the packages, it is highly recommended to install from the [requirements](https://github.com/code-reaper08/VALFE08/blob/main/requirements.txt) file using the below command from the root directory.

```bash
pip install -r requirements.txt
```

After all the requirements are downloaded and installed, you can use VALFE08 by directly executing it with python.

```bash
python genisis.py
```

## Encryption in VALFE08

VALFE08 by default encrypts the extracted log files for ensuring file integrity. It is advised not to tamper with file structures so that the decryption process is carried out efficiently. Each run of VALFE08 produces a filekey.key, this key must be handled with care since it is symmetric. Though in most cases immediate decryption is preferred, there's an option to decrypt later as well. When choosing the decrypt later option, the filekey.key should be securely held and it is the user's responsibility to do so.

### VALFE-Decryptor

It is a decryption entity, which takes care of decrypting the encrypted extracted files. By Nature VALFE-Decryptor needs filekey.key, specimen/ directory, and locked files inside it to start the decryption process. So when decrypting please ensure the above criteria are met.

## Contribution

VALFE08 is still in its pre-release and welcomes all kinds of contributions.

<!-- Please read [CONTRIBUTING]() file to know more about how to contribute and what contribution methods the projects follow. -->

## License

VALFE08 is licensed under the BSD 3-Clause License.

```
BSD 3-Clause License

Copyright (c) 2022, Vishwa.R

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this
   list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice,
   this list of conditions and the following disclaimer in the documentation
   and/or other materials provided with the distribution.

3. Neither the name of the copyright holder nor the names of its
   contributors may be used to endorse or promote products derived from
   this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

```

If you like the project, please give a ⭐ for the repo. If you have any feedback regarding VALFE08, kindly [contact](https://cr08.netlify.app/en/contact/) me.
