# About
Graphical user interface for the kinneyotp (one time pad) module.

# Screens
![encode tab](https://github.com/mkinney/kinneyotpgui/blob/main/screens/encode.png?raw=true "Encode")
![decode tab](https://github.com/mkinney/kinneyotpgui/blob/main/screens/decode.png?raw=true "Decode")
![generate tab](https://github.com/mkinney/kinneyotpgui/blob/main/screens/generate.png?raw=true "Generate")
![settings tab](https://github.com/mkinney/kinneyotpgui/blob/main/screens/settings.png?raw=true "Settings")
![about tab](https://github.com/mkinney/kinneyotpgui/blob/main/screens/about.png?raw=true "About")

# To install

Run the following commands to setup a python virtual environment, then install the module.

```
python3 -m venv venv
venv/bin/activate
pip install kinneyotpgui
```

After the installation, you should be able to run:

```
otp
```

# For a local installation (for development):
```
pip install -r requirements.txt
pip install -e .

```
