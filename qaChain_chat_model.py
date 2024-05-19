from langchain.chat_models import ChatOpenAI

DEPLOYMENT_NAME = "<deployment_name>"
# llm = AzureChatOpenAI(
#     openai_api_base=BASE_URL,
#     openai_api_version="2023-03-15-preview",
#     deployment_name=DEPLOYMENT_NAME,
#     openai_api_key=API_KEY,
#     openai_api_type="azure",
#     streaming=True,
#     verbose=True,
#     temperature=0,
#     max_tokens=1500,
#     top_p=0.95
# )

model = ChatOpenAI(model_name='gpt-4', temperature=0.0)

qa = ConversationalRetrievalChain.from_llm(
    llm=llm,
    retriever=compression_retriever,
    memory=memory,
    verbose=True,
    chain_type="stuff",
    return_source_documents=True
)
