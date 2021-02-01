## [Easiest way to download kaggle data in Google Colab](https://www.kaggle.com/general/74235)

Please follow the steps below to download and use kaggle data within Google Colab:

1. Go to your account, Scroll to API section and Click **Expire API Token** to remove previous tokens

2. Click on **Create New API Token** - It will download kaggle.json file on your machine.

3. Go to your Google Colab project file and run the following commands:

**1) `! pip install -q kaggle`**

**2) `from google.colab import files`**

**files.upload()**

- Choose the kaggle.json file that you downloaded

**3)` ! mkdir ~/.kaggle`**

**`! cp kaggle.json ~/.kaggle/`**

- Make directory named kaggle and copy kaggle.json file there.

**4)` ! chmod 600 ~/.kaggle/kaggle.json`**

- Change the permissions of the file.

**5)` ! kaggle datasets list`**
\- That's all ! You can check if everything's okay by running this command.

## Download Data
**```! kaggle competitions download -c 'name-of-competition'```**

Use unzip command to **unzip the data**:

For example,

Create a directory named train,

**```! mkdir train```**

unzip train data there,

**```! unzip train.zip -d train```**