# Обязательная метадата плагина
__id__ = "ai_assistant"
__name__ = "ии ассистент"
__version__ = "1.0"
__author__ = "myatnik"
__description__ = "Личный ИИ-ассистент, наводящий суету прямо из Экстеры"

from base_plugin import BasePlugin

class AiAssistantPlugin(BasePlugin):
    # Этот метод срабатывает, когда плагин загружается
    def on_plugin_load(self):
        self.add_on_send_message_hook()
        self.logger.info("ИИ-ассистент от myatnik успешно заряжен!")

    # Магия перехвата
    def on_send_message_hook(self, params):
        # Команда .суета
        if params.message and params.message.startswith(".суета"):
            params.message = "🌪 **Суета активирована!** myatnik на связи, всем приготовиться!"
            
        # Команда .статус
        elif params.message and params.message.startswith(".статус"):
            params.message = "⚡️ **ИИ-ассистент:** Всё ровно. Пишу код, пью энергос."