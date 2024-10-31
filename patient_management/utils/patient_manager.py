from ..database.patient_db_access import create_or_update_patient, create_or_update_patient_info_section, add_flunked_entries, add_treatment_entries

VALID_PATIENT_INFO_SECTIONS = {
    'main_section' : {'full_name', 'registry_number', 'date_of_birth', 'mothers_name', 'fathers_name', 'guardian_name', 'address', 'phone', 'email', 'referal_from', 'post'},
    'evo_development' : {'evo_history_origin', 'mom_at_home', 'dad_at_home', 'siblings_at_home', 'grandparents_at_home', 'other_at_home', 'problems_at_home', 'problems_at_home_text'},
    'prenatal_history' : {'prenatal_normal', 'prenatal_falls', 'prenatal_druguse', 'prenatal_high_bp', 'prenatal_bleeds', 'prenatal_vomits', 'prenatal_diabetes', 'prenatal_accidents', 
                          'prenatal_meduse', 'prenatal_other', 'prenatal_other_text', 'prenatal_mothers_emotional_state', 'perinatal_natural', 'perinatal_csection', 'perinatal_premature',
                            'perinatal_complications', 'perinatal_complications_text'},
    'postnatal_history' : {'postnatal_normal', 'postnatal_cianosis', 'postnatal_meningitis', 'postnatal_ictericia', 'postnatal_seizures', 'postnatal_incubator', 'postnatal_incubator_time',
                            'postnatal_other', 'postnatal_other_text', 'weight_pounds', 'weight_oz', 'size_at_birth'},
    'development' : {'psycholinguistic_development', 'psycholinguistic_difficulty', 'pshycholinguistic_difficulty_text', 'psychomotor_development', 'psychomotor_difficulty', 'psychomotor_difficulty_text', 
                     'activity_level', 'turn_level', 'sit_level', 'crawl_level', 'walk_level', 'stand_with_support_level', 'stand_without_support_level', 'jump_with_one_foot_level', 'jump_with_both_feet_level',
                       'leap_level', 'play_level'},
    'illnesses' : {'illness_asma', 'illness_pulmonia', 'illness_fiebres', 'illness_seizures', 'illness_surgeries', 'illness_diabetes', 'illness_other_illnesses', 'illness_other_illnesses_text'},
    'scholar_history': {'school_name', 'education_region', 'municipality', 'district', 'grade_group', 'head_start', 'kindergarten', 'other_programs', 'other_programs_text', 'held_back', 'academic_performance',
                         'special_ed', 'special_ed_salon_recurso', 'special_ed_salon_fulltime', 'special_ed_other', 'special_ed_other_text', 'current_academic_performance'},
    'academic_difficulties' : {'reading_difficulty', 'writing_difficulty', 'math_difficulty', 'reading_comprehension_difficulty', 'inverts_substitutes_reading_difficulty',
                                'omits_reading_difficulty', 'copy_writing_difficulty', 'inverts_substitutes_writing_difficulty', 'omits_writing_difficulty', 'sum_substraction_math_difficulty',
                                  'multiplication_math_difficulty', 'division_math_difficulty', 'other_difficulties', 'other_difficulties_text'},
    'personal_relationships': {'father_or_guardian_relationship', 'sibling_relationship', 'peer_group_relationship', 'adult_relationship', 'authority_relationship'},
    'health_history': {'good_health', 'visual_problems', 'uses_glasses', 'hearing_problems', 'uses_hearing_aids', 'neurological_problems', 'motor_problems', 'uses_wheelchair', 'uses_prosthesis',
                        'medical_treatment', 'medical_treatment_text', 'other_health_issues', 'other_health_issues_text'},
    'behavior_history' : {'scared_to_go_to_school', 'enuresis', 'nervous_tic','retraimiento', 'encopresis', 'sadness', 'aggression', 'nail_biting','frequent_crying', 'anxiety', 'auto_aggression', 
                          'challenge_authority', 'irritability', 'defiant', 'impulsivity', 'other_behavioral_traits', 'other_behavioral_traits_text'},                    
}
VALID_TREATMENT_COLUMNS = {'treatment_type', 'weekly_frequency', 'duration', 'modality', 'start_date', 'status'}

def create_new_patient(patient_info):
    """
    main_section_data = prepare_section_data(patient_info, "main_section")
    create_or_update_patient(main_section_data)
    registry_number = patient_info['registry_number']
    evo_development_data = prepare_section_data(patient_info, "evo_development")
    create_or_update_patient_info_section("evo_development", registry_number, evo_development_data)
    prenatal_history_data = prepare_section_data(patient_info, "prenatal_history")
    create_or_update_patient_info_section("prenatal_history", registry_number, prenatal_history_data)
    postnatal_history_data = prepare_section_data(patient_info, "postnatal_history")
    create_or_update_patient_info_section("postnatal_history", registry_number, postnatal_history_data)
    development_data = prepare_section_data(patient_info, "development")
    create_or_update_patient_info_section("development", registry_number, development_data)
    illnesses_data = prepare_section_data(patient_info, "illnesses")
    create_or_update_patient_info_section("illnesses", registry_number, illnesses_data)
    scholar_history_data = prepare_section_data(patient_info, "scholar_history")
    create_or_update_patient_info_section("scholar_history", registry_number, scholar_history_data)
    if scholar_history_data['held_back']:
        add_flunked_entries(patient_info['held_back_grades'])
    academic_difficulties_data = prepare_section_data(patient_info, "academic_difficulties")
    create_or_update_patient_info_section("academic_difficulties", registry_number, academic_difficulties_data)
    personal_relationships_data = prepare_section_data(patient_info, "personal_relationships")
    create_or_update_patient_info_section("personal_relationships", registry_number, personal_relationships_data)
    health_history_data = prepare_section_data(patient_info, "health_history")
    create_or_update_patient_info_section("health_history", registry_number, health_history_data)
    behavior_history_data = prepare_section_data(patient_info, "behavior_history")
    create_or_update_patient_info_section("behavior_history", registry_number, behavior_history_data)
    add_treatment_entries(patient_info['treatments'], registry_number)
    """

def prepare_section_data(patient_info, section):
    if section not in VALID_PATIENT_INFO_SECTIONS:
        raise ValueError(f"Invalid section: {section}")

    # Get the valid fields for the target section
    section_fields = VALID_PATIENT_INFO_SECTIONS[section]

    section_data = {key: value for key, value in patient_info.items() if key in section_fields}

    if not section_data:
        raise ValueError(f"No valid data found for section: {section}")

    return section_data