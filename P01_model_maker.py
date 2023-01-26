{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOXNt2nrjN7Iic2IU4SKfFz",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/tennenchannel/deep-learning/blob/main/P01_model_maker.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "CfBB-KrA_h_r"
      },
      "outputs": [],
      "source": [
        "from tensorflow.keras.layers import Flatten,Input\n",
        "from tensorflow.keras.models import Model\n",
        "from tensorflow.keras.optimizers import Adam\n",
        "\n",
        "import P10_util as util\n",
        "import P11_model_util as mutil\n",
        "\n",
        "class ModelMaker:\n",
        "  def __init__(self,dst_dir,est_file,input_size,filters,kernel_size,pool_size,dense_dims,lr,data_size,batch_size,epochs,valid_rate):\n",
        "    self.dst_dir=dst_dir\n",
        "    self.est_file=est_file\n",
        "    self.input_size=input_size\n",
        "    self.filters=filters\n",
        "    self.kernel_size=kernel_size\n",
        "    self.pool_size=pool_size\n",
        "    self.dense_dims=dense_dims\n",
        "    self.lr=lr\n",
        "    self.data_size=data_size\n",
        "    self.batch_size=batch_size\n",
        "    self.epochs=epochs\n",
        "    self.valid_rate=valid_rate\n",
        "    #setting of hyper parameter\n",
        "  \n",
        "  def define_model(self):\n",
        "    #入力層の定義\n",
        "    input_x=Input(shape=(*self.input_size,1))\n",
        "    x=input_x\n",
        "    #畳み込み層、プーリング層の定義\n",
        "    for f in self.filters:\n",
        "      x=mutil.add_conv_pool_layers(x,f,self.kernel_size,self.pool_size)\n",
        "    #平滑化層の定義\n",
        "    x=Flatten()(x)\n",
        "    #全結合層の定義\n",
        "    for dim in self.dense_dims[:-1]:\n",
        "      x=mutil.add_dense_layer(x,dim)\n",
        "    #出力層の定義\n",
        "    x=mutil.add_dense_layer(x,self.dense_dims[-1],activation='softmax')\n",
        "    #モデル全体の出力層の定\n",
        "    model=Model(input_x,x)\n",
        "    #モデルの訓練条件の設定\n",
        "    model.compile(optimizer=Adam(lr=self.lr),\n",
        "                  loss='categorical_crossentropy',\n",
        "                  metrics=['accuracy'])\n",
        "    return model\n",
        "\n",
        "  #モデルを訓練するメソッド\n",
        "  def fit_model(self):\n",
        "    #データセットの読み込み\n",
        "    train_images,train_classes=util.load_data(self.data_size)\n",
        "    #モデルの定義\n",
        "    model=self.define_model()\n",
        "    #訓練の実行\n",
        "    history=model.fit(\n",
        "        train_images,train_classes,batch_size=self.batch_size,epochs=self.epochs,validation_split=self.valid_rate\n",
        "    )\n",
        "    return model,history.history\n",
        "    #define_model()を呼び出してモデルを定義し、そのモデルを訓練する。\n",
        "  def execute(self):\n",
        "    #モデルを訓練\n",
        "    model,history=self.fit_model()\n",
        "    #訓練したモデルを保存\n",
        "    util.mkdir(self.dst_dor,rm=True)\n",
        "    model.save(self.est_file)\n",
        "    #最終エポックの検証用データにおける損失を標準出力\n",
        "    print('val_loss: %f'%history['val_loss'][-1])\n",
        "   \n",
        "\n",
        "  "
      ]
    }
  ]
}