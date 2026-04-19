# Toolchain for Visual Novel Setup

Date checked: 2026-04-19
Scope: portable setup only inside `C:\Users\Бабушка\Desktop\игры\setup\`

## Decision

Chosen engine: Ren'Py 8.5.2

Why this stack:
- The official Ren'Py site lists 8.5.2 as the latest stable Ren'Py 8 release, released on 2026-01-03.
- The same official page recommends Ren'Py 8 for new projects.
- For a book-based visual novel on Windows, Ren'Py is the minimal practical stack: script, branching, sprites, backgrounds, music, save/load, and packaging are already built in.

Official sources used:
- https://www.renpy.org/
- https://www.renpy.org/release/8.5.2

## What was already on this PC

- Windows 10 Pro x64
- Python 3.12.4 at `C:\Users\Бабушка\AppData\Local\Programs\Python\Python312\python.exe`
- Git 2.53.0.windows.1 at `C:\Program Files\Git\cmd\git.exe`
- VS Code 1.116.0 at `C:\Users\Бабушка\AppData\Local\Programs\Microsoft VS Code\bin\code.cmd`

Notes:
- No existing Ren'Py install was found in the common local locations checked.
- No Ren'Py VS Code extension was installed.
- I did not perform system-wide installs, because the task scope is limited to this `setup` directory.

## Downloaded and prepared in setup

- Archive: `C:\Users\Бабушка\Desktop\игры\setup\downloads\renpy-8.5.2-sdk.zip`
- Checksums file: `C:\Users\Бабушка\Desktop\игры\setup\downloads\checksums.txt`
- Extracted SDK: `C:\Users\Бабушка\Desktop\игры\setup\renpy-8.5.2-sdk`
- Launch helper: `C:\Users\Бабушка\Desktop\игры\setup\launch-renpy.ps1`

Integrity check:
- Official checksum file was downloaded from Ren'Py.
- Local MD5 for `renpy-8.5.2-sdk.zip`: `fbea3087a1a1b1f69261e352d54b5d10`
- That matches the official checksum entry for `renpy-8.5.2-sdk.zip`.

## Minimal stack for starting the project

Required:
- Ren'Py 8.5.2 SDK

Already available and enough for first development pass:
- VS Code as editor
- Git for versioning

Not downloaded on purpose yet:
- Android support (RAPT)
- iOS support (Renios)
- Web export support (Renpyweb)

Reason:
- These are optional official add-ons and are not required to start writing and testing a Windows visual novel.

## How to launch

Direct launcher:

```powershell
& 'C:\Users\Бабушка\Desktop\игры\setup\renpy-8.5.2-sdk\renpy.exe'
```

Helper script:

```powershell
powershell -ExecutionPolicy Bypass -File 'C:\Users\Бабушка\Desktop\игры\setup\launch-renpy.ps1'
```

What to do after launch:
1. Create a new project in your chosen game folder.
2. In the editor selection, use `Visual Studio Code (System)` because VS Code already exists on this PC.
3. Put generated character art and backgrounds into the project's `game` assets folders.
4. Start writing branches in `script.rpy`.

## Status

Completed automatically:
- Verified the local baseline tools.
- Confirmed the current official Ren'Py release.
- Downloaded the official Ren'Py SDK archive.
- Verified the archive checksum.
- Extracted the SDK locally inside `setup`.

Blockers:
- No hard blocker for starting a Windows Ren'Py prototype.
- If you later need Android, iOS, or web builds, the matching official add-ons still need to be downloaded.
