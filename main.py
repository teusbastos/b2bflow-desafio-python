from supabase import create_client
from config import SUPABASE_KEY, SUPABASE_URL, ZAPI_INSTANCE_ID, ZAPI_INSTANCE_TOKEN
import logging
import requests


logger = logging.getLogger()

def get_contacts():
    supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

    response = (supabase.table("Contacts").select("id", "name", "phone_num").execute())
    print(response)
    
    return response.data or []

def send_message(phone_num, message):

    url = (f"https://api.z-api.io/instances/{ZAPI_INSTANCE_ID}/token/{ZAPI_INSTANCE_TOKEN}/send-text")

    headers = {
        "Content-Type": "application/json"
    }

    payload = {
        "phone": phone_num,
        "message": message
    }

    try:
        response = requests.post(url, json=payload, headers=headers, timeout=10)
        print(response.status_code)
        logger.info(f"Mensagem enviada para: {phone_num}")
    
    except Exception as e:
        logger.error(f"Erro ao enviar a mensagem para {phone_num}: {e}")

if __name__ == "__main__":
    contacts = get_contacts()

    if not contacts:
        logging.warning("Nenhum contato encontrado na tabela")
        exit

    for contact in contacts:
        name = contact.get("name")
        phone = contact.get("phone_num")

        if not name or not phone:
            logging.warning("Pulando contato inválido")
            continue

        message = f"Olá {name}, tudo bem com você?"
        send_message(phone, message)

    
