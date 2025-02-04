from telethon import TelegramClient
import os

api_id = 28144670
api_hash = "c8d54d2e152faa5e143393fca4ca3c93"

quantidade = int(input("Quantas sessões deseja criar: "))

# Diretório para armazenar as sessões
session_dir = "SESSÕES"
os.makedirs(session_dir, exist_ok=True)

for i in range(1, quantidade + 1):
    phone = input(f"\n📱 Insira o nome da session {i}: ").strip()
    session_name = os.path.join(session_dir, phone)  # Nome da sessão = Número de telefone

    print(f"\n🔹 Criando sessão para {phone}...")

    client = TelegramClient(session_name, api_id, api_hash)

    async def main():
        await client.start(phone)
        me = await client.get_me()
        print(f"✅ Sessão criada com sucesso para: {me.phone}")

    with client:
        client.loop.run_until_complete(main())

print("\n🎉 Todas as sessões foram criadas com sucesso!")
