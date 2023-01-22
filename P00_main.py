{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOjDmOSENdkK5noArPbh6HL",
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
        "<a href=\"https://colab.research.google.com/github/tennenchannel/deep-learning/blob/main/P00_main.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 2,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 378
        },
        "id": "yCnd8wdg_Tei",
        "outputId": "bcf0eac5-f645-420f-aad1-ae824fc216a5"
      },
      "outputs": [
        {
          "output_type": "error",
          "ename": "ModuleNotFoundError",
          "evalue": "ignored",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mModuleNotFoundError\u001b[0m                       Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-2-eeb4afc97119>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[1;32m     13\u001b[0m \u001b[0mEPOCHS\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;36m10\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     14\u001b[0m \u001b[0mVALID_RATE\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;36m0.2\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 15\u001b[0;31m \u001b[0;32mfrom\u001b[0m \u001b[0mPO1_model_maker\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mModelMaker\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     16\u001b[0m maker=ModelMaker(\n\u001b[1;32m     17\u001b[0m     \u001b[0mdst_dir\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mDST_DIR\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;31mModuleNotFoundError\u001b[0m: No module named 'PO1_model_maker'",
            "",
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0;32m\nNOTE: If your import is failing due to a missing package, you can\nmanually install dependencies using either !pip or !apt.\n\nTo view examples of installing some common dependencies, click the\n\"Open Examples\" button below.\n\u001b[0;31m---------------------------------------------------------------------------\u001b[0m\n"
          ],
          "errorDetails": {
            "actions": [
              {
                "action": "open_url",
                "actionText": "Open Examples",
                "url": "/notebooks/snippets/importing_libraries.ipynb"
              }
            ]
          }
        }
      ],
      "source": [
        "import os\n",
        "\n",
        "DST_DIR='D01_estimator'\n",
        "EST_FILE=os.path.join(DST_DIR,'estimator.h5')\n",
        "INPUT_SIZE=(28,28)\n",
        "FILTERS=(32,64)\n",
        "KERNEL_SIZE=(3,3)\n",
        "POOL_SIZE=(2,2)\n",
        "DENSE_DIMS=(1024,128,10)\n",
        "LR=1e-3\n",
        "DATA_SIZE=1000\n",
        "BATCH_SIZE=128\n",
        "EPOCHS=10\n",
        "VALID_RATE=0.2\n",
        "from P01_model_maker import ModelMaker\n",
        "maker=ModelMaker(\n",
        "    dst_dir=DST_DIR,\n",
        "    est_file=EST_FILE,\n",
        "    input_size=INPUT_SIZE,\n",
        "    filters=FILTERS,\n",
        "    kernel_size=KERNEL_SIZE,\n",
        "    pool_size=POOL_SIZE,\n",
        "    dense_dims=DENSE_DIMS,\n",
        "    lr=LR,\n",
        "    data_size=DATA_SIZE,\n",
        "    batch_size=BATCH_SIZE,\n",
        "    epochs=EPOCHS,\n",
        "    valid_rate=VALID_RATE)\n",
        "maker.execute()\n",
        "\n"
      ]
    }
  ]
}