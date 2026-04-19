# Final Acceptance Check

Дата проверки: 2026-04-19

## Итог

Сборка выглядит пригодной для playable demo. Фоны, спрайты и музыка подключены через Ren'Py-логику и проходят автоматические проверки. Desktop shortcut тоже создан, но расположен не внутри workspace, а напрямую на рабочем столе Windows.

## Проверка по пунктам

### 1. Фоновые сцены

PASS: все 10 сцен из `SCENE_LIBRARY` закрыты реальными файлами в `prototype/gorny_prototype/game/assets/backgrounds`.
Часть сцен переиспользует один и тот же тревожный фон, поэтому обязательный комплект меньше числа самих сцен.

### 2. Персонажи и позы

PASS: персонажи в разных позах подключены в коде через `prototype_character(...)` и используются в `script.rpy`.
Покрытие по текущему набору:
- Диана: 3 позы
- Дима: 3 позы
- Миша: 3 позы
- Вика: 3 позы
- Марина: 2 позы

### 3. Музыка и атрибуция

PASS: подключено 5 треков BGM в `prototype/gorny_prototype/game/audio/bgm`, музыка выбирается через `play_prototype_bgm(...)`.
Атрибуция сохранена в `prototype/gorny_prototype/game/audio/CREDITS.txt` и продублирована в `prototype/gorny_prototype/game/options.rpy`.

### 4. Launcher и desktop shortcut

PASS: launcher для сборки есть - `prototype/launch-book.ps1` и `setup/launch-renpy.ps1`.
PASS: desktop shortcut создан по пути `C:\Users\Бабушка\Desktop\Горный воздух пахнет сиренью и ложью.lnk`.
Ярлык запускает `prototype/launch-book.ps1` через PowerShell и использует пользовательскую иконку `design/generated/icon/shortcut_cover.ico`.

### 5. Blocker'ы для playable demo

Нет blocker'ов по запуску самой демо-сборки.
Автопроверки Ren'Py завершились успешно:
- `lint`: без блокирующих ошибок, только ожидаемое предупреждение `Unreachable Statements` в `game/testcases.rpy`
- `compile`: exit code 0
- `test`: exit code 0

## Краткий вывод

Играбельное демо собрано: сцены закрыты, спрайты и музыка вшиты, запуск через скрипт и ярлык рабочего стола есть. Обязательных blocker'ов для текущей демо-версии не найдено.
