# Прототип визуальной новеллы

В этой папке собран первый играбельный прототип акта на Ren'Py.

## Что внутри

- `gorny_prototype/` — сам проект Ren'Py.
- `logs/` — сохранённые результаты автоматических проверок.
- `build_report.md` — краткий отчёт по сборке, ограничениям и тестам.

## Что уже реализовано

- Играбельный первый акт с 5 ключевыми выборами.
- 5 актовых исходов по сценарным документам: союз с Димой, изоляция, давление криминальной линии, социальный щит Вики и ранний провал.
- Системные переменные и флаги, согласованные с `script/game_variables.md`.
- Сборка работает в строгом режиме по ассетам: обязательные фоны, спрайты и музыка должны существовать на диске.
- Подключены реальные фоны, прозрачные спрайты персонажей и музыкальные треки первого акта.
- Для быстрого запуска добавлен `launch-book.ps1` и ярлык на рабочем столе Windows.

## Как запустить

```powershell
& 'C:\Users\Бабушка\Desktop\игры\setup\renpy-8.5.2-sdk\renpy.exe' 'C:\Users\Бабушка\Desktop\игры\prototype\gorny_prototype'
```

Или:

```powershell
powershell -ExecutionPolicy Bypass -File 'C:\Users\Бабушка\Desktop\игры\prototype\launch-book.ps1'
```

## Как прогнать проверки

```powershell
& 'C:\Users\Бабушка\Desktop\игры\setup\renpy-8.5.2-sdk\renpy.exe' 'C:\Users\Бабушка\Desktop\игры\prototype\gorny_prototype' lint 'C:\Users\Бабушка\Desktop\игры\prototype\logs\lint.txt'
& 'C:\Users\Бабушка\Desktop\игры\setup\renpy-8.5.2-sdk\renpy.exe' 'C:\Users\Бабушка\Desktop\игры\prototype\gorny_prototype' compile *> 'C:\Users\Бабушка\Desktop\игры\prototype\logs\compile.txt'
& 'C:\Users\Бабушка\Desktop\игры\setup\renpy-8.5.2-sdk\renpy.exe' 'C:\Users\Бабушка\Desktop\игры\prototype\gorny_prototype' test *> 'C:\Users\Бабушка\Desktop\игры\prototype\logs\test.txt'
```

## Фоны

Проект ожидает реальные файлы в `gorny_prototype/game/assets/backgrounds` и считает их обязательными для запуска демо.

Канонические имена для автоматического подхвата:

- `arrival_train`
- `gorny_village_day`
- `school_exterior`
- `school_corridor`
- `classroom_literature`
- `diana_room_night`
- `shed_night`
- `misha_porch_evening`
- `stadium_sunset`
- `alley_well_night`

Допустимые расширения: `.png`, `.jpg`, `.jpeg`, `.webp`.

## Спрайты и музыка

- Спрайты персонажей лежат в `gorny_prototype/game/assets/characters/transparent`.
- Иконка ярлыка лежит в `design/generated/icon/shortcut_cover.ico`.
- Музыка лежит в `gorny_prototype/game/audio/bgm`.
- Атрибуция музыки лежит в `gorny_prototype/game/audio/CREDITS.txt`.
