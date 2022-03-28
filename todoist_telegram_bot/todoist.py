from typing import Dict, Optional

from telebot.async_telebot import AsyncTeleBot


def help_command(
    bot: AsyncTeleBot, available_commands: Optional[Dict[str, str]] = None
):
    if not available_commands:
        available_commands = dict()

    async def hello(message) -> None:
        available_commands_str = "\n".join(
            f"/{command} - {description}"
            for command, description in available_commands.items()
        )
        me = await bot.get_me()
        await bot.reply_to(
            message,
            f"""\
Hi there, I am {me.full_name}
Available commands:
{available_commands_str}
""",
        )

    return hello


def create_task(bot: AsyncTeleBot):
    async def create_task_command(message) -> None:
        await bot.send_chat_action(message.chat.id, "typing")
        await bot.send_message(message.chat.id, "Creating task...")
        await bot.send_chat_action(message.chat.id, "typing")
        await bot.send_message(message.chat.id, "Task created!")

    return create_task_command


def list_tasks(bot: AsyncTeleBot):
    async def list_tasks_command(message) -> None:
        await bot.send_chat_action(message.chat.id, "typing")
        await bot.send_message(message.chat.id, "Listing tasks...")
        await bot.send_chat_action(message.chat.id, "typing")
        await bot.send_message(message.chat.id, "Tasks listed!")

    return list_tasks_command


def delete_task(bot: AsyncTeleBot):
    async def delete_task_command(message) -> None:
        await bot.send_chat_action(message.chat.id, "typing")
        await bot.send_message(message.chat.id, "Deleting task...")
        await bot.send_chat_action(message.chat.id, "typing")
        await bot.send_message(message.chat.id, "Task deleted!")

    return delete_task_command


def complete_task(bot: AsyncTeleBot):
    async def complete_task_command(message) -> None:
        await bot.send_chat_action(message.chat.id, "typing")
        await bot.send_message(message.chat.id, "Completing task...")
        await bot.send_chat_action(message.chat.id, "typing")
        await bot.send_message(message.chat.id, "Task completed!")

    return complete_task_command


def rebalance_task(bot: AsyncTeleBot):
    async def rebalance_task_command(message) -> None:
        await bot.send_chat_action(message.chat.id, "typing")
        await bot.send_message(message.chat.id, "Rebalancing task...")
        await bot.send_chat_action(message.chat.id, "typing")
        await bot.send_message(message.chat.id, "Task rebalanced!")

    return rebalance_task_command
