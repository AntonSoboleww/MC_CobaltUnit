# МультиЧат CobaltUnit

CobaltUnit - удобное средство для общения с людьми из всех Ваших мессенджеров и соц. сетей.

Инструкция по запуску синхов:
--
Телеграмм:
1) Открыть чат с @BotFather в телеграмм. Следуя инструкциям создать бота
2) После создания бота нужно получить его токен.
Вводим комманду /mybots
Выбираем нужного бота из списка
Кликаем на "API Token"
Копируем токен. (Строка формата 1234567:ABCDEFGHJKLMNOPQRSTUVWXYZ)
3) Затем в настройках(я их ещё не реализовал 🥲) вставляем токен в соответствующее поле
TODO: когда будут готовы настройки, прописать более подробно куда и что вводить.
4) Готово. Теперь наш сервер принимает сообщения отправленные Вашему боту и показывает их оператору

Реализованные синхи:
--

В разработке:
--
- Телеграмм

В планах:
--
- ВК


TODO:
--
- Подгрузка чата снизу вверх. При достижении верха подгрузка ещё пяти сообщений.
- Отправка сообщений без редиректа (скорее всего придётся подключать JSON или AJAX)
- Подключить VK api, создать поле в моделе, показывающее откуда пишут.
- Подключиться к Webhook'у Вк
- Когда доделаю Телегу, покрыть тестами каждый миллиметр
- Сделать интерфейс
-   - Настройки
-   - Диалоги
-   - Вывод всех операторов проекта
