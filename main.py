import asyncio
import logging

from telebot.async_telebot import AsyncTeleBot

from settings import config
from todoist_telegram_bot.todoist import (
    complete_task,
    create_task,
    delete_task,
    help_command,
    list_tasks,
    rebalance_task,
)

logging.basicConfig(level=logging.INFO)


async def main():
    available_commands = {
        "help": "Show this message",
        "start": "Show this message",
        "new_task": "Create new task",
        "list_tasks": "List all tasks",
        "delete_task": "Delete task",
        "complete_task": "Complete task",
        "rebalance_task": "Rebalance task",
    }

    bot = AsyncTeleBot(config.TELEGRAM_BOT_TOKEN)
    bot.message_handler(commands=["help", "start"])(
        help_command(bot, available_commands)
    )
    bot.message_handler(commands=["new_task"])(create_task(bot))
    bot.message_handler(commands=["list_tasks"])(list_tasks(bot))
    bot.message_handler(commands=["delete_task"])(delete_task(bot))
    bot.message_handler(commands=["complete_task"])(complete_task(bot))
    bot.message_handler(commands=["rebalance_task"])(rebalance_task(bot))

    await bot.infinity_polling()


if __name__ == "__main__":
    asyncio.run(main())
