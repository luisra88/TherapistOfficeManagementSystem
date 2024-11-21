-- Table for storing patient details
CREATE TABLE IF NOT EXISTS patients (
    patient_id SERIAL PRIMARY KEY,
    full_name TEXT NOT NULL,
    registry_number TEXT NOT NULL UNIQUE,
    date_of_birth DATE NOT NULL,
    mothers_name TEXT DEFAULT 'N/A',
    fathers_name TEXT DEFAULT 'N/A',
    guardian_name TEXT DEFAULT 'N/A',
    address TEXT DEFAULT 'N/A',
    phone TEXT DEFAULT 'N/A',
    email TEXT DEFAULT 'N/A',
    referal_from TEXT DEFAULT 'N/A',
    post TEXT DEFAULT 'N/A'
);

-- Personal relationship history table
CREATE TYPE evo_history_origin_type AS ENUM ('entrevista', 'lectura de expediente');
CREATE TABLE IF NOT EXISTS evo_development (
    patient_id INTEGER PRIMARY KEY REFERENCES patients(patient_id) ON DELETE CASCADE,
    evo_history_origin evo_history_origin_type DEFAULT 'entrevista',
    mom_at_home BOOLEAN DEFAULT FALSE,
    dad_at_home BOOLEAN DEFAULT FALSE,
    siblings_at_home BOOLEAN DEFAULT FALSE, 
    grandparents_at_home BOOLEAN DEFAULT FALSE, 
    other_at_home BOOLEAN DEFAULT FALSE,
    other_at_home_text TEXT DEFAULT 'N/A',
    problems_at_home BOOLEAN DEFAULT FALSE,
    problems_at_home_text TEXT DEFAULT 'N/A'
);

CREATE TABLE IF NOT EXISTS prenatal_history (
    patient_id INTEGER PRIMARY KEY REFERENCES patients(patient_id),
    prenatal_normal BOOLEAN DEFAULT FALSE,
    prenatal_falls BOOLEAN DEFAULT FALSE,
    prenatal_druguse BOOLEAN DEFAULT FALSE,
    prenatal_high_bp BOOLEAN DEFAULT FALSE,
    prenatal_bleeds BOOLEAN DEFAULT FALSE,
    prenatal_vomits BOOLEAN DEFAULT FALSE,
    prenatal_diabetes BOOLEAN DEFAULT FALSE,
    prenatal_accidents BOOLEAN DEFAULT FALSE,
    prenatal_meduse BOOLEAN DEFAULT FALSE,
    prenatal_other BOOLEAN DEFAULT FALSE,
    prenatal_other_text TEXT DEFAULT 'N/A',
    prenatal_mothers_emotional_state BOOLEAN DEFAULT FALSE,
    prenatal_mothers_emotional_state_text TEXT DEFAULT 'N/A',
    perinatal_natural BOOLEAN DEFAULT FALSE,
    perinatal_csection BOOLEAN DEFAULT FALSE,
    perinatal_premature BOOLEAN DEFAULT FALSE,
    perinatal_complications BOOLEAN DEFAULT FALSE,
    perinatal_complications_text TEXT DEFAULT 'N/A'
);

CREATE TABLE IF NOT EXISTS postnatal_history(
    patient_id INTEGER PRIMARY KEY REFERENCES patients(patient_id),
    postnatal_normal BOOLEAN DEFAULT FALSE,
    postnatal_cianosis BOOLEAN DEFAULT FALSE,
    postnatal_meningitis BOOLEAN DEFAULT FALSE,
    postnatal_ictericia BOOLEAN DEFAULT FALSE,
    postnatal_seizures BOOLEAN DEFAULT FALSE,
    postnatal_incubator BOOLEAN DEFAULT FALSE,
    postnatal_incubator_time INTEGER DEFAULT 0,
    postnatal_other BOOLEAN DEFAULT FALSE,
    postnatal_other_text TEXT DEFAULT 'N/A',
    weight_pounds DECIMAL(10,2) DEFAULT 0,
    weight_oz DECIMAL(10,2) DEFAULT 0,
    size_at_birth DECIMAL(10,2) DEFAULT 0
);

CREATE TYPE development_type AS ENUM ('Normal', 'Rápido', 'Lento');
CREATE TYPE activity_type AS ENUM ('Tranquilo', 'Inquieto', 'Hiperactivo', 'Hipoactivo');
CREATE TYPE activity_completion AS ENUM ('L', 'AN', 'NL');
CREATE TABLE IF NOT EXISTS development(
    patient_id INTEGER PRIMARY KEY REFERENCES patients(patient_id),
    psycholinguistic_development development_type DEFAULT 'Normal',
    psycholinguistic_difficulty BOOLEAN DEFAULT FALSE,
    pshycholinguistic_difficulty_text TEXT DEFAULT 'N/A',
    psychomotor_development development_type DEFAULT 'Normal',
    psychomotor_difficulty BOOLEAN DEFAULT FALSE,
    psychomotor_difficulty_text TEXT DEFAULT 'N/A',
    activity_level activity_type DEFAULT 'Tranquilo',
    turn_level activity_completion DEFAULT 'AN',
    sit_level activity_completion DEFAULT 'AN',
    crawl_level activity_completion DEFAULT 'AN',
    walk_level activity_completion DEFAULT 'AN',
    stand_with_support_level activity_completion DEFAULT 'AN',
    stand_without_support_level activity_completion DEFAULT 'AN',
    jump_with_one_foot_level activity_completion DEFAULT 'AN',
    jump_with_both_feet_level activity_completion DEFAULT 'AN',
    leap_level activity_completion DEFAULT 'AN',
    play_level activity_completion DEFAULT 'AN'
);

CREATE TABLE IF NOT EXISTS illnesses(
    patient_id INTEGER PRIMARY KEY REFERENCES patients(patient_id) ON DELETE CASCADE,
    illness_asma BOOLEAN DEFAULT FALSE,
    illness_pulmonia BOOLEAN DEFAULT FALSE,
    illness_fiebres BOOLEAN DEFAULT FALSE,
    illness_seizures BOOLEAN DEFAULT FALSE,
    illness_surgeries BOOLEAN DEFAULT FALSE,
    illness_diabetes BOOLEAN DEFAULT FALSE,
    illness_other_illnesses BOOLEAN DEFAULT FALSE,
    illness_other_illnesses_text TEXT DEFAULT 'N/A'
);

CREATE TABLE IF NOT EXISTS scholar_info (
    patient_id INTEGER PRIMARY KEY REFERENCES patients(patient_id) ON DELETE CASCADE,
    school_name TEXT DEFAULT 'N/A',
    education_region TEXT DEFAULT 'N/A',
    municipality TEXT DEFAULT 'N/A',
    district TEXT DEFAULT 'N/A',
    grade_group TEXT DEFAULT 'N/A'
);

CREATE TYPE academic_performance_enum AS ENUM('Satisfactorio', 'Regular', 'Deficiente');
-- Scholar history table
CREATE TABLE IF NOT EXISTS scholar_history (
    patient_id INTEGER PRIMARY KEY REFERENCES patients(patient_id) ON DELETE CASCADE,
    head_start BOOLEAN DEFAULT FALSE,
    kindergarten BOOLEAN DEFAULT FALSE,
    other_programs BOOLEAN DEFAULT FALSE,
    other_programs_text TEXT DEFAULT 'N/A',
    held_back BOOLEAN DEFAULT FALSE,
    academic_performance academic_performance_enum DEFAULT 'Satisfactorio',
    special_ed BOOLEAN DEFAULT FALSE,
    special_ed_salon_recurso BOOLEAN DEFAULT FALSE,
    special_ed_salon_fulltime BOOLEAN DEFAULT FALSE,
    special_ed_other BOOLEAN DEFAULT FALSE,
    special_ed_other_text TEXT DEFAULT 'N/A',
    current_academic_performance TEXT DEFAULT 'N/A'
);

CREATE TYPE grade_enum AS ENUM (
    'Pre-K', 
    'Kindergarten', 
    '1er Grado', 
    '2do Grado', 
    '3er Grado', 
    '4to Grado', 
    '5to Grado', 
    '6to Grado', 
    '7mo Grado', 
    '8vo Grado', 
    '9no Grado', 
    '10mo Grado', 
    '11mo Grado', 
    '12mo Grado'
);
-- Table for held back grades
CREATE TABLE IF NOT EXISTS held_back_grades (
    held_back_grade_id SERIAL PRIMARY KEY,
    patient_id INTEGER REFERENCES patients(patient_id) ON DELETE CASCADE,
    grade grade_enum NOT NULL,
    times_failed INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS academic_difficulties (
    patient_id INTEGER PRIMARY KEY REFERENCES patients(patient_id) ON DELETE CASCADE,
    reading_difficulty BOOLEAN DEFAULT FALSE,
    writing_difficulty BOOLEAN DEFAULT FALSE,
    math_difficulty BOOLEAN DEFAULT FALSE,
    reading_comprehension_difficulty BOOLEAN DEFAULT FALSE,
    inverts_substitutes_reading_difficulty BOOLEAN DEFAULT FALSE,
    omits_reading_difficulty BOOLEAN DEFAULT FALSE,
    copy_writing_difficulty BOOLEAN DEFAULT FALSE,
    inverts_substitutes_writing_difficulty BOOLEAN DEFAULT FALSE,
    omits_writing_difficulty BOOLEAN DEFAULT FALSE,
    sum_substraction_math_difficulty BOOLEAN DEFAULT FALSE,
    multiplication_math_difficulty BOOLEAN DEFAULT FALSE,
    division_math_difficulty BOOLEAN DEFAULT FALSE,
    other_difficulties BOOLEAN DEFAULT FALSE,
    other_difficulties_text TEXT DEFAULT 'N/A'

);

-- Treatment table
CREATE TYPE weekly_frequency_type AS ENUM ('1x semanal', '2x semanal', '3x semanal', '4x semanal');
CREATE TYPE duration_type AS ENUM ('30 min', '45 min');
CREATE TYPE modality_type AS ENUM ('Individual', 'Grupal', 'Otra');
CREATE TYPE treatment_status_type AS ENUM ('Alta', 'Baja');
CREATE TABLE IF NOT EXISTS treatments (
    treatment_id SERIAL PRIMARY KEY,
    patient_id INTEGER REFERENCES patients(patient_id) ON DELETE CASCADE,
    treatment_type TEXT NOT NULL,
    weekly_frequency weekly_frequency_type NOT NULL,
    duration duration_type NOT NULL,
    modality modality_type NOT NULL,
    start_date DATE NOT NULL,
    status treatment_status_type NOT NULL
);

-- Personal relationships table
CREATE TYPE relationship_enum AS ENUM ('Adecuada', 'No adecuada', 'N/A');
CREATE TABLE IF NOT EXISTS personal_relationships(
    patient_id INTEGER PRIMARY KEY REFERENCES patients(patient_id) ON DELETE CASCADE,
    father_or_guardian_relationship relationship_enum DEFAULT 'N/A',
    sibling_relationship relationship_enum DEFAULT 'N/A',
    peer_group_relationship relationship_enum DEFAULT 'N/A',
    adult_relationship relationship_enum DEFAULT 'N/A',
    authority_relationship relationship_enum DEFAULT 'N/A'
);

-- Current health table
CREATE TABLE IF NOT EXISTS health_history (
    patient_id INTEGER PRIMARY KEY REFERENCES patients(patient_id) ON DELETE CASCADE,
    good_health BOOLEAN DEFAULT FALSE,
    visual_problems BOOLEAN DEFAULT FALSE,
    uses_glasses BOOLEAN DEFAULT FALSE,
    hearing_problems BOOLEAN DEFAULT FALSE,
    uses_hearing_aids BOOLEAN DEFAULT FALSE,
    neurological_problems BOOLEAN DEFAULT FALSE,
    motor_problems BOOLEAN DEFAULT FALSE,
    uses_wheelchair BOOLEAN DEFAULT FALSE,
    uses_prosthesis BOOLEAN DEFAULT FALSE,
    medical_treatment BOOLEAN DEFAULT FALSE,
    medical_treatment_text TEXT DEFAULT 'N/A',
    other_health_issues BOOLEAN DEFAULT False,
    other_health_issues_text TEXT  DEFAULT 'N/A'
);

-- Behavior history table
CREATE TABLE IF NOT EXISTS behavior_history (
    patient_id INTEGER PRIMARY KEY REFERENCES patients(patient_id) ON DELETE CASCADE,
    scared_to_go_to_school BOOLEAN DEFAULT FALSE,
    enuresis BOOLEAN DEFAULT FALSE,
    nervous_tic BOOLEAN DEFAULT FALSE,
    retraimiento BOOLEAN DEFAULT FALSE,
    encopresis BOOLEAN DEFAULT FALSE,
    sadness BOOLEAN DEFAULT FALSE,
    aggression BOOLEAN DEFAULT FALSE,
    nail_biting BOOLEAN DEFAULT FALSE,
    frequent_crying BOOLEAN DEFAULT FALSE,
    anxiety BOOLEAN DEFAULT FALSE,
    auto_aggression BOOLEAN DEFAULT FALSE,
    challenge_authority BOOLEAN DEFAULT FALSE,
    irritability BOOLEAN DEFAULT FALSE,
    defiant BOOLEAN DEFAULT FALSE,
    impulsivity BOOLEAN DEFAULT FALSE,
    other_behavioral_traits BOOLEAN DEFAULT FALSE,
    other_behavioral_traits_text TEXT DEFAULT 'N/A'
);

CREATE TYPE examination_method_type AS ENUM (
    'Escala de Inteligencia Wechsler para Preescolares (WPPSI-III)',
    'Escala de Inteligencia Wechsler para Niños-R-PR (EIWN-R PR)',
    'Escala de Inteligencia Wechsler para Niños (WISC-V Spanish)',
    'Escala de InteligenciaWechsler para Adultos-PR (EIWA-PR)',
    'Escala de InteligenciaWechsler para Adultos (EIWA-III)',
    'Escala de Inteligencia Stanford-Binet (5ta ed.)',
    'Prueba de Inteligencia No Verbal (TONI)',
    'Leiter International Performance Scale-No Verbal-3',
    'Escala Madurez Social Vineland 3',
    'Prueba de Integración Visomotora Berry (6 ta ed.)',
    'Prueba Percepción Visomotora Bender-Gestalt II',
    'Batería IV, Woodcock-Muñoz',
    'Prueba Conceptos Básicos Boehm',
    'Prueba de Matrices Progresivas Raven para Niños',
    'Prueba de Matrices Progresivas Raven para Adultos',
    'Escala de Clasificación Gilliam Autismo-GARS-3',
    'Prueba del Dibujo de la Figura Humana',
    'Prueba Dibujo Kinético de la Familia',
    'Prueba de Oraciones Incompletas',
    'Prueba del Dibujo Casa-Árbol-Persona',
    'Prueba Apercepción Temática (CAT-TAT)',
    'Inventario de Depresión Kovacs-CDI',
    'ADHD Rating Scale',
    'Cuestionario de Problemas (Est./Padres)',
    'Revisión del expediente',
    'Observaciones',
    'Entrevista a:',
    'Others:'
);
CREATE TYPE examiner_relationship_type AS ENUM ('Positiva', 'Pasiva', 'Negativa', 'Agresiva');
CREATE TYPE disposition_type AS ENUM ('Interesado', 'Desinteresado');
CREATE TYPE attention_level_type AS ENUM ('Apropiada', 'Disminuye gradualmente');
CREATE TYPE activity_level_type AS ENUM ('Apropiada', 'Aumenta gradualmente', 'Baja');
CREATE TYPE execution_level_type AS ENUM (
'Realiza las tareas en forma independiente y consistente', 
'Muestra interés e intenta realizar las tareas',
'No logra realizar las tareas'
);
CREATE TYPE laterality_type AS ENUM ('Derecha', 'Izquierda', 'Ambidiestro');
-- Table for storing evaluations
CREATE TABLE IF NOT EXISTS evaluations (
    evaluation_id SERIAL PRIMARY KEY,
    chronological_age_months INTEGER NOT NULL,
    patient_id INTEGER REFERENCES patients(patient_id) ON DELETE CASCADE,
    evaluation_date DATE NOT NULL,
    evaluator TEXT NOT NULL,
    Corporation TEXT NOT NULL
);

-- Table for storing examination results (with flexible structure) multiple per evaluation
CREATE TABLE IF NOT EXISTS examination_results (
    examination_result_id SERIAL PRIMARY KEY,
    evaluation_id INTEGER REFERENCES evaluations(evaluation_id) ON DELETE CASCADE,
    examination_method examination_method_type NOT NULL,
    result_data JSONB NOT NULL
);

CREATE TABLE IF NOT EXISTS evaluation_observed_conduct (
    evaluation_id INTEGER PRIMARY KEY REFERENCES evaluations(evaluation_id) ON DELETE CASCADE,
    colaborator BOOLEAN DEFAULT FALSE,
    organized BOOLEAN DEFAULT FALSE,
    motivated BOOLEAN DEFAULT FALSE,
    works_Fast BOOLEAN DEFAULT FALSE,
    impulsive BOOLEAN DEFAULT FALSE,
    negative BOOLEAN DEFAULT FALSE,
    careless BOOLEAN DEFAULT FALSE,
    disorganized BOOLEAN DEFAULT FALSE,
    hostile BOOLEAN DEFAULT FALSE,
    relationship_with_examiner examiner_relationship_type NOT NULL,
    disposition disposition_type NOT NULL,
    attention_level attention_level_type NOT NULL,
    activity_level activity_level_type NOT NULL,
    execution_level execution_level_type NOT NULL,
    laterality laterality_type NOT NULL,
    other_observations TEXT DEFAULT 'N/A'
);

-- Table for storing user details with hashed passwords
CREATE TYPE user_role_type AS ENUM ('ADMINISTRATOR', 'SECRETARY', 'EVALUATOR');
CREATE TABLE IF NOT EXISTS users (
    user_id SERIAL PRIMARY KEY,
    username TEXT NOT NULL UNIQUE,
    user_role user_role_type NOT NULL, 
    password_hash TEXT NOT NULL
);