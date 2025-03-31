import csv
import os

from bottools.helpers.utils import get_env


def add_client(name, phone, country, username, telegram_id):  # Add a new client to the database
    file_exists = os.path.isfile("clients.csv")

    with open("clients.csv", mode="a", newline="") as file:
        writer = csv.writer(file)

        if not file_exists:
            writer.writerow(["Name", "Phone", "Country", "Username", "Telegram ID"])

        writer.writerow([name, phone, country, username, telegram_id])


def get_clients():  # Get all clients from the database
    file_exists = os.path.isfile("clients.csv")
    if not file_exists:
        return []

    with open("clients.csv", mode="r") as file:
        reader = csv.reader(file)
        return list(reader)


def is_client_exists(phone):  # Check if the client already exists in the database
    clients = get_clients()
    for client in clients:
        if client[1] == phone:
            return True
    return False


def send_channel(context, fullname, phone_number, country, username):  # Send a message to the channel
    channel_username = get_env("CHANNEL_USERNAME")
    message = (
        f"📢 *Новый клиент!*\n"
        f"👤 Имя: *{fullname}*\n"
        f"📞 Телефон: `{phone_number}`\n"
        f"🌍 Желаемая страна: {country}\n"
        f"💬 Телеграм: @{username}"

    )
    context.bot.send_message(chat_id=channel_username, text=message, parse_mode="Markdown")
