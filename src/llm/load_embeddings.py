import sys
import os
import json
import pickle
from sentence_transformers import SentenceTransformer
from langchain.chat_models import ChatOpenAI
from langchain.chains.question_answering import load_qa_chain
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain.embeddings import HuggingFaceEmbeddings

prompt_template = """
Eres un asistente experto. Responde la pregunta usando la información unicamente de los documentos proporcionados.
Debes dar una respuesta **detallada y completa**, explicando todos los puntos relevantes en español.

=== CONTEXTO DE DOCUMENTOS ===
{context}

=== PREGUNTA ===
{question}

=== RESPUESTA ===
"""

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


def save_conversation(response, user_id):
    filename = f"data/outputs/conv_{user_id}.json"
    if os.path.exists(filename):
        with open(filename, "r") as f:
            conversation = json.load(f)
    else:
        conversation = []

    conversation.append(
        {"text": response, "type": "text", "status": "viewed", "isSender": False}
    )

    with open(filename, "w") as f:
        json.dump(conversation, f, ensure_ascii=False, indent=4)


def load_conversation(user_id):
    filename = f"data/outputs/conv_{user_id}.json"
    if os.path.exists(filename):
        with open(filename, "r") as f:
            conversation = json.load(f)
            return conversation
    else:
        return []


def load(user_question, user_id):
    embedding_file = "./data/embeddings/embedding_base.pkl"
    if not os.path.exists(embedding_file):
        result = {
            "success": False,
            "status_code": 404,
            "message": "Base de conocimientos vacia.",
            "error": "Embedding file not found.",
        }
        return result

    with open(embedding_file, "rb") as f:
        knowledge_base = pickle.load(f)

    embedding_model = HuggingFaceEmbeddings(
        model_name="sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
    )
    knowledge_base.embedding_function = embedding_model

    # Mensaje de embeddings cargados
    result = {
        "success": True,
        "status_code": 200,
        "message": "Información obtenida de la base de conocimientos.",
        "response": "",
    }

    if knowledge_base:
        os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY
        try:
            docs = knowledge_base.similarity_search(user_question, 3)
            if not docs:
                result = {
                    "success": False,
                    "status_code": 404,
                    "message": "Sin documentos en la base de conocimientos.",
                    "error": "No documents found for the given query.",
                }
                return result

            prompt = PromptTemplate(
                template=prompt_template, input_variables=["context", "question"]
            )

            llm = ChatOpenAI(
                model_name="gpt-3.5-turbo", temperature=0.2, max_tokens=1500
            )
            chain = load_qa_chain(llm, chain_type="stuff", prompt=prompt)

            response = chain.run(input_documents=docs, question=user_question)

            result["response"] = response  # Agregar la respuesta al resultado
            save_conversation(response, user_id)
        except Exception as e:
            result = {
                "success": False,
                "status_code": 500,
                "message": "Ocurrio un problema al solicitar la respuesta.",
                "error": e,
            }
    else:
        result = {
            "success": False,
            "status_code": 404,
            "message": "Sin base de conocimientos actual.",
            "error": "Knowledge_base is null.",
        }

    return result
