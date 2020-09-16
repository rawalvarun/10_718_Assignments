
CREATE SCHEMA IF NOT EXISTS acs_2018_ass1_schema;

DROP TABLE IF EXISTS acs_2018_ass1_schema.acs_2018_ass1_table;

CREATE TABLE IF NOT EXISTS acs_2018_ass1_schema.acs_2018_ass1_table (
    state INTEGER NOT NULL,
    county INTEGER NOT NULL,
    tract INTEGER NOT NULL,
    Block_Group INTEGER NOT NULL,
    NAME VARCHAR NOT NULL,
    Unemployed INTEGER NOT NULL,
    Income INTEGER NOT NULL,
    WhiteRace INTEGER NOT NULL,
    BlackRace INTEGER NOT NULL,
    IndianAlaskanRace INTEGER NOT NULL,
    AsianRace INTEGER NOT NULL,
    Population INTEGER NOT NULL,
    MaleGender INTEGER NOT NULL,
    FemaleGender INTEGER NOT NULL,
    HighSchoolEducation INTEGER NOT NULL,
    College_Less_1yrEducation INTEGER NOT NULL,
    College_More_1YREducation INTEGER NOT NULL,
    AssociateDegreeEducation INTEGER NOT NULL,
    BachelorDegreeEducation INTEGER NOT NULL,
    MasterDegreeEducation INTEGER NOT NULL,
    ProfessionalDegreeEducation INTEGER NOT NULL,
    DoctorateDegreeEducation INTEGER NOT NULL
);

\COPY acs_2018_ass1_schema.acs_2018_ass1_table from 'acs5_2018.csv' WITH CSV HEADER;