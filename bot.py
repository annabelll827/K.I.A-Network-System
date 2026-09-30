from telethon import TelegramClient, events

# زانیارییە سەرەتاییەکانی تلیگرام
API_ID = 38144988
API_HASH = "3b226e6b70076a7557dab51b4d20f546"
BOT_TOKEN = "8889066225:AAHPiHdo7FMdHe_SCU_0r-ba9jztVYpZWxBo"

# دروستکردنی کڵایتی تلیگرام بۆ بۆتەکە
client = TelegramClient("telegram_bot_session", API_ID, API_HASH)


@client.on(events.NewMessage(pattern="/start"))
async def start_handler(event):
  await event.respond("✅ سڵاو! بۆتەکە بە سەرکەوتوویی کار دەکات و ئامادەیە.")


@client.on(events.NewMessage(pattern="/ask"))
async def ask_handler(event):
  # لێرەدا دەتوانیت هەر کاردانەوەیەک یان ناردنێک بۆ بۆتێکی تر (وەک falcondbBOT@) زیاد بکەیت
  text = event.raw_text.replace("/ask", "").strip()
  if text:
    await event.respond(f"📩 پەیامەکەت وەرگیرا: {text}")
  else:
    await event.respond("⚠️ تکایە پەیامێک یان پرسارێک دوای `/ask` بنووسە.")


def main():
  print("🤖 بۆتی تلیگرام دەستی بە کارکردن کرد...")
  client.start(bot_token=BOT_TOKEN)
  client.run_until_disconnected()


if __name__ == "__main__":
  main()
