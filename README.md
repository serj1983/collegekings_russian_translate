# collegekings_russian_translate
Полный русский перевод для стим версии игры College Kings
Переведено 14 глав из 14ти.

Установка v13.1.*:
1. Разместить папку tl с содержимым в папку "College Kings/game/"
2. В настройках игры, снизу, появится возможность выбрать русский язык

Установка v13.2.*:

1. Разместить папку tl с содержимым в папку "College Kings/game/"
2. Начать новую игру, нажать Shift+O, попадаем в консоль, печатаем renpy.change_language('russian')

Внимание, у кого установлены другие русификаторы восстановите исходные файлы игры! Это можно сделать через Свойства игры - Локальные файлы - Проверить целостность игровых файлов.

FAQ:

? Зашёл по ссылке, всё на английском. Как скачать перевод?
> Ищи зелёную кнопку "Code", нажимай на неё и выпадающем списке, жми "Download ZIP"

? У меня перевелись диалоги, имена. Меню и ответы в диалогах на английском. Почему?
> Это проблема игры и разработчики обещали исправить в следующих обновлениях.

? Почему перевелись только имена? Диалоги так и остались на английском.
> Проверьте правильность ввода команды в консоле. Оно должно быть целиком на английском. Правильно -> renpy.change_language("russian"). НЕПРАВИЛЬНО -> renpy.change_language(‘Русский’)

? Как убрать зеленые надписи в левом, верхнем углу экрана?
> Надписи появляются после ввода команды в консоле перевода игры. Нажмите SHIFT+R, это перезагрузит игру и надписи уйдут.

? При запуске игры возникла ошибка, что-то типо:
I'm sorry, but an uncaught exception occurred.
While running game code:
File "game/v10/Scene30a.rpy", line 528, in script
old "Watch"
File "game/v10/Scene30a.rpy", line 528, in script
old "Watch"
Exception: A translation for "Watch" already exists at game/tl/russian/v10/Scene30a.rpy:529.
> Проверь правильность хождения папки "tl" в папке game игры. Проверь, не скопировал случайно помимо папки tl, ещё такие же папки как "tl (копия)" или "collegekings_russian_translate-master", что может создать конфликт с переводом. Если да, копии папок удалить. В противном случае, удалить в папке game игры все папки v1 до v13 и запустить в Стиме проверку целостности игры.
