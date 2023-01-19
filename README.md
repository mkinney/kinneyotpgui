# About
Graphical user interface for the kinneyotp (one time pad) module.

# Screens
![encode tab](screens/encode.png "Encode")
![decode tab](screens/decode.png "Decode")
![generate tab](screens/generate.png "Generate")
![settings tab](screens/settings.png "Settings")
![about tab](screens/settings.png "About")

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
