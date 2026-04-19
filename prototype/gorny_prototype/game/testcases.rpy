testsuite global:
    after testcase:
        python:
            reset_prototype_state()

    teardown:
        exit

testcase asset_registry:
    assert eval (prototype_asset_counts()[1] == 10)
    assert eval (prototype_asset_counts()[0] >= 0)

testcase ending_logic_alliance:
    assert eval (determine_act_ending({
        "trust_dima": 4,
        "trust_misha": 1,
        "trust_vika": 0,
        "trust_marina": 2,
        "legend_integrity": 2,
        "school_heat": 2,
        "criminal_heat": 1,
        "evidence_strength": 3,
        "ai_dependency": 1,
        "phone_found": True,
        "dima_confession_unlocked": True,
        "nikita_lead_open": True,
        "misha_warning_received": False,
    }) == "A")

testcase ending_logic_isolation:
    assert eval (determine_act_ending({
        "trust_dima": 1,
        "trust_misha": 1,
        "trust_vika": 0,
        "trust_marina": 1,
        "legend_integrity": 2,
        "school_heat": 1,
        "criminal_heat": 1,
        "evidence_strength": 2,
        "ai_dependency": 5,
        "phone_found": True,
        "dima_confession_unlocked": False,
        "nikita_lead_open": False,
        "misha_warning_received": True,
    }) == "B")

testcase ending_logic_surveillance:
    assert eval (determine_act_ending({
        "trust_dima": 1,
        "trust_misha": 0,
        "trust_vika": 1,
        "trust_marina": 2,
        "legend_integrity": 1,
        "school_heat": 3,
        "criminal_heat": 4,
        "evidence_strength": 2,
        "ai_dependency": 1,
        "phone_found": True,
        "dima_confession_unlocked": False,
        "nikita_lead_open": False,
        "misha_warning_received": True,
    }) == "C")

testcase ending_logic_social:
    assert eval (determine_act_ending({
        "trust_dima": 1,
        "trust_misha": 0,
        "trust_vika": 4,
        "trust_marina": 2,
        "legend_integrity": 4,
        "school_heat": 1,
        "criminal_heat": 1,
        "evidence_strength": 2,
        "ai_dependency": 1,
        "phone_found": True,
        "dima_confession_unlocked": False,
        "nikita_lead_open": False,
        "misha_warning_received": False,
    }) == "D")

testcase ending_logic_mask:
    assert eval (determine_act_ending({
        "trust_dima": 1,
        "trust_misha": 0,
        "trust_vika": 1,
        "trust_marina": 2,
        "legend_integrity": 1,
        "school_heat": 3,
        "criminal_heat": 3,
        "evidence_strength": 1,
        "ai_dependency": 1,
        "phone_found": True,
        "dima_confession_unlocked": False,
        "nikita_lead_open": False,
        "misha_warning_received": True,
    }) == "E")

testcase branch_smoke_alliance:
    run Jump("smoke_alliance")
    assert eval (ending_code == "A")

testcase branch_smoke_isolation:
    run Jump("smoke_isolation")
    assert eval (ending_code == "B")

testcase branch_smoke_social:
    run Jump("smoke_social")
    assert eval (ending_code == "D")
