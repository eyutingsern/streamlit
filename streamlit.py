import streamlit as st
import pandas as pd


embedding_models = [
    "dunzhang/stella_en_400M_v5", 
    "intfloat/e5-large-v2",
    "jinaai/jina-embeddings-v3",
    "mixedbread-ai/mxbai-embed-large-v1",
    "Alibaba-NLP/gte-large-en-v1.5",
    "nomic-ai/nomic-embed-text-v1.5"
]

queries = [   
    "What is Joget?",
    "What are the most frequent issues when scaling Joget applications?",
    "How to use User Role selector Plugin",
    "How do you fix Java security error in the Workflow designer?",
    "If I want to install Version 4 (Enterprise Edition) in AWS, where can I get installation guide?"
]

results_data = {
    "Query": [],
    "Model": [],
    "Top document retrieved": [],
    "Retrieval time (s)": [],
    "Embedding time (s)": [],
    "Total latency (s)": []
}

# Curretly hardcoding from csv
results = {
    "What is Joget?": {
        "dunzhang/stella_en_400M_v5": {"retrieval_time": 0, "embedding_time": 1.05, "latency": 1.06, "top_doc": "Joget is an open-source no-code/low-code application platform combining the best of business process automation, workflow management, and rapid application development."},
        "intfloat/e5-large-v2": { "retrieval_time": 0, "embedding_time": 0.3, "latency": 0.3, "top_doc": "Joget is an open-source web-based workflow platform that develops enterprise process management applications and workflows. While it offers flexibility and customization, access to certain advanced features, specialized technical support, and a Joget license are necessary. "},
        "jinaai/jina-embeddings-v3": { "retrieval_time": "", "embedding_time": "", "latency": "", "top_doc": ""},
        "mixedbread-ai/mxbai-embed-large-v1": {"retrieval_time": 0.01, "embedding_time": 0.44, "latency": 0.45, "top_doc": "Navigating the complexities of modern business operations can be challenging. That\'s where Joget comes in. "},
        "Alibaba-NLP/gte-large-en-v1.5": {"retrieval_time": "", "embedding_time": "", "latency": "", "top_doc": ""},
        "nomic-ai/nomic-embed-text-v1.5": {"retrieval_time": "", "embedding_time": "", "latency": "", "top_doc": ""}
    },
    "What are the most frequent issues when scaling Joget applications?": {
        "dunzhang/stella_en_400M_v5": {"retrieval_time": 0, "embedding_time": 1.05, "latency": 1.05, "top_doc": "This section delves into the mechanisms and strategies to enhance the scalability and availability of your Joget systems, providing a foundation for continuous operation and efficient response to varying workloads."},
        "intfloat/e5-large-v2": {"retrieval_time": 0, "embedding_time": 0.3, "latency": 0.3, "top_doc": "General\xa0\nWhy choose Joget?\xa0How does Joget compare to traditional languages and frameworks like JS, CSS, React or Ruby on Rails?\xa0What’s different about working with Joget vs. traditional programming?"},
        "jinaai/jina-embeddings-v3": { "retrieval_time": "", "embedding_time": "", "latency": "", "top_doc": ""},
        "mixedbread-ai/mxbai-embed-large-v1": {"retrieval_time": 0.12, "embedding_time": 1.15, "latency": 1.27, "top_doc": "The Joget Platform and Apps FAQ section covers various topics related to the requirements, functionalities, workflows, and non-functional aspects of Joget."},
        "Alibaba-NLP/gte-large-en-v1.5": {"retrieval_time": "", "embedding_time": "", "latency": "", "top_doc": ""},
        "nomic-ai/nomic-embed-text-v1.5": {"retrieval_time": "", "embedding_time": "", "latency": "", "top_doc": ""}
    },
    "How to use User Role selector Plugin": {
        "dunzhang/stella_en_400M_v5": {"retrieval_time": 0, "embedding_time": 1.05, "latency": 1.05, "top_doc": "The Users menu allows to manage the users of the platform and set one or more Organizations which contain:\n\nDepartments\nGrades\nReporting structure\n\nGroups are also available as informal groupings or categories of users."},
        "intfloat/e5-large-v2": {"retrieval_time": 0, "embedding_time": 0.3, "latency": 0.3, "top_doc": "Permission Control in Joget allows you to manage user access to various components within your Joget App. Here\'s an overview of the main components and permission plugins available:"},
        "jinaai/jina-embeddings-v3": { "retrieval_time": "", "embedding_time": "", "latency": "", "top_doc": ""},
        "mixedbread-ai/mxbai-embed-large-v1": {"retrieval_time": 0.01, "embedding_time": 0.44, "latency": 0.45, "top_doc": "Troubleshooting common errors in Joget Workflow is crucial for maintaining a seamless application experience. "},
        "Alibaba-NLP/gte-large-en-v1.5": {"retrieval_time": "", "embedding_time": "", "latency": "", "top_doc": ""},
        "nomic-ai/nomic-embed-text-v1.5": {"retrieval_time": "", "embedding_time": "", "latency": "", "top_doc": ""}
    },
        "How do you fix Java security error in the Workflow designer?": {
        "dunzhang/stella_en_400M_v5": {"retrieval_time": 0, "embedding_time": 1.05, "latency": 1.05, "top_doc": "Troubleshooting common errors in Joget Workflow is crucial for maintaining a seamless application experience. Whether you\'re encountering issues with database connections, configuration files, or server settings, understanding these common errors and their solutions can help you resolve them quickly and efficiently."},
        "intfloat/e5-large-v2": {"retrieval_time": 0, "embedding_time": 0.3, "latency": 0.3, "top_doc": "The Database SQL Query (formerly JDBC Form Binder) allows you to use custom SQL statements to retrieve and load records into your form fields. Similarly, you can write SQL statements to save the records in your form fields into a database table."},
        "jinaai/jina-embeddings-v3": { "retrieval_time": "", "embedding_time": "", "latency": "", "top_doc": ""},
        "mixedbread-ai/mxbai-embed-large-v1": {"retrieval_time": 0.12, "embedding_time": 1.15, "latency": 1.27, "top_doc": "Troubleshooting common errors in Joget Workflow is crucial for maintaining a seamless application experience. "},
        "Alibaba-NLP/gte-large-en-v1.5": {"retrieval_time": "", "embedding_time": "", "latency": "", "top_doc": ""},
        "nomic-ai/nomic-embed-text-v1.5": {"retrieval_time": "", "embedding_time": "", "latency": "", "top_doc": "Scaling challenges and fixes."}
    },
        "If I want to install Version 4 (Enterprise Edition) in AWS, where can I get installation guide?": {
        "dunzhang/stella_en_400M_v5": {"retrieval_time": 0, "embedding_time": 1.05, "latency": 1.05, "top_doc": "Joget can be launched from the AWS marketplace if you have an Amazon AWS account. All the available images come with Joget DX 8 Enterprise Edition and 10-user licenses, and if you wish to increase your user license, you may purchase it from\xa0AWS Marketplace."},
        "intfloat/e5-large-v2": {"retrieval_time": 0, "embedding_time": 0.3, "latency": 0.3, "top_doc": "The Advanced Installation Guides offer comprehensive, step-by-step instructions tailored to diverse platforms and environments, ensuring you can confidently deploy Joget on-premise or in the cloud. "},
        "jinaai/jina-embeddings-v3": { "retrieval_time": "", "embedding_time": "", "latency": "", "top_doc": ""},
        "mixedbread-ai/mxbai-embed-large-v1": {"retrieval_time": 0.12, "embedding_time": 1.15, "latency": 1.27, "top_doc": "How-to articles tell users how to complete a task. These articles are the workhorses of the knowledge base; they enable self-service for new and experienced users."},
        "Alibaba-NLP/gte-large-en-v1.5": {"retrieval_time": "", "embedding_time": "", "latency": "", "top_doc": ""},
        "nomic-ai/nomic-embed-text-v1.5": {"retrieval_time": "", "embedding_time": "", "latency": "", "top_doc": ""}
    }
}

# creating results data 
for query in queries:
    if query in results:
        for model, metrics in results[query].items():
            results_data["Query"].append(query)
            results_data["Model"].append(model)
            results_data["Top document retrieved"].append(metrics["top_doc"])
            results_data["Retrieval time (s)"].append(metrics["retrieval_time"])
            results_data["Embedding time (s)"].append(metrics["embedding_time"])
            results_data["Total latency (s)"].append(metrics["latency"])

# convert to df 
results_df = pd.DataFrame(results_data)

# 
st.title("Embedding Model Comparison")

st.sidebar.title("Query Selection")
user_query = st.sidebar.selectbox("Select a query:", queries)

# condition to show results 
if user_query:
    st.write(f"### Results for Query: `{user_query}`")
    
    # Filter the DataFrame for the selected query
    filtered_results = results_df[results_df["Query"] == user_query]
    
    # Display results in a table
    st.table(filtered_results[["Model", "Top document retrieved", "Retrieval time (s)", "Embedding time (s)", "Total latency (s)"]])

# actual answers section 
st.write("### Accurate answer")
st.write("Actual answer to compare for accuracy with produced results")

generated_questions = [""]
st.table(pd.DataFrame({"Actual answers": generated_questions}))
