from sql.nano_survey_configuration.base_migration import BaseMigration
import collections

class MigrationScript(BaseMigration):
    """
        Academic Recovery Survey 2020-2021
    """
    sql = None
    sql_dictionary = None

    SURVEY_TEMPLATE_INTERNAL_KEY = 'recovery_20_21'

    # Purpose text
    SURVEY_WHY_TEXT = 'This survey helps collect information on academic behaviors and attitudes for students on probation to help focus conversations with these students. This survey adds additional questions focused on time management and understanding of the requirements of being on probation.'
    SURVEY_HOW_TEXT = 'This survey uses data from Mapworks to select questions that are tied to retention and academic success.'
    SURVEY_HOVER_TEXT = 'Survey for students on probation.'
    # All New questions - # before and # after
    SURVEY_QUESTION_ONE = ' To what degree are you keeping current with your academic work? '
    SURVEY_QUESTION_TWO = ' To what extent do you work harder in a course, when you get a poor grade? '
    SURVEY_QUESTION_THREE = ' How many of your scheduled classes have you attended this term? '
    SURVEY_QUESTION_FOUR = ' How many courses are you struggling in? '
    SURVEY_QUESTION_FIVE = " To what degree are you confident that you can pay for next term's tuition and fees? "
    SURVEY_QUESTION_SIX = ' To what degree do you intend to come back to this institution for the next academic term? '
    SURVEY_QUESTION_SEVEN = ' How would you rate your experience at this institution? '
    SURVEY_QUESTION_EIGHT = ' To what degree do you belong here? '
    SURVEY_QUESTION_NINE = ' To what degree are you experiencing stress because of COVID-19 health and safety concerns at your institution? '
    SURVEY_QUESTION_TEN = ' To what extent are you aware of the requirements for students on academic probation? '
    SURVEY_QUESTION_ELEVEN = ' How confident are you that you can raise your GPA to the necessary level? '
    SURVEY_QUESTION_TWELVE = ' To what extent do you plan to utilize the academic resources available (e.g., tutoring, writing support) at this institution this term? '
    SURVEY_QUESTION_THIRTEEN = ' In an average week, how many hours do you spend on out-of-classroom academic commitments (e.g., homework, studying, practice time)? '
    SURVEY_QUESTION_FOURTEEN = ' To what degree are you the kind of person who balances time between classes and other commitments (e.g., work, student activities)? '
    SURVEY_QUESTION_FIFTEEN = ' To what degree are you the kind of person who communicates with instructors outside of class? '

     # Categorical question options
    QUESTION_THREE_OPTION_ONE = 'I attended all my classes.'
    QUESTION_THREE_OPTION_TWO = 'I missed one class.'
    QUESTION_THREE_OPTION_THREE = 'I missed a few classes.'
    QUESTION_THREE_OPTION_FOUR = 'I missed class frequently.'
    QUESTION_THREE_OPTION_FIVE = 'I missed class most of the time.'
    QUESTION_FOUR_OPTION_ONE = 'Not struggling in any course'
    QUESTION_FOUR_OPTION_TWO = '1 course'
    QUESTION_FOUR_OPTION_THREE = '2 courses'
    QUESTION_FOUR_OPTION_FOUR = '3 courses'
    QUESTION_FOUR_OPTION_FIVE = '4 courses'
    QUESTION_FOUR_OPTION_SIX = '5 courses'
    QUESTION_FOUR_OPTION_SEVEN = 'More than 5 courses'
    QUESTION_THIRTEEN_OPTION_ONE = 'None'
    QUESTION_THIRTEEN_OPTION_TWO = '1 to 5 hours'
    QUESTION_THIRTEEN_OPTION_THREE = '6 to 10 hours'
    QUESTION_THIRTEEN_OPTION_FOUR = '11 to 15 hours'
    QUESTION_THIRTEEN_OPTION_FIVE = '16 to 20 hours'
    QUESTION_THIRTEEN_OPTION_SIX = '21 to 25 hours'
    QUESTION_THIRTEEN_OPTION_SEVEN = '26 to 30 hours'
    QUESTION_THIRTEEN_OPTION_EIGHT = '31 to 35 hours'
    QUESTION_THIRTEEN_OPTION_NINE = '36 to 40 hours'

    # Issue text for this template
    ISSUE_ACADEMIC_COURSEWORK = "Academic Coursework - Academic Recovery"
    ISSUE_ACADEMIC_RESILIENCE = "Academic Resilience - Academic Recovery"
    ISSUE_CLASS_ATTENDANCE = "Class Attendance - Missed class (self-report) - Academic Recovery"
    ISSUE_COURSE_STRUGGLES = "Course Struggles - Academic Recovery"
    ISSUE_FINANCIAL_MEANS = "Financial Means - Academic Recovery"
    ISSUE_INTENT_TO_RETURN = "Intent to Return - Academic Recovery"
    ISSUE_OVERALL_SATISFACTION = "Overall Satisfaction - Academic Recovery"
    ISSUE_SENSE_OF_BELONGING = "Sense of Belonging - Academic Recovery"
    ISSUE_HEALTH_RELATED_STRESS = "Health-Related Stress - Academic Recovery"
    ISSUE_PROBATION_REQUIREMENTS = "Probation Requirements - Academic Recovery"
    ISSUE_GPA_EXPECTATIONS = "GPA Expectations - Academic Recovery"
    ISSUE_UTILIZE_ACADEMIC_RESOURCES = "Utilize Academic Resources - Academic Recovery"
    ISSUE_STUDY_TIME = "Study Time - Academic Recovery"
    ISSUE_TIME_MANAGEMENT = "Time Management - Academic Recovery"
    ISSUE_INSTRUCTOR_COMMUNICATION = "Instructor Communication - Academic Recovery"

    # Talking Points
    QUESTION_ONE_TALKING_POINT_WEAKNESS = 'Student is struggling to stay current with coursework.'
    QUESTION_ONE_TALKING_POINT_STRENGTH = 'Student is up to date with coursework.'
    QUESTION_ONE_NEXT_STEPS = 'Help students understand the importance of completing assignments and required reading. Students may not understand the long term implications of poor preparedness on their academic success.'
    QUESTION_TWO_TALKING_POINT_WEAKNESS = 'Student may be deterred by academic setbacks.'
    QUESTION_TWO_TALKING_POINT_STRENGTH = 'Student persists on coursework despite setbacks.'
    QUESTION_TWO_NEXT_STEPS = 'Students with low academic resilience may need encouragement and support to persevere after poor performance in a class.'
    QUESTION_THREE_TALKING_POINT_WEAKNESS = 'Routinely misses classes (i.e., frequently or most of the time). Strong predictor of academic performance. Explore reasons for class absences.'
    QUESTION_THREE_TALKING_POINT_STRENGTH = 'Reports having attended every class to date.'
    QUESTION_THREE_NEXT_STEPS = 'Routinely misses classes is a strong predictor of academic performance. Students transitioning to college may enjoy the freedom of their schedule and may need assistance understanding the importance of attending class.'
    QUESTION_FOUR_TALKING_POINT_WEAKNESS = 'Struggling in two or more courses. Strong predictor of poor academic performance. Discuss issues, encourage meeting with instructors, and refer to learning resources.'
    QUESTION_FOUR_TALKING_POINT_STRENGTH = 'Reports no serious course difficulties at this time.'
    QUESTION_FOUR_NEXT_STEPS = 'Students report struggling in at least one course. Communicate the academic resources available to these students.'
    QUESTION_FIVE_TALKING_POINT_WEAKNESS = "Expects difficulties paying next term's tuition/fees. Refer to Financial Aid."
    QUESTION_FIVE_NEXT_STEPS = 'Students who lack confidence to pay their tuition and fees may experience stress from upcoming bills and may need support. Ensure students know about the financial aid office and services available to them.'
    QUESTION_SIX_TALKING_POINT_WEAKNESS = 'Student is unlikely to return next term. This response is a strong predictor of attrition.'
    QUESTION_SIX_TALKING_POINT_STRENGTH = 'Student intends to return next term.'
    QUESTION_SIX_NEXT_STEPS = "Students who say they don't intend to return, often don't. Intervening with these students may help them to continue their education."
    QUESTION_SEVEN_TALKING_POINT_WEAKNESS = 'Student reports low satisfaction with the institution.'
    QUESTION_SEVEN_TALKING_POINT_STRENGTH = 'Student reports high satisfaction with this institution.'
    QUESTION_SEVEN_NEXT_STEPS = 'Dissatisfaction with the institution is correlated with lower retention. Identifying the cause of their dissatisfaction may help retain the student at the institution.'
    QUESTION_EIGHT_TALKING_POINT_WEAKNESS = "Doesn't feel he/she belongs at this school. Strong predictor of attrition. Explore issue(s), discuss getting involved in student organizations."
    QUESTION_EIGHT_TALKING_POINT_STRENGTH = 'Feels he/she belongs at this school. Strong predictor of retention.'
    QUESTION_EIGHT_NEXT_STEPS = 'Help students make connections to peers and organizations on campus and in the community.'
    QUESTION_NINE_TALKING_POINT_WEAKNESS = 'This student is experience stress related to COVID-19 and attending this institution. Ensure this student knows what the institution is doing to ensure health and safety.'
    QUESTION_NINE_TALKING_POINT_STRENGTH = 'Student does not report stress related to attending class amid the changes caused by COVID-19.'
    QUESTION_NINE_NEXT_STEPS = 'Keep students informed about what the institution is doing to keep the campus community safe. Students may need support or feel heard about concerns.'
    QUESTION_TEN_TALKING_POINT_WEAKNESS = 'This student is unclear of the requirements of being on academic probation.'
    QUESTION_TEN_NEXT_STEPS = "Students may not understand the requirements or consequences of being on academic probation. Meet with students to clarify what's at stake, what action the student needs to take, and what resources are available to help them."
    QUESTION_ELEVEN_TALKING_POINT_WEAKNESS = 'Student does not believe they can achieve a GPA necessary to meet probation requirements.'
    QUESTION_ELEVEN_TALKING_POINT_STRENGTH = 'Student believes they will be able to increase their GPA.'
    QUESTION_ELEVEN_NEXT_STEPS = 'Students sometimes discount previous academic struggles and overpredict their ability to succeed in current or future courses. Students may need assistance in setting and meeting their academic goals.'
    QUESTION_TWELEVE_TALKING_POINT_WEAKNESS = 'Student does not plan to use campus resources.'
    QUESTION_TWELVE_TALKING_POINT_STRENGTH = 'Student plans to use campus resources.'
    QUESTION_TWELEVE_NEXT_STEPS = 'Students may need help understanding what resources are available and how using those resources can positively contribute to their academic success.'
    QUESTION_THIRTEEN_TALKING_POINT_WEAKNESS = 'Student plans to spend less than 10 hours a week on academic work outside of attending class.'
    QUESTION_THIRTEEN_TALKING_POINT_STRENGTH = 'Student plans to spend at least 20 hours a week on academics outside of class.'
    QUESTION_THIRTEEN_NEXT_STEPS = 'Students may need to allocate additional time to completing their coursework, especially if courses are more rigorous than they are accustomed to. Students who did not previously need to study may need help learning positive study behaviors.'
    QUESTION_FOURTEEN_TALKING_POINT_WEAKNESS = 'Student reports poor time management skills.'
    QUESTION_FOURTEEN_TALKING_POINT_STRENGTH = 'Student reports positive time management skills.'
    QUESTION_FOURTEEN_NEXT_STEPS = 'Students have many obligations competing for their time and attention. The ability to successfully balance competing needs can be a difficult skill for students to develop. Students struggling may need help priortizing their time.'
    QUESTION_FIFTEEN_TALKING_POINT_WEAKNESS = 'Student does not communicate with instructors outside of class.'
    QUESTION_FIFTEEN_TALKING_POINT_STRENGTH = 'Student reports communicating with instructors outside of class.'
    QUESTION_FIFTEEN_NEXT_STEPS = 'Asking instructors for help or clarification can feel daunting to some students. Proactive communication with instructors about questions and challenges with the course material can help the student be successful in their course.'

    #Do we need a consent statement?

    def __init__(self):
        super().__init__()
        self.sql = {
            1: f"""
                INSERT INTO nano_survey_configuration.survey_template (title, internal_key, hover_text, time_to_complete, user_data_consent_statement, created_by, modified_by) VALUES
                ('Academic Recovery Survey 2020-2021', '{self.SURVEY_TEMPLATE_INTERNAL_KEY}', '{self.SURVEY_HOVER_TEXT}', 7, "{self.CONSENT_STATEMENT}", 2, 2);
            """,
            3: f"""
                INSERT INTO nano_survey_configuration.question_bank (question_text, alternate_question_text, question_type, created_by, modified_by) VALUES
                ('{self.SURVEY_QUESTION_ONE}', '', '{self.TEXT_SCALED}', 2, 2),
                ('{self.SURVEY_QUESTION_TWO}', '', '{self.TEXT_SCALED}', 2, 2),
                ('{self.SURVEY_QUESTION_THREE}', '', '{self.TEXT_CATEGORICAL}', 2, 2),
                ('{self.SURVEY_QUESTION_FOUR}', '', '{self.TEXT_CATEGORICAL}', 2, 2),
                ("{self.SURVEY_QUESTION_FIVE}", '', '{self.TEXT_SCALED}', 2, 2),
                ('{self.SURVEY_QUESTION_SIX}', '', '{self.TEXT_SCALED}', 2, 2),
                ('{self.SURVEY_QUESTION_SEVEN}', '', '{self.TEXT_SCALED}', 2, 2),
                ('{self.SURVEY_QUESTION_EIGHT}', '', '{self.TEXT_SCALED}', 2, 2),
                ('{self.SURVEY_QUESTION_NINE}', '', '{self.TEXT_SCALED}', 2, 2),
                ('{self.SURVEY_QUESTION_TEN}', '', '{self.TEXT_SCALED}', 2, 2),
                ('{self.SURVEY_QUESTION_ELEVEN}', '', '{self.TEXT_SCALED}', 2, 2),
                ('{self.SURVEY_QUESTION_TWELVE}', '', '{self.TEXT_SCALED}', 2, 2),
                ('{self.SURVEY_QUESTION_THIRTEEN}', '', '{self.TEXT_CATEGORICAL}', 2, 2),
                ('{self.SURVEY_QUESTION_FOURTEEN}', '', '{self.TEXT_SCALED}', 2, 2),
                ('{self.SURVEY_QUESTION_FIFTEEN}', '', '{self.TEXT_SCALED}', 2, 2);
                """,
            4: f"""
                INSERT INTO nano_survey_configuration.question_bank_option (question_bank_id, option_value, additional_text, option_type, created_by, modified_by) VALUES
                (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_ONE}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.NUMERICAL_OPTION_ONE}',
                    'Not at All',
                    '{self.TYPE_INTEGER}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_ONE}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.NUMERICAL_OPTION_TWO}',
                    null,
                    '{self.TYPE_INTEGER}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_ONE}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.NUMERICAL_OPTION_THREE}',
                    null,
                    '{self.TYPE_INTEGER}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_ONE}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.NUMERICAL_OPTION_FOUR}',
                    null,
                    '{self.TYPE_INTEGER}',
                    2,
                    2
                ),
                 (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_ONE}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.NUMERICAL_OPTION_FIVE}',
                    null,
                    '{self.TYPE_INTEGER}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_ONE}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.NUMERICAL_OPTION_SIX}',
                    null,
                    '{self.TYPE_INTEGER}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_ONE}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.NUMERICAL_OPTION_SEVEN}',
                    'Extremely',
                    '{self.TYPE_INTEGER}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_ONE}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.NUMERICAL_OPTION_99}',
                    'Not Applicable',
                    '{self.TYPE_INTEGER}',
                    2,
                    2
                ),
                # question two
                (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_TWO}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.NUMERICAL_OPTION_ONE}',
                    null,
                    '{self.TYPE_INTEGER}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_TWO}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.NUMERICAL_OPTION_TWO}',
                    null,
                    '{self.TYPE_INTEGER}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_TWO}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.NUMERICAL_OPTION_THREE}',
                    null,
                    '{self.TYPE_INTEGER}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_TWO}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.NUMERICAL_OPTION_FOUR}',
                    null,
                    '{self.TYPE_INTEGER}',
                    2,
                    2
                ),
                 (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_TWO}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.NUMERICAL_OPTION_FIVE}',
                    null,
                    '{self.TYPE_INTEGER}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_TWO}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.NUMERICAL_OPTION_SIX}',
                    null,
                    '{self.TYPE_INTEGER}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_TWO}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.NUMERICAL_OPTION_SEVEN}',
                    'Extremely',
                    '{self.TYPE_INTEGER}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_TWO}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.NUMERICAL_OPTION_99}',
                    'Not Applicable',
                    '{self.TYPE_INTEGER}',
                    2,
                    2
                ),
                 # question three
                (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_THREE}' AND question_type = '{self.TEXT_CATEGORICAL}'),
                    '{self.QUESTION_THREE_OPTION_ONE}',
                    null
                    '{self.TYPE_STRING}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_THREE}' AND question_type = '{self.TEXT_CATEGORICAL}'),
                    '{self.QUESTION_THREE_OPTION_TWO}',
                    null,
                    '{self.TYPE_STRING}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_THREE}' AND question_type = '{self.TEXT_CATEGORICAL}'),
                    '{self.QUESTION_THREE_OPTION_THREE}',
                    null,
                    '{self.TYPE_STRING}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_THREE}' AND question_type = '{self.TEXT_CATEGORICAL}'),
                    '{self.QUESTION_THREE_OPTION_FOUR}',
                    null,
                    '{self.TYPE_STRING}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_THREE}' AND question_type = '{self.TEXT_CATEGORICAL}'),
                    '{self.QUESTION_THREE_OPTION_FIVE}',
                    null,
                    '{self.TYPE_STRING}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_THREE}' AND question_type = '{self.TEXT_CATEGORICAL}'),
                    '{self.NUMERICAL_OPTION_99}',
                    'Not Applicable',
                    '{self.TYPE_STRING}',
                    2,
                    2
                ),
                # question four
                (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_FOUR}' AND question_type = '{self.TEXT_CATEGORICAL}'),
                    '{self.QUESTION_FOUR_OPTION_ONE}',
                    null
                    '{self.TYPE_STRING}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_FOUR}' AND question_type = '{self.TEXT_CATEGORICAL}'),
                    '{self.QUESTION_FOUR_OPTION_TWO}',
                    null,
                    '{self.TYPE_STRING}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_FOUR}' AND question_type = '{self.TEXT_CATEGORICAL}'),
                    '{self.QUESTION_FOUR_OPTION_THREE}',
                    null,
                    '{self.TYPE_STRING}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_FOUR}' AND question_type = '{self.TEXT_CATEGORICAL}'),
                    '{self.QUESTION_FOUR_OPTION_FOUR}',
                    null,
                    '{self.TYPE_STRING}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_FOUR}' AND question_type = '{self.TEXT_CATEGORICAL}'),
                    '{self.QUESTION_FOUR_OPTION_FIVE}',
                    null,
                    '{self.TYPE_STRING}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_FOUR}' AND question_type = '{self.TEXT_CATEGORICAL}'),
                    '{self.QUESTION_FOUR_OPTION_SIX}',
                    null,
                    '{self.TYPE_STRING}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_FOUR}' AND question_type = '{self.TEXT_CATEGORICAL}'),
                    '{self.QUESTION_FOUR_OPTION_SEVEN}',
                    null,
                    '{self.TYPE_STRING}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_FOUR}' AND question_type = '{self.TEXT_CATEGORICAL}'),
                    '{self.NUMERICAL_OPTION_99}',
                    'Not Applicable',
                    '{self.TYPE_STRING}',
                    2,
                    2
                ),
                # question five
                (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = "{self.SURVEY_QUESTION_FIVE}" AND question_type = '{self.TEXT_SCALED}'),
                    '{self.NUMERICAL_OPTION_ONE}',
                    'Not at All',
                    '{self.TYPE_INTEGER}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = "{self.SURVEY_QUESTION_FIVE}" AND question_type = '{self.TEXT_SCALED}'),
                    '{self.NUMERICAL_OPTION_TWO}',
                    null,
                    '{self.TYPE_INTEGER}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = "{self.SURVEY_QUESTION_FIVE}" AND question_type = '{self.TEXT_SCALED}'),
                    '{self.NUMERICAL_OPTION_THREE}',
                    null,
                    '{self.TYPE_INTEGER}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = "{self.SURVEY_QUESTION_FIVE}" AND question_type = '{self.TEXT_SCALED}'),
                    '{self.NUMERICAL_OPTION_FOUR}',
                    null,
                    '{self.TYPE_INTEGER}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = "{self.SURVEY_QUESTION_FIVE}" AND question_type = '{self.TEXT_SCALED}'),
                    '{self.NUMERICAL_OPTION_FIVE}',
                    null,
                    '{self.TYPE_INTEGER}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = "{self.SURVEY_QUESTION_FIVE}" AND question_type = '{self.TEXT_SCALED}'),
                    '{self.NUMERICAL_OPTION_SIX}',
                    null,
                    '{self.TYPE_INTEGER}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = "{self.SURVEY_QUESTION_FIVE}" AND question_type = '{self.TEXT_SCALED}'),
                    '{self.NUMERICAL_OPTION_SEVEN}',
                    'Extremely',
                    '{self.TYPE_INTEGER}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = "{self.SURVEY_QUESTION_FIVE}" AND question_type = '{self.TEXT_SCALED}'),
                    '{self.NUMERICAL_OPTION_99}',
                    'Not Applicable',
                    '{self.TYPE_INTEGER}',
                    2,
                    2
                ),
                # question six
                 (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_SIX}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.NUMERICAL_OPTION_ONE}',
                    'Not at All',
                    '{self.TYPE_INTEGER}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_SIX}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.NUMERICAL_OPTION_TWO}',
                    null,
                    '{self.TYPE_INTEGER}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_SIX}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.NUMERICAL_OPTION_THREE}',
                    null,
                    '{self.TYPE_INTEGER}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_SIX}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.NUMERICAL_OPTION_FOUR}',
                    null,
                    '{self.TYPE_INTEGER}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_SIX}'  AND question_type = '{self.TEXT_SCALED}'),
                    '{self.NUMERICAL_OPTION_FIVE}',
                    null,
                    '{self.TYPE_INTEGER}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_SIX}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.NUMERICAL_OPTION_SIX}',
                    null,
                    '{self.TYPE_INTEGER}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_SIX}'  AND question_type = '{self.TEXT_SCALED}'),
                    '{self.NUMERICAL_OPTION_SEVEN}',
                    'Extremely',
                    '{self.TYPE_INTEGER}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_SIX}'  AND question_type = '{self.TEXT_SCALED}'),
                    '{self.NUMERICAL_OPTION_99}',
                    'Not Applicable',
                    '{self.TYPE_INTEGER}',
                    2,
                    2
                ),
                # question seven
                (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_SEVEN}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.NUMERICAL_OPTION_ONE}',
                    'Very Poor',
                    '{self.TYPE_INTEGER}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_SEVEN}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.NUMERICAL_OPTION_TWO}',
                    null,
                    '{self.TYPE_INTEGER}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_SEVEN}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.NUMERICAL_OPTION_THREE}',
                    null,
                    '{self.TYPE_INTEGER}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_SEVEN}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.NUMERICAL_OPTION_FOUR}',
                    null,
                    '{self.TYPE_INTEGER}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_SEVEN}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.NUMERICAL_OPTION_FIVE}',
                    null,
                    '{self.TYPE_INTEGER}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_SEVEN}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.NUMERICAL_OPTION_SIX}',
                    null,
                    '{self.TYPE_INTEGER}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_SEVEN}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.NUMERICAL_OPTION_SEVEN}',
                    'Exceptional',
                    '{self.TYPE_INTEGER}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_SEVEN}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.NUMERICAL_OPTION_99}',
                    'Not Applicable',
                    '{self.TYPE_INTEGER}',
                    2,
                    2
                ),
                # question eight
                (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_EIGHT}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.NUMERICAL_OPTION_ONE}',
                    'Not at All',
                    '{self.TYPE_INTEGER}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_EIGHT}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.NUMERICAL_OPTION_TWO}',
                    null,
                    '{self.TYPE_INTEGER}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_EIGHT}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.NUMERICAL_OPTION_THREE}',
                    null,
                    '{self.TYPE_INTEGER}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_EIGHT}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.NUMERICAL_OPTION_FOUR}',
                    null,
                    '{self.TYPE_INTEGER}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_EIGHT}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.NUMERICAL_OPTION_FIVE}',
                    null,
                    '{self.TYPE_INTEGER}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_EIGHT}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.NUMERICAL_OPTION_SIX}',
                    null,
                    '{self.TYPE_INTEGER}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_EIGHT}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.NUMERICAL_OPTION_SEVEN}',
                    'Extremely',
                    '{self.TYPE_INTEGER}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_EIGHT}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.NUMERICAL_OPTION_99}',
                    'Not Applicable',
                    '{self.TYPE_INTEGER}',
                    2,
                    2
                ),
                # question nine
                (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_NINE}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.NUMERICAL_OPTION_ONE}',
                    'Not at All',
                    '{self.TYPE_INTEGER}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_NINE}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.NUMERICAL_OPTION_TWO}',
                    null,
                    '{self.TYPE_INTEGER}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_NINE}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.NUMERICAL_OPTION_THREE}',
                    null,
                    '{self.TYPE_INTEGER}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_NINE}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.NUMERICAL_OPTION_FOUR}',
                    null,
                    '{self.TYPE_INTEGER}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_NINE}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.NUMERICAL_OPTION_FIVE}',
                    null,
                    '{self.TYPE_INTEGER}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_NINE}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.NUMERICAL_OPTION_SIX}',
                    null,
                    '{self.TYPE_INTEGER}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_NINE}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.NUMERICAL_OPTION_SEVEN}',
                    'Extremely',
                    '{self.TYPE_INTEGER}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_NINE}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.NUMERICAL_OPTION_99}',
                    'Not Applicable',
                    '{self.TYPE_INTEGER}',
                    2,
                    2
                ),
                # question ten
                (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_TEN}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.NUMERICAL_OPTION_ONE}',
                    'Not at All',
                    '{self.TYPE_INTEGER}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_TEN}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.NUMERICAL_OPTION_TWO}',
                    null,
                    '{self.TYPE_INTEGER}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_TEN}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.NUMERICAL_OPTION_THREE}',
                    null,
                    '{self.TYPE_INTEGER}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_TEN}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.NUMERICAL_OPTION_FOUR}',
                    null,
                    '{self.TYPE_INTEGER}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_TEN}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.NUMERICAL_OPTION_FIVE}',
                    null,
                    '{self.TYPE_INTEGER}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_TEN}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.NUMERICAL_OPTION_SIX}',
                    null,
                    '{self.TYPE_INTEGER}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_TEN}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.NUMERICAL_OPTION_SEVEN}',
                    'Extremely',
                    '{self.TYPE_INTEGER}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_TEN}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.NUMERICAL_OPTION_99}',
                    'Not Applicable',
                    '{self.TYPE_INTEGER}',
                    2,
                    2
                ),
                # question eleven
                (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_ELEVEN}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.NUMERICAL_OPTION_ONE}',
                    'Not at All',
                    '{self.TYPE_INTEGER}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_ELEVEN}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.NUMERICAL_OPTION_TWO}',
                    null,
                    '{self.TYPE_INTEGER}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_ELEVEN}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.NUMERICAL_OPTION_THREE}',
                    null,
                    '{self.TYPE_INTEGER}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_ELEVEN}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.NUMERICAL_OPTION_FOUR}',
                    null,
                    '{self.TYPE_INTEGER}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_ELEVEN}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.NUMERICAL_OPTION_FIVE}',
                    null,
                    '{self.TYPE_INTEGER}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_ELEVEN}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.NUMERICAL_OPTION_SIX}',
                    null,
                    '{self.TYPE_INTEGER}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_ELEVEN}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.NUMERICAL_OPTION_SEVEN}',
                    'Extremely',
                    '{self.TYPE_INTEGER}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_ELEVEN}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.NUMERICAL_OPTION_99}',
                    'Not Applicable',
                    '{self.TYPE_INTEGER}',
                    2,
                    2
                ),
                # question twelve
                (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_TWELVE}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.NUMERICAL_OPTION_ONE}',
                    'Not at All',
                    '{self.TYPE_INTEGER}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_TWELVE}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.NUMERICAL_OPTION_TWO}',
                    null,
                    '{self.TYPE_INTEGER}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_TWELVE}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.NUMERICAL_OPTION_THREE}',
                    null,
                    '{self.TYPE_INTEGER}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_TWELVE}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.NUMERICAL_OPTION_FOUR}',
                    null,
                    '{self.TYPE_INTEGER}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_TWELVE}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.NUMERICAL_OPTION_FIVE}',
                    null,
                    '{self.TYPE_INTEGER}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_ELEVEN}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.NUMERICAL_OPTION_SIX}',
                    null,
                    '{self.TYPE_INTEGER}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_TWELVE}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.NUMERICAL_OPTION_SEVEN}',
                    'Extremely',
                    '{self.TYPE_INTEGER}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_TWELVE}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.NUMERICAL_OPTION_99}',
                    'Not Applicable',
                    '{self.TYPE_INTEGER}',
                    2,
                    2
                ),
                # question thirteen
                 (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_THIRTEEN}' AND question_type = '{self.TEXT_CATEGORICAL}'),
                    '{self.QUESTION_THIRTEEN_OPTION_ONE}',
                    null
                    '{self.TYPE_STRING}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_THIRTEEN}' AND question_type = '{self.TEXT_CATEGORICAL}'),
                    '{self.QUESTION_THIRTEEN_OPTION_TWO}',
                    null,
                    '{self.TYPE_STRING}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_THIRTEEN}' AND question_type = '{self.TEXT_CATEGORICAL}'),
                    '{self.QUESTION_THIRTEEN_OPTION_THREE}',
                    null,
                    '{self.TYPE_STRING}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_THIRTEEN}' AND question_type = '{self.TEXT_CATEGORICAL}'),
                    '{self.QUESTION_THIRTEEN_OPTION_FOUR}',
                    null,
                    '{self.TYPE_STRING}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_THIRTEEN}' AND question_type = '{self.TEXT_CATEGORICAL}'),
                    '{self.QUESTION_THIRTEEN_OPTION_FIVE}',
                    null,
                    '{self.TYPE_STRING}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_THIRTEEN}' AND question_type = '{self.TEXT_CATEGORICAL}'),
                    '{self.QUESTION_THIRTEEN_OPTION_SIX}',
                    null,
                    '{self.TYPE_STRING}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_THIRTEEN}' AND question_type = '{self.TEXT_CATEGORICAL}'),
                    '{self.QUESTION_THIRTEEN_OPTION_SEVEN}',
                    null,
                    '{self.TYPE_STRING}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_THIRTEEN}' AND question_type = '{self.TEXT_CATEGORICAL}'),
                    '{self.QUESTION_THIRTEEN_OPTION_EIGHT}',
                    null,
                    '{self.TYPE_STRING}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_THIRTEEN}' AND question_type = '{self.TEXT_CATEGORICAL}'),
                    '{self.QUESTION_THIRTEEN_OPTION_NINE}',
                    'null',
                    '{self.TYPE_STRING}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_THIRTEEN}' AND question_type = '{self.TEXT_CATEGORICAL}'),
                    '{self.NUMERICAL_OPTION_99}',
                    'Not Applicable',
                    '{self.TYPE_STRING}',
                    2,
                    2
                ),
                # question fourteen
                (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_FOURTEEN}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.NUMERICAL_OPTION_ONE}',
                    'Not at All',
                    '{self.TYPE_INTEGER}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_FOURTEEN}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.NUMERICAL_OPTION_TWO}',
                    null,
                    '{self.TYPE_INTEGER}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_FOURTEEN}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.NUMERICAL_OPTION_THREE}',
                    null,
                    '{self.TYPE_INTEGER}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_FOURTEEN}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.NUMERICAL_OPTION_FOUR}',
                    null,
                    '{self.TYPE_INTEGER}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_FOURTEEN}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.NUMERICAL_OPTION_FIVE}',
                    null,
                    '{self.TYPE_INTEGER}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_FOURTEEN}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.NUMERICAL_OPTION_SIX}',
                    null,
                    '{self.TYPE_INTEGER}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_FOURTEEN}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.NUMERICAL_OPTION_SEVEN}',
                    'Extremely',
                    '{self.TYPE_INTEGER}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_FOURTEEN}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.NUMERICAL_OPTION_99}',
                    'Not Applicable',
                    '{self.TYPE_INTEGER}',
                    2,
                    2
                ),
                # question fifteen
                (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_FIFTEEN}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.NUMERICAL_OPTION_ONE}',
                    'Not at All',
                    '{self.TYPE_INTEGER}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_FIFTEEN}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.NUMERICAL_OPTION_TWO}',
                    null,
                    '{self.TYPE_INTEGER}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_FIFTEEN}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.NUMERICAL_OPTION_THREE}',
                    null,
                    '{self.TYPE_INTEGER}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_FIFTEEN}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.NUMERICAL_OPTION_FOUR}',
                    null,
                    '{self.TYPE_INTEGER}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_FIFTEEN}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.NUMERICAL_OPTION_FIVE}',
                    null,
                    '{self.TYPE_INTEGER}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_FIFTEEN}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.NUMERICAL_OPTION_SIX}',
                    null,
                    '{self.TYPE_INTEGER}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_FIFTEEN}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.NUMERICAL_OPTION_SEVEN}',
                    'Extremely',
                    '{self.TYPE_INTEGER}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_FIFTEEN}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.NUMERICAL_OPTION_99}',
                    'Not Applicable',
                    '{self.TYPE_INTEGER}',
                    2,
                    2
                );
            """,

            5: f"""
                INSERT INTO nano_survey_configuration.issue (reporting_category_id, question_bank_id, issue_text, issue_type, created_by, modified_by) VALUES
                (
                    (SELECT id FROM nano_survey_configuration.reporting_category WHERE text = '{self.REPORTING_CATEGORY_ACADEMIC}'),
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_ONE}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.ISSUE_ACADEMIC_COURSEWORK}',
                    '{self.ISSUE_TYPE_WEAKNESS}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.reporting_category WHERE text = '{self.REPORTING_CATEGORY_ACADEMIC}'),
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_ONE}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.ISSUE_ACADEMIC_COURSEWORK}',
                    '{self.ISSUE_TYPE_STRENGTH}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.reporting_category WHERE text = '{self.REPORTING_CATEGORY_ACADEMIC}'),
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_TWO}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.ISSUE_ACADEMIC_RESILIENCE}',
                    '{self.ISSUE_TYPE_WEAKNESS}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.reporting_category WHERE text = '{self.REPORTING_CATEGORY_ACADEMIC}'),
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_TWO}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.ISSUE_ACADEMIC_RESILIENCE}',
                    '{self.ISSUE_TYPE_STRENGTH}',
                    2,
                    2
                ),
                 (
                    (SELECT id FROM nano_survey_configuration.reporting_category WHERE text = '{self.REPORTING_CATEGORY_ACADEMIC}'),
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_THREE}' AND question_type = '{self.TEXT_CATEGORICAL}'),
                    '{self.ISSUE_CLASS_ATTENDANCE}',
                    '{self.ISSUE_TYPE_WEAKNESS}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.reporting_category WHERE text = '{self.REPORTING_CATEGORY_ACADEMIC}'),
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_THREE}' AND question_type = '{self.TEXT_CATEGORICAL}'),
                    '{self.ISSUE_CLASS_ATTENDANCE}',
                    '{self.ISSUE_TYPE_STRENGTH}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.reporting_category WHERE text = '{self.REPORTING_CATEGORY_ACADEMIC}'),
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_FOUR}' AND question_type = '{self.TEXT_CATEGORICAL}'),
                    '{self.ISSUE_COURSE_STRUGGLES}',
                    '{self.ISSUE_TYPE_WEAKNESS}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.reporting_category WHERE text = '{self.REPORTING_CATEGORY_ACADEMIC}'),
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_FOUR}' AND question_type = '{self.TEXT_CATEGORICAL}'),
                    '{self.ISSUE_COURSE_STRUGGLES}',
                    '{self.ISSUE_TYPE_STRENGTH}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.reporting_category WHERE text = '{self.REPORTING_CATEGORY_FINANCIAL}'),
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = "{self.SURVEY_QUESTION_FIVE}" AND question_type = '{self.TEXT_SCALED}'),
                    '{self.ISSUE_FINANCIAL_MEANS}',
                    '{self.ISSUE_TYPE_WEAKNESS}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.reporting_category WHERE text = '{self.REPORTING_CATEGORY_INSTITUTIONAL}'),
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_SIX}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.ISSUE_INTENT_TO_RETURN}',
                    '{self.ISSUE_TYPE_WEAKNESS}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.reporting_category WHERE text = '{self.REPORTING_CATEGORY_INSTITUTIONAL}'),
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_SIX}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.ISSUE_INTENT_TO_RETURN}',
                    '{self.ISSUE_TYPE_STRENGTH}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.reporting_category WHERE text = '{self.REPORTING_CATEGORY_INSTITUTIONAL}'),
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_SEVEN}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.ISSUE_OVERALL_SATISFACTION}',
                    '{self.ISSUE_TYPE_WEAKNESS}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.reporting_category WHERE text = '{self.REPORTING_CATEGORY_INSTITUTIONAL}'),
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_SEVEN}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.ISSUE_OVERALL_SATISFACTION}',
                    '{self.ISSUE_TYPE_STRENGTH}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.reporting_category WHERE text = '{self.REPORTING_CATEGORY_SOCIAL}'),
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_EIGHT}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.ISSUE_SENSE_OF_BELONGING}',
                    '{self.ISSUE_TYPE_WEAKNESS}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.reporting_category WHERE text = '{self.REPORTING_CATEGORY_SOCIAL}'),
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_EIGHT}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.ISSUE_SENSE_OF_BELONGING}',
                    '{self.ISSUE_TYPE_STRENGTH}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.reporting_category WHERE text = '{self.REPORTING_CATEGORY_INSTITUTIONAL}'),
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_NINE}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.ISSUE_HEALTH_RELATED_STRESS}',
                    '{self.ISSUE_TYPE_WEAKNESS}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.reporting_category WHERE text = '{self.REPORTING_CATEGORY_INSTITUTIONAL}'),
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_NINE}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.ISSUE_HEALTH_RELATED_STRESS}',
                    '{self.ISSUE_TYPE_STRENGTH}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.reporting_category WHERE text = '{self.REPORTING_CATEGORY_ACADEMIC}'),
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_TEN}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.ISSUE_PROBATION_REQUIREMENTS}',
                    '{self.ISSUE_TYPE_WEAKNESS}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.reporting_category WHERE text = '{self.REPORTING_CATEGORY_ACADEMIC}'),
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_ELEVEN}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.ISSUE_GPA_EXPECTATIONS}',
                    '{self.ISSUE_TYPE_WEAKNESS}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.reporting_category WHERE text = '{self.REPORTING_CATEGORY_ACADEMIC}'),
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_ELEVEN}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.ISSUE_GPA_EXPECTATIONS}',
                    '{self.ISSUE_TYPE_STRENGTH}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.reporting_category WHERE text = '{self.REPORTING_CATEGORY_ACADEMIC}'),
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_TWELVE}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.ISSUE_UTILIZE_ACADEMIC_RESOURCES}',
                    '{self.ISSUE_TYPE_WEAKNESS}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.reporting_category WHERE text = '{self.REPORTING_CATEGORY_ACADEMIC}'),
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_TWELVE}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.ISSUE_UTILIZE_ACADEMIC_RESOURCES}',
                    '{self.ISSUE_TYPE_STRENGTH}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.reporting_category WHERE text = '{self.REPORTING_CATEGORY_ACADEMIC}'),
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_THIRTEEN}' AND question_type = '{self.TEXT_CATEGORICAL}'),
                    '{self.ISSUE_STUDY_TIME}',
                    '{self.ISSUE_TYPE_WEAKNESS}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.reporting_category WHERE text = '{self.REPORTING_CATEGORY_ACADEMIC}'),
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_THIRTEEN}' AND question_type = '{self.TEXT_CATEGORICAL}'),
                    '{self.ISSUE_STUDY_TIME}',
                    '{self.ISSUE_TYPE_STRENGTH}',
                    2,
                    2
                ),
                 (
                    (SELECT id FROM nano_survey_configuration.reporting_category WHERE text = '{self.REPORTING_CATEGORY_ACADEMIC}'),
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_FOURTEEN}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.ISSUE_TIME_MANAGEMENT}',
                    '{self.ISSUE_TYPE_WEAKNESS}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.reporting_category WHERE text = '{self.REPORTING_CATEGORY_ACADEMIC}'),
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_FOURTEEN}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.ISSUE_TIME_MANAGEMENT}',
                    '{self.ISSUE_TYPE_STRENGTH}',
                    2,
                    2
                ),
                 (
                    (SELECT id FROM nano_survey_configuration.reporting_category WHERE text = '{self.REPORTING_CATEGORY_ACADEMIC}'),
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_FIFTEEN}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.ISSUE_INSTRUCTOR_COMMUNICATION}',
                    '{self.ISSUE_TYPE_WEAKNESS}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.reporting_category WHERE text = '{self.REPORTING_CATEGORY_ACADEMIC}'),
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_FIFTEEN}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.ISSUE_INSTRUCTOR_COMMUNICATION}',
                    '{self.ISSUE_TYPE_STRENGTH}',
                    2,
                    2
                );
            """,

            6: f"""
                INSERT INTO nano_survey_configuration.issue_question_bank_option (issue_id, question_bank_option_id, created_by) VALUES
                # Question one weakness values
                (
                    (SELECT id FROM nano_survey_configuration.issue WHERE issue_text = '{self.ISSUE_ACADEMIC_COURSEWORK}' AND issue_type = '{self.ISSUE_TYPE_WEAKNESS}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_ONE}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_ONE}' AND qbo.option_value = '{self.NUMERICAL_OPTION_ONE}'),
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.issue WHERE issue_text = '{self.ISSUE_ACADEMIC_COURSEWORK}' AND issue_type = '{self.ISSUE_TYPE_WEAKNESS}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_ONE}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_ONE}' AND qbo.option_value = '{self.NUMERICAL_OPTION_TWO}'),
                    2
                ),
                # Question one strength values
                (
                    (SELECT id FROM nano_survey_configuration.issue WHERE issue_text = '{self.ISSUE_ACADEMIC_COURSEWORK}' AND issue_type = '{self.ISSUE_TYPE_STRENGTH}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_ONE}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_ONE}' AND qbo.option_value = '{self.NUMERICAL_OPTION_SIX}'),
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.issue WHERE issue_text = '{self.ISSUE_ACADEMIC_COURSEWORK}' AND issue_type = '{self.ISSUE_TYPE_STRENGTH}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_ONE}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_ONE}' AND qbo.option_value = '{self.NUMERICAL_OPTION_SEVEN}'),
                    2
                ),
                # Question two weakness values
                (
                    (SELECT id FROM nano_survey_configuration.issue WHERE issue_text = '{self.ISSUE_ACADEMIC_RESILIENCE}' AND issue_type = '{self.ISSUE_TYPE_WEAKNESS}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_TWO}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_TWO}' AND qbo.option_value = '{self.NUMERICAL_OPTION_ONE}'),
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.issue WHERE issue_text = '{self.ISSUE_ACADEMIC_RESILIENCE}' AND issue_type = '{self.ISSUE_TYPE_WEAKNESS}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_TWO}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_TWO}' AND qbo.option_value = '{self.NUMERICAL_OPTION_TWO}'),
                    2
                ),
                # Question two strength values
                (
                    (SELECT id FROM nano_survey_configuration.issue WHERE issue_text = '{self.ISSUE_ACADEMIC_RESILIENCE}' AND issue_type = '{self.ISSUE_TYPE_STRENGTH}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_TWO}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_TWO}' AND qbo.option_value = '{self.NUMERICAL_OPTION_SIX}'),
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.issue WHERE issue_text = '{self.ISSUE_ACADEMIC_RESILIENCE}' AND issue_type = '{self.ISSUE_TYPE_STRENGTH}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_TWO}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_TWO}' AND qbo.option_value = '{self.NUMERICAL_OPTION_SEVEN}'),
                    2
                ),
                # Question three weakness values
                (
                    (SELECT id FROM nano_survey_configuration.issue WHERE issue_text = '{self.ISSUE_CLASS_ATTENDANCE}' AND issue_type = '{self.ISSUE_TYPE_WEAKNESS}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_THREE}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_THREE}' AND qbo.option_value = '{self.QUESTION_THREE_OPTION_THREE}'),
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.issue WHERE issue_text = '{self.ISSUE_CLASS_ATTENDANCE}' AND issue_type = '{self.ISSUE_TYPE_WEAKNESS}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_THREE}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_THREE}' AND qbo.option_value = '{self.QUESTION_THREE_OPTION_FOUR}'),
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.issue WHERE issue_text = '{self.ISSUE_CLASS_ATTENDANCE}' AND issue_type = '{self.ISSUE_TYPE_WEAKNESS}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_THREE}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_THREE}' AND qbo.option_value = '{self.QUESTION_THREE_OPTION_FIVE}'),
                    2
                ),
                # Question three strength values
                (
                    (SELECT id FROM nano_survey_configuration.issue WHERE issue_text = '{self.ISSUE_CLASS_ATTENDANCE}' AND issue_type = '{self.ISSUE_TYPE_STRENGTH}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_THREE}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_THREE}' AND qbo.option_value = '{self.QUESTION_THREE_OPTION_ONE}'),
                    2
                ),
                 # Question four weakness values
                (
                    (SELECT id FROM nano_survey_configuration.issue WHERE issue_text = '{self.ISSUE_COURSE_STRUGGLES}' AND issue_type = '{self.ISSUE_TYPE_WEAKNESS}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_FOUR}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_FOUR}' AND qbo.option_value = '{self.QUESTION_FOUR_OPTION_THREE}'),
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.issue WHERE issue_text = '{self.ISSUE_COURSE_STRUGGLES}' AND issue_type = '{self.ISSUE_TYPE_WEAKNESS}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_FOUR}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_FOUR}' AND qbo.option_value = '{self.QUESTION_FOUR_OPTION_FOUR}'),
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.issue WHERE issue_text = '{self.ISSUE_COURSE_STRUGGLES}' AND issue_type = '{self.ISSUE_TYPE_WEAKNESS}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_FOUR}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_FOUR}' AND qbo.option_value = '{self.QUESTION_FOUR_OPTION_FIVE}'),
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.issue WHERE issue_text = '{self.ISSUE_COURSE_STRUGGLES}' AND issue_type = '{self.ISSUE_TYPE_WEAKNESS}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_FOUR}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_FOUR}' AND qbo.option_value = '{self.QUESTION_FOUR_OPTION_SIX}'),
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.issue WHERE issue_text = '{self.ISSUE_COURSE_STRUGGLES}' AND issue_type = '{self.ISSUE_TYPE_WEAKNESS}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_FOUR}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_FOUR}' AND qbo.option_value = '{self.QUESTION_FOUR_OPTION_SEVEN}'),
                    2
                ),
                # Question four strength values
                (
                    (SELECT id FROM nano_survey_configuration.issue WHERE issue_text = '{self.ISSUE_COURSE_STRUGGLES}' AND issue_type = '{self.ISSUE_TYPE_STRENGTH}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_FOUR}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_FOUR}' AND qbo.option_value = '{self.QUESTION_FOUR_OPTION_ONE}'),
                    2
                ),
                # Question five weakness only values
                (
                    (SELECT id FROM nano_survey_configuration.issue WHERE issue_text = '{self.ISSUE_FINANCIAL_MEANS}' AND issue_type = '{self.ISSUE_TYPE_WEAKNESS}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = "{self.SURVEY_QUESTION_FIVE}")),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = "{self.SURVEY_QUESTION_FIVE}" AND qbo.option_value = '{self.NUMERICAL_OPTION_ONE}'),
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.issue WHERE issue_text = '{self.ISSUE_FINANCIAL_MEANS}' AND issue_type = '{self.ISSUE_TYPE_WEAKNESS}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = "{self.SURVEY_QUESTION_FIVE}")),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = "{self.SURVEY_QUESTION_FIVE}" AND qbo.option_value = '{self.NUMERICAL_OPTION_TWO}'),
                    2
                ),
                 # Question six weakness values
                (
                    (SELECT id FROM nano_survey_configuration.issue WHERE issue_text = '{self.ISSUE_INTENT_TO_RETURN}' AND issue_type = '{self.ISSUE_TYPE_WEAKNESS}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_SIX}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_SIX}' AND qbo.option_value = '{self.NUMERICAL_OPTION_ONE}'),
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.issue WHERE issue_text = '{self.ISSUE_INTENT_TO_RETURN}' AND issue_type = '{self.ISSUE_TYPE_WEAKNESS}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_SIX}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_SIX}' AND qbo.option_value = '{self.NUMERICAL_OPTION_TWO}'),
                    2
                ),
                # Question six strength values
                (
                    (SELECT id FROM nano_survey_configuration.issue WHERE issue_text = '{self.ISSUE_INTENT_TO_RETURN}' AND issue_type = '{self.ISSUE_TYPE_STRENGTH}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_SIX}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_SIX}' AND qbo.option_value = '{self.NUMERICAL_OPTION_SIX}'),
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.issue WHERE issue_text = '{self.ISSUE_INTENT_TO_RETURN}' AND issue_type = '{self.ISSUE_TYPE_STRENGTH}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_SIX}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_SIX}' AND qbo.option_value = '{self.NUMERICAL_OPTION_SEVEN}'),
                    2
                ),
                  # Question seven weakness values
                (
                    (SELECT id FROM nano_survey_configuration.issue WHERE issue_text = '{self.ISSUE_OVERALL_SATISFACTION}' AND issue_type = '{self.ISSUE_TYPE_WEAKNESS}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_SEVEN}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_SEVEN}' AND qbo.option_value = '{self.NUMERICAL_OPTION_ONE}'),
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.issue WHERE issue_text = '{self.ISSUE_OVERALL_SATISFACTION}' AND issue_type = '{self.ISSUE_TYPE_WEAKNESS}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_SEVEN}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_SEVEN}' AND qbo.option_value = '{self.NUMERICAL_OPTION_TWO}'),
                    2
                ),
                # Question seven strength values
                (
                    (SELECT id FROM nano_survey_configuration.issue WHERE issue_text = '{self.ISSUE_OVERALL_SATISFACTION}' AND issue_type = '{self.ISSUE_TYPE_STRENGTH}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_SEVEN}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_SEVEN}' AND qbo.option_value = '{self.NUMERICAL_OPTION_SIX}'),
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.issue WHERE issue_text = '{self.ISSUE_OVERALL_SATISFACTION}' AND issue_type = '{self.ISSUE_TYPE_STRENGTH}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_SEVEN}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_SEVEN}' AND qbo.option_value = '{self.NUMERICAL_OPTION_SEVEN}'),
                    2
                ),
                # Question eight weakness values
                (
                    (SELECT id FROM nano_survey_configuration.issue WHERE issue_text = '{self.ISSUE_SENSE_OF_BELONGING}' AND issue_type = '{self.ISSUE_TYPE_WEAKNESS}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_EIGHT}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_EIGHT}' AND qbo.option_value = '{self.NUMERICAL_OPTION_ONE}'),
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.issue WHERE issue_text = '{self.ISSUE_SENSE_OF_BELONGING}' AND issue_type = '{self.ISSUE_TYPE_WEAKNESS}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_EIGHT}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_EIGHT}' AND qbo.option_value = '{self.NUMERICAL_OPTION_TWO}'),
                    2
                ),
                # Question eight strength values
                (
                    (SELECT id FROM nano_survey_configuration.issue WHERE issue_text = '{self.ISSUE_SENSE_OF_BELONGING}' AND issue_type = '{self.ISSUE_TYPE_STRENGTH}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_EIGHT}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_EIGHT}' AND qbo.option_value = '{self.NUMERICAL_OPTION_SIX}'),
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.issue WHERE issue_text = '{self.ISSUE_SENSE_OF_BELONGING}' AND issue_type = '{self.ISSUE_TYPE_STRENGTH}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_EIGHT}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_EIGHT}' AND qbo.option_value = '{self.NUMERICAL_OPTION_SEVEN}'),
                    2
                ),
                # Question nine weakness values inverse
                (
                    (SELECT id FROM nano_survey_configuration.issue WHERE issue_text = '{self.ISSUE_HEALTH_RELATED_STRESS}' AND issue_type = '{self.ISSUE_TYPE_WEAKNESS}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_NINE}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_NINE}' AND qbo.option_value = '{self.NUMERICAL_OPTION_SIX}'),
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.issue WHERE issue_text = '{self.ISSUE_HEALTH_RELATED_STRESS}' AND issue_type = '{self.ISSUE_TYPE_WEAKNESS}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_NINE}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_NINE}' AND qbo.option_value = '{self.NUMERICAL_OPTION_SEVEN}'),
                    2
                ),
                # Question nine strength values inverse
                (
                    (SELECT id FROM nano_survey_configuration.issue WHERE issue_text = '{self.ISSUE_HEALTH_RELATED_STRESS}' AND issue_type = '{self.ISSUE_TYPE_STRENGTH}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_NINE}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_NINE}' AND qbo.option_value = '{self.NUMERICAL_OPTION_ONE}'),
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.issue WHERE issue_text = '{self.ISSUE_HEALTH_RELATED_STRESS}' AND issue_type = '{self.ISSUE_TYPE_STRENGTH}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_NINE}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_NINE}' AND qbo.option_value = '{self.NUMERICAL_OPTION_TWO}'),
                    2
                ),
                # Question ten weakness values
                (
                    (SELECT id FROM nano_survey_configuration.issue WHERE issue_text = '{self.ISSUE_PROBATION_REQUIREMENTS}' AND issue_type = '{self.ISSUE_TYPE_WEAKNESS}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_TEN}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_TEN}' AND qbo.option_value = '{self.NUMERICAL_OPTION_ONE}'),
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.issue WHERE issue_text = '{self.ISSUE_PROBATION_REQUIREMENTS}' AND issue_type = '{self.ISSUE_TYPE_WEAKNESS}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_TEN}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_TEN}' AND qbo.option_value = '{self.NUMERICAL_OPTION_TWO}'),
                    2
                ),
                # Question ten strength values
                (
                    (SELECT id FROM nano_survey_configuration.issue WHERE issue_text = '{self.ISSUE_PROBATION_REQUIREMENTS}' AND issue_type = '{self.ISSUE_TYPE_STRENGTH}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_TEN}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_TEN}' AND qbo.option_value = '{self.NUMERICAL_OPTION_SIX}'),
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.issue WHERE issue_text = '{self.ISSUE_PROBATION_REQUIREMENTS}' AND issue_type = '{self.ISSUE_TYPE_STRENGTH}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_TEN}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_TEN}' AND qbo.option_value = '{self.NUMERICAL_OPTION_SEVEN}'),
                    2
                ),
                  # Question eleven weakness values
                (
                    (SELECT id FROM nano_survey_configuration.issue WHERE issue_text = '{self.ISSUE_GPA_EXPECTATIONS}' AND issue_type = '{self.ISSUE_TYPE_WEAKNESS}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_ELEVEN}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_ELEVEN}' AND qbo.option_value = '{self.NUMERICAL_OPTION_ONE}'),
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.issue WHERE issue_text = '{self.ISSUE_GPA_EXPECTATIONS}' AND issue_type = '{self.ISSUE_TYPE_WEAKNESS}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_ELEVEN}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_ELEVEN}' AND qbo.option_value = '{self.NUMERICAL_OPTION_TWO}'),
                    2
                ),
                # Question eleven strength values
                (
                    (SELECT id FROM nano_survey_configuration.issue WHERE issue_text = '{self.ISSUE_GPA_EXPECTATIONS}' AND issue_type = '{self.ISSUE_TYPE_STRENGTH}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_ELEVEN}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_ELEVEN}' AND qbo.option_value = '{self.NUMERICAL_OPTION_SIX}'),
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.issue WHERE issue_text = '{self.ISSUE_GPA_EXPECTATIONS}' AND issue_type = '{self.ISSUE_TYPE_STRENGTH}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_ELEVEN}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_ELEVEN}' AND qbo.option_value = '{self.NUMERICAL_OPTION_SEVEN}'),
                    2
                ),
                  # Question twelve weakness values
                (
                    (SELECT id FROM nano_survey_configuration.issue WHERE issue_text = '{self.ISSUE_UTILIZE_ACADEMIC_RESOURCES}' AND issue_type = '{self.ISSUE_TYPE_WEAKNESS}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_TWELVE}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_TWELVE}' AND qbo.option_value = '{self.NUMERICAL_OPTION_ONE}'),
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.issue WHERE issue_text = '{self.ISSUE_UTILIZE_ACADEMIC_RESOURCES}' AND issue_type = '{self.ISSUE_TYPE_WEAKNESS}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_TWELVE}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_TWELVE}' AND qbo.option_value = '{self.NUMERICAL_OPTION_TWO}'),
                    2
                ),
                # Question twelve strength values
                (
                    (SELECT id FROM nano_survey_configuration.issue WHERE issue_text = '{self.ISSUE_UTILIZE_ACADEMIC_RESOURCES}' AND issue_type = '{self.ISSUE_TYPE_STRENGTH}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_TWELVE}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_TWELVE}' AND qbo.option_value = '{self.NUMERICAL_OPTION_SIX}'),
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.issue WHERE issue_text = '{self.ISSUE_UTILIZE_ACADEMIC_RESOURCES}' AND issue_type = '{self.ISSUE_TYPE_STRENGTH}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_TWELVE}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_TWELVE}' AND qbo.option_value = '{self.NUMERICAL_OPTION_SEVEN}'),
                    2
                ),

                # Question thirteen weakness values
                (
                    (SELECT id FROM nano_survey_configuration.issue WHERE issue_text = '{self.ISSUE_STUDY_TIME}' AND issue_type = '{self.ISSUE_TYPE_WEAKNESS}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_THIRTEEN}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_THIRTEEN}' AND qbo.option_value = '{self.QUESTION_THIRTEEN_OPTION_ONE}'),
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.issue WHERE issue_text = '{self.ISSUE_STUDY_TIME}' AND issue_type = '{self.ISSUE_TYPE_WEAKNESS}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_THIRTEEN}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_THIRTEEN}' AND qbo.option_value = '{self.QUESTION_THIRTEEN_OPTION_TWO}'),
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.issue WHERE issue_text = '{self.ISSUE_STUDY_TIME}' AND issue_type = '{self.ISSUE_TYPE_WEAKNESS}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_THIRTEEN}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_THIRTEEN}' AND qbo.option_value = '{self.QUESTION_THIRTEEN_OPTION_THREE}'),
                    2
                ),
                # Question thirteen strength values
                (
                    (SELECT id FROM nano_survey_configuration.issue WHERE issue_text = '{self.ISSUE_STUDY_TIME}' AND issue_type = '{self.ISSUE_TYPE_STRENGTH}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_THIRTEEN}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_THIRTEEN}' AND qbo.option_value = '{self.QUESTION_THIRTEEN_OPTION_SIX}'),
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.issue WHERE issue_text = '{self.ISSUE_STUDY_TIME}' AND issue_type = '{self.ISSUE_TYPE_STRENGTH}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_THIRTEEN}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_THIRTEEN}' AND qbo.option_value = '{self.QUESTION_THIRTEEN_OPTION_SEVEN}'),
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.issue WHERE issue_text = '{self.ISSUE_STUDY_TIME}' AND issue_type = '{self.ISSUE_TYPE_STRENGTH}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_THIRTEEN}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_THIRTEEN}' AND qbo.option_value = '{self.QUESTION_THIRTEEN_OPTION_EIGHT}'),
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.issue WHERE issue_text = '{self.ISSUE_STUDY_TIME}' AND issue_type = '{self.ISSUE_TYPE_STRENGTH}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_THIRTEEN}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_THIRTEEN}' AND qbo.option_value = '{self.QUESTION_THIRTEEN_OPTION_NINE}'),
                    2
                ),
                  # Question Fourteen weakness values
                (
                    (SELECT id FROM nano_survey_configuration.issue WHERE issue_text = '{self.ISSUE_TIME_MANAGEMENT}' AND issue_type = '{self.ISSUE_TYPE_WEAKNESS}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_FOURTEEN}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_FOURTEEN}' AND qbo.option_value = '{self.NUMERICAL_OPTION_ONE}'),
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.issue WHERE issue_text = '{self.ISSUE_TIME_MANAGEMENT}' AND issue_type = '{self.ISSUE_TYPE_WEAKNESS}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_FOURTEEN}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_FOURTEEN}' AND qbo.option_value = '{self.NUMERICAL_OPTION_TWO}'),
                    2
                ),
                # Question fourteen strength values
                (
                    (SELECT id FROM nano_survey_configuration.issue WHERE issue_text = '{self.ISSUE_TIME_MANAGEMENT}' AND issue_type = '{self.ISSUE_TYPE_STRENGTH}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_FOURTEEN}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_FOURTEEN}' AND qbo.option_value = '{self.NUMERICAL_OPTION_SIX}'),
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.issue WHERE issue_text = '{self.ISSUE_TIME_MANAGEMENT}' AND issue_type = '{self.ISSUE_TYPE_STRENGTH}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_FOURTEEN}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_FOURTEEN}' AND qbo.option_value = '{self.NUMERICAL_OPTION_SEVEN}'),
                    2
                ),
                  # Question fifteen weakness values
                (
                    (SELECT id FROM nano_survey_configuration.issue WHERE issue_text = '{self.ISSUE_INSTRUCTOR_COMMUNICATION}' AND issue_type = '{self.ISSUE_TYPE_WEAKNESS}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_FIFTEEN}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_FIFTEEN}' AND qbo.option_value = '{self.NUMERICAL_OPTION_ONE}'),
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.issue WHERE issue_text = '{self.ISSUE_INSTRUCTOR_COMMUNICATION}' AND issue_type = '{self.ISSUE_TYPE_WEAKNESS}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_FIFTEEN}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_FIFTEEN}' AND qbo.option_value = '{self.NUMERICAL_OPTION_TWO}'),
                    2
                ),
                # Question fifteen strength values
                (
                    (SELECT id FROM nano_survey_configuration.issue WHERE issue_text = '{self.ISSUE_INSTRUCTOR_COMMUNICATION}' AND issue_type = '{self.ISSUE_TYPE_STRENGTH}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_FIFTEEN}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_FIFTEEN}' AND qbo.option_value = '{self.NUMERICAL_OPTION_SIX}'),
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.issue WHERE issue_text = '{self.ISSUE_INSTRUCTOR_COMMUNICATION}' AND issue_type = '{self.ISSUE_TYPE_STRENGTH}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_FIFTEEN}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_FIFTEEN}' AND qbo.option_value = '{self.NUMERICAL_OPTION_SEVEN}'),
                    2
                );
            """,
            7: f"""
                INSERT INTO nano_survey_configuration.survey_template_purpose (survey_template_id, survey_purpose_id) VALUES
                (
                    (SELECT id FROM nano_survey_configuration.survey_template WHERE internal_key = '{self.SURVEY_TEMPLATE_INTERNAL_KEY}'),
                    (SELECT id FROM nano_survey_configuration.survey_purpose WHERE section = 'Why' AND purpose_text = '{self.SURVEY_WHY_TEXT}')
                ),
                (
                    (SELECT id FROM nano_survey_configuration.survey_template WHERE internal_key = '{self.SURVEY_TEMPLATE_INTERNAL_KEY}'),
                    (SELECT id FROM nano_survey_configuration.survey_purpose WHERE section = 'How' AND purpose_text = '{self.SURVEY_HOW_TEXT}')
                );
            """,
            8: f"""
                INSERT INTO nano_survey_configuration.survey_template_question (survey_template_id, question_bank_id, sequence, created_by, modified_by) VALUES
                (
                    (SELECT id FROM nano_survey_configuration.survey_template WHERE internal_key = '{self.SURVEY_TEMPLATE_INTERNAL_KEY}'),
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_ONE}' AND question_type = '{self.TEXT_SCALED}'),
                    1,
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.survey_template WHERE internal_key = '{self.SURVEY_TEMPLATE_INTERNAL_KEY}'),
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_TWO}' AND question_type = '{self.TEXT_SCALED}'),
                    1,
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.survey_template WHERE internal_key = '{self.SURVEY_TEMPLATE_INTERNAL_KEY}'),
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_THREE}' AND question_type = '{self.TEXT_CATEGORICAL}'),
                    3,
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.survey_template WHERE internal_key = '{self.SURVEY_TEMPLATE_INTERNAL_KEY}'),
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_FOUR}' AND question_type = '{self.TEXT_CATEGORICAL}'),
                    3,
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.survey_template WHERE internal_key = '{self.SURVEY_TEMPLATE_INTERNAL_KEY}'),
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = "{self.SURVEY_QUESTION_FIVE}" AND question_type = '{self.TEXT_SCALED}'),
                    5,
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.survey_template WHERE internal_key = '{self.SURVEY_TEMPLATE_INTERNAL_KEY}'),
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_SIX}' AND question_type = '{self.TEXT_SCALED}'),
                    6,
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.survey_template WHERE internal_key = '{self.SURVEY_TEMPLATE_INTERNAL_KEY}'),
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_SEVEN}' AND question_type = '{self.TEXT_SCALED}'),
                    7,
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.survey_template WHERE internal_key = '{self.SURVEY_TEMPLATE_INTERNAL_KEY}'),
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_EIGHT}' AND question_type = '{self.TEXT_SCALED}'),
                    8,
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.survey_template WHERE internal_key = '{self.SURVEY_TEMPLATE_INTERNAL_KEY}'),
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_NINE}' AND question_type = '{self.TEXT_SCALED}'),
                    7,
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.survey_template WHERE internal_key = '{self.SURVEY_TEMPLATE_INTERNAL_KEY}'),
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_TEN}' AND question_type = '{self.TEXT_SCALED}'),
                    7,
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.survey_template WHERE internal_key = '{self.SURVEY_TEMPLATE_INTERNAL_KEY}'),
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_ELEVEN}' AND question_type = '{self.TEXT_SCALED}'),
                    7,
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.survey_template WHERE internal_key = '{self.SURVEY_TEMPLATE_INTERNAL_KEY}'),
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_TWELVE}' AND question_type = '{self.TEXT_SCALED}'),
                    7,
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.survey_template WHERE internal_key = '{self.SURVEY_TEMPLATE_INTERNAL_KEY}'),
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_THIRTEEN}' AND question_type = '{self.TEXT_CATEGORICAL}'),
                    3,
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.survey_template WHERE internal_key = '{self.SURVEY_TEMPLATE_INTERNAL_KEY}'),
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_FOURTEEN}' AND question_type = '{self.TEXT_SCALED}'),
                    7,
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.survey_template WHERE internal_key = '{self.SURVEY_TEMPLATE_INTERNAL_KEY}'),
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_FIFTEEN}' AND question_type = '{self.TEXT_SCALED}'),
                    7,
                    2,
                    2
                );
            """,

            9: f"""
                INSERT INTO nano_survey_configuration.talking_point (question_bank_id, talking_point_type, text, next_steps, created_by, modified_by) VALUES
                (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_ONE}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.ISSUE_TYPE_WEAKNESS}',
                    '{self.QUESTION_ONE_TALKING_POINT_WEAKNESS}',
                    '{self.QUESTION_ONE_NEXT_STEPS}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_ONE}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.ISSUE_TYPE_STRENGTH}',
                    '{self.QUESTION_ONE_TALKING_POINT_STRENGTH}',
                    null,
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_TWO}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.ISSUE_TYPE_WEAKNESS}',
                    '{self.QUESTION_TWO_TALKING_POINT_WEAKNESS}',
                    '{self.QUESTION_TWO_NEXT_STEPS}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_TWO}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.ISSUE_TYPE_STRENGTH}',
                    '{self.QUESTION_TWO_TALKING_POINT_STRENGTH}',
                    null,
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_THREE}' AND question_type = '{self.TEXT_CATEGORICAL}'),
                    '{self.ISSUE_TYPE_WEAKNESS}',
                    '{self.QUESTION_THREE_TALKING_POINT_WEAKNESS}',
                    '{self.QUESTION_THREE_NEXT_STEPS}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_THREE}' AND question_type = '{self.TEXT_CATEGORICAL}'),
                    '{self.ISSUE_TYPE_STRENGTH}',
                    '{self.QUESTION_THREE_TALKING_POINT_STRENGTH}',
                    null,
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_FOUR}' AND question_type = '{self.TEXT_CATEGORICAL}'),
                    '{self.ISSUE_TYPE_WEAKNESS}',
                    '{self.QUESTION_FOUR_TALKING_POINT_WEAKNESS}',
                    '{self.QUESTION_FOUR_NEXT_STEPS}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_FOUR}' AND question_type = '{self.TEXT_CATEGORICAL}'),
                    '{self.ISSUE_TYPE_STRENGTH}',
                    '{self.QUESTION_FOUR_TALKING_POINT_STRENGTH}',
                    null,
                    2,
                    2
                ),
                 (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = "{self.SURVEY_QUESTION_FIVE}" AND question_type = '{self.TEXT_SCALED}'),
                    '{self.ISSUE_TYPE_WEAKNESS}',
                    "{self.QUESTION_FIVE_TALKING_POINT_WEAKNESS}",
                    '{self.QUESTION_FIVE_NEXT_STEPS}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_SIX}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.ISSUE_TYPE_WEAKNESS}',
                    '{self.QUESTION_SIX_TALKING_POINT_WEAKNESS}',
                    "{self.QUESTION_SIX_NEXT_STEPS}",
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_SIX}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.ISSUE_TYPE_STRENGTH}',
                    '{self.QUESTION_SIX_TALKING_POINT_STRENGTH}',
                    null,
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_SEVEN}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.ISSUE_TYPE_WEAKNESS}',
                    '{self.QUESTION_SEVEN_TALKING_POINT_WEAKNESS}',
                    '{self.QUESTION_SEVEN_NEXT_STEPS}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_SEVEN}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.ISSUE_TYPE_STRENGTH}',
                    '{self.QUESTION_SEVEN_TALKING_POINT_STRENGTH}',
                    null,
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_EIGHT}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.ISSUE_TYPE_WEAKNESS}',
                    "{self.QUESTION_EIGHT_TALKING_POINT_WEAKNESS}",
                    '{self.QUESTION_EIGHT_NEXT_STEPS}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_EIGHT}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.ISSUE_TYPE_STRENGTH}',
                    '{self.QUESTION_EIGHT_TALKING_POINT_STRENGTH}',
                    null,
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_NINE}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.ISSUE_TYPE_WEAKNESS}',
                    '{self.QUESTION_NINE_TALKING_POINT_WEAKNESS}',
                    '{self.QUESTION_NINE_NEXT_STEPS}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_NINE}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.ISSUE_TYPE_STRENGTH}',
                    '{self.QUESTION_NINE_TALKING_POINT_STRENGTH}',
                    null,
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_TEN}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.ISSUE_TYPE_WEAKNESS}',
                    '{self.QUESTION_TEN_TALKING_POINT_WEAKNESS}',
                    "{self.QUESTION_TEN_NEXT_STEPS}",
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_ELEVEN}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.ISSUE_TYPE_WEAKNESS}',
                    '{self.QUESTION_ELEVEN_TALKING_POINT_WEAKNESS}',
                    '{self.QUESTION_ELEVEN_NEXT_STEPS}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_ELEVEN}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.ISSUE_TYPE_STRENGTH}',
                    '{self.QUESTION_ELEVEN_TALKING_POINT_STRENGTH}',
                    null,
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_TWELVE}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.ISSUE_TYPE_WEAKNESS}',
                    '{self.QUESTION_TWELEVE_TALKING_POINT_WEAKNESS}',
                    '{self.QUESTION_TWELVE_NEXT_STEPS}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_TWELVE}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.ISSUE_TYPE_STRENGTH}',
                    '{self.QUESTION_TWELVE_TALKING_POINT_STRENGTH}',
                    null,
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_THIRTEEN}' AND question_type = '{self.TEXT_CATEGORICAL}'),
                    '{self.ISSUE_TYPE_WEAKNESS}',
                    '{self.QUESTION_THIRTEEN_TALKING_POINT_WEAKNESS}',
                    '{self.QUESTION_THIRTEEN_NEXT_STEPS}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_THIRTEEN}' AND question_type = '{self.TEXT_CATEGORICAL}'),
                    '{self.ISSUE_TYPE_STRENGTH}',
                    '{self.QUESTION_THIRTEEN_TALKING_POINT_STRENGTH}',
                    null,
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_FORTEEN}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.ISSUE_TYPE_WEAKNESS}',
                    '{self.QUESTION_FORTEEN_TALKING_POINT_WEAKNESS}',
                    '{self.QUESTION_FORTEEN_NEXT_STEPS}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_FOURTEEN}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.ISSUE_TYPE_STRENGTH}',
                    '{self.QUESTION_FOURTEEN_TALKING_POINT_STRENGTH}',
                    null,
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_FIFTEEN}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.ISSUE_TYPE_WEAKNESS}',
                    '{self.QUESTION_FIFTEEN_TALKING_POINT_WEAKNESS}',
                    '{self.QUESTION_FIFTEEN_NEXT_STEPS}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_FIFTEEN}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.ISSUE_TYPE_STRENGTH}',
                    '{self.QUESTION_FIFTEEN_TALKING_POINT_STRENGTH}',
                    null,
                    2,
                    2
                );
    			""",
            10: f"""
                INSERT INTO nano_survey_configuration.talking_point_question_bank_option (talking_point_id, question_bank_option_id, created_by) VALUES
                # Question one
                (
                    (SELECT id FROM nano_survey_configuration.talking_point WHERE text = '{self.QUESTION_ONE_TALKING_POINT_WEAKNESS}' AND talking_point_type = '{self.ISSUE_TYPE_WEAKNESS}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_ONE}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_ONE}' AND qbo.option_value = '{self.NUMERICAL_OPTION_ONE}'),
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.talking_point WHERE text = '{self.QUESTION_ONE_TALKING_POINT_WEAKNESS}' AND talking_point_type = '{self.ISSUE_TYPE_WEAKNESS}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_ONE}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_ONE}' AND qbo.option_value = '{self.NUMERICAL_OPTION_TWO}'),
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.talking_point WHERE text = '{self.QUESTION_ONE_TALKING_POINT_STRENGTH}' AND talking_point_type = '{self.ISSUE_TYPE_STRENGTH}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_ONE}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_ONE}' AND qbo.option_value = '{self.NUMERICAL_OPTION_SIX}'),
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.talking_point WHERE text = '{self.QUESTION_ONE_TALKING_POINT_STRENGTH}' AND talking_point_type = '{self.ISSUE_TYPE_STRENGTH}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_ONE}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_ONE}' AND qbo.option_value = '{self.NUMERICAL_OPTION_SEVEN}'),
                    2
                ),
                # Question two
                (
                    (SELECT id FROM nano_survey_configuration.talking_point WHERE text = '{self.QUESTION_TWO_TALKING_POINT_WEAKNESS}' AND talking_point_type = '{self.ISSUE_TYPE_WEAKNESS}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_TWO}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_TWO}' AND qbo.option_value = '{self.QUESTION_TWO_OPTION_ONE}'),
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.talking_point WHERE text = '{self.QUESTION_TWO_TALKING_POINT_WEAKNESS}' AND talking_point_type = '{self.ISSUE_TYPE_WEAKNESS}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_TWO}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_TWO}' AND qbo.option_value = '{self.QUESTION_TWO_OPTION_TWO}'),
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.talking_point WHERE text = '{self.QUESTION_TWO_TALKING_POINT_STRENGTH}' AND talking_point_type = '{self.ISSUE_TYPE_STRENGTH}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_TWO}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_TWO}' AND qbo.option_value = '{self.QUESTION_TWO_OPTION_SIX}'),
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.talking_point WHERE text = '{self.QUESTION_TWO_TALKING_POINT_STRENGTH}' AND talking_point_type = '{self.ISSUE_TYPE_STRENGTH}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_TWO}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_TWO}' AND qbo.option_value = '{self.QUESTION_TWO_OPTION_SEVEN}'),
                    2
                ),
                 # Question three
                (
                    (SELECT id FROM nano_survey_configuration.talking_point WHERE text = '{self.QUESTION_THREE_TALKING_POINT_WEAKNESS}' AND talking_point_type = '{self.ISSUE_TYPE_WEAKNESS}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_THREE}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_THREE}' AND qbo.option_value = '{self.QUESTION_THREE_OPTION_THREE}'),
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.talking_point WHERE text = '{self.QUESTION_THREE_TALKING_POINT_WEAKNESS}' AND talking_point_type = '{self.ISSUE_TYPE_WEAKNESS}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_THREE}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_THREE}' AND qbo.option_value = '{self.QUESTION_THREE_OPTION_FOUR}'),
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.talking_point WHERE text = '{self.QUESTION_THREE_TALKING_POINT_WEAKNESS}' AND talking_point_type = '{self.ISSUE_TYPE_WEAKNESS}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_THREE}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_THREE}' AND qbo.option_value = '{self.QUESTION_THREE_OPTION_FIVE}'),
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.talking_point WHERE text = '{self.QUESTION_THREE_TALKING_POINT_STRENGTH}' AND talking_point_type = '{self.ISSUE_TYPE_STRENGTH}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_THREE}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_THREE}' AND qbo.option_value = '{self.QUESTION_THREE_OPTION_ONE}'),
                    2
                ),
                # Question four
                (
                    (SELECT id FROM nano_survey_configuration.talking_point WHERE text = '{self.QUESTION_FOUR_TALKING_POINT_WEAKNESS}' AND talking_point_type = '{self.ISSUE_TYPE_WEAKNESS}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_FOUR}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_FOUR}' AND qbo.option_value = '{self.QUESTION_FOUR_OPTION_THREE}'),
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.talking_point WHERE text = '{self.QUESTION_FOUR_TALKING_POINT_WEAKNESS}' AND talking_point_type = '{self.ISSUE_TYPE_WEAKNESS}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_FOUR}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_FOUR}' AND qbo.option_value = '{self.QUESTION_FOUR_OPTION_FOUR}'),
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.talking_point WHERE text = '{self.QUESTION_FOUR_TALKING_POINT_WEAKNESS}' AND talking_point_type = '{self.ISSUE_TYPE_WEAKNESS}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_FOUR}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_FOUR}' AND qbo.option_value = '{self.QUESTION_FOUR_OPTION_FIVE}'),
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.talking_point WHERE text = '{self.QUESTION_FOUR_TALKING_POINT_WEAKNESS}' AND talking_point_type = '{self.ISSUE_TYPE_WEAKNESS}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_FOUR}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_FOUR}' AND qbo.option_value = '{self.QUESTION_FOUR_OPTION_SIX}'),
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.talking_point WHERE text = '{self.QUESTION_FOUR_TALKING_POINT_WEAKNESS}' AND talking_point_type = '{self.ISSUE_TYPE_WEAKNESS}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_FOUR}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_FOUR}' AND qbo.option_value = '{self.QUESTION_FOUR_OPTION_SEVEN}'),
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.talking_point WHERE text = '{self.QUESTION_FOUR_TALKING_POINT_STRENGTH}' AND talking_point_type = '{self.ISSUE_TYPE_STRENGTH}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_FOUR}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_FOUR}' AND qbo.option_value = '{self.QUESTION_FOUR_OPTION_ONE}'),
                    2
                ),
                # Question five no strength
                (
                    (SELECT id FROM nano_survey_configuration.talking_point WHERE text = "{self.QUESTION_FIVE_TALKING_POINT_WEAKNESS}" AND talking_point_type = '{self.ISSUE_TYPE_WEAKNESS}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = "{self.SURVEY_QUESTION_FIVE}")),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = "{self.SURVEY_QUESTION_FIVE}" AND qbo.option_value = '{self.NUMERICAL_OPTION_ONE}'),
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.talking_point WHERE text = "{self.QUESTION_FIVE_TALKING_POINT_WEAKNESS}" AND talking_point_type = '{self.ISSUE_TYPE_WEAKNESS}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = "{self.SURVEY_QUESTION_FIVE}")),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = "{self.SURVEY_QUESTION_FIVE}" AND qbo.option_value = '{self.NUMERICAL_OPTION_TWO}'),
                    2
                ),
                # Question six
                (
                    (SELECT id FROM nano_survey_configuration.talking_point WHERE text = '{self.QUESTION_SIX_TALKING_POINT_WEAKNESS}' AND talking_point_type = '{self.ISSUE_TYPE_WEAKNESS}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_SIX}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_SIX}' AND qbo.option_value = '{self.NUMERICAL_OPTION_ONE}'),
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.talking_point WHERE text = '{self.QUESTION_SIX_TALKING_POINT_WEAKNESS}' AND talking_point_type = '{self.ISSUE_TYPE_WEAKNESS}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_SIX}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_SIX}' AND qbo.option_value = '{self.NUMERICAL_OPTION_TWO}'),
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.talking_point WHERE text = '{self.QUESTION_SIX_TALKING_POINT_STRENGTH}' AND talking_point_type = '{self.ISSUE_TYPE_STRENGTH}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_SIX}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_SIX}' AND qbo.option_value = '{self.NUMERICAL_OPTION_SIX}'),
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.talking_point WHERE text = '{self.QUESTION_SIX_TALKING_POINT_STRENGTH}' AND talking_point_type = '{self.ISSUE_TYPE_STRENGTH}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_SIX}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_SIX}' AND qbo.option_value = '{self.NUMERICAL_OPTION_SEVEN}'),
                    2
                ),
                 # Question seven
                (
                    (SELECT id FROM nano_survey_configuration.talking_point WHERE text = '{self.QUESTION_SEVEN_TALKING_POINT_WEAKNESS}' AND talking_point_type = '{self.ISSUE_TYPE_WEAKNESS}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_SEVEN}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_SEVEN}' AND qbo.option_value = '{self.NUMERICAL_OPTION_ONE}'),
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.talking_point WHERE text = '{self.QUESTION_SEVEN_TALKING_POINT_WEAKNESS}' AND talking_point_type = '{self.ISSUE_TYPE_WEAKNESS}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_SEVEN}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_SEVEN}' AND qbo.option_value = '{self.NUMERICAL_OPTION_TWO}'),
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.talking_point WHERE text = '{self.QUESTION_SEVEN_TALKING_POINT_STRENGTH}' AND talking_point_type = '{self.ISSUE_TYPE_STRENGTH}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_SEVEN}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_SEVEN}' AND qbo.option_value = '{self.NUMERICAL_OPTION_SIX}'),
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.talking_point WHERE text = '{self.QUESTION_SEVEN_TALKING_POINT_STRENGTH}' AND talking_point_type = '{self.ISSUE_TYPE_STRENGTH}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_SEVEN}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_SEVEN}' AND qbo.option_value = '{self.NUMERICAL_OPTION_SEVEN}'),
                    2
                ),
                # Question eight
                (
                    (SELECT id FROM nano_survey_configuration.talking_point WHERE text = "{self.QUESTION_EIGHT_TALKING_POINT_WEAKNESS}" AND talking_point_type = '{self.ISSUE_TYPE_WEAKNESS}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_EIGHT}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_EIGHT}' AND qbo.option_value = '{self.NUMERICAL_OPTION_ONE}'),
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.talking_point WHERE text = "{self.QUESTION_EIGHT_TALKING_POINT_WEAKNESS}" AND talking_point_type = '{self.ISSUE_TYPE_WEAKNESS}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_EIGHT}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_EIGHT}' AND qbo.option_value = '{self.NUMERICAL_OPTION_TWO}'),
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.talking_point WHERE text = '{self.QUESTION_EIGHT_TALKING_POINT_STRENGTH}' AND talking_point_type = '{self.ISSUE_TYPE_STRENGTH}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_EIGHT}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_EIGHT}' AND qbo.option_value = '{self.NUMERICAL_OPTION_SIX}'),
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.talking_point WHERE text = '{self.QUESTION_EIGHT_TALKING_POINT_STRENGTH}' AND talking_point_type = '{self.ISSUE_TYPE_STRENGTH}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_EIGHT}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_EIGHT}' AND qbo.option_value = '{self.NUMERICAL_OPTION_SEVEN}'),
                    2
                ),
                # Question nine inverse
                (
                    (SELECT id FROM nano_survey_configuration.talking_point WHERE text = '{self.QUESTION_NINE_TALKING_POINT_WEAKNESS}' AND talking_point_type = '{self.ISSUE_TYPE_WEAKNESS}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_NINE}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_NINE}' AND qbo.option_value = '{self.NUMERICAL_OPTION_SIX}'),
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.talking_point WHERE text = '{self.QUESTION_NINE_TALKING_POINT_WEAKNESS}' AND talking_point_type = '{self.ISSUE_TYPE_WEAKNESS}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_NINE}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_NINE}' AND qbo.option_value = '{self.NUMERICAL_OPTION_SEVEN}'),
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.talking_point WHERE text = '{self.QUESTION_NINE_TALKING_POINT_STRENGTH}' AND talking_point_type = '{self.ISSUE_TYPE_STRENGTH}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_NINE}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_NINE}' AND qbo.option_value = '{self.NUMERICAL_OPTION_ONE}'),
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.talking_point WHERE text = '{self.QUESTION_NINE_TALKING_POINT_STRENGTH}' AND talking_point_type = '{self.ISSUE_TYPE_STRENGTH}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_NINE}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_NINE}' AND qbo.option_value = '{self.NUMERICAL_OPTION_TWO}'),
                    2
                ),
                # Question ten
                (
                    (SELECT id FROM nano_survey_configuration.talking_point WHERE text = '{self.QUESTION_TEN_TALKING_POINT_WEAKNESS}' AND talking_point_type = '{self.ISSUE_TYPE_WEAKNESS}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_TEN}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_TEN}' AND qbo.option_value = '{self.NUMERICAL_OPTION_ONE}'),
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.talking_point WHERE text = '{self.QUESTION_TEN_TALKING_POINT_WEAKNESS}' AND talking_point_type = '{self.ISSUE_TYPE_WEAKNESS}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_TEN}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_TEN}' AND qbo.option_value = '{self.NUMERICAL_OPTION_TWO}'),
                    2
                ),
                # Question eleven
                (
                    (SELECT id FROM nano_survey_configuration.talking_point WHERE text = '{self.QUESTION_ELEVEN_TALKING_POINT_WEAKNESS}' AND talking_point_type = '{self.ISSUE_TYPE_WEAKNESS}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_ELEVEN}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_ELEVEN}' AND qbo.option_value = '{self.NUMERICAL_OPTION_ONE}'),
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.talking_point WHERE text = '{self.QUESTION_ELEVEN_TALKING_POINT_WEAKNESS}' AND talking_point_type = '{self.ISSUE_TYPE_WEAKNESS}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_ELEVEN}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_ELEVEN}' AND qbo.option_value = '{self.NUMERICAL_OPTION_TWO}'),
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.talking_point WHERE text = '{self.QUESTION_ELEVEN_TALKING_POINT_STRENGTH}' AND talking_point_type = '{self.ISSUE_TYPE_STRENGTH}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_ELEVEN}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_ELEVEN}' AND qbo.option_value = '{self.NUMERICAL_OPTION_SIX}'),
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.talking_point WHERE text = '{self.QUESTION_ELEVEN_TALKING_POINT_STRENGTH}' AND talking_point_type = '{self.ISSUE_TYPE_STRENGTH}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_ELEVEN}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_ELEVEN}' AND qbo.option_value = '{self.NUMERICAL_OPTION_SEVEN}'),
                    2
                ),
                # Question twelve
                (
                    (SELECT id FROM nano_survey_configuration.talking_point WHERE text = '{self.QUESTION_TWELVE_TALKING_POINT_WEAKNESS}' AND talking_point_type = '{self.ISSUE_TYPE_WEAKNESS}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_TWELVE}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_TWELVE}' AND qbo.option_value = '{self.NUMERICAL_OPTION_ONE}'),
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.talking_point WHERE text = '{self.QUESTION_TWELVE_TALKING_POINT_WEAKNESS}' AND talking_point_type = '{self.ISSUE_TYPE_WEAKNESS}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_TWELVE}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_TWELVE}' AND qbo.option_value = '{self.NUMERICAL_OPTION_TWO}'),
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.talking_point WHERE text = '{self.QUESTION_TWELVE_TALKING_POINT_STRENGTH}' AND talking_point_type = '{self.ISSUE_TYPE_STRENGTH}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_TWELVE}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_TWELVE}' AND qbo.option_value = '{self.NUMERICAL_OPTION_SIX}'),
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.talking_point WHERE text = '{self.QUESTION_TWELVE_TALKING_POINT_STRENGTH}' AND talking_point_type = '{self.ISSUE_TYPE_STRENGTH}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_TWELVE}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_TWELVE}' AND qbo.option_value = '{self.NUMERICAL_OPTION_SEVEN}'),
                    2
                ),
                # Question thirteen
                (
                    (SELECT id FROM nano_survey_configuration.talking_point WHERE text = '{self.QUESTION_THIRTEEN_TALKING_POINT_WEAKNESS}' AND talking_point_type = '{self.ISSUE_TYPE_WEAKNESS}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_THIRTEEN}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_THIRTEEN}' AND qbo.option_value = '{self.QUESTION_THIRTEEN_OPTION_ONE}'),
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.talking_point WHERE text = '{self.QUESTION_THIRTEEN_TALKING_POINT_WEAKNESS}' AND talking_point_type = '{self.ISSUE_TYPE_WEAKNESS}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_THIRTEEN}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_THIRTEEN}' AND qbo.option_value = '{self.QUESTION_THIRTEEN_OPTION_TWO}'),
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.talking_point WHERE text = '{self.QUESTION_THIRTEEN_TALKING_POINT_WEAKNESS}' AND talking_point_type = '{self.ISSUE_TYPE_WEAKNESS}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_THIRTEEN}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_THIRTEEN}' AND qbo.option_value = '{self.QUESTION_THIRTEEN_OPTION_THREE}'),
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.talking_point WHERE text = '{self.QUESTION_THIRTEEN_TALKING_POINT_STRENGTH}' AND talking_point_type = '{self.ISSUE_TYPE_STRENGTH}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_THIRTEEN}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_THIRTEEN}' AND qbo.option_value = '{self.QUESTION_THIRTEEN_OPTION_SIX}'),
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.talking_point WHERE text = '{self.QUESTION_THIRTEEN_TALKING_POINT_STRENGTH}' AND talking_point_type = '{self.ISSUE_TYPE_STRENGTH}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_THIRTEEN}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_THIRTEEN}' AND qbo.option_value = '{self.QUESTION_THIRTEEN_OPTION_SEVEN}'),
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.talking_point WHERE text = '{self.QUESTION_THIRTEEN_TALKING_POINT_STRENGTH}' AND talking_point_type = '{self.ISSUE_TYPE_STRENGTH}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_THIRTEEN}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_THIRTEEN}' AND qbo.option_value = '{self.QUESTION_THIRTEEN_OPTION_EIGHT}'),
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.talking_point WHERE text = '{self.QUESTION_THIRTEEN_TALKING_POINT_STRENGTH}' AND talking_point_type = '{self.ISSUE_TYPE_STRENGTH}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_THIRTEEN}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_THIRTEEN}' AND qbo.option_value = '{self.QUESTION_THIRTEEN_OPTION_NINE}'),
                    2
                ),
                # Question fourteen
                (
                    (SELECT id FROM nano_survey_configuration.talking_point WHERE text = '{self.QUESTION_FOURTEEN_TALKING_POINT_WEAKNESS}' AND talking_point_type = '{self.ISSUE_TYPE_WEAKNESS}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_FOURTEEN}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_FOURTEEN}' AND qbo.option_value = '{self.NUMERICAL_OPTION_ONE}'),
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.talking_point WHERE text = '{self.QUESTION_FOURTEEN_TALKING_POINT_WEAKNESS}' AND talking_point_type = '{self.ISSUE_TYPE_WEAKNESS}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_FOURTEEN}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_FOURTEEN}' AND qbo.option_value = '{self.NUMERICAL_OPTION_TWO}'),
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.talking_point WHERE text = '{self.QUESTION_FOURTEEN_TALKING_POINT_STRENGTH}' AND talking_point_type = '{self.ISSUE_TYPE_STRENGTH}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_FOURTEEN}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_FOURTEEN}' AND qbo.option_value = '{self.NUMERICAL_OPTION_SIX}'),
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.talking_point WHERE text = '{self.QUESTION_FOURTEEN_TALKING_POINT_STRENGTH}' AND talking_point_type = '{self.ISSUE_TYPE_STRENGTH}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_FOURTEEN}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_FOURTEEN}' AND qbo.option_value = '{self.NUMERICAL_OPTION_SEVEN}'),
                    2
                ),
                # Question fifteen
                (
                    (SELECT id FROM nano_survey_configuration.talking_point WHERE text = '{self.QUESTION_FIFTEEN_TALKING_POINT_WEAKNESS}' AND talking_point_type = '{self.ISSUE_TYPE_WEAKNESS}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_FIFTEEN}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_FIFTEEN}' AND qbo.option_value = '{self.NUMERICAL_OPTION_ONE}'),
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.talking_point WHERE text = '{self.QUESTION_FIFTEEN_TALKING_POINT_WEAKNESS}' AND talking_point_type = '{self.ISSUE_TYPE_WEAKNESS}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_FIFTEEN}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_FIFTEEN}' AND qbo.option_value = '{self.NUMERICAL_OPTION_TWO}'),
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.talking_point WHERE text = '{self.QUESTION_FIFTEEN_TALKING_POINT_STRENGTH}' AND talking_point_type = '{self.ISSUE_TYPE_STRENGTH}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_FIFTEEN}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_FIFTEEN}' AND qbo.option_value = '{self.NUMERICAL_OPTION_SIX}'),
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.talking_point WHERE text = '{self.QUESTION_FIFTEEN_TALKING_POINT_STRENGTH}' AND talking_point_type = '{self.ISSUE_TYPE_STRENGTH}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_FIFTEEN}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_FIFTEEN}' AND qbo.option_value = '{self.NUMERICAL_OPTION_SEVEN}'),
                    2
                );
            """
        }

        self.sql_dictionary = collections.OrderedDict(sorted(self.sql.items()))
