Overview:

This project aims to automatically generate concise and informative discharge summaries from various documents of patients. It utilizes state-of-the art model to extract relevant information and generate summaries that capture the key details of a patient's hospital stay.

Access to MIMIC-III Dataset: 

MIMIC-III is a collection of comma separated value (CSV) files which contains detailed information regarding the clinical care of nearly 40,000 patients.

There are two key steps that must be completed before access is granted:

**the researcher must complete a recognized course in protecting human research participants that includes Health Insurance Portability and Accountability Act (HIPAA) requirements.

**the researcher must sign a data use agreement, which outlines appropriate data usage and security standards, and forbids efforts to identify individual patients.

Approval requires at least a week. Once an application has been approved the researcher will receive emails containing instructions for downloading the database from PhysioNetWorks, a restricted access component of PhysioNet. After which the data can be accessed with utmost care.

Data Extraction:

This process draws out the features which are considered to be playing the vital role in the process of generating summaries. The features are combined together to train the transformer models.

Data Split:

The process of splitting dataset into train data, validation data and test data which are used to train the model, validate the model and test the model.

Model Training:

The transformer models such as BioBert, T5, BART are trained using the train data.

Evaluation:

The ROUGE and F1 scores are used as the evaluation metric which depicts the relevancy of the generated summary.

BART model exhibits highest ROUGE score which indicates more relevancy of the generated summary in accordance with the data. 

