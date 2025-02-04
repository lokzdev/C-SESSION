from telethon import TelegramClient
import os

api_id = 28144670
api_hash = "c8d54d2e152faa5e143393fca4ca3c93"

quantidade = int(input("Quantas sessões deseja criar: "))

# Diretório para armazenar as sessões
session_dir = "SESSÕES"
os.makedirs(session_dir, exist_ok=True)

for i in range(1, quantidade + 1):
    session_name = f"{session_dir}/session_{i}"
    print(f"\n🔹 Criando sessão {i}...")

    client = TelegramClient(session_name, api_id, api_hash)

    async def main():
        await client.start()
        print(f"✅ Sessão {i} criada com sucesso para o número: {await client.get_me()}")

    with client:
        client.loop.run_until_complete(main())

print("\n🎉 Todas as sessões foram criadas com sucesso!")
