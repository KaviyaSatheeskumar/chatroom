{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPbr/vQiverycngLYZjgw0L",
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
        "<a href=\"https://colab.research.google.com/github/KaviyaSatheeskumar/chatroom/blob/main/imdb.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "rUPyFin0HXHO"
      },
      "outputs": [],
      "source": [
        "import warnings\n",
        "warnings.filterwarnings('ignore')\n",
        "import numpy as np\n",
        "import pandas as pd\n"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [],
      "metadata": {
        "id": "jriZmmoJckfT"
      }
    },
    {
      "cell_type": "markdown",
      "source": [],
      "metadata": {
        "id": "LP8D7Bs4ckkv"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# Write your code for inspection here\n",
        "movies.dtypes\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "HZTXriwiJs5E",
        "outputId": "3cbc9568-5af7-4f9d-f203-bf1631980dfb"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "Title          object\n",
              "Genre          object\n",
              "Premiere       object\n",
              "Runtime         int64\n",
              "IMDB Score    float64\n",
              "Language       object\n",
              "dtype: object"
            ]
          },
          "metadata": {},
          "execution_count": 19
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "jCkktslkJ_Em"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "movies = pd.read_csv('/content/imdb_dataset.csv')\n",
        "movies"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 423
        },
        "id": "2atZMStSI8-m",
        "outputId": "48be4696-dfd9-4a7f-c6b1-96a8b18a4d0f"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "                                           Title                  Genre  \\\n",
              "0                                Enter the Anime            Documentary   \n",
              "1                                    Dark Forces               Thriller   \n",
              "2                                        The App  Science fiction/Drama   \n",
              "3                                 The Open House        Horror thriller   \n",
              "4                                    Kaali Khuhi                Mystery   \n",
              "..                                           ...                    ...   \n",
              "579        Taylor Swift: Reputation Stadium Tour           Concert Film   \n",
              "580  Winter on Fire: Ukraine's Fight for Freedom            Documentary   \n",
              "581                      Springsteen on Broadway           One-man show   \n",
              "582    Emicida: AmarElo - It's All For Yesterday            Documentary   \n",
              "583     David Attenborough: A Life on Our Planet            Documentary   \n",
              "\n",
              "              Premiere  Runtime  IMDB Score                  Language  \n",
              "0       August 5, 2019       58         2.5          English/Japanese  \n",
              "1      August 21, 2020       81         2.6                   Spanish  \n",
              "2    December 26, 2019       79         2.6                   Italian  \n",
              "3     January 19, 2018       94         3.2                   English  \n",
              "4     October 30, 2020       90         3.4                     Hindi  \n",
              "..                 ...      ...         ...                       ...  \n",
              "579  December 31, 2018      125         8.4                   English  \n",
              "580    October 9, 2015       91         8.4  English/Ukranian/Russian  \n",
              "581  December 16, 2018      153         8.5                   English  \n",
              "582   December 8, 2020       89         8.6                Portuguese  \n",
              "583    October 4, 2020       83         9.0                   English  \n",
              "\n",
              "[584 rows x 6 columns]"
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-64fee39f-36e8-4136-a5cb-701162caa211\" class=\"colab-df-container\">\n",
              "    <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>Title</th>\n",
              "      <th>Genre</th>\n",
              "      <th>Premiere</th>\n",
              "      <th>Runtime</th>\n",
              "      <th>IMDB Score</th>\n",
              "      <th>Language</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>Enter the Anime</td>\n",
              "      <td>Documentary</td>\n",
              "      <td>August 5, 2019</td>\n",
              "      <td>58</td>\n",
              "      <td>2.5</td>\n",
              "      <td>English/Japanese</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>Dark Forces</td>\n",
              "      <td>Thriller</td>\n",
              "      <td>August 21, 2020</td>\n",
              "      <td>81</td>\n",
              "      <td>2.6</td>\n",
              "      <td>Spanish</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>The App</td>\n",
              "      <td>Science fiction/Drama</td>\n",
              "      <td>December 26, 2019</td>\n",
              "      <td>79</td>\n",
              "      <td>2.6</td>\n",
              "      <td>Italian</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>The Open House</td>\n",
              "      <td>Horror thriller</td>\n",
              "      <td>January 19, 2018</td>\n",
              "      <td>94</td>\n",
              "      <td>3.2</td>\n",
              "      <td>English</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>Kaali Khuhi</td>\n",
              "      <td>Mystery</td>\n",
              "      <td>October 30, 2020</td>\n",
              "      <td>90</td>\n",
              "      <td>3.4</td>\n",
              "      <td>Hindi</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>...</th>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>579</th>\n",
              "      <td>Taylor Swift: Reputation Stadium Tour</td>\n",
              "      <td>Concert Film</td>\n",
              "      <td>December 31, 2018</td>\n",
              "      <td>125</td>\n",
              "      <td>8.4</td>\n",
              "      <td>English</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>580</th>\n",
              "      <td>Winter on Fire: Ukraine's Fight for Freedom</td>\n",
              "      <td>Documentary</td>\n",
              "      <td>October 9, 2015</td>\n",
              "      <td>91</td>\n",
              "      <td>8.4</td>\n",
              "      <td>English/Ukranian/Russian</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>581</th>\n",
              "      <td>Springsteen on Broadway</td>\n",
              "      <td>One-man show</td>\n",
              "      <td>December 16, 2018</td>\n",
              "      <td>153</td>\n",
              "      <td>8.5</td>\n",
              "      <td>English</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>582</th>\n",
              "      <td>Emicida: AmarElo - It's All For Yesterday</td>\n",
              "      <td>Documentary</td>\n",
              "      <td>December 8, 2020</td>\n",
              "      <td>89</td>\n",
              "      <td>8.6</td>\n",
              "      <td>Portuguese</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>583</th>\n",
              "      <td>David Attenborough: A Life on Our Planet</td>\n",
              "      <td>Documentary</td>\n",
              "      <td>October 4, 2020</td>\n",
              "      <td>83</td>\n",
              "      <td>9.0</td>\n",
              "      <td>English</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "<p>584 rows × 6 columns</p>\n",
              "</div>\n",
              "    <div class=\"colab-df-buttons\">\n",
              "\n",
              "  <div class=\"colab-df-container\">\n",
              "    <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-64fee39f-36e8-4136-a5cb-701162caa211')\"\n",
              "            title=\"Convert this dataframe to an interactive table.\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\" viewBox=\"0 -960 960 960\">\n",
              "    <path d=\"M120-120v-720h720v720H120Zm60-500h600v-160H180v160Zm220 220h160v-160H400v160Zm0 220h160v-160H400v160ZM180-400h160v-160H180v160Zm440 0h160v-160H620v160ZM180-180h160v-160H180v160Zm440 0h160v-160H620v160Z\"/>\n",
              "  </svg>\n",
              "    </button>\n",
              "\n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    .colab-df-buttons div {\n",
              "      margin-bottom: 4px;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "    <script>\n",
              "      const buttonEl =\n",
              "        document.querySelector('#df-64fee39f-36e8-4136-a5cb-701162caa211 button.colab-df-convert');\n",
              "      buttonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "      async function convertToInteractive(key) {\n",
              "        const element = document.querySelector('#df-64fee39f-36e8-4136-a5cb-701162caa211');\n",
              "        const dataTable =\n",
              "          await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                    [key], {});\n",
              "        if (!dataTable) return;\n",
              "\n",
              "        const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "          '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "          + ' to learn more about interactive tables.';\n",
              "        element.innerHTML = '';\n",
              "        dataTable['output_type'] = 'display_data';\n",
              "        await google.colab.output.renderOutput(dataTable, element);\n",
              "        const docLink = document.createElement('div');\n",
              "        docLink.innerHTML = docLinkHtml;\n",
              "        element.appendChild(docLink);\n",
              "      }\n",
              "    </script>\n",
              "  </div>\n",
              "\n",
              "\n",
              "<div id=\"df-fe90f224-6751-4af1-8880-f4deb2c3243a\">\n",
              "  <button class=\"colab-df-quickchart\" onclick=\"quickchart('df-fe90f224-6751-4af1-8880-f4deb2c3243a')\"\n",
              "            title=\"Suggest charts.\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "<svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "     width=\"24px\">\n",
              "    <g>\n",
              "        <path d=\"M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zM9 17H7v-7h2v7zm4 0h-2V7h2v10zm4 0h-2v-4h2v4z\"/>\n",
              "    </g>\n",
              "</svg>\n",
              "  </button>\n",
              "\n",
              "<style>\n",
              "  .colab-df-quickchart {\n",
              "      --bg-color: #E8F0FE;\n",
              "      --fill-color: #1967D2;\n",
              "      --hover-bg-color: #E2EBFA;\n",
              "      --hover-fill-color: #174EA6;\n",
              "      --disabled-fill-color: #AAA;\n",
              "      --disabled-bg-color: #DDD;\n",
              "  }\n",
              "\n",
              "  [theme=dark] .colab-df-quickchart {\n",
              "      --bg-color: #3B4455;\n",
              "      --fill-color: #D2E3FC;\n",
              "      --hover-bg-color: #434B5C;\n",
              "      --hover-fill-color: #FFFFFF;\n",
              "      --disabled-bg-color: #3B4455;\n",
              "      --disabled-fill-color: #666;\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart {\n",
              "    background-color: var(--bg-color);\n",
              "    border: none;\n",
              "    border-radius: 50%;\n",
              "    cursor: pointer;\n",
              "    display: none;\n",
              "    fill: var(--fill-color);\n",
              "    height: 32px;\n",
              "    padding: 0;\n",
              "    width: 32px;\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart:hover {\n",
              "    background-color: var(--hover-bg-color);\n",
              "    box-shadow: 0 1px 2px rgba(60, 64, 67, 0.3), 0 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "    fill: var(--button-hover-fill-color);\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart-complete:disabled,\n",
              "  .colab-df-quickchart-complete:disabled:hover {\n",
              "    background-color: var(--disabled-bg-color);\n",
              "    fill: var(--disabled-fill-color);\n",
              "    box-shadow: none;\n",
              "  }\n",
              "\n",
              "  .colab-df-spinner {\n",
              "    border: 2px solid var(--fill-color);\n",
              "    border-color: transparent;\n",
              "    border-bottom-color: var(--fill-color);\n",
              "    animation:\n",
              "      spin 1s steps(1) infinite;\n",
              "  }\n",
              "\n",
              "  @keyframes spin {\n",
              "    0% {\n",
              "      border-color: transparent;\n",
              "      border-bottom-color: var(--fill-color);\n",
              "      border-left-color: var(--fill-color);\n",
              "    }\n",
              "    20% {\n",
              "      border-color: transparent;\n",
              "      border-left-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "    }\n",
              "    30% {\n",
              "      border-color: transparent;\n",
              "      border-left-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "      border-right-color: var(--fill-color);\n",
              "    }\n",
              "    40% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "    }\n",
              "    60% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "    }\n",
              "    80% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "      border-bottom-color: var(--fill-color);\n",
              "    }\n",
              "    90% {\n",
              "      border-color: transparent;\n",
              "      border-bottom-color: var(--fill-color);\n",
              "    }\n",
              "  }\n",
              "</style>\n",
              "\n",
              "  <script>\n",
              "    async function quickchart(key) {\n",
              "      const quickchartButtonEl =\n",
              "        document.querySelector('#' + key + ' button');\n",
              "      quickchartButtonEl.disabled = true;  // To prevent multiple clicks.\n",
              "      quickchartButtonEl.classList.add('colab-df-spinner');\n",
              "      try {\n",
              "        const charts = await google.colab.kernel.invokeFunction(\n",
              "            'suggestCharts', [key], {});\n",
              "      } catch (error) {\n",
              "        console.error('Error during call to suggestCharts:', error);\n",
              "      }\n",
              "      quickchartButtonEl.classList.remove('colab-df-spinner');\n",
              "      quickchartButtonEl.classList.add('colab-df-quickchart-complete');\n",
              "    }\n",
              "    (() => {\n",
              "      let quickchartButtonEl =\n",
              "        document.querySelector('#df-fe90f224-6751-4af1-8880-f4deb2c3243a button');\n",
              "      quickchartButtonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "    })();\n",
              "  </script>\n",
              "</div>\n",
              "    </div>\n",
              "  </div>\n"
            ]
          },
          "metadata": {},
          "execution_count": 17
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "movies.describe\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "HaQP2HcrKRy4",
        "outputId": "228af1b1-d4d2-4b09-cfd7-ada0db103033"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "<bound method NDFrame.describe of                                            Title                  Genre  \\\n",
              "0                                Enter the Anime            Documentary   \n",
              "1                                    Dark Forces               Thriller   \n",
              "2                                        The App  Science fiction/Drama   \n",
              "3                                 The Open House        Horror thriller   \n",
              "4                                    Kaali Khuhi                Mystery   \n",
              "..                                           ...                    ...   \n",
              "579        Taylor Swift: Reputation Stadium Tour           Concert Film   \n",
              "580  Winter on Fire: Ukraine's Fight for Freedom            Documentary   \n",
              "581                      Springsteen on Broadway           One-man show   \n",
              "582    Emicida: AmarElo - It's All For Yesterday            Documentary   \n",
              "583     David Attenborough: A Life on Our Planet            Documentary   \n",
              "\n",
              "              Premiere  Runtime  IMDB Score                  Language  \n",
              "0       August 5, 2019       58         2.5          English/Japanese  \n",
              "1      August 21, 2020       81         2.6                   Spanish  \n",
              "2    December 26, 2019       79         2.6                   Italian  \n",
              "3     January 19, 2018       94         3.2                   English  \n",
              "4     October 30, 2020       90         3.4                     Hindi  \n",
              "..                 ...      ...         ...                       ...  \n",
              "579  December 31, 2018      125         8.4                   English  \n",
              "580    October 9, 2015       91         8.4  English/Ukranian/Russian  \n",
              "581  December 16, 2018      153         8.5                   English  \n",
              "582   December 8, 2020       89         8.6                Portuguese  \n",
              "583    October 4, 2020       83         9.0                   English  \n",
              "\n",
              "[584 rows x 6 columns]>"
            ]
          },
          "metadata": {},
          "execution_count": 9
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Write your code for column-wise null count here\n",
        "column_null = movies.isna().sum()\n",
        "column_null"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "jEX-FnvgKkGQ",
        "outputId": "845ee447-075e-4895-92a4-21bf80ac5596"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "Title         0\n",
              "Genre         0\n",
              "Premiere      0\n",
              "Runtime       0\n",
              "IMDB Score    0\n",
              "Language      0\n",
              "dtype: int64"
            ]
          },
          "metadata": {},
          "execution_count": 10
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Write your code for row-wise null count here\n",
        "row_wise = movies.isnull().sum(axis=1)\n",
        "row_wise\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "efYCOh8HLHvD",
        "outputId": "eb5ccc37-c5a7-4626-b591-e7d075f15672"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "0      0\n",
              "1      0\n",
              "2      0\n",
              "3      0\n",
              "4      0\n",
              "      ..\n",
              "579    0\n",
              "580    0\n",
              "581    0\n",
              "582    0\n",
              "583    0\n",
              "Length: 584, dtype: int64"
            ]
          },
          "metadata": {},
          "execution_count": 11
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Write your code for column-wise null percentages here\n",
        "percent_missing = movies.isnull().sum() * 100 / len(movies)\n",
        "percent_missing"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "QJk32nZrLQai",
        "outputId": "ba96da0e-9ff7-4afb-b913-6ba8702592e9"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "Title         0.0\n",
              "Genre         0.0\n",
              "Premiere      0.0\n",
              "Runtime       0.0\n",
              "IMDB Score    0.0\n",
              "Language      0.0\n",
              "dtype: float64"
            ]
          },
          "metadata": {},
          "execution_count": 12
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "movies.info()\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "emVGufV2LlZ6",
        "outputId": "31f999c7-fce5-4bcd-c9a8-aa2a74b2d374"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "<class 'pandas.core.frame.DataFrame'>\n",
            "RangeIndex: 584 entries, 0 to 583\n",
            "Data columns (total 6 columns):\n",
            " #   Column      Non-Null Count  Dtype  \n",
            "---  ------      --------------  -----  \n",
            " 0   Title       584 non-null    object \n",
            " 1   Genre       584 non-null    object \n",
            " 2   Premiere    584 non-null    object \n",
            " 3   Runtime     584 non-null    int64  \n",
            " 4   IMDB Score  584 non-null    float64\n",
            " 5   Language    584 non-null    object \n",
            "dtypes: float64(1), int64(1), object(4)\n",
            "memory usage: 27.5+ KB\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#drop rows with missing values\n",
        "movies=movies.dropna()\n",
        "movies.info()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "yarzpamoPINa",
        "outputId": "5db555ae-98fc-4c8e-96c6-74b4aa7b52d6"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "<class 'pandas.core.frame.DataFrame'>\n",
            "RangeIndex: 584 entries, 0 to 583\n",
            "Data columns (total 6 columns):\n",
            " #   Column      Non-Null Count  Dtype  \n",
            "---  ------      --------------  -----  \n",
            " 0   Title       584 non-null    object \n",
            " 1   Genre       584 non-null    object \n",
            " 2   Premiere    584 non-null    object \n",
            " 3   Runtime     584 non-null    int64  \n",
            " 4   IMDB Score  584 non-null    float64\n",
            " 5   Language    584 non-null    object \n",
            "dtypes: float64(1), int64(1), object(4)\n",
            "memory usage: 27.5+ KB\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#describe\n",
        "movies.describe()\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 300
        },
        "id": "IA15nWRiPrJV",
        "outputId": "e14d7859-fda9-46ec-fa10-d892446cd458"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "          Runtime  IMDB Score\n",
              "count  584.000000  584.000000\n",
              "mean    93.577055    6.271747\n",
              "std     27.761683    0.979256\n",
              "min      4.000000    2.500000\n",
              "25%     86.000000    5.700000\n",
              "50%     97.000000    6.350000\n",
              "75%    108.000000    7.000000\n",
              "max    209.000000    9.000000"
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-9855b353-a618-42c8-8cd3-56a5287cf23f\" class=\"colab-df-container\">\n",
              "    <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>Runtime</th>\n",
              "      <th>IMDB Score</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>count</th>\n",
              "      <td>584.000000</td>\n",
              "      <td>584.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>mean</th>\n",
              "      <td>93.577055</td>\n",
              "      <td>6.271747</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>std</th>\n",
              "      <td>27.761683</td>\n",
              "      <td>0.979256</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>min</th>\n",
              "      <td>4.000000</td>\n",
              "      <td>2.500000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>25%</th>\n",
              "      <td>86.000000</td>\n",
              "      <td>5.700000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>50%</th>\n",
              "      <td>97.000000</td>\n",
              "      <td>6.350000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>75%</th>\n",
              "      <td>108.000000</td>\n",
              "      <td>7.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>max</th>\n",
              "      <td>209.000000</td>\n",
              "      <td>9.000000</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "    <div class=\"colab-df-buttons\">\n",
              "\n",
              "  <div class=\"colab-df-container\">\n",
              "    <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-9855b353-a618-42c8-8cd3-56a5287cf23f')\"\n",
              "            title=\"Convert this dataframe to an interactive table.\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\" viewBox=\"0 -960 960 960\">\n",
              "    <path d=\"M120-120v-720h720v720H120Zm60-500h600v-160H180v160Zm220 220h160v-160H400v160Zm0 220h160v-160H400v160ZM180-400h160v-160H180v160Zm440 0h160v-160H620v160ZM180-180h160v-160H180v160Zm440 0h160v-160H620v160Z\"/>\n",
              "  </svg>\n",
              "    </button>\n",
              "\n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    .colab-df-buttons div {\n",
              "      margin-bottom: 4px;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "    <script>\n",
              "      const buttonEl =\n",
              "        document.querySelector('#df-9855b353-a618-42c8-8cd3-56a5287cf23f button.colab-df-convert');\n",
              "      buttonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "      async function convertToInteractive(key) {\n",
              "        const element = document.querySelector('#df-9855b353-a618-42c8-8cd3-56a5287cf23f');\n",
              "        const dataTable =\n",
              "          await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                    [key], {});\n",
              "        if (!dataTable) return;\n",
              "\n",
              "        const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "          '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "          + ' to learn more about interactive tables.';\n",
              "        element.innerHTML = '';\n",
              "        dataTable['output_type'] = 'display_data';\n",
              "        await google.colab.output.renderOutput(dataTable, element);\n",
              "        const docLink = document.createElement('div');\n",
              "        docLink.innerHTML = docLinkHtml;\n",
              "        element.appendChild(docLink);\n",
              "      }\n",
              "    </script>\n",
              "  </div>\n",
              "\n",
              "\n",
              "<div id=\"df-3831e684-7a42-4058-8e63-0b9683567a7a\">\n",
              "  <button class=\"colab-df-quickchart\" onclick=\"quickchart('df-3831e684-7a42-4058-8e63-0b9683567a7a')\"\n",
              "            title=\"Suggest charts.\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "<svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "     width=\"24px\">\n",
              "    <g>\n",
              "        <path d=\"M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zM9 17H7v-7h2v7zm4 0h-2V7h2v10zm4 0h-2v-4h2v4z\"/>\n",
              "    </g>\n",
              "</svg>\n",
              "  </button>\n",
              "\n",
              "<style>\n",
              "  .colab-df-quickchart {\n",
              "      --bg-color: #E8F0FE;\n",
              "      --fill-color: #1967D2;\n",
              "      --hover-bg-color: #E2EBFA;\n",
              "      --hover-fill-color: #174EA6;\n",
              "      --disabled-fill-color: #AAA;\n",
              "      --disabled-bg-color: #DDD;\n",
              "  }\n",
              "\n",
              "  [theme=dark] .colab-df-quickchart {\n",
              "      --bg-color: #3B4455;\n",
              "      --fill-color: #D2E3FC;\n",
              "      --hover-bg-color: #434B5C;\n",
              "      --hover-fill-color: #FFFFFF;\n",
              "      --disabled-bg-color: #3B4455;\n",
              "      --disabled-fill-color: #666;\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart {\n",
              "    background-color: var(--bg-color);\n",
              "    border: none;\n",
              "    border-radius: 50%;\n",
              "    cursor: pointer;\n",
              "    display: none;\n",
              "    fill: var(--fill-color);\n",
              "    height: 32px;\n",
              "    padding: 0;\n",
              "    width: 32px;\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart:hover {\n",
              "    background-color: var(--hover-bg-color);\n",
              "    box-shadow: 0 1px 2px rgba(60, 64, 67, 0.3), 0 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "    fill: var(--button-hover-fill-color);\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart-complete:disabled,\n",
              "  .colab-df-quickchart-complete:disabled:hover {\n",
              "    background-color: var(--disabled-bg-color);\n",
              "    fill: var(--disabled-fill-color);\n",
              "    box-shadow: none;\n",
              "  }\n",
              "\n",
              "  .colab-df-spinner {\n",
              "    border: 2px solid var(--fill-color);\n",
              "    border-color: transparent;\n",
              "    border-bottom-color: var(--fill-color);\n",
              "    animation:\n",
              "      spin 1s steps(1) infinite;\n",
              "  }\n",
              "\n",
              "  @keyframes spin {\n",
              "    0% {\n",
              "      border-color: transparent;\n",
              "      border-bottom-color: var(--fill-color);\n",
              "      border-left-color: var(--fill-color);\n",
              "    }\n",
              "    20% {\n",
              "      border-color: transparent;\n",
              "      border-left-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "    }\n",
              "    30% {\n",
              "      border-color: transparent;\n",
              "      border-left-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "      border-right-color: var(--fill-color);\n",
              "    }\n",
              "    40% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "    }\n",
              "    60% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "    }\n",
              "    80% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "      border-bottom-color: var(--fill-color);\n",
              "    }\n",
              "    90% {\n",
              "      border-color: transparent;\n",
              "      border-bottom-color: var(--fill-color);\n",
              "    }\n",
              "  }\n",
              "</style>\n",
              "\n",
              "  <script>\n",
              "    async function quickchart(key) {\n",
              "      const quickchartButtonEl =\n",
              "        document.querySelector('#' + key + ' button');\n",
              "      quickchartButtonEl.disabled = true;  // To prevent multiple clicks.\n",
              "      quickchartButtonEl.classList.add('colab-df-spinner');\n",
              "      try {\n",
              "        const charts = await google.colab.kernel.invokeFunction(\n",
              "            'suggestCharts', [key], {});\n",
              "      } catch (error) {\n",
              "        console.error('Error during call to suggestCharts:', error);\n",
              "      }\n",
              "      quickchartButtonEl.classList.remove('colab-df-spinner');\n",
              "      quickchartButtonEl.classList.add('colab-df-quickchart-complete');\n",
              "    }\n",
              "    (() => {\n",
              "      let quickchartButtonEl =\n",
              "        document.querySelector('#df-3831e684-7a42-4058-8e63-0b9683567a7a button');\n",
              "      quickchartButtonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "    })();\n",
              "  </script>\n",
              "</div>\n",
              "    </div>\n",
              "  </div>\n"
            ]
          },
          "metadata": {},
          "execution_count": 23
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#checking null values\n",
        "movies.isnull().values.any()\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "qPc1eam0QRNE",
        "outputId": "7b5c663a-b0d4-42b0-d055-abb10976d442"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "False"
            ]
          },
          "metadata": {},
          "execution_count": 24
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#shape\n",
        "movies.shape"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "zDMnoXg6QbTr",
        "outputId": "722040fc-f282-493b-d6fc-fa2038fa4efb"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "(584, 6)"
            ]
          },
          "metadata": {},
          "execution_count": 26
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Sort the DataFrame by IMDb scores in descending order\n",
        "movies_sorted = movies.sort_values(by='IMDB Score', ascending=False)\n",
        "\n",
        "# Display the top N movies with the highest scores (e.g., top 10)\n",
        "top_n = 10\n",
        "top_movies = movies_sorted.head(top_n)\n",
        "\n",
        "# Print the top movies\n",
        "print(\"Movies with the Highest IMDb Scores:\")\n",
        "print(top_movies)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "6yZPEwa4SlF8",
        "outputId": "b2d694f3-0e96-4fcb-f83b-bbfc81bd744d"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Movies with the Highest IMDb Scores:\n",
            "                                           Title  \\\n",
            "583     David Attenborough: A Life on Our Planet   \n",
            "582    Emicida: AmarElo - It's All For Yesterday   \n",
            "581                      Springsteen on Broadway   \n",
            "580  Winter on Fire: Ukraine's Fight for Freedom   \n",
            "579        Taylor Swift: Reputation Stadium Tour   \n",
            "578   Ben Platt: Live from Radio City Music Hall   \n",
            "577                       Dancing with the Birds   \n",
            "576                      Cuba and the Cameraman    \n",
            "573                                        Klaus   \n",
            "571                                         13th   \n",
            "\n",
            "                                    Genre           Premiere  Runtime  \\\n",
            "583                           Documentary    October 4, 2020       83   \n",
            "582                           Documentary   December 8, 2020       89   \n",
            "581                          One-man show  December 16, 2018      153   \n",
            "580                           Documentary    October 9, 2015       91   \n",
            "579                          Concert Film  December 31, 2018      125   \n",
            "578                          Concert Film       May 20, 2020       85   \n",
            "577                           Documentary   October 23, 2019       51   \n",
            "576                           Documentary  November 24, 2017      114   \n",
            "573  Animation/Christmas/Comedy/Adventure  November 15, 2019       97   \n",
            "571                           Documentary    October 7, 2016      100   \n",
            "\n",
            "     IMDB Score                  Language  \n",
            "583         9.0                   English  \n",
            "582         8.6                Portuguese  \n",
            "581         8.5                   English  \n",
            "580         8.4  English/Ukranian/Russian  \n",
            "579         8.4                   English  \n",
            "578         8.4                   English  \n",
            "577         8.3                   English  \n",
            "576         8.3                   English  \n",
            "573         8.2                   English  \n",
            "571         8.2                   English  \n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Display the top N movies with the highest scores (e.g., top 10)\n",
        "top_n = 10\n",
        "top_movies = movies_sorted.head(top_n)\n",
        "# Print the top movies\n",
        "print(\"Movies with the Highest IMDb Scores:\")\n",
        "print(top_movies)\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "HUJ4WaVTTXNy",
        "outputId": "232e3398-608e-42b0-cfdf-742870ac1b64"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Movies with the Highest IMDb Scores:\n",
            "                                           Title  \\\n",
            "583     David Attenborough: A Life on Our Planet   \n",
            "582    Emicida: AmarElo - It's All For Yesterday   \n",
            "581                      Springsteen on Broadway   \n",
            "580  Winter on Fire: Ukraine's Fight for Freedom   \n",
            "579        Taylor Swift: Reputation Stadium Tour   \n",
            "578   Ben Platt: Live from Radio City Music Hall   \n",
            "577                       Dancing with the Birds   \n",
            "576                      Cuba and the Cameraman    \n",
            "573                                        Klaus   \n",
            "571                                         13th   \n",
            "\n",
            "                                    Genre           Premiere  Runtime  \\\n",
            "583                           Documentary    October 4, 2020       83   \n",
            "582                           Documentary   December 8, 2020       89   \n",
            "581                          One-man show  December 16, 2018      153   \n",
            "580                           Documentary    October 9, 2015       91   \n",
            "579                          Concert Film  December 31, 2018      125   \n",
            "578                          Concert Film       May 20, 2020       85   \n",
            "577                           Documentary   October 23, 2019       51   \n",
            "576                           Documentary  November 24, 2017      114   \n",
            "573  Animation/Christmas/Comedy/Adventure  November 15, 2019       97   \n",
            "571                           Documentary    October 7, 2016      100   \n",
            "\n",
            "     IMDB Score                  Language  \n",
            "583         9.0                   English  \n",
            "582         8.6                Portuguese  \n",
            "581         8.5                   English  \n",
            "580         8.4  English/Ukranian/Russian  \n",
            "579         8.4                   English  \n",
            "578         8.4                   English  \n",
            "577         8.3                   English  \n",
            "576         8.3                   English  \n",
            "573         8.2                   English  \n",
            "571         8.2                   English  \n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Assuming the dataset has a 'Genre' column (adjust column name as needed)\n",
        "genre_column = 'Genre'\n",
        "# Count the occurrences of each genre\n",
        "genre_counts = movies[genre_column].value_counts()\n",
        "# Find the most popular genre\n",
        "most_popular_genre = genre_counts.idxmax()\n",
        "# Display the most popular genre and its count\n",
        "print(\"Most Popular Genre:\", most_popular_genre)\n",
        "print(\"Count:\", genre_counts.max())\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "pKKLTMgoUGTL",
        "outputId": "b24c2b63-77ec-45ed-a03e-65766dcd5159"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Most Popular Genre: Documentary\n",
            "Count: 159\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import matplotlib.pyplot as plt\n",
        "# Choose the two variables for the scatter plot\n",
        "x_variable = 'Runtime'  # Replace with the actual column name\n",
        "y_variable = 'IMDB Score'     # Replace with the actual column name\n",
        "\n",
        "# Create a scatter plot\n",
        "plt.figure(figsize=(10, 6))\n",
        "plt.scatter(movies[x_variable], movies[y_variable], alpha=0.5)\n",
        "plt.title(f'Scatter Plot of {x_variable} vs. {y_variable}')\n",
        "plt.xlabel(x_variable)\n",
        "plt.ylabel(y_variable)\n",
        "plt.grid(True)\n",
        "plt.show()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 564
        },
        "id": "BjS7_0FebAgG",
        "outputId": "7bac5b68-f08e-4ee8-961b-4b47f1d93819"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 1000x600 with 1 Axes>"
            ],
            "image/png": "iVBORw0KGgoAAAANSUhEUgAAA0EAAAIjCAYAAADFthA8AAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjcuMSwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy/bCgiHAAAACXBIWXMAAA9hAAAPYQGoP6dpAAEAAElEQVR4nOz9eZxjVZ33gX/ufrPXktp7qa6qXqDpAYFGARGQpQdRcQNHdNhcf6PyOP50Hn0cEfRhXMeBnzKK+giMDoyIojiINAy4AKLs2k3va3XXmkpV9uRu5/fHTdJJKpVKUklVUvV9v1686ErOPed7vud7zr0n59zP4RhjDARBEARBEARBECsEfqkNIAiCIAiCIAiCWExoEkQQBEEQBEEQxIqCJkEEQRAEQRAEQawoaBJEEARBEARBEMSKgiZBBEEQBEEQBEGsKGgSRBAEQRAEQRDEioImQQRBEARBEARBrChoEkQQBEEQBEEQxIqCJkEEQRAEQRAEQawoaBJEEASxBBw+fBgcx+Huu+9ealPy+M1vfoPTTjsNqqqC4zjMzMwstUkVw3Ecbr755qU2gyAIgmhgaBJEEERN+etf/4p3vetdWLt2LVRVRV9fHy655BJ861vfqluZ9957L2677bZZn4+MjODmm2/Gyy+/XLeyC/ntb38LjuOy/0mShIGBAVxzzTU4ePBgTcp45plncPPNN9d8gjI1NYWrrroKDocDd9xxB370ox/B5XIVTXv33Xfn1VMURfT19eG6667D8ePHa2pXMX7961/TRKcEN998MziOQyAQyH523XXXgeM4eL1eJBKJWdfs27cv257f+MY3sp8XxrSiKOjq6sIFF1yAf/mXf8Hk5OSsvArjg+M4dHZ24sILL8QjjzxSVh0sy8J//Md/4LWvfS3a2trg8XiwYcMGXHPNNXj22Wer8ApBEMQJxKU2gCCI5cMzzzyDCy+8EGvWrMEHP/hBdHd3Y3h4GM8++yxuv/12fPzjH69Luffeey927NiBT3ziE3mfj4yM4JZbbkF/fz9OO+20upQ9FzfeeCO2bt0KXdfx4osv4nvf+x4efvhh/PWvf0Vvb++C8n7mmWdwyy234LrrrkNLS0ttDAbw3HPPIRKJ4Etf+hIuvvjisq754he/iHXr1iGZTOLZZ5/F3Xffjaeeego7duyAqqo1s62QX//617jjjjuKToQSiQREkW5vxRBFEfF4HL/61a9w1VVX5X33n//5n1BVFclksui1mZg2TROTk5N45pln8IUvfAHf/OY3cf/99+ONb3zjrGsy8cEYw/j4OO6++2686U1vwq9+9Su8+c1vLmnrjTfeiDvuuANXXHEF3vve90IURezZswePPPIIBgYG8LrXva56RxAEseKhuwRBEDXj1ltvhc/nw3PPPTfr4XxiYmJpjKoDsVhszhWSDOeddx7e9a53AQCuv/56bNiwATfeeCPuuecefPazn10MMysm00aVTKwuu+wynHnmmQCAD3zgA/D7/fjqV7+Khx56aNZD9mJRz8lXs6MoCs4991zcd999s9rn3nvvxeWXX46f/exnRa/NjekMr7zyCi699FK8853vxKuvvoqenp6873PjAwDe//73o6urC/fdd1/JSdD4+Dj+/d//HR/84Afxve99L++72267rejqU70wDAOWZUGW5UUrkyCI+kPb4QiCqBkHDhzA5s2biz5Ed3Z2zvrsxz/+Mc466yw4nU60trbiDW94A7Zv3579/pe//CUuv/xy9Pb2QlEUDA4O4ktf+hJM08ymueCCC/Dwww/jyJEj2W03/f39+O1vf4utW7cCsCchme9y38H505/+hL/927+Fz+eD0+nE+eefj6effjrPxsy2oldffRVXX301Wltb8frXv75i32R+JT906FDJdE888QTOO+88uFwutLS04IorrsCuXbvy7Pn0pz8NAFi3bl22XocPHy6Z709/+lOcccYZcDgc8Pv9eN/73pe3be2CCy7AtddeCwDYunUrOI7DddddV3E9zzvvPAB2LOTmfcEFF8xKe91116G/vz/7d+Y9qW984xv43ve+h8HBQSiKgq1bt+K5557Lu+6OO+4AgLztVhkK3wnKtOHevXvxvve9Dz6fDx0dHfj85z8PxhiGh4dxxRVXwOv1oru7G//6r/86y9ZUKoUvfOELGBoagqIoWL16Nf7pn/4JqVSqpD8+9rGPwe12Ix6Pz/ruPe95D7q7u7Px/Pzzz2Pbtm3w+/1wOBxYt24dbrjhhpL5V8PVV1+NRx55JG875XPPPYd9+/bh6quvriivU089FbfddhtmZmbw7W9/e970LS0tcDgc867UHTp0CIwxnHvuubO+y2yty2VmZgb/+I//iP7+fiiKglWrVuGaa67J2w44MTGRnYSpqopTTz0V99xzT14+uTF42223ZWPw1VdfBQDs3r0b73rXu9DW1gZVVXHmmWfioYcemrfeBEE0HrQSRBBEzVi7di3++Mc/YseOHTjllFNKpr3llltw880345xzzsEXv/hFyLKMP/3pT3jiiSdw6aWXArDfK3C73fjkJz8Jt9uNJ554AjfddBPC4TC+/vWvAwA+97nPIRQK4dixY/i3f/s3AIDb7cZJJ52EL37xi7jpppvwoQ99KPtwfs455wCwJxuXXXYZzjjjDHzhC18Az/O466678MY3vhF/+MMfcNZZZ+XZe+WVV2L9+vX4l3/5FzDGKvZNZlLQ3t4+Z5rHH38cl112GQYGBnDzzTcjkUjgW9/6Fs4991y8+OKL6O/vxzve8Q7s3bsX9913H/7t3/4Nfr8fANDR0TFnvnfffTeuv/56bN26FV/+8pcxPj6O22+/HU8//TReeukltLS04HOf+xw2btyI733ve9ktTIODgxXXMzMZa21trfjaDPfeey8ikQg+/OEPg+M4fO1rX8M73vEOHDx4EJIk4cMf/jBGRkbw2GOP4Uc/+lHZ+b773e/GSSedhK985St4+OGH8X//7/9FW1sb7rzzTrzxjW/EV7/6Vfznf/4nPvWpT2Hr1q14wxveAMB+N+Wtb30rnnrqKXzoQx/CSSedhL/+9a/4t3/7N+zduxe/+MUvSpZ5xx134OGHH8aVV16Z/TyzJe26666DIAiYmJjApZdeio6ODnzmM59BS0sLDh8+jJ///OdV+3Eu3vGOd+AjH/kIfv7zn2cnWffeey82bdqE008/veL83vWud+H9738/tm/fjltvvTXvu1AohEAgAMYYJiYm8K1vfQvRaBTve9/7Sua5du1aAPbk/corr4TT6ZwzbTQaxXnnnYddu3bhhhtuwOmnn45AIICHHnoIx44dg9/vRyKRwAUXXID9+/fjYx/7GNatW4ef/vSnuO666zAzM4P/9b/+V16ed911F5LJJD70oQ9BURS0tbVh586dOPfcc9HX14fPfOYzcLlcuP/++/G2t70NP/vZz/D2t7+9Yt8RBLGEMIIgiBqxfft2JggCEwSBnX322eyf/umf2KOPPso0TctLt2/fPsbzPHv729/OTNPM+86yrOy/4/H4rDI+/OEPM6fTyZLJZPazyy+/nK1du3ZW2ueee44BYHfdddesMtavX8+2bds2q7x169axSy65JPvZF77wBQaAvec97ynLB08++SQDwH74wx+yyclJNjIywh5++GHW39/POI5jzz33HGOMsUOHDs2y7bTTTmOdnZ1samoq+9krr7zCeJ5n11xzTfazr3/96wwAO3To0Lz2aJrGOjs72SmnnMISiUT28//+7/9mANhNN92U/eyuu+5iALI2liKT9vHHH2eTk5NseHiYPfDAA6yjo4MpisKGh4ezac8//3x2/vnnz8rj2muvzWu3jE/a29tZMBjMfv7LX/6SAWC/+tWvsp999KMfZXPdwgCwL3zhC9m/M234oQ99KPuZYRhs1apVjOM49pWvfCX7+fT0NHM4HOzaa6/NfvajH/2I8TzP/vCHP+SV893vfpcBYE8//fScfrIsi/X19bF3vvOdeZ/ff//9DAD7/e9/zxhj7MEHHyzb9+WQqfPk5GT2s2uvvZa5XC7GGGPvete72EUXXcQYY8w0Tdbd3c1uueWWbBt8/etfz16Xiemf/vSnc5Z36qmnstbW1uzfmfgo/E9RFHb33XeXVYdrrrmGAWCtra3s7W9/O/vGN77Bdu3aNSvdTTfdxACwn//857O+y/Tv2267jQFgP/7xj7PfaZrGzj77bOZ2u1k4HGaMnYhBr9fLJiYm8vK66KKL2JYtW/LGHsuy2DnnnMPWr19fVp0IgmgcaDscQRA145JLLsEf//hHvPWtb8Urr7yCr33ta9i2bRv6+vrytoz84he/gGVZuOmmm8Dz+cNQ7rYmh8OR/XckEkEgEMB5552HeDyO3bt3V23nyy+/nN36MzU1hUAggEAggFgshosuugi///3vYVlW3jUf+chHKirjhhtuQEdHB3p7e3H55ZcjFovhnnvuyXs/IpfR0VG8/PLLuO6669DW1pb9/G/+5m9wySWX4Ne//nXlFYW9xWpiYgL/8A//kPeuzOWXX45Nmzbh4YcfrirfDBdffDE6OjqwevVqvOtd74LL5cJDDz2EVatWVZ3nu9/97ryVpMwq3kLV9T7wgQ9k/y0IAs4880wwxvD+978/+3lLSws2btyYV9ZPf/pTnHTSSdi0aVM2VgKBQHaL45NPPjlnmRzH4corr8Svf/1rRKPR7Oc/+clP0NfXl91amdlC+t///d/QdX1B9SyHq6++Gr/97W8xNjaGJ554AmNjYxVvhcvF7XYjEonM+vyOO+7AY489hsceeww//vGPceGFF+IDH/hAWStcd911F7797W9j3bp1ePDBB/GpT30KJ510Ei666KK8rZw/+9nPcOqppxZdicmMJ7/+9a/R3d2N97znPdnvJEnCjTfeiGg0it/97nd5173zne/MW10NBoN44okncNVVV2XHokAggKmpKWzbtg379u1bFFVEgiBqB02CCIKoKVu3bsXPf/5zTE9P489//jM++9nPIhKJ4F3veld2X/2BAwfA8zxOPvnkknnt3LkTb3/72+Hz+eD1etHR0ZHdRhMKhaq2cd++fQCAa6+9Fh0dHXn//eAHP0AqlZqV/7p16yoq46abbsJjjz2GJ554An/5y18wMjKCv//7v58z/ZEjRwAAGzdunPXdSSedlJ2kVUqpfDdt2pT9vloyD7kPPPAA3vSmNyEQCEBRlAXluWbNmry/MxOi6enpmubr8/mgqmp2S2Hu57ll7du3Dzt37pwVKxs2bAAwv+jHu9/9biQSiewPAdFoFL/+9a9x5ZVXZh/Szz//fLzzne/ELbfcAr/fjyuuuAJ33XXXvO8cVcub3vQmeDwe/OQnP8F//ud/YuvWrRgaGqo6v2g0Co/HM+vzs846CxdffDEuvvhivPe978XDDz+Mk08+GR/72MegaVrJPHmex0c/+lG88MILCAQC+OUvf4nLLrsMTzzxBP7u7/4um+7AgQPzbr89cuQI1q9fP+tHl5NOOin7fS6F/X3//v1gjOHzn//8rDj4whe+AGB5ib8QxEqA3gkiCKIuyLKMrVu3YuvWrdiwYQOuv/56/PSnP80+MMzHzMwMzj//fHi9Xnzxi1/E4OAgVFXFiy++iP/9v//3rJWaSshc+/Wvf31O6Wy32533d+6qVDls2bKlbJnpZuass87Krm697W1vw+tf/3pcffXV2LNnT9aHHMcVfY8qV+AiF0EQin5eLI9KKJZvOWVZloUtW7bgm9/8ZtG0q1evLlnu6173OvT39+P+++/H1VdfjV/96ldIJBJ497vfnU3DcRweeOABPPvss/jVr36FRx99FDfccAP+9V//Fc8+++yseFwoiqLgHe94B+655x4cPHhwQWcu6bqOvXv3zjsRAeyJzYUXXojbb78d+/btw+bNm8sqo729HW9961vx1re+FRdccAF+97vf4ciRI9l3h2pNYX/PjBmf+tSnsG3btqLXLGQSSRDE4kOTIIIg6k7mIXl0dBQAMDg4CMuy8Oqrr845Cfntb3+Lqakp/PznP8++oA4UV1fL3UJXzueZF/69Xm/DTFQyD3N79uyZ9d3u3bvh9/uzstxz1Wu+fAvPcdmzZ09NHyIFQcCXv/xlXHjhhfj2t7+Nz3zmMwDslZxiW9kWsgpViQ8WyuDgIF555RVcdNFFVZd71VVX4fbbb0c4HMZPfvIT9Pf3Fz3n5nWvex1e97rX4dZbb8W9996L9773vfiv//qvvK18teLqq6/GD3/4Q/A8n7eyUikPPPAAEonEnJODQgzDAIC87YGVcOaZZ+J3v/sdRkdHsXbtWgwODmLHjh0lr1m7di3+8pe/wLKsvNWgzLba+frBwMAAAHsLXaOMGQRBLAzaDkcQRM148skni/5an3mfJbMl621vext4nscXv/jFWSs6meszv9Dn5qdpGv793/99Vv4ul6vo9rjMpCFXChgAzjjjDAwODuIb3/hG0QexxTyDJENPTw9OO+003HPPPXn27tixA9u3b8eb3vSm7Gdz1asYZ555Jjo7O/Hd7343b2vVI488gl27duHyyy+vWR0AWw77rLPOwm233ZY9dHNwcBC7d+/O8+srr7wyS468EirxwUK56qqrcPz4cXz/+9+f9V0ikShrm+K73/1upFIp3HPPPfjNb34z64ye6enpWX0n8wNBbrsdOHAgT358IVx44YX40pe+hG9/+9vo7u6uKo9XXnkFn/jEJ9Da2oqPfvSj86bXdR3bt2+HLMvZrWjFGBsby26fzUXTNPzP//wPeJ7Prry8853vxCuvvIIHH3xwVvqMT9/0pjdhbGwMP/nJT7LfGYaBb33rW3C73Tj//PNL2t3Z2YkLLrgAd955Z/bHnFyWYswgCGJh0EoQQRA14+Mf/zji8Tje/va3Y9OmTdA0Dc8880z2l+/rr78egL1t5HOf+xy+9KUv4bzzzsM73vEOKIqC5557Dr29vfjyl7+Mc845B62trbj22mtx4403guM4/OhHPyo6yTrjjDPwk5/8BJ/85CexdetWuN1uvOUtb8Hg4CBaWlrw3e9+Fx6PBy6XC6997Wuxbt06/OAHP8Bll12GzZs34/rrr0dfXx+OHz+OJ598El6vF7/61a8W2334+te/jssuuwxnn3023v/+92clsn0+X952pTPOOAOALQ/+d3/3d5AkCW95y1uKHuAqSRK++tWv4vrrr8f555+P97znPVmJ7P7+fvzjP/5jzevx6U9/GldeeSXuvvtufOQjH8ENN9yAb37zm9i2bRve//73Y2JiAt/97nexefNmhMPhqsrI+ODGG2/Etm3bIAjCglYzSvH3f//3uP/++/GRj3wETz75JM4991yYpondu3fj/vvvx6OPPjqn4EWG008/PRv3qVQqbyscANxzzz3493//d7z97W/H4OAgIpEIvv/978Pr9eZNgC+66CIAmPdcqHLgeR7//M//XHb6P/zhD0gmkzBNE1NTU3j66afx0EMPwefz4cEHHyw6kXrkkUeyqy0TExO49957sW/fPnzmM5+B1+uds6xjx47hrLPOwhvf+EZcdNFF6O7uxsTEBO67777sxCvzLtenP/1pPPDAA7jyyitxww034IwzzkAwGMRDDz2E7373uzj11FPxoQ99CHfeeSeuu+46vPDCC+jv78cDDzyAp59+GrfddlvR95kKueOOO/D6178eW7ZswQc/+EEMDAxgfHwcf/zjH3Hs2DG88sorZfuSIIgGYIlU6QiCWIY88sgj7IYbbmCbNm1ibrebybLMhoaG2Mc//nE2Pj4+K/0Pf/hD9prXvIYpisJaW1vZ+eefzx577LHs908//TR73etexxwOB+vt7c1KbgNgTz75ZDZdNBplV199NWtpaWEA8mSXf/nLX7KTTz6ZiaI4S5L6pZdeYu94xztYe3s7UxSFrV27ll111VXsf/7nf7JpikkNl6IcOWHGiktkM8bY448/zs4991zmcDiY1+tlb3nLW9irr7466/ovfelLrK+vj/E8X5Zc9k9+8pOsr9va2th73/teduzYsbw01UhkF0trmiYbHBxkg4ODzDAMxhhjP/7xj9nAwACTZZmddtpp7NFHH51TIjtXnjkDCmSvDcNgH//4x1lHRwfjOC5PLrsw7VxtmCsZncv555/PNm/enPeZpmnsq1/9Ktu8eXM2Xs844wx2yy23sFAoVNJXGT73uc8xAGxoaGjWdy+++CJ7z3vew9asWcMURWGdnZ3szW9+M3v++efz0q1du7aoHHwh80lkz0UpiezMf5IksY6ODvaGN7yB3XrrrbOkpBkrLpGtqio77bTT2He+8508afpihMNhdvvtt7Nt27axVatWMUmSmMfjYWeffTb7/ve/P+v6qakp9rGPfYz19fUxWZbZ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DFABgxGIiIiIiGhd4SSIiIiIiIjWFU6CKvD5fPj85z8Pn8/X6KoQLYhjlVYTjldaTTheaTXheF26VR2MQEREREREtFQ8E0REREREROsKJ0FERERERLSucBJERERERETrCidBRERERES0rnASNMs3vvENbNq0CYZh4NJLL8Xjjz/e6CoR4Qtf+AIkSSr7d+655xaXZ7NZfOQjH0F7eztCoRB+7dd+DaOjow2sMa0nDz74IN761reir68PkiTh//7f/1u2XAiBz33uc+jt7YXf78dVV12FI0eOlK0zNTWF66+/HpFIBC0tLXjf+96HZDK5gntB68Vi4/Wmm26ac7y99tpry9bheKWVcOutt+IVr3gFwuEwurq68I53vAOHDh0qW6eav/8nT57Em9/8ZgQCAXR1deH3f//3Ydv2Su5KU+IkqMS//uu/4pOf/CQ+//nP46mnnsKFF16IvXv3YmxsrNFVI8KuXbswPDxc/PeLX/yiuOwTn/gEfvjDH+L73/8+HnjgAZw+fRq/+qu/2sDa0nqSSqVw4YUX4hvf+EbF5X/2Z3+Gr33ta/ibv/kbPPbYYwgGg9i7dy+y2Wxxneuvvx779+/Hvffeix/96Ed48MEH8YEPfGCldoHWkcXGKwBce+21Zcfb7373u2XLOV5pJTzwwAP4yEc+gkcffRT33nsvLMvCNddcg1QqVVxnsb//juPgzW9+M0zTxMMPP4x//Md/xO23347Pfe5zjdil5iKo6JWvfKX4yEc+UvzZcRzR19cnbr311gbWikiIz3/+8+LCCy+suGxmZkZomia+//3vF3934MABAUA88sgjK1RDIg8AceeddxZ/dl1X9PT0iP/9v/938XczMzPC5/OJ7373u0IIIV544QUBQDzxxBPFde666y4hSZIYGhpasbrT+jN7vAohxI033ije/va3z/sajldqlLGxMQFAPPDAA0KI6v7+/9d//ZeQZVmMjIwU1/nmN78pIpGIyOVyK7sDTYZngvJM08STTz6Jq666qvg7WZZx1VVX4ZFHHmlgzYg8R44cQV9fH7Zs2YLrr78eJ0+eBAA8+eSTsCyrbOyee+65GBgY4Nilhjt+/DhGRkbKxmc0GsWll15aHJ+PPPIIWlpacMkllxTXueqqqyDLMh577LEVrzPR/fffj66uLuzcuRMf+tCHMDk5WVzG8UqNEovFAABtbW0Aqvv7/8gjj2DPnj3o7u4urrN3717E43Hs379/BWvffDgJypuYmIDjOGWDBAC6u7sxMjLSoFoReS699FLcfvvt+PGPf4xvfvObOH78OK688kokEgmMjIxA13W0tLSUvYZjl5pBYQwudGwdGRlBV1dX2XJVVdHW1sYxTCvu2muvxXe+8x389Kc/xZe//GU88MADeOMb3wjHcQBwvFJjuK6Lj3/847jiiiuwe/duAKjq7//IyEjF429h2XqmNroCRLS4N77xjcX/X3DBBbj00kuxceNG/J//83/g9/sbWDMiorXl3e9+d/H/e/bswQUXXICtW7fi/vvvxxve8IYG1ozWs4985CPYt29f2f3AdHZ4Jiivo6MDiqLMSdQYHR1FT09Pg2pFVFlLSwt27NiBwcFB9PT0wDRNzMzMlK3DsUvNoDAGFzq29vT0zAmgsW0bU1NTHMPUcFu2bEFHRwcGBwcBcLzSyvvoRz+KH/3oR/jZz36Gc845p/j7av7+9/T0VDz+FpatZ5wE5em6josvvhg//elPi79zXRc//elPcdlllzWwZkRzJZNJHD16FL29vbj44ouhaVrZ2D106BBOnjzJsUsNt3nzZvT09JSNz3g8jscee6w4Pi+77DLMzMzgySefLK5z3333wXVdXHrppSteZ6JSL730EiYnJ9Hb2wuA45VWjhACH/3oR3HnnXfivvvuw+bNm8uWV/P3/7LLLsPzzz9fNnG/9957EYlEcP7556/MjjSrRiczNJPvfe97wufzidtvv1288MIL4gMf+IBoaWkpS9QgaoTf+73fE/fff784fvy4eOihh8RVV10lOjo6xNjYmBBCiN/5nd8RAwMD4r777hO//OUvxWWXXSYuu+yyBtea1otEIiGefvpp8fTTTwsA4i//8i/F008/LV588UUhhBBf+tKXREtLi/jP//xP8dxzz4m3v/3tYvPmzSKTyRTLuPbaa8XLX/5y8dhjj4lf/OIXYvv27eK6665r1C7RGrbQeE0kEuJTn/qUeOSRR8Tx48fFT37yE3HRRReJ7du3i2w2WyyD45VWwoc+9CERjUbF/fffL4aHh4v/0ul0cZ3F/v7bti12794trrnmGvHMM8+IH//4x6Kzs1N89rOfbcQuNRVOgmb567/+azEwMCB0XRevfOUrxaOPPtroKhGJ3/iN3xC9vb1C13XR398vfuM3fkMMDg4Wl2cyGfHhD39YtLa2ikAgIN75zneK4eHhBtaY1pOf/exnAsCcfzfeeKMQwovJ/uM//mPR3d0tfD6feMMb3iAOHTpUVsbk5KS47rrrRCgUEpFIRNx8880ikUg0YG9orVtovKbTaXHNNdeIzs5OoWma2Lhxo3j/+98/58tQjldaCZXGKQBx2223Fdep5u//iRMnxBvf+Ebh9/tFR0eH+L3f+z1hWdYK703zkYQQYqXPPhERERERETUK7wkiIiIiIqJ1hZMgIiIiIiJaVzgJIiIiIiKidYWTICIiIiIiWlc4CSIiIiIionWFkyAiIiIiIlpXOAkiIiIiIqJ1hZMgIiIiIiJaVzgJIiKiNee1r30tPv7xjze6GkRE1KQ4CSIiorq46aabIEkSJEmCpmnYvHkz/uAP/gDZbLZm27j//vshSRJmZmbKfv8f//Ef+JM/+ZOabYeIiNYWtdEVICKitevaa6/FbbfdBsuy8OSTT+LGG2+EJEn48pe/XNfttrW11bV8IiJa3XgmiIiI6sbn86GnpwcbNmzAO97xDlx11VW49957AQCbNm3CV77ylbL1X/ayl+ELX/hC8WdJkvDtb38b73znOxEIBLB9+3b84Ac/AACcOHECr3vd6wAAra2tkCQJN910E4C5l8Nt2rQJf/qnf4obbrgBoVAIGzduxA9+8AOMj4/j7W9/O0KhEC644AL88pe/LKvPL37xC1x55ZXw+/3YsGEDPvaxjyGVStW2kYiIaMVxEkRERCti3759ePjhh6Hr+pJed8stt+DXf/3X8dxzz+FNb3oTrr/+ekxNTWHDhg3493//dwDAoUOHMDw8jK9+9avzlvNXf/VXuOKKK/D000/jzW9+M9773vfihhtuwG/+5m/iqaeewtatW3HDDTdACAEAOHr0KK699lr82q/9Gp577jn867/+K37xi1/gox/96PIbgYiImgInQUREVDc/+tGPEAqFYBgG9uzZg7GxMfz+7//+ksq46aabcN1112Hbtm344he/iGQyiccffxyKohQve+vq6kJPTw+i0ei85bzpTW/CBz/4QWzfvh2f+9znEI/H8YpXvALvete7sGPHDnz605/GgQMHMDo6CgC49dZbcf311+PjH/84tm/fjssvvxxf+9rX8J3vfKem9zUREdHK4z1BRERUN6973evwzW9+E6lUCn/1V38FVVXxa7/2a0sq44ILLij+PxgMIhKJYGxsbMl1KS2nu7sbALBnz545vxsbG0NPTw+effZZPPfcc/iXf/mX4jpCCLiui+PHj+O8885bch2IiKg5cBJERER1EwwGsW3bNgDAP/zDP+DCCy/E3//93+N973sfZFkuXnpWYFnWnDI0TSv7WZIkuK675LqUliNJ0ry/K5SdTCbxwQ9+EB/72MfmlDUwMLDk7RMRUfPgJIiIiFaELMv4wz/8Q3zyk5/Ee97zHnR2dmJ4eLi4PB6P4/jx40sqs3B/keM4Na0rAFx00UV44YUXipM4IiJaO3hPEBERrZh3vetdUBQF3/jGN/D6178e//RP/4Sf//zneP7553HjjTdCUZQllbdx40ZIkoQf/ehHGB8fRzKZrFldP/3pT+Phhx/GRz/6UTzzzDM4cuQI/vM//5PBCEREawAnQUREtGJUVcVHP/pR/Nmf/Rk+85nP4DWveQ3e8pa34M1vfjPe8Y53YOvWrUsqr7+/H7fccgs+85nPoLu7u6YTlAsuuAAPPPAADh8+jCuvvBIvf/nL8bnPfQ59fX012wYRETWGJGZfkE1ERERERLSG8UwQERERERGtK5wEERERERHRusJJEBERERERrSucBBERERER0brCSRAREREREa0rnAQREREREdG6wkkQERERERGtK5wEERERERHRusJJEBERERERrSucBBERERER0brCSRAREREREa0r/z8XtiF0zlX4mwAAAABJRU5ErkJggg==\n"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Assuming the dataset has a 'Language' column (adjust column name as needed)\n",
        "language_column = 'Language'\n",
        "\n",
        "# Filter the dataset to include only English-language movies\n",
        "english_movies = movies[movies[language_column].str.contains('English', case=False)]\n",
        "\n",
        "# Display the DataFrame with English-language movies\n",
        "print(\"English-language Movies:\")\n",
        "print(english_movies)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "6IkXBo1MXzqT",
        "outputId": "d3d9cb4a-94af-484a-be41-a2254a58157c"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "English-language Movies:\n",
            "                                           Title                    Genre  \\\n",
            "0                                Enter the Anime              Documentary   \n",
            "3                                 The Open House          Horror thriller   \n",
            "7                The Last Days of American Crime      Heist film/Thriller   \n",
            "8                                        Paradox  Musical/Western/Fantasy   \n",
            "10                          Searching for Sheela              Documentary   \n",
            "..                                           ...                      ...   \n",
            "578   Ben Platt: Live from Radio City Music Hall             Concert Film   \n",
            "579        Taylor Swift: Reputation Stadium Tour             Concert Film   \n",
            "580  Winter on Fire: Ukraine's Fight for Freedom              Documentary   \n",
            "581                      Springsteen on Broadway             One-man show   \n",
            "583     David Attenborough: A Life on Our Planet              Documentary   \n",
            "\n",
            "              Premiere  Runtime  IMDB Score                  Language  \n",
            "0       August 5, 2019       58         2.5          English/Japanese  \n",
            "3     January 19, 2018       94         3.2                   English  \n",
            "7         June 5, 2020      149         3.7                   English  \n",
            "8       March 23, 2018       73         3.9                   English  \n",
            "10      April 22, 2021       58         4.1                   English  \n",
            "..                 ...      ...         ...                       ...  \n",
            "578       May 20, 2020       85         8.4                   English  \n",
            "579  December 31, 2018      125         8.4                   English  \n",
            "580    October 9, 2015       91         8.4  English/Ukranian/Russian  \n",
            "581  December 16, 2018      153         8.5                   English  \n",
            "583    October 4, 2020       83         9.0                   English  \n",
            "\n",
            "[422 rows x 6 columns]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Find the movie with the highest runtime\n",
        "highest_runtime_movie = movies[movies['Runtime'] == movies['Runtime'].max()]\n",
        "\n",
        "# Find the movie with the lowest runtime\n",
        "lowest_runtime_movie = movies[movies['Runtime'] == movies['Runtime'].min()]\n",
        "\n",
        "# Print the movies with the highest and lowest runtimes\n",
        "print(\"Movie with the Highest Runtime:\")\n",
        "print(highest_runtime_movie)\n",
        "\n",
        "print(\"\\nMovie with the Lowest Runtime:\")\n",
        "print(lowest_runtime_movie)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "YGWJfE4laGFM",
        "outputId": "cdf55091-62fb-49f4-a943-3d4522522027"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Movie with the Highest Runtime:\n",
            "            Title        Genre           Premiere  Runtime  IMDB Score  \\\n",
            "561  The Irishman  Crime drama  November 27, 2019      209         7.8   \n",
            "\n",
            "    Language  \n",
            "561  English  \n",
            "\n",
            "Movie with the Lowest Runtime:\n",
            "          Title          Genre       Premiere  Runtime  IMDB Score Language\n",
            "40  Sol Levante  Anime / Short  April 2, 2020        4         4.7  English\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import seaborn as sns\n",
        "# Set the style for Seaborn plots (optional but makes plots more visually appealing)\n",
        "sns.set(style=\"whitegrid\")\n",
        "\n",
        "# Create a histogram of IMDb scores\n",
        "plt.figure(figsize=(10, 6))\n",
        "sns.histplot(movies['IMDB Score'], kde=True, color='skyblue')\n",
        "plt.title('Distribution of IMDb Scores')\n",
        "plt.xlabel('IMDb Score')\n",
        "plt.ylabel('Frequency')\n",
        "plt.show()\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 573
        },
        "id": "YsHCoeGObxjm",
        "outputId": "45658653-6add-42a8-83ea-b97b79b7cd9c"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 1000x600 with 1 Axes>"
            ],
            "image/png": "iVBORw0KGgoAAAANSUhEUgAAA1MAAAIsCAYAAAAXu/M8AAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjcuMSwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy/bCgiHAAAACXBIWXMAAA9hAAAPYQGoP6dpAACP6klEQVR4nOzdeXxcVf3/8dedfbIvTVu6p2lp6V62tgJFS7WUlp26IIg/RUAEBEVAEHHB5Ysbq2grqIgbyKJABWQRtGxC2emepk1buqTJZJLZ79z7+2OS0NAtmUwyM8n7+Xj0kWbmzr2f3JPMvZ8553yOYdu2jYiIiIiIiHSLI9sBiIiIiIiI5CMlUyIiIiIiImlQMiUiIiIiIpIGJVMiIiIiIiJpUDIlIiIiIiKSBiVTIiIiIiIiaVAyJSIiIiIikgYlUyIiIiIiImlQMiUiIiIiIpIGJVMiIll22223MWHChD451rnnnsu5557b8f3LL7/MhAkTePzxx/vk+Ndccw3z5s3rk2OlKxQKcd1113HMMccwYcIEfvCDH2Q7pP2aN28eF154YbbDEBEZsFzZDkBEpD958MEH+eY3v9nxvcfjobS0lAkTJnD88cdzxhlnUFRU1OPj7Nixg/vuu4/58+dz2GGH9Xh/mZTLsXXFr3/9ax566CEuvvhiRo4cSU1NzX63nTdvHuPHj+fXv/51x2PtifFZZ521z0TsF7/4Bb/61a8AePHFF6moqABSieZDDz3UsV1BQQEVFRVMnjyZRYsW8fGPfxyHI7OfgYZCIe666y6efPJJtmzZgtfrZejQoRx11FF86UtfYsiQIRk9nohIf6NkSkSkF1x22WWMGDEC0zRpaGjglVde4Yc//CG/+93v+OUvf8nEiRM7tv3yl7/MBRdc0K3979y5k9tvv53hw4d3K2G56667unWcdBwotu9///vYtt3rMfTESy+9xPTp07nkkkvS3ofX6+XJJ5/khhtuwOPxdHru0Ucfxev1EovF9nqdx+PhxhtvBCAWi7F161aeffZZLrvsMo4++mjuvPPOjCTjAIlEgnPOOYfa2lpOO+00zjnnHMLhMOvWrePRRx/l4x//uJIpEZGDUDIlItIL5s6dy9SpUzu+v/DCC3nxxRe56KKLuPjii1m+fDk+nw8Al8uFy9W7b8eRSAS/37/XjX1fc7vdWT1+V+zevZtx48b1aB/HHXcczzzzDM8//zzz58/veHzlypVs2bKFBQsW8MQTT+z1OpfLxamnntrpsSuuuIKlS5fys5/9jG9961vcfPPNPYqt3VNPPcV7773HT3/6U04++eROz8ViMRKJREaO0xXhcJiCgoI+O56ISKZozpSISB+ZM2cOF198MVu3buUf//hHx+P7mjO1YsUKPvOZz3DkkUcyc+ZMFixYwM9//nMgNc/prLPOAuCb3/wmEyZMYMKECTz44INAal7U4sWLeeedd/jsZz/L9OnTO1774TlT7SzL4uc//znHHHMMM2bM4KKLLuL999/vtM28efO45ppr9nrtnvs8WGz7mjMVDof58Y9/zPHHH8+UKVNYsGABd9111149WBMmTOB73/seTz31FIsXL2bKlCksWrSI559//kCnvcPu3bu59tpr+chHPsLUqVM55ZRTOg2ra58/tmXLFv797393xL5ly5Yu7X9PQ4YM4cgjj+TRRx/t9PgjjzzCoYceyvjx47u1vwsuuIBjjz2Wxx9/nI0bN+71/H//+19OPfVUpk6dykknncSTTz550H3W19cDcPjhh+/1nNfr3asHbMOGDXz1q19l9uzZTJs2jQULFvCLX/yi0zbvvfce559/PocffjgzZ87kvPPO44033ui0zYMPPsiECRN45ZVX+M53vsOcOXM4/vjjO55/7rnnOPvss5kxYwYzZ87kggsuYN26dZ32sWvXLr75zW8yd+5cpkyZwrHHHsuXv/zltNpKRKQnlEyJiPSh9l6H//73v/vdZt26dVx44YXE43Euu+wyrr76aubNm8fKlSsBqKmp4bLLLgPgU5/6FDfddBM33XQTRx11VMc+AoEAX/rSlzjssMO49tprmTVr1gHjuvPOO/n3v//Nl770Jc4991xeeOEFPv/5zxONRrv183Ultj3Zts2Xv/xlfve733HcccfxzW9+k+rqam666SZ+9KMf7bX9a6+9xne+8x1OOukkvvGNbxCLxbjssstoamo6YFzRaJRzzz2Xf/zjH5x88slcddVVFBcXc8011/D73/++I/abbrqJ8vJyDjvssI7Y2+c0ddfJJ5/Ms88+SygUAsA0TR5//PG9eoG66pRTTsG2bV544YVOj9fV1XHFFVcwd+5cvv71r+N0OvnqV7/KihUrDri/YcOGAfDwww8fdOjl6tWr+eQnP8lLL73EJz/5Sa677jrmz5/PM88807HNunXr+OxnP8vq1as5//zzO5Kbc889lzfffHOvfX73u99lw4YNfOUrX+FLX/pSRywXXnghBQUFXHnllVx88cWsX7+es88+u1OidOmll/Kvf/2LM844gxtuuIFzzz2XUCi01wcAIiK9TcP8RET60NChQykuLu7oFdiXFStWkEgkWLZs2T5v5AcNGsTcuXO59dZbmTFjxl7DwiD1yf13v/tdPv3pT3cprubmZpYvX97RGzFp0iQuv/xy7rvvPj73uc918afrWmx7evrpp3nppZe4/PLL+fKXvwzAZz/7WS677DLuuecezjnnHEaNGtWx/YYNG1i+fHnHY7NmzeLUU0/lscce45xzztnvcf7617+yYcMGfvKTn3DKKacA8OlPf5pzzz2Xm2++mTPPPJNBgwZx6qmncssttzBkyJCDxn4wCxYs6OhJO/XUU1mxYgVNTU0sWrSoo6euOw499FAANm/e3Onxuro6brvtNj7xiU8AqcIXJ554Ij/96U855phj9ru/+fPnU11dza233soDDzzArFmzOOKII/jYxz5GZWVlp21vvPFGbNvmoYce6kjCAK688sqO/998880kEgn+/Oc/M3LkSABOO+00TjzxRH7yk59w7733dtpnaWkpv/vd73A6nUCqGMYPfvADlixZwve///2O7U4//XROPPFEfv3rX/P973+fYDDI66+/zlVXXcUXv/jFju1U1VBEskE9UyIifaygoKCjt2JfSkpKgFSiYVlWWsfweDycccYZXd7+tNNO6zSs68QTT6SqqornnnsureN31fPPP4/T6dxr6OEXvvAFbNveawjfRz7ykU7J1cSJEykqKjpgctp+nKqqKhYvXtzxmNvt5txzzyUcDvO///0vAz9NZ6WlpRx33HE89thjQGqI38yZMxk+fHha+2ufU/Th353Bgwfz8Y9/vOP7oqIiTjvtNN577z127dq13/35fD7uv//+joTkwQcf5LrrruPYY4/l+9//PvF4HIDGxkb+97//ceaZZ3ZKpAAMwwAgmUyyYsUK5s+f35FItce2ePFiXnvtNVpbWzu99pOf/GRHIgXwwgsvEAwGWbRoEY2NjR3/HA4H06dP5+WXX+6I2+1288orr9Dc3Ny1kyci0kuUTImI9LFwOExhYeF+nz/ppJM4/PDD+da3vsVHPvIRrrjiCpYvX96txGrIkCHdKjYxevToTt8bhsHo0aPZunVrl/eRjq1btzJ48OC95ue0lyP/8PEPOeSQvfZRWlpKMBg86HFGjx69V2nx9uNs27at27F3xcknn8wLL7zAtm3bePrppzslc90VDocB9vrdGT16dEdS027MmDHA3ufvw4qLi7nqqqt45plneOaZZ/jBD35AdXU19957L3fccQfwwdyq9p6xfWlsbCQSiVBdXb3XczU1NViWtdcQvBEjRnT6vq6uDoDzzjuPOXPmdPr33//+l927dwOpDwquvPJKnn/+eY455hg++9nPsmzZsgMmjiIivUXD/ERE+tD27dtpaWnp1LvyYT6fjz/+8Y+8/PLL/Pvf/+Y///kPy5cv569//St33313p0/zD7SPvpJMJrsUUybs7zi5Wm593rx5uN1urr76auLxOAsXLkx7X2vXrgU44O9OTwwfPpyzzjqLj3/848yfP59HHnmEK664oleOBakiF3tqb8ObbrqJqqqqvbbfs+0///nPM2/ePJ566in++9//csstt7B06VJ+//vfM2nSpF6LWUTkw9QzJSLSh/7+978DcOyxxx5wO4fDwZw5c/jmN7/J8uXLueKKK3jppZc6hjp9uCeipzZt2tTpe9u22bRpU6chafvrAfpwr053Yhs+fDg7d+7cawhYbW1tx/OZMHz4cDZt2rRX7177cT48fC1TfD4f8+fP55VXXuEjH/lI2sUsAP7xj39gGMZe86A2bdq0VzLZ3suTzvkrLS1l5MiRHT097cP22pO5famoqMDv9++z0mBtbS0Oh2OfvYp7aj9OZWUlH/nIR/b69+EiKqNGjeILX/gCd999N48++iiJRIK77767Wz+riEhPKZkSEekjL774Ir/85S8ZMWJERxGEfQkEAns91r74bfs8Fr/fD3DQ4W1d9fDDD3dKaB5//HF27drF3LlzOx4bOXIkb775ZkcMAM8+++xew7e6E9vcuXNJJpP88Y9/7PT47373OwzD6HT8npg7dy67du1i+fLlHY+Zpskf/vAHCgoK9lttMBO++MUvcskll3DxxRenvY+lS5fy3//+l5NOOqljCF+7nTt38q9//avj+9bWVh5++GEOO+ywffbwtFu9ejWNjY17Pb5161Y2bNjQMWSvoqKCo446igceeGCvxLk9iXM6nRxzzDE8/fTTnaruNTQ08Oijj3LEEUccdLHh4447jqKiIn7961/vc42r9lgjkcheCx6PGjWKwsLCTr+bIiJ9QcP8RER6wfPPP09tbS3JZJKGhgZefvllVqxYwbBhw7jzzjv3GuK0pzvuuINXX32V448/nuHDh7N7927+9Kc/MXToUI444gggdfNYUlLCX/7yFwoLCykoKGDatGmdJv93R2lpKWeffTZnnHEGu3fv5ve//z2jR4/mk5/8ZMc2S5Ys4YknnuD8889n4cKFbN68mUceeWSvYWfdiW3evHnMmjWLX/ziF2zdupUJEyawYsUKnn76ac4777yMDWn71Kc+xV//+leuueYa3n33XYYPH84TTzzBypUrufbaaw96o98TEydOZOLEiV3a1jTNjt7LeDzO1q1beeaZZ1izZg2zZs3ie9/73l6vGTNmDNdddx1vv/02lZWVPPDAA+zevXufpeX3tGLFCm677TbmzZvH9OnTKSgoYMuWLTzwwAPE43EuvfTSjm2/9a1v8ZnPfIbTTz+dT33qU4wYMYKtW7fy73//uyPeyy+/nBdeeIGzzz6bs88+G6fTyV//+lfi8Tjf+MY3DvqzFxUV8Z3vfIerrrqKM844g5NOOomKigq2bdvGc889x+GHH863v/1t6urq+PznP8+JJ57IuHHjcDqdPPXUUzQ0NLBo0aIunWcRkUxRMiUi0gtuvfVWIFUxrqysjEMPPZRrr72WM84446A37vPmzWPr1q088MADNDU1UV5eztFHH82ll15KcXFxx35//OMf8/Of/5zvfOc7mKbJj370o7STqYsuuog1a9awdOlSQqEQc+bM4YYbbujoZYJUz8E111zDb3/7W374wx8yZcoUfvWrX/F///d/nfbVndgcDgd33nknt956K8uXL+fBBx9k+PDhXHXVVXzhC19I62fZF5/Pxx/+8Ad++tOf8tBDD9Ha2kp1dTU/+tGPulX1sLfF43GuuuoqINXDV1FRwZQpU/jKV77Cxz/+8b0KaEAqmbr++uu56aab2LhxIyNGjOAXv/gFxx133AGP9YlPfIJQKMSKFSt46aWXaG5upqSkhGnTpvH//t//Y/bs2R3bTpw4kfvuu49bbrmFP//5z8RiMYYNG9ZpDtj48eP54x//yM9+9jN+/etfY9s206ZN4yc/+QnTp0/v0s9/8sknM3jwYJYuXcpdd91FPB7vWAC5vZ2GDh3KokWLePHFF/nHP/6B0+lk7Nix3HzzzSxYsKBLxxERyRTDztVZuyIiIiIiIjlMc6ZERERERETSoGRKREREREQkDUqmRERERERE0qBkSkREREREJA1KpkRERERERNKgZEpERERERCQNWmcKeP3117FtG7fbne1QREREREQkixKJBIZhMHPmzINuq54pwLZttNxW77Ntm3g8rnOdJ9Re+UXtlX/UZvlF7ZV/1Gb5JZfaqzu5gXqmoKNHaurUqVmOpH8Lh8OsWrWKcePGUVBQkO1w5CDUXvlF7ZV/1Gb5Re2Vf9Rm+SWX2uvtt9/u8rbqmRIREREREUmDkikREREREZE0KJkSERERERFJg5IpERERERGRNCiZEhERERERSYOSKRERERERkTQomRIREREREUmDkikREREREZE0KJkSERERERFJg5IpERERERGRNCiZEhERERERSYOSKRERERERkTQomRIREREREUmDkikREREREZE0KJkSERERERFJg5IpERERERGRNCiZEhERERERSYOSKRERERERkTQomRIREREREUmDkikREREREZE0KJkSERHph2zbznYIORGDiEhvcmU7ABEREck8wzBY3RQlbGYnoSlwGUws92Xl2CIifUXJlIiISD8VNm1CppWlo2vwi4j0f3qnExERERERSYOSKRERERERkTQomRIREREREUmDkikREREREZE0KJkSERERERFJg5IpERERERGRNCiZEhERERERSYOSKRERERERkTQomRIREREREUmDkikREREREZE0KJkSERERERFJg5IpERERERGRNORcMvX000+zZMkSZs6cybHHHstXv/pV6uvr99ru/vvvZ8GCBUydOpVTTjmFZ599NgvRioiIiIjIQJVTydTLL7/MJZdcwrhx47jjjju49tprWb16NV/4wheIRqMd2z322GNcf/31LFy4kGXLljFjxgwuueQS3njjjewFLyIiWWfbdrZDyIkYRESkb7iyHcCeHnvsMYYNG8YPf/hDDMMAoKKigvPOO4933nmHI488EoBbb72VRYsWcfnllwMwe/Zs1q5dyx133MGyZcuyFb6IiGSZYRisbooSNrOT0BS4DCaW+7JybBER6Xs5lUyZpklhYWFHIgVQXFwMfPBJX319PXV1dXzjG9/o9NqTTjqJm266iXg8jsfj6bugRUQkp4RNm5BpZeno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AMDMzEynffz48TrHZmZmsLa2hkqleuqYcrkccrkczc3NuHz5MnJzc3HkyBFERUUhLy8PVlZWqK6uxujRo2FpadntOCqVCoaGhrCzs9Npt7a2hoWFRacsIpGo0xhVVVX45ZdfMHny5C6vcffu3ae+HiIi6n8spoiISBBBQUHIzMyEmZkZAgMDdabP9dWvv/4KKysrnSl+/cXExASenp7w9PTEiBEjkJiYiG+//RZz587t0zg9rdH6p6527mtvb4e3tzdWrFjR5TlPpv4REdHA4jQ/IiISRHBwMOrq6vDbb7/9qyl+Fy9eRHV1Nby9vTv1VVVV6Rw3Njairq4Otra2el3L2dkZwOPdBwHAzs4Od+7cwf3797s9x9bWFu3t7Z2y/PHHH2hoaOhVFjs7OzQ1NWHKlCldPmxsbPR6PURE9O+wmCIiIkHY2dlh48aNiImJgYuLi15jqFQqbNiwAUZGRoiIiOjUf/ToUajVau1xZmYmWltbMW3atB7HPXv2bJftT9Y32dvbAwBmzpwJjUaDxMTETs99sgGFj48PACA9PV2n/8CBAzr9PQkMDMTFixdRXFzcqa+hoQGtra1PHYOIiPofp/kREZFgwsLCev3cK1eu4MSJE9BoNGhoaEB5ebl2A4gdO3Z0+YW9arUay5YtQ2BgIG7cuIHDhw/Dw8Ojx538AOCdd96BSCSCn58fxo0bh+bmZpw5cwZff/01pFIp/Pz8AABeXl6YM2cOMjIyUFVVBblcjvb2dvz000+QyWRYsmQJHBwcMHfuXBw9ehQNDQ2YNGkSysvLkZ2djYCAgF6tFYuIiEBRURGioqIwd+5cODk5obm5GdeuXcOpU6dQWFiIkSNH9vq9JCKi/sFiioiIXghKpRJKpRKDBw+Gubk5xo8fj7CwMCgUim6nucXFxSEnJweffPIJ1Go1Zs+ejU2bNj11/VJ8fDwKCwuRl5eHO3fuQKPRYNy4cYiKikJkZCQGD/77z+e2bdsgFovxxRdfYMeOHRg2bBicnZ3h5uamM55IJEJ2djZOnz6NUaNGYdWqVV3uAtgVExMTZGRkICUlBfn5+fjyyy9hbm6OCRMmIDo6GsOGDevVOERE1L8MNE/mIRAREREREVGvcc0UERERERGRHlhMERERERER6YHFFBERERERkR5YTBEREREREemBxRQREREREZEeWEwRERERERHpgcUUERERERGRHlhMERERERER6YHFFBERERERkR5YTBEREREREemBxRQREREREZEeWEwRERERERHpgcUUERERERGRHv4HhB88hhQWwqIAAAAASUVORK5CYII=\n"
          },
          "metadata": {}
        }
      ]
    }
  ]
}