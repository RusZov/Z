init -10 python:
    import glob
    import os
    import store

    SCENE_LIBRARY = {
        "arrival_train": {
            "title": "Поезд и сирень",
            "description": "Нужен фон приезда в Горный.",
            "color": "#55606A",
            "filenames": ["arrival_train", "bg_arrival_train", "train_arrival", "bg_01_train_mountains"],
        },
        "gorny_village_day": {
            "title": "Горный днём",
            "description": "Нужен общий вид посёлка.",
            "color": "#6D8C63",
            "filenames": ["gorny_village_day", "village_day", "gorny_postcard", "bg_02_gorny_panorama"],
        },
        "school_exterior": {
            "title": "Школа",
            "description": "Нужен фасад школы.",
            "color": "#D9D4CB",
            "filenames": ["school_exterior", "school_facade", "bg_school_exterior", "bg_06_school_facade_day"],
        },
        "school_corridor": {
            "title": "Коридор",
            "description": "Нужен школьный коридор.",
            "color": "#CBB7E5",
            "filenames": ["school_corridor", "corridor_window", "bg_school_corridor", "bg_08_school_corridor_window"],
        },
        "classroom_literature": {
            "title": "Класс литературы",
            "description": "Нужен класс для школьных сцен.",
            "color": "#F1D49A",
            "filenames": ["classroom_literature", "school_classroom", "bg_classroom_literature", "bg_07_classroom"],
        },
        "diana_room_night": {
            "title": "Комната Дианы ночью",
            "description": "Нужен ночной интерьер комнаты.",
            "color": "#2A2D33",
            "filenames": ["diana_room_night", "room_night", "bg_diana_room_night", "bg_04_diana_room_night"],
        },
        "shed_night": {
            "title": "Сарай",
            "description": "Нужен тревожный ночной сарай.",
            "color": "#2A2D33",
            "filenames": ["shed_night", "bg_shed_night", "shed_phone_scene", "bg_10_thriller_night_alley_shed"],
        },
        "misha_porch_evening": {
            "title": "Крыльцо Миши",
            "description": "Нужно вечернее соседское крыльцо.",
            "color": "#55606A",
            "filenames": ["misha_porch_evening", "porch_evening", "neighbor_porch", "bg_05_misha_porch_evening"],
        },
        "stadium_sunset": {
            "title": "Трибуны на закате",
            "description": "Нужен фон признания на трибунах.",
            "color": "#B6443A",
            "filenames": ["stadium_sunset", "bleachers_sunset", "bg_stadium_sunset", "bg_11_stadium_sunset"],
        },
        "alley_well_night": {
            "title": "Проулок и колодец",
            "description": "Нужна ночная локация для финального давления.",
            "color": "#2A2D33",
            "filenames": ["alley_well_night", "alley_well", "bg_alley_well_night", "bg_10_thriller_night_alley_shed"],
        },
    }

    SPRITE_LIBRARY = {
        "diana": {
            "title": "Диана",
            "color": "#7387A6",
            "poses": {
                "phone": ["diana_phone"],
                "folded": ["diana_folded"],
                "shocked": ["diana_shocked"],
            },
        },
        "dima": {
            "title": "Дима",
            "color": "#7887B8",
            "poses": {
                "thinking": ["dima_thinking"],
                "crossed": ["dima_crossed"],
                "guarded": ["dima_guarded"],
            },
        },
        "misha": {
            "title": "Миша",
            "color": "#6D6D74",
            "poses": {
                "closed": ["misha_closed"],
                "stop": ["misha_stop"],
                "warning": ["misha_warning"],
            },
        },
        "vika": {
            "title": "Вика",
            "color": "#B86E9B",
            "poses": {
                "dominant": ["vika_dominant"],
                "pointing": ["vika_pointing"],
                "smirk": ["vika_smirk"],
            },
        },
        "marina": {
            "title": "Марина",
            "color": "#9C7656",
            "poses": {
                "bag": ["marina_bag"],
                "stop": ["marina_stop"],
            },
        },
    }

    MUSIC_LIBRARY = {
        "school_day": {
            "title": "Amberlight",
            "filenames": ["school_day_amberlight"],
        },
        "suspense": {
            "title": "Sanctuary",
            "filenames": ["suspense_sanctuary"],
        },
        "home_tension": {
            "title": "The Long Dark",
            "filenames": ["home_tension_the_long_dark"],
        },
        "investigation": {
            "title": "Nightfall",
            "filenames": ["investigation_night_nightfall"],
        },
        "finale": {
            "title": "Echoes Of Home",
            "filenames": ["finale_echoes_of_home"],
        },
    }

    ROUTE_TITLES = {
        "none": "без фокуса",
        "dima": "маршрут Димы",
        "misha": "маршрут Миши",
        "vika": "маршрут Вики",
    }

    def prototype_renpy_path(path):
        absolute = os.path.abspath(path)
        relative = os.path.relpath(absolute, config.gamedir)
        return relative.replace("\\", "/")

    def prototype_design_root():
        return os.path.abspath(os.path.join(config.gamedir, "assets", "backgrounds"))

    def prototype_sprite_root():
        return os.path.abspath(os.path.join(config.gamedir, "assets", "characters", "transparent"))

    def prototype_music_root():
        return os.path.abspath(os.path.join(config.gamedir, "audio", "bgm"))

    def prototype_find_background(scene_key):
        root = prototype_design_root()
        meta = SCENE_LIBRARY.get(scene_key)

        if (not meta) or (not os.path.isdir(root)):
            return None

        extensions = (".png", ".jpg", ".jpeg", ".webp")

        for stem in meta["filenames"]:
            for extension in extensions:
                direct = os.path.join(root, stem + extension)
                if os.path.isfile(direct):
                    return prototype_renpy_path(direct)

                recursive = glob.glob(os.path.join(root, "**", stem + extension), recursive=True)
                if recursive:
                    return prototype_renpy_path(recursive[0])

        return None

    def prototype_scene_has_asset(scene_key):
        return prototype_find_background(scene_key) is not None

    def prototype_find_sprite(character_key, pose_key=None):
        root = prototype_sprite_root()
        meta = SPRITE_LIBRARY.get(character_key)

        if (not meta) or (not os.path.isdir(root)):
            return None

        poses = meta.get("poses", {})

        if pose_key is None and poses:
            pose_key = next(iter(poses))

        stems = poses.get(pose_key, [])
        extensions = (".png", ".webp")

        for stem in stems:
            for extension in extensions:
                direct = os.path.join(root, stem + extension)
                if os.path.isfile(direct):
                    return prototype_renpy_path(direct)

                recursive = glob.glob(os.path.join(root, "**", stem + extension), recursive=True)
                if recursive:
                    return prototype_renpy_path(recursive[0])

        return None

    def prototype_character(character_key, pose_key=None):
        asset_path = prototype_find_sprite(character_key, pose_key)

        if asset_path:
            return store.Image(asset_path)

        raise Exception("Missing required sprite: " + character_key + ":" + str(pose_key))

    def prototype_find_music(track_key):
        root = prototype_music_root()
        meta = MUSIC_LIBRARY.get(track_key)

        if (not meta) or (not os.path.isdir(root)):
            return None

        extensions = (".mp3", ".ogg", ".wav", ".opus")

        for stem in meta["filenames"]:
            for extension in extensions:
                direct = os.path.join(root, stem + extension)
                if os.path.isfile(direct):
                    return prototype_renpy_path(direct)

                recursive = glob.glob(os.path.join(root, "**", stem + extension), recursive=True)
                if recursive:
                    return prototype_renpy_path(recursive[0])

        return None

    def play_prototype_bgm(track_key, fadeout=0.8, fadein=0.8, loop=True):
        if getattr(store, "current_music_key", None) == track_key:
            return None

        if not track_key:
            renpy.music.stop(channel="music", fadeout=fadeout)
            store.current_music_key = None
            return None

        asset_path = prototype_find_music(track_key)

        if asset_path:
            renpy.music.play(asset_path, channel="music", loop=loop, fadeout=fadeout, fadein=fadein)
            store.current_music_key = track_key
            return asset_path

        store.current_music_key = None
        return None

    def prototype_scene_displayable(scene_key):
        asset_path = prototype_find_background(scene_key)

        if asset_path:
            return store.Transform(
                store.Image(asset_path),
                xysize=(config.screen_width, config.screen_height),
                fit="cover",
            )

        raise Exception("Missing required background for scene: " + scene_key)

    def prototype_scene(scene_key):
        store.current_scene_key = scene_key
        return prototype_scene_displayable(scene_key)

    def prototype_asset_counts():
        total = len(SCENE_LIBRARY)
        present = sum(1 for key in SCENE_LIBRARY if prototype_scene_has_asset(key))
        return present, total

    def prototype_route_title(route_key):
        return ROUTE_TITLES.get(route_key or "none", "без фокуса")

    def prototype_missing_backgrounds():
        return [key for key in SCENE_LIBRARY if prototype_find_background(key) is None]

    def prototype_missing_sprites():
        missing = []

        for character_key, meta in SPRITE_LIBRARY.items():
            for pose_key in meta.get("poses", {}):
                if prototype_find_sprite(character_key, pose_key) is None:
                    missing.append(character_key + ":" + pose_key)

        return missing

    def prototype_missing_music():
        return [key for key in MUSIC_LIBRARY if prototype_find_music(key) is None]

    def prototype_assert_assets_ready():
        missing = []
        backgrounds = prototype_missing_backgrounds()
        sprites = prototype_missing_sprites()
        music = prototype_missing_music()

        if backgrounds:
            missing.append("backgrounds=" + ", ".join(backgrounds))

        if sprites:
            missing.append("sprites=" + ", ".join(sprites))

        if music:
            missing.append("music=" + ", ".join(music))

        if missing:
            raise Exception("Prototype assets are incomplete: " + " | ".join(missing))

    def determine_act_ending(values):
        def stat(name):
            return values.get(name, 0)

        if (
            stat("trust_dima") >= 3
            and stat("evidence_strength") >= 3
            and values.get("dima_confession_unlocked")
            and values.get("nikita_lead_open")
        ):
            return "A"

        if (
            stat("trust_vika") >= 4
            and stat("legend_integrity") >= 3
            and stat("school_heat") <= 2
        ):
            return "D"

        if (
            (stat("evidence_strength") <= 1 and stat("criminal_heat") >= 3)
            or (
                values.get("mother_warned_full")
                and stat("criminal_heat") >= 2
                and stat("evidence_strength") <= 2
            )
        ):
            return "E"

        if (
            stat("criminal_heat") >= 4
            and values.get("misha_warning_received")
            and values.get("phone_found")
        ):
            return "C"

        if (
            stat("ai_dependency") >= 4
            and stat("trust_dima") <= 2
            and stat("trust_misha") <= 2
            and stat("trust_vika") <= 2
        ):
            return "B"

        final_choice = values.get("final_choice")

        if final_choice == "dima":
            return "A" if stat("evidence_strength") >= 2 else "C"

        if final_choice == "vika":
            return "D" if stat("legend_integrity") >= 2 else "C"

        if final_choice == "alone":
            return "B"

        if final_choice == "mixed":
            return "C" if stat("criminal_heat") >= 2 else "B"

        if stat("criminal_heat") >= 3:
            return "C"

        return "B"
