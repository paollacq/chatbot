from fastapi import APIRouter
from pydantic import BaseModel
import chromadb
from chromadb.utils import embedding_functions

# Configuração do router
chatbot_router = APIRouter()

# Configuração do ChromaDB
DB_PATH = "./chroma.sqlite3"
COLLECTION_NAME = "blockchain_courses"
client = chromadb.PersistentClient(path=DB_PATH)
embedding_function = embedding_functions.SentenceTransformerEmbeddingFunction(model_name="thenlper/gte-large")
collection = client.get_or_create_collection(COLLECTION_NAME, embedding_function=embedding_function)

# Modelo para entrada de dados
class ChatbotRequest(BaseModel):
    user_query: str

# Endpoint do chatbot
@chatbot_router.post("/")
def chatbot_interaction(request: ChatbotRequest):
    user_query = request.user_query
    results = collection.query(query_texts=[user_query], n_results=1)
    print("Resultados da Query:", results)  # Log dos resultados
    
    if results["documents"] and results["metadatas"]:
        # Obtenha o primeiro metadado corretamente como dicionário
        course_metadata = results["metadatas"][0] if results["metadatas"][0] else {}
        response = {
            "course_name": course_metadata.get("course_name", "N/A"),
            "description": results["documents"][0],  # Primeiro documento relevante
            "price": f"${course_metadata.get('price', 'N/A')}",
            "discounted_price": f"${course_metadata.get('discounted_price', 'N/A')} (for XRP payments)",
            "duration": course_metadata.get("duration", "N/A")
        }
        return {"response": response}
    
    # Retornar resposta padrão caso não haja resultados
    return {"response": "No relevant courses found."}
