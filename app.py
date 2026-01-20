{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": []
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
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "rPMp46iEHVGx"
      },
      "outputs": [],
      "source": [
        "import streamlit as st\n",
        "import pickle\n",
        "\n",
        "# Load model & vectorizer\n",
        "model = pickle.load(open(\"model.pkl\", \"rb\"))\n",
        "vectorizer = pickle.load(open(\"vectorizer.pkl\", \"rb\"))\n",
        "\n",
        "st.set_page_config(page_title=\"Sentiment Analysis\", page_icon=\"🧠\")\n",
        "\n",
        "st.title(\"🧠 Sentiment Analysis App\")\n",
        "st.write(\"Predict sentiment: Negative | Neutral | Positive\")\n",
        "\n",
        "user_input = st.text_area(\"Enter your text\")\n",
        "\n",
        "if st.button(\"Predict Sentiment\"):\n",
        "    if user_input.strip() == \"\":\n",
        "        st.warning(\"Please enter some text\")\n",
        "    else:\n",
        "        text_vector = vectorizer.transform([user_input])\n",
        "        prediction = model.predict(text_vector)[0]\n",
        "\n",
        "        if prediction == 0:\n",
        "            st.error(\"🔴 Negative Sentiment\")\n",
        "        elif prediction == 1:\n",
        "            st.info(\"🟡 Neutral Sentiment\")\n",
        "        elif prediction == 2:\n",
        "            st.success(\"🟢 Positive Sentiment\")\n"
      ]
    }
  ]
}