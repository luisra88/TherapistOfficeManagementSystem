from ..database.patient_db_access import create_patient_with_sections

VALID_PATIENT_INFO_SECTIONS = {
    'main_section' : {'full_name', 'registry_number', 'date_of_birth', 'mothers_name', 'fathers_name', 'guardian_name', 'address', 'phone', 'email', 'referal_from', 'post'},
    'scholar_info' : {'school_name', 'education_region', 'municipality', 'district', 'grade_group'},
    'evo_development' : {'evo_history_origin', 'mom_at_home', 'dad_at_home', 'siblings_at_home', 'grandparents_at_home', 'other_at_home', 'problems_at_home', 'problems_at_home_text'},
    'prenatal_history' : {'prenatal_normal', 'prenatal_falls', 'prenatal_druguse', 'prenatal_high_bp', 'prenatal_bleeds', 'prenatal_vomits', 'prenatal_diabetes', 'prenatal_accidents', 
                          'prenatal_meduse', 'prenatal_other', 'prenatal_other_text', 'prenatal_mothers_emotional_state', 'prenatal_mothers_emotional_state_text', 'perinatal_natural', 'perinatal_csection', 'perinatal_premature',
                            'perinatal_complications', 'perinatal_complications_text'},
    'postnatal_history' : {'postnatal_normal', 'postnatal_cianosis', 'postnatal_meningitis', 'postnatal_ictericia', 'postnatal_seizures', 'postnatal_incubator', 'postnatal_incubator_time',
                            'postnatal_other', 'postnatal_other_text', 'weight_pounds', 'weight_oz', 'size_at_birth'},
    'development' : {'psycholinguistic_development', 'psycholinguistic_difficulty', 'pshycholinguistic_difficulty_text', 'psychomotor_development', 'psychomotor_difficulty', 'psychomotor_difficulty_text', 
                     'activity_level', 'turn_level', 'sit_level', 'crawl_level', 'walk_level', 'stand_with_support_level', 'stand_without_support_level', 'jump_with_one_foot_level', 'jump_with_both_feet_level',
                       'leap_level', 'play_level'},
    'illnesses' : {'illness_asma', 'illness_pulmonia', 'illness_fiebres', 'illness_seizures', 'illness_surgeries', 'illness_diabetes', 'illness_other_illnesses', 'illness_other_illnesses_text'},
    'scholar_history': {'head_start', 'kindergarten', 'other_programs', 'other_programs_text', 'held_back', 'academic_performance',
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

def create_new_patient(main_section_values, scholar_info_section_values, evo_section_values, prenatal_section_values, postnatal_section_values, development_section_values, illnesses_values,
                            treatments_section_values, scholar_history_section_values, flunked_grades, academic_difficulty_section_values, relationships_section_values, current_health_section_values, behavior_section_values):
    """
    Wrapper function to create a new patient by organizing and validating input for each section 
    before calling create_patient_with_sections.
    """
    # Main patient data setup
    patient_info = main_section_values

    # Dictionary to hold data for each section
    sections_data = {
        'scholar_info': scholar_info_section_values,
        'evo_development': evo_section_values,
        'prenatal_history': prenatal_section_values,
        'postnatal_history': postnatal_section_values,
        'development': development_section_values,
        'illnesses': illnesses_values,
        'scholar_history': scholar_history_section_values,
        'academic_difficulties': academic_difficulty_section_values,
        'personal_relationships': relationships_section_values,
        'health_history': current_health_section_values,
        'behavior_history': behavior_section_values
    }

    # Validate that each section matches the required keys in VALID_PATIENT_INFO_SECTIONS
    for section_name, section_data in sections_data.items():
        required_keys = VALID_PATIENT_INFO_SECTIONS[section_name]
        missing_keys = required_keys - section_data.keys()
        print (section_name + " section data" +str(section_data))
        if missing_keys:
            raise ValueError(f"Missing required keys in {section_name}: {', '.join(missing_keys)}")

    # Treatments and flunked grades sections
    treatment_entries = treatments_section_values
    flunked_entries = flunked_grades

    # Call create_patient_with_sections with structured data
    #patient_id = create_patient_with_sections(patient_info, sections_data, treatment_entries, flunked_entries)
    print ("patient_info" + str(patient_info))
    print ("treatment_entries data" + str(treatment_entries))
    print ("flunked_entries data" + str(flunked_entries))

    #return patient_id

def prepare_section_data(patient_info, section):
    if section not in VALID_PATIENT_INFO_SECTIONS:
        raise ValueError(f"Invalid section: {section}")

    # Get the valid fields for the target section
    section_fields = VALID_PATIENT_INFO_SECTIONS[section]

    section_data = {key: value for key, value in patient_info.items() if key in section_fields}

    if not section_data:
        raise ValueError(f"No valid data found for section: {section}")

    return section_data