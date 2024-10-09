-- Table for storing patient details
CREATE TABLE IF NOT EXISTS patients (
    patient_id SERIAL PRIMARY KEY,
    full_name TEXT NOT NULL,
    registry_number TEXT NOT NULL UNIQUE,
    date_of_birth DATE NOT NULL,
    mothers_name TEXT,
    fathers_name TEXT,
    guardian_name TEXT,
    address TEXT,
    phone TEXT,
    email TEXT,
    history_origin BOOLEAN
);

-- Table for storing evaluation types
CREATE TABLE IF NOT EXISTS evaluation_types (
    evaluation_type_id SERIAL PRIMARY KEY,
    type_name TEXT NOT NULL UNIQUE
);

-- Table for storing evaluations
CREATE TABLE IF NOT EXISTS evaluations (
    evaluation_id SERIAL PRIMARY KEY,
    chronological_age TEXT NOT NULL,
    patient_id INTEGER REFERENCES patients(patient_id) ON DELETE CASCADE,
    evaluation_type_id INTEGER NOT NULL REFERENCES evaluation_types(evaluation_type_id) ON DELETE CASCADE,
    evaluation_date DATE NOT NULL
);

-- Table for storing evaluation results (with flexible structure)
CREATE TABLE IF NOT EXISTS evaluation_results (
    result_id SERIAL PRIMARY KEY,
    evaluation_id INTEGER REFERENCES evaluations(evaluation_id) ON DELETE CASCADE,
    result_data JSONB NOT NULL,
    relationship_with_examiner TEXT NOT NULL,
    disposition BOOLEAN NOT NULL,
    attention_level TEXT NOT NULL,
    activity_level TEXT NOT NULL,
    execution_level TEXT NOT NULL,
    observed_behavior TEXT NOT NULL,
    laterality TEXT NOT NULL,
    other_observations TEXT
);

-- Treatment table
CREATE TABLE IF NOT EXISTS treatments (
    treatment_id SERIAL PRIMARY KEY,
    patient_id INTEGER REFERENCES patients(patient_id) ON DELETE CASCADE,
    treatment_type TEXT NOT NULL,
    weekly_frequency INTEGER NOT NULL,
    duration INTEGER NOT NULL,
    modality TEXT NOT NULL,
    start_date DATE NOT NULL,
    status TEXT NOT NULL
);

-- Scholar history table
CREATE TABLE IF NOT EXISTS scholar_history (
    scholar_history_id SERIAL PRIMARY KEY,
    patient_id INTEGER REFERENCES patients(patient_id) ON DELETE CASCADE,
    school TEXT,
    education_region TEXT,
    municipality TEXT,
    district TEXT,
    grade_group TEXT,
    post TEXT,
    head_start BOOLEAN,
    kindergarten BOOLEAN,
    other_programs TEXT,
    held_back BOOLEAN,
    held_back_times INTEGER,
    academic_presentation TEXT,
    difficulties JSONB,
    special_ed BOOLEAN,
    special_ed_type TEXT,
    current_academic_function TEXT
);

-- Personal relationship history table
CREATE TABLE IF NOT EXISTS relationship_history (
    relationship_history_id SERIAL PRIMARY KEY,
    patient_id INTEGER REFERENCES patients(patient_id) ON DELETE CASCADE,
    people_at_home TEXT,  
    problems_at_home BOOLEAN,
    father_or_guardian_relationship BOOLEAN,
    sibling_relationship BOOLEAN,
    peer_group_relationship BOOLEAN,
    adult_relationship BOOLEAN,
    authority_relationship BOOLEAN
);

-- Current health table
CREATE TABLE IF NOT EXISTS health_history (
    health_history_id SERIAL PRIMARY KEY,
    patient_id INTEGER REFERENCES patients(patient_id) ON DELETE CASCADE,
    illnesses TEXT,
    visual_problems BOOLEAN,
    uses_glasses BOOLEAN,
    hearing_problems BOOLEAN,
    uses_hearing_aids BOOLEAN,
    neurological_problems BOOLEAN,
    motor_problems BOOLEAN,
    uses_wheelchair BOOLEAN,
    uses_prosthesis BOOLEAN,
    medical_treatments TEXT,
    other_health_issues TEXT
);

-- Behavior history table
CREATE TABLE IF NOT EXISTS behavior_history (
    behavior_history_id SERIAL PRIMARY KEY,
    patient_id INTEGER REFERENCES patients(patient_id) ON DELETE CASCADE,
    scared_to_go_to_school BOOLEAN,
    enuresis BOOLEAN,
    nervous_tic BOOLEAN,
    retraimiento BOOLEAN,
    encopresis BOOLEAN,
    sadness BOOLEAN,
    aggression BOOLEAN,
    nail_biting BOOLEAN,
    frequent_crying BOOLEAN,
    anxiety BOOLEAN,
    auto_aggression BOOLEAN,
    challenge_authority BOOLEAN,
    irritability BOOLEAN,
    defiant BOOLEAN,
    impulsivity BOOLEAN,
    other TEXT
);

CREATE TABLE IF NOT EXISTS prenatal_history (
    prenatal_history_id SERIAL PRIMARY KEY,
    patient_id INTEGER REFERENCES patients(patient_id),
    prenatal_history TEXT,
    perinatal_history TEXT,
    postnatal_history TEXT,
    weight_at_birth TEXT,
    size_at_birth TEXT,
    psycholinguistic_development TEXT,
    psychomotor_development TEXT,
    activity_level TEXT,
    turn_level INTEGER,
    sit_level INTEGER,
    crawl_level INTEGER,
    walk_level INTEGER,
    stand_with_support_level INTEGER,
    stand_without_support_level INTEGER,
    jump_with_one_foot_level INTEGER,
    jump_with_both_feet_level INTEGER,
    jump_and_play_level INTEGER
);
-- Table for storing user details with hashed passwords
CREATE TABLE IF NOT EXISTS users (
    user_id SERIAL PRIMARY KEY,
    username TEXT NOT NULL UNIQUE,
    password_hash TEXT NOT NULL
);