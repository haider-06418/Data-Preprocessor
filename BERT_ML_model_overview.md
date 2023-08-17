# **Building Name Extraction from Addresses Using Machine Learning Model BERT**

## High level overview of the process. Find the complete implementation [here](https://github.com/haider-06418/Data-Preprocessor/blob/main/BERT_ML_model.ipynb)!.

## **Introduction:**
Given a large dataset of raw, non-standardized addresses, the objective is to accurately extract building names. The challenges include incorrect or missing delimiters, such as commas, and varied spellings of the same building name.

## **Step 1. Setup**
To set up the required environment:

- Install necessary Python libraries:
  ```bash
  pip install transformers torch scikit-learn
  ```

## **Step 2. Data Preparation**
The dataset consists of raw addresses and corresponding building names.

- Define a sample dataset of addresses and their respective building names.
- Split the data into training, validation, and test sets.

## **Step 3. Model Initialization**
Initialize the BERT model and tokenizer, optimized for span prediction tasks:

```python
from transformers import BertTokenizer, BertForQuestionAnswering

tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertForQuestionAnswering.from_pretrained('bert-base-uncased')
```

## **Step 4. Data Preprocessing**
Prior to training, data needs to be tokenized and structured for BERT.

- **Clean the addresses**: Remove unwanted characters, standardize to lowercase, etc.
- **Tokenize for BERT**: Convert address strings to token IDs, suitable for BERT.
- **Generate span labels**: Identify the start and end token positions of the building name within the tokenized address.

## **Step 5. Model Training**
Train the BERT model on the prepared data:

- Set up a DataLoader to feed batches of data into the model.
- Define the AdamW optimizer and a learning rate scheduler.
- Implement a training loop to fine-tune the model for the specific task.

## **Step 6. Model Evaluation**
Evaluate the model's performance on the validation set:

- Set up a DataLoader for validation data.
- Implement an evaluation loop to compute validation loss and metrics such as Exact Match (EM).

## **Step 7. Deployment & Usage**
Finally, deploy the trained model for real-world use:

- **Save the trained model**: Store the model weights for future use.
- **Extraction function**: Implement `extract_building_names` to take a list of addresses and return the extracted building names.
- **Load the model & tokenizer**: For subsequent runs, load the saved model and tokenizer.
  
For large-scale applications, consider hosting the model on cloud platforms, containerizing it, or creating an API service.

---

# **Conclusion**:
This report details an end-to-end process for building name extraction from raw addresses using the BERT model. With accurate training and optimization, the system offers a robust solution to extract building names, significantly aiding data standardization and analysis tasks.