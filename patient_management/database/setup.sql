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
    referal_from TEXT,
    post TEXT,
    history_origin BOOLEAN
);

-- Personal relationship history table
CREATE TYPE evo_history_origin_type AS ENUM ('entrevista', 'lectura de expediente');
CREATE TABLE IF NOT EXISTS evo_development (
    patient_id INTEGER PRIMARY KEY REFERENCES patients(patient_id) ON DELETE CASCADE,
    evo_history_origin evo_history_origin_type,
    mom_at_home BOOLEAN,
    dad_at_home BOOLEAN,
    siblings_at_home BOOLEAN, 
    grandparents_at_home BOOLEAN, 
    other_at_home TEXT,
    problems_at_home BOOLEAN
);

CREATE TABLE IF NOT EXISTS prenatal_history (
    patient_id INTEGER PRIMARY KEY REFERENCES patients(patient_id),
    prenatal_normal BOOLEAN,
    prenatal_falls BOOLEAN,
    prenatal_druguse BOOLEAN,
    prenatal_high_bp BOOLEAN,
    prenatal_bleeds BOOLEAN,
    prenatal_vomits BOOLEAN,
    prenatal_diabetes BOOLEAN,
    prenatal_accidents BOOLEAN,
    prenatal_meduse BOOLEAN,
    prenatal_other TEXT,
    prenatal_mothers_emotional_state TEXT,
    perinatal_natural BOOLEAN,
    perinatal_csection BOOLEAN,
    perinatal_premature BOOLEAN,
    perinatal_complications TEXT
);

CREATE TABLE IF NOT EXISTS postnatal_history(
    patient_id INTEGER PRIMARY KEY REFERENCES patients(patient_id),
    postnatal_normal BOOLEAN,
    postnatal_cianosis BOOLEAN,
    postnatal_meningitis BOOLEAN,
    postnatal_ictericia BOOLEAN,
    postnatal_seizures BOOLEAN,
    postnatal_incubator BOOLEAN,
    postnatal_incubator_time INTEGER,
    postnatal_other TEXT,
    weight_pounds DECIMAL(10,2),
    weight_oz DECIMAL(10,2),
    size_at_birth DECIMAL(10,2)
);

CREATE TYPE development_type AS ENUM ('Normal', 'Rápido', 'Lento');
CREATE TYPE activity_type AS ENUM ('Tranquilo', 'Inquieto', 'Hiperactivo', 'Hipoactivo');
CREATE TYPE activity_completion AS ENUM ('L', 'AN', 'NL');
CREATE TABLE IF NOT EXISTS development(
    patient_id INTEGER PRIMARY KEY REFERENCES patients(patient_id),
    psycholinguistic_development development_type,
    psycholinguistic_difficulty BOOLEAN,
    pshycholinguistic_difficulty_text TEXT,
    psychomotor_development development_type,
    psychomotor_difficulty BOOLEAN,
    psychomotor_difficulty_text TEXT,
    activity_level activity_type,
    turn_level activity_completion,
    sit_level activity_completion,
    crawl_level activity_completion,
    walk_level activity_completion,
    stand_with_support_level activity_completion,
    stand_without_support_level activity_completion,
    jump_with_one_foot_level activity_completion,
    jump_with_both_feet_level activity_completion,
    jump_and_play_level activity_completion
);

CREATE TABLE IF NOT EXISTS illnesses(
    patient_id INTEGER PRIMARY KEY REFERENCES patients(patient_id) ON DELETE CASCADE,
    illness_asma BOOLEAN,
    illness_pulmonia BOOLEAN,
    illness_fiebres BOOLEAN,
    illness_seizures BOOLEAN,
    illness_surgeries BOOLEAN,
    illness_diabetes BOOLEAN,
    illness_other_illnesses TEXT
);

CREATE TYPE academic_performance_enum AS ENUM('Satisfactorio', 'Regular', 'Deficiente');
-- Scholar history table
CREATE TABLE IF NOT EXISTS scholar_history (
    patient_id INTEGER PRIMARY KEY REFERENCES patients(patient_id) ON DELETE CASCADE,
    school TEXT,
    education_region TEXT,
    municipality TEXT,
    district TEXT,
    grade_group TEXT,
    head_start BOOLEAN,
    kindergarten BOOLEAN,
    other_programs TEXT,
    held_back BOOLEAN,
    academic_performance academic_performance_enum,
    special_ed BOOLEAN,
    special_ed_salon_recurso BOOLEAN,
    special_ed_salon_fulltime BOOLEAN,
    special_ed_other TEXT,
    current_academic_performance TEXT
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
    reading_difficulty BOOLEAN,
    writing_difficulty BOOLEAN,
    math_difficulty BOOLEAN,
    reading_comprehension_difficulty BOOLEAN,
    inverts_substitutes_reading_difficulty BOOLEAN,
    omits_reading_difficulty BOOLEAN,
    copy_writing_difficulty BOOLEAN,
    inverts_substitutes_writing_difficulty BOOLEAN,
    omits_writing_difficulty BOOLEAN,
    sum_substraction_math_difficulty BOOLEAN,
    multiplication_math_difficulty BOOLEAN,
    division_math_difficulty BOOLEAN,
    other_difficulties TEXT

);

-- Treatment table
CREATE TABLE IF NOT EXISTS treatments (
    treatment_id SERIAL PRIMARY KEY,
    patient_id INTEGER REFERENCES patients(patient_id) ON DELETE CASCADE,
    treatment_type TEXT NOT NULL,
    weekly_frequency INTEGER NOT NULL,
    duration INTEGER NOT NULL,
    modality TEXT NOT NULL,
    start_date TEXT NOT NULL,
    status TEXT NOT NULL
);

-- Personal relationships table
CREATE TYPE relationship_enum AS ENUM ('Adecuada', 'No adecuada');
CREATE TABLE IF NOT EXISTS personal_relationships(
    patient_id INTEGER PRIMARY KEY REFERENCES patients(patient_id) ON DELETE CASCADE,
    father_or_guardian_relationship relationship_enum,
    sibling_relationship relationship_enum,
    peer_group_relationship relationship_enum,
    adult_relationship relationship_enum,
    authority_relationship relationship_enum
);

-- Current health table
CREATE TABLE IF NOT EXISTS health_history (
    patient_id INTEGER PRIMARY KEY REFERENCES patients(patient_id) ON DELETE CASCADE,
    good_health BOOLEAN,
    visual_problems BOOLEAN,
    uses_glasses BOOLEAN,
    hearing_problems BOOLEAN,
    uses_hearing_aids BOOLEAN,
    neurological_problems BOOLEAN,
    motor_problems BOOLEAN,
    uses_wheelchair BOOLEAN,
    uses_prosthesis BOOLEAN,
    medical_treatment TEXT,
    other_health_issues TEXT
);

-- Behavior history table
CREATE TABLE IF NOT EXISTS behavior_history (
    patient_id INTEGER PRIMARY KEY REFERENCES patients(patient_id) ON DELETE CASCADE,
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
    other_behavioral_traits TEXT
);

CREATE TYPE evaluation_type AS ENUM (
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

-- Table for storing evaluations
CREATE TABLE IF NOT EXISTS evaluations (
    evaluation_id SERIAL PRIMARY KEY,
    chronological_age TEXT NOT NULL,
    patient_id INTEGER REFERENCES patients(patient_id) ON DELETE CASCADE,
    evaluation_type_id evaluation_type NOT NULL,
    evaluation_date DATE NOT NULL,
    evaluator TEXT NOT NULL,
    Corporation TEXT NOT NULL
);

-- Table for storing evaluation results (with flexible structure)
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
CREATE TABLE IF NOT EXISTS evaluation_results (
    evaluation_result_id SERIAL PRIMARY KEY,
    evaluation_id INTEGER REFERENCES evaluations(evaluation_id) ON DELETE CASCADE,
    result_data JSONB NOT NULL
);

CREATE TABLE IF NOT EXISTS evaluation_observed_conduct (
    evaluation_id INTEGER PRIMARY KEY REFERENCES evaluations(evaluation_id) ON DELETE CASCADE,
    colaborator BOOLEAN,
    organized BOOLEAN,
    motivated BOOLEAN,
    works_Fast BOOLEAN,
    impulsive BOOLEAN,
    negative BOOLEAN,
    careless BOOLEAN,
    disorganized BOOLEAN,
    hostile BOOLEAN
    relationship_with_examiner examiner_relationship_type NOT NULL,
    disposition disposition_type NOT NULL,
    attention_level attention_level_type NOT NULL,
    activity_level activity_level_type NOT NULL,
    execution_level execution_level_type NOT NULL,
    laterality laterality_type NOT NULL,
    other_observations TEXT
);

-- Table for storing user details with hashed passwords
CREATE TABLE IF NOT EXISTS users (
    user_id SERIAL PRIMARY KEY,
    username TEXT NOT NULL UNIQUE,
    password_hash TEXT NOT NULL
);