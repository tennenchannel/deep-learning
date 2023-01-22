{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyMw0MfVQ/h4qhFeFMX6TlwZ",
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
        "<a href=\"https://colab.research.google.com/github/tennenchannel/deep-learning/blob/main/P11_model_util.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "id": "Z_a4AIlNzW9J"
      },
      "outputs": [],
      "source": [
        "from tensorflow.keras.layers import Conv2D,Dense,MaxPooling2D\n",
        "\n",
        "def add_conv_pool_layers(x,filters,kernel_size,pool_size,activation='relu'):\n",
        "  x=Conv2D(filters,kernel_size,padding='same',activation=activation)(x)\n",
        "  x=Conv2D(filters,kernel_size,padding='same',activation=activation)(x)\n",
        "  x=MaxPooling2D(pool_size)(x)\n",
        "  return x\n",
        "\n",
        "def add_dense_layer(x,dim,activation='relu'):\n",
        "  x=Dense(dim,activation=activation)(x)\n",
        "  return x\n",
        "\n"
      ]
    }
  ]
}