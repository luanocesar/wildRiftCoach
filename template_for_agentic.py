from langchain.prompts import PromptTemplate

# 1. Defina o comportamento "Curto e Grosso"
custom_template = """Você é um assistente técnico objetivo. 
Use os seguintes pedaços de contexto para responder à pergunta.
Se não souber a resposta, apenas diga que não sabe, não tente inventar.
Responda de forma extremamente curta, direta e sem introduções (não diga 'baseado no texto').

Contexto: {context}
Pergunta: {question}

Resposta Direta:"""

CUSTOM_PROMPT = PromptTemplate(
    template=custom_template, 
    input_variables=["context", "question"]
)

# 2. Ao criar a Chain, passe o seu prompt
qa_chain = ConversationalRetrievalChain.from_llm(
    llm=llm,
    retriever=setup_rag(),
    memory=memory,
    combine_docs_chain_kwargs={'prompt': CUSTOM_PROMPT} # O segredo está aqui
)