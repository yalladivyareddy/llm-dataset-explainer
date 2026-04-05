# LLM Dataset Explainer

This project is an interactive tool for quickly understanding a dataset through a combination of traditional exploratory data analysis (EDA) and large language model (LLM)-generated insights.

Instead of manually inspecting columns, plotting distributions, and forming hypotheses, the goal here is to automate that first layer of analysis and make it conversational.

## Overview

The application allows users to upload a CSV file and immediately get:

* Basic dataset structure (rows, columns, missing values)
* Correlation analysis and visual summaries
* Automatically generated insights about patterns in the data
* The ability to ask natural language questions about the dataset

This is meant to simulate how an analyst would approach a new dataset, but in a faster and more interactive way.

## Approach

The workflow combines two components:

**1. Statistical EDA**

* Summary statistics using pandas
* Missing value detection
* Correlation matrix for numerical features
* Distribution visualization for selected variables

**2. LLM-based reasoning**

* A sample of the dataset is passed to the model
* The model is prompted to:

  * describe the dataset
  * identify key patterns
  * suggest potential use cases
* Users can ask follow-up questions in natural language

This hybrid approach ensures that insights are grounded in actual data while still benefiting from LLM interpretation.

## Key Features

* Upload and explore any tabular dataset
* Automatic EDA without manual coding
* AI-generated insights that summarize patterns
* Natural language interface for querying data

## Tech Stack

* Python
* Streamlit
* Pandas
* Plotly
* OpenAI API
## How to Run

Clone the repository:

```bash
git clone https://github.com/yalladivyareddy/llm-dataset-explainer.git
cd llm-dataset-explainer
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file in the root directory:

```bash
OPENAI_API_KEY=your_api_key_here
```

Run the app:

```bash
streamlit run src/app.py
```

## Limitations

* Insights are based on a sample of the dataset, not the full data
* LLM responses may not always reflect statistically rigorous conclusions
* No model training or predictive analysis is included

## Future Work

* Add feature importance and model-based insights
* Improve ranking of insights based on statistical significance
* Support larger datasets more efficiently
* Enhance UI for better usability

## Author

Divya
