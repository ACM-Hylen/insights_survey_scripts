
from sql.nano_survey_configuration.base_migration import BaseMigration
import collections

class MigrationScript(BaseMigration):
    """
        Check-in Survey Fall 2020 Non-Residential
    """
    sql = None
    sql_dictionary = None

    SURVEY_TEMPLATE_INTERNAL_KEY = 'check_in_fall_2020_non_residential'

    # Purpose text
    SURVEY_WHY_TEXT = 'By asking students to answer these questions, we can provide you with actionable data. These insights and reports will help foster student success.'
    SURVEY_HOW_TEXT = 'To capture quick, meaningful insights, we took some of the best questions from the Mapworks Transition Survey. The content was built and tested over 3 decades using data from 200+ institutions and 1 million+ students. We reduced this survey to cover the most critical questions. This focused content was vetted with student success practitioners and students.'
    SURVEY_HOVER_TEXT = 'Identify students in need of support and get actionable data to help students succeed.'
    # New questions
    SURVEY_QUESTION_ONE = '   To what degree are you keeping current with your academic work?'
    SURVEY_QUESTION_TWO = '   How many of your scheduled classes have you attended this term?'
    SURVEY_QUESTION_THREE = '   How many courses are you struggling in?'
    SURVEY_QUESTION_FOUR = '   To what degree are you certain that you can do well in your hardest course?'
    SURVEY_QUESTION_FIVE = "   To what degree are you confident that you can pay for next term's tuition and fees?"
    SURVEY_QUESTION_SIX = "   To what degree do you intend to come back to this institution for the next academic term? (If you are graduating this term, please leave this question blank.)"
    SURVEY_QUESTION_SEVEN = '   How would you rate your experience at this institution?'
    SURVEY_QUESTION_EIGHT = '   To what degree do you belong here?'
    SURVEY_QUESTION_NINE = '   During this term, to what degree do you intend to participate in a student organization?'
    SURVEY_QUESTION_TEN = '   To what degree are you experiencing stress because of COVID-19 health and safety concerns at your institution?'
    SURVEY_QUESTION_ELEVEN = '   To what degree are you able to access campus services online?'

    # Categorical question options
    QUESTION_TWO_OPTION_ONE = 'I attended all my classes.'
    QUESTION_TWO_OPTION_TWO = 'I missed one class.'
    QUESTION_TWO_OPTION_THREE = 'I missed a few classes.'
    QUESTION_TWO_OPTION_FOUR = 'I missed class frequently'
    QUESTION_TWO_OPTION_FIVE = 'I missed class most of the time'
    QUESTION_THREE_OPTION_ONE = 'Not struggling in any course'
    QUESTION_THREE_OPTION_TWO = '1 course'
    QUESTION_THREE_OPTION_THREE = '2 courses'
    QUESTION_THREE_OPTION_FOUR = '3 courses'
    QUESTION_THREE_OPTION_FIVE = '4 courses'
    QUESTION_THREE_OPTION_SIX = '5 courses'
    QUESTION_THREE_OPTION_SEVEN = 'More than 5 courses'

    # Issue text for this template
    ISSUE_ACADEMIC_COURSEWORK = "Academic Coursework - Fall 2020 Check in"
    ISSUE_CLASS_ATTENDANCE = "Class Attendance - Missed class (self-report) - Fall 2020 Check in"
    ISSUE_COURSE_STRUGGLES = "Course Struggles - Fall 2020 Check in"
    ISSUE_SELF_EFFICACY = "Self-Efficacy - Fall 2020 Check in"
    ISSUE_FINANCIAL_MEANS = "Financial Means - Fall 2020 Check in"
    ISSUE_INTENT_TO_RETURN = "Intent to Return - Fall 2020 Check in"
    ISSUE_SATISFACTION = "Overall Satisfaction - Fall 2020 Check in"
    ISSUE_SENSE_OF_BELONGING = "Sense of Belonging  - Fall 2020 Check in"
    ISSUE_STUDENT_INVOLVEMENT = "Student Involvement - Fall 2020 Check in"
    ISSUE_HEALTH_RELATED_STRESS = "Health-Related Stress - Fall 2020 Check in"
    ONLINE_CAMPUS_SERVICES = "Online Campus Services - Fall 2020 Check in"

    # Talking Points
    QUESTION_ONE_TALKING_POINT_WEAKNESS = 'Student is struggling to stay current with coursework.'
    QUESTION_ONE_TALKING_POINT_STRENGTH = 'Student is up to date with coursework.'
    QUESTION_ONE_NEXT_STEPS = 'Help students understand the importance of completing assignments and required reading. Students may not understand the long term implications of poor preparedness on their academic success.'
    QUESTION_TWO_TALKING_POINT_WEAKNESS = 'Routinely misses classes (i.e., frequently or most of the time). Strong predictor of academic performance. Explore reasons for class absences.'
    QUESTION_TWO_TALKING_POINT_STRENGTH = 'Reports having attended every class to date.'
    QUESTION_TWO_NEXT_STEPS = 'Routinely misses classes is a strong predictor of academic performance. Students transitioning to college may enjoy the freedom of their schedule and may need assistance understanding the importance of attending class.'
    QUESTION_THREE_TALKING_POINT_WEAKNESS = 'Struggling in two or more courses. Strong predictor of poor academic performance. Discuss issues, encourage meeting with instructors, and refer to learning resources.'
    QUESTION_THREE_TALKING_POINT_STRENGTH = 'Reports no serious course difficulties at this time.'
    QUESTION_THREE_NEXT_STEPS = 'Students report struggling in at least one course. Communicate the academic resources available to these students.'
    QUESTION_FOUR_TALKING_POINT_WEAKNESS = 'Student is not confident they will do well in their hardest course.'
    QUESTION_FOUR_TALKING_POINT_STRENGTH = 'Student is confident in their ability to do well in difficult courses'
    QUESTION_FOUR_NEXT_STEPS = 'Students with low self-efficacy need additional support to increase their self-confidence. First-year students may need help adapting their skills and confidence to the rigor of this institution.'
    QUESTION_FIVE_TALKING_POINT_WEAKNESS = "Student expects difficulties paying this term's tuition and fees. Resolving these issues before classes begin can help reduce stress and enable students to register for future terms. Refer this student to financial aid resources."
    QUESTION_FIVE_NEXT_STEPS = 'Students who lack confidence to pay their tuition and fees may experience stress from upcoming bills and may need support. Ensure students know about the financial aid office and services available to them.'
    QUESTION_SIX_TALKING_POINT_WEAKNESS = 'Student is unlikely to return next term. This response is a strong predictor of attrition.'
    QUESTION_SIX_TALKING_POINT_STRENGTH = 'Student intends to return next term.'
    QUESTION_SIX_NEXT_STEPS = "Students who say they don't intend to return, often don't. Intervening with these students may help them to continue their education."
    QUESTION_SEVEN_TALKING_POINT_WEAKNESS = 'Student reports low satisfaction with the institution.'
    QUESTION_SEVEN_TALKING_POINT_STRENGTH = 'Student reports high satisfaction with the institution.'
    QUESTION_SEVEN_NEXT_STEPS = 'Dissatisfaction with the institution is correlated with lower retention. Identifying the cause of their dissatisfaction may help retain the student at the institution.'
    QUESTION_EIGHT_TALKING_POINT_WEAKNESS = "Doesn't feel he/she belongs at this school. Strong predictor of attrition. Explore issue(s), discuss getting involved in student organizations."
    QUESTION_EIGHT_TALKING_POINT_STRENGTH = 'Feels he/she belongs at this school. Strong predictor of retention.'
    QUESTION_EIGHT_NEXT_STEPS = 'Help students make connections to peers and organizations on campus and in the community.'
    QUESTION_NINE_TALKING_POINT_WEAKNESS = 'Low interest in campus activities. Campus involvement helps students integrate. Explore lack of interest in campus involvement.'
    QUESTION_NINE_TALKING_POINT_STRENGTH = 'Very interested in being involved in campus activities. Support efforts to get involved.'
    QUESTION_NINE_NEXT_STEPS = 'Help students find opportunities to connect with other students.'
    QUESTION_TEN_TALKING_POINT_WEAKNESS = 'This student is experiencing stress related to COVID-19 and attending this institution. Ensure this student knows what the institution is doing to ensure health and safety.'
    QUESTION_TEN_TALKING_POINT_STRENGTH = 'Student does not report stress related to attending class amid the changes caused by COVID-19.'
    QUESTION_TEN_NEXT_STEPS = 'Keep students informed about what the institution is doing to keep the campus community safe. Students may need support or feel heard about concerns.'
    QUESTION_ELEVEN_TALKING_POINT_WEAKNESS = 'Student is having difficulty accessing campus services online.'
    QUESTION_ELEVEN_TALKING_POINT_STRENGTH = 'Student is able to access campus services online.'
    QUESTION_ELEVEN_NEXT_STEPS = 'Students who struggle to access campus services may be at increased risk of not returning to the institution. Reach out to these students to further investigate why they are having difficulty accessing services or provide them with resources on how to access services virtually.'

    # Other
    CONSENT_STATEMENT = "Macmillan Learning is conducting the following survey on behalf of your organization/institution. Your survey responses are submitted to us utilizing data encryption methodology (SSL) used to protect financial transactions conducted over the internet and we handle your data pursuant to the <a target='_blank' href='https://store.macmillanlearning.com/us/privacy-notice'>Macmillan Learning Privacy Notice.</a> Your responses will be collected by us in a personally identifiable format and we will provide it to your organization/institutions linked to your personal identifiers.  Your organization/institution can use your personal information and survey results pursuant to their own Privacy Policy, including using the results of your survey responses in an aggregated and anonymized form in connection with its presentations, reports and publications. Macmillan Learning may de-identify your survey responses and analyze the data to improve its educational products and services, including to create aggregated or statistical insights and baseline reports that are not identifiable to you or any other individual for use in other Macmillan Learning educational products and services.  If you prefer not to participate in this survey, you may leave questions blank or close the browser and leave the survey.  Contact your organisation/institution for more information about its use of the responses."

    def __init__(self):
        super().__init__()
        self.sql = {
            1: f"""
                INSERT INTO nano_survey_configuration.survey_template (title, internal_key, hover_text, time_to_complete, user_data_consent_statement, created_by, modified_by) VALUES
                ('Check-in Survey Fall 2020 Non-Residential', '{self.SURVEY_TEMPLATE_INTERNAL_KEY}', '{self.SURVEY_HOVER_TEXT}', 6, "{self.CONSENT_STATEMENT}", 2, 2);
            """,
            2: f"""
                INSERT INTO nano_survey_configuration.survey_purpose (section, purpose_text, section_title, icon_filename, created_by, modified_by) VALUES
                ('How', '{self.SURVEY_HOW_TEXT}', 'How was this survey created?', 'question_mark_in_lightbulb.svg', 2, 2)
                ;
            """,
            3: f"""
                INSERT INTO nano_survey_configuration.question_bank (question_text, alternate_question_text, question_type, created_by, modified_by) VALUES
                ('{self.SURVEY_QUESTION_ONE}', '', '{self.TEXT_SCALED}', 2, 2),
                ('{self.SURVEY_QUESTION_TWO}', '', '{self.TEXT_CATEGORICAL}', 2, 2),
                ('{self.SURVEY_QUESTION_THREE}', '', '{self.TEXT_CATEGORICAL}', 2, 2),
                ('{self.SURVEY_QUESTION_FOUR}', '', '{self.TEXT_SCALED}', 2, 2),
                ("{self.SURVEY_QUESTION_FIVE}", '', '{self.TEXT_SCALED}', 2, 2),
                ("{self.SURVEY_QUESTION_SIX}", '', '{self.TEXT_SCALED}', 2, 2),
                ('{self.SURVEY_QUESTION_SEVEN}', '', '{self.TEXT_SCALED}', 2, 2),
                ('{self.SURVEY_QUESTION_EIGHT}', '', '{self.TEXT_SCALED}', 2, 2),
                ('{self.SURVEY_QUESTION_NINE}', '', '{self.TEXT_SCALED}', 2, 2),
                ('{self.SURVEY_QUESTION_TEN}', '', '{self.TEXT_SCALED}', 2, 2),
                ('{self.SURVEY_QUESTION_ELEVEN}', '', '{self.TEXT_SCALED}', 2, 2),
                ('{self.SURVEY_QUESTION_TWELVE}', '', '{self.TEXT_SCALED}', 2, 2);
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
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_TWO}' AND question_type = '{self.TEXT_CATEGORICAL}'),
                    '{self.QUESTION_TWO_OPTION_ONE}',
                    null,
                    '{self.TYPE_STRING}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_TWO}' AND question_type = '{self.TEXT_CATEGORICAL}'),
                    '{self.QUESTION_TWO_OPTION_TWO}',
                    null,
                    '{self.TYPE_STRING}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_TWO}' AND question_type = '{self.TEXT_CATEGORICAL}'),
                    '{self.QUESTION_TWO_OPTION_THREE}',
                    null,
                    '{self.TYPE_STRING}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_TWO}' AND question_type = '{self.TEXT_CATEGORICAL}'),
                    '{self.QUESTION_TWO_OPTION_FOUR}',
                    null,
                    '{self.TYPE_STRING}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_TWO}' AND question_type = '{self.TEXT_CATEGORICAL}'),
                    '{self.QUESTION_TWO_OPTION_FIVE}',
                    null,
                    '{self.TYPE_STRING}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_TWO}' AND question_type = '{self.TEXT_CATEGORICAL}'),
                    '{self.NUMERICAL_OPTION_99}',
                    'Not Applicable',
                    '{self.TYPE_STRING}',
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
                    '{self.QUESTION_THREE_OPTION_SIX}',
                    null,
                    '{self.TYPE_STRING}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_THREE}' AND question_type = '{self.TEXT_CATEGORICAL}'),
                    '{self.QUESTION_THREE_OPTION_SEVEN}',
                    'Extremely',
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
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_FOUR}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.NUMERICAL_OPTION_ONE}',
                    'Not at All',
                    '{self.TYPE_INTEGER}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_FOUR}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.NUMERICAL_OPTION_TWO}',
                    null,
                    '{self.TYPE_INTEGER}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_FOUR}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.NUMERICAL_OPTION_THREE}',
                    null,
                    '{self.TYPE_INTEGER}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_FOUR}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.NUMERICAL_OPTION_FOUR}',
                    null,
                    '{self.TYPE_INTEGER}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_FOUR}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.NUMERICAL_OPTION_FIVE}',
                    null,
                    '{self.TYPE_INTEGER}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_FOUR}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.NUMERICAL_OPTION_SIX}',
                    null,
                    '{self.TYPE_INTEGER}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_FOUR}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.NUMERICAL_OPTION_SEVEN}',
                    'Extremely',
                    '{self.TYPE_INTEGER}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_FOUR}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.NUMERICAL_OPTION_99}',
                    'Not Applicable',
                    '{self.TYPE_INTEGER}',
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
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = "{self.SURVEY_QUESTION_SIX}" AND question_type = '{self.TEXT_SCALED}'),
                    '{self.NUMERICAL_OPTION_ONE}',
                    'Not at All',
                    '{self.TYPE_INTEGER}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = "{self.SURVEY_QUESTION_SIX}"  AND question_type = '{self.TEXT_SCALED}'),
                    '{self.NUMERICAL_OPTION_TWO}',
                    null,
                    '{self.TYPE_INTEGER}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = "{self.SURVEY_QUESTION_SIX}"  AND question_type = '{self.TEXT_SCALED}'),
                    '{self.NUMERICAL_OPTION_THREE}',
                    null,
                    '{self.TYPE_INTEGER}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = "{self.SURVEY_QUESTION_SIX}"  AND question_type = '{self.TEXT_SCALED}'),
                    '{self.NUMERICAL_OPTION_FOUR}',
                    null,
                    '{self.TYPE_INTEGER}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = "{self.SURVEY_QUESTION_SIX}"  AND question_type = '{self.TEXT_SCALED}'),
                    '{self.NUMERICAL_OPTION_FIVE}',
                    null,
                    '{self.TYPE_INTEGER}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = "{self.SURVEY_QUESTION_SIX}" AND question_type = '{self.TEXT_SCALED}'),
                    '{self.NUMERICAL_OPTION_SIX}',
                    null,
                    '{self.TYPE_INTEGER}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = "{self.SURVEY_QUESTION_SIX}"  AND question_type = '{self.TEXT_SCALED}'),
                    '{self.NUMERICAL_OPTION_SEVEN}',
                    'Extremely',
                    '{self.TYPE_INTEGER}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = "{self.SURVEY_QUESTION_SIX}"  AND question_type = '{self.TEXT_SCALED}'),
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
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_TWO}' AND question_type = '{self.TEXT_CATEGORICAL}'),
                    '{self.ISSUE_CLASS_ATTENDANCE}',
                    '{self.ISSUE_TYPE_WEAKNESS}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.reporting_category WHERE text = '{self.REPORTING_CATEGORY_ACADEMIC}'),
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_TWO}' AND question_type = '{self.TEXT_CATEGORICAL}'),
                    '{self.ISSUE_CLASS_ATTENDANCE}',
                    '{self.ISSUE_TYPE_STRENGTH}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.reporting_category WHERE text = '{self.REPORTING_CATEGORY_ACADEMIC}'),
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_THREE}' AND question_type = '{self.TEXT_CATEGORICAL}'),
                    '{self.ISSUE_COURSE_STRUGGLES}',
                    '{self.ISSUE_TYPE_WEAKNESS}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.reporting_category WHERE text = '{self.REPORTING_CATEGORY_ACADEMIC}'),
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_THREE}' AND question_type = '{self.TEXT_CATEGORICAL}'),
                    '{self.ISSUE_COURSE_STRUGGLES}',
                    '{self.ISSUE_TYPE_STRENGTH}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.reporting_category WHERE text = '{self.REPORTING_CATEGORY_ACADEMIC}'),
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_FOUR}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.ISSUE_SELF_EFFICACY}',
                    '{self.ISSUE_TYPE_WEAKNESS}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.reporting_category WHERE text = '{self.REPORTING_CATEGORY_ACADEMIC}'),
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_FOUR}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.ISSUE_SELF_EFFICACY}',
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
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = "{self.SURVEY_QUESTION_SIX}" AND question_type = '{self.TEXT_SCALED}'),
                    '{self.ISSUE_INTENT_TO_RETURN}',
                    '{self.ISSUE_TYPE_WEAKNESS}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.reporting_category WHERE text = '{self.REPORTING_CATEGORY_INSTITUTIONAL}'),
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = "{self.SURVEY_QUESTION_SIX}" AND question_type = '{self.TEXT_SCALED}'),
                    '{self.ISSUE_INTENT_TO_RETURN}',
                    '{self.ISSUE_TYPE_STRENGTH}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.reporting_category WHERE text = '{self.REPORTING_CATEGORY_INSTITUTIONAL}'),
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_SEVEN}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.ISSUE_SATISFACTION}',
                    '{self.ISSUE_TYPE_WEAKNESS}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.reporting_category WHERE text = '{self.REPORTING_CATEGORY_INSTITUTIONAL}'),
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_SEVEN}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.ISSUE_SATISFACTION}',
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
                    (SELECT id FROM nano_survey_configuration.reporting_category WHERE text = '{self.REPORTING_CATEGORY_SOCIAL}'),
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_NINE}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.ISSUE_STUDENT_INVOLVEMENT}',
                    '{self.ISSUE_TYPE_WEAKNESS}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.reporting_category WHERE text = '{self.REPORTING_CATEGORY_SOCIAL}'),
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_NINE}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.ISSUE_STUDENT_INVOLVEMENT}',
                    '{self.ISSUE_TYPE_STRENGTH}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.reporting_category WHERE text = '{self.REPORTING_CATEGORY_INSTITUTIONAL}'),
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_TEN}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.ISSUE_HEALTH_RELATED_STRESS}',
                    '{self.ISSUE_TYPE_WEAKNESS}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.reporting_category WHERE text = '{self.REPORTING_CATEGORY_INSTITUTIONAL}'),
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_TEN}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.ISSUE_HEALTH_RELATED_STRESS}',
                    '{self.ISSUE_TYPE_STRENGTH}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.reporting_category WHERE text = '{self.REPORTING_CATEGORY_INSTITUTIONAL}'),
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_ELEVEN}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.ONLINE_CAMPUS_SERVICES}',
                    '{self.ISSUE_TYPE_WEAKNESS}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.reporting_category WHERE text = '{self.REPORTING_CATEGORY_INSTITUTIONAL}'),
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_ELEVEN}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.ONLINE_CAMPUS_SERVICES}',
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
                    (SELECT id FROM nano_survey_configuration.issue WHERE issue_text = '{self.ISSUE_CLASS_ATTENDANCE}' AND issue_type = '{self.ISSUE_TYPE_WEAKNESS}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_TWO}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_TWO}' AND qbo.option_value = '{self.QUESTION_TWO_OPTION_THREE}'),
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.issue WHERE issue_text = '{self.ISSUE_CLASS_ATTENDANCE}' AND issue_type = '{self.ISSUE_TYPE_WEAKNESS}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_TWO}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_TWO}' AND qbo.option_value = '{self.QUESTION_TWO_OPTION_FOUR}'),
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.issue WHERE issue_text = '{self.ISSUE_CLASS_ATTENDANCE}' AND issue_type = '{self.ISSUE_TYPE_WEAKNESS}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_TWO}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_TWO}' AND qbo.option_value = '{self.QUESTION_TWO_OPTION_FIVE}'),
                    2
                ),
                # Question two strength values
                (
                    (SELECT id FROM nano_survey_configuration.issue WHERE issue_text = '{self.ISSUE_CLASS_ATTENDANCE}' AND issue_type = '{self.ISSUE_TYPE_STRENGTH}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_TWO}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_TWO}' AND qbo.option_value = '{self.QUESTION_TWO_OPTION_ONE}'),
                    2
                ),
                # Question three weakness values
                (
                    (SELECT id FROM nano_survey_configuration.issue WHERE issue_text = '{self.ISSUE_COURSE_STRUGGLES}' AND issue_type = '{self.ISSUE_TYPE_WEAKNESS}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_THREE}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_THREE}' AND qbo.option_value = '{self.QUESTION_THREE_OPTION_TWO}'),
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.issue WHERE issue_text = '{self.ISSUE_COURSE_STRUGGLES}' AND issue_type = '{self.ISSUE_TYPE_WEAKNESS}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_THREE}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_THREE}' AND qbo.option_value = '{self.QUESTION_THREE_OPTION_THREE}'),
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.issue WHERE issue_text = '{self.ISSUE_COURSE_STRUGGLES}' AND issue_type = '{self.ISSUE_TYPE_WEAKNESS}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_THREE}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_THREE}' AND qbo.option_value = '{self.QUESTION_THREE_OPTION_FOUR}'),
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.issue WHERE issue_text = '{self.ISSUE_COURSE_STRUGGLES}' AND issue_type = '{self.ISSUE_TYPE_WEAKNESS}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_THREE}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_THREE}' AND qbo.option_value = '{self.QUESTION_THREE_OPTION_FIVE}'),
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.issue WHERE issue_text = '{self.ISSUE_COURSE_STRUGGLES}' AND issue_type = '{self.ISSUE_TYPE_WEAKNESS}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_THREE}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_THREE}' AND qbo.option_value = '{self.QUESTION_THREE_OPTION_SIX}'),
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.issue WHERE issue_text = '{self.ISSUE_COURSE_STRUGGLES}' AND issue_type = '{self.ISSUE_TYPE_WEAKNESS}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_THREE}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_THREE}' AND qbo.option_value = '{self.QUESTION_THREE_OPTION_SEVEN}'),
                    2
                ),
                # Question three strength values
                (
                    (SELECT id FROM nano_survey_configuration.issue WHERE issue_text = '{self.ISSUE_COURSE_STRUGGLES}' AND issue_type = '{self.ISSUE_TYPE_STRENGTH}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_THREE}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_THREE}' AND qbo.option_value = '{self.QUESTION_THREE_OPTION_ONE}'),
                    2
                ),
                # Question four weakness values
                (
                    (SELECT id FROM nano_survey_configuration.issue WHERE issue_text = '{self.ISSUE_SELF_EFFICACY}' AND issue_type = '{self.ISSUE_TYPE_WEAKNESS}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_FOUR}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_FOUR}' AND qbo.option_value = '{self.NUMERICAL_OPTION_ONE}'),
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.issue WHERE issue_text = '{self.ISSUE_SELF_EFFICACY}' AND issue_type = '{self.ISSUE_TYPE_WEAKNESS}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_FOUR}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_FOUR}' AND qbo.option_value = '{self.NUMERICAL_OPTION_TWO}'),
                    2
                ),
                # Question four strength values
                (
                    (SELECT id FROM nano_survey_configuration.issue WHERE issue_text = '{self.ISSUE_SELF_EFFICACY}' AND issue_type = '{self.ISSUE_TYPE_STRENGTH}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_FOUR}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_FOUR}' AND qbo.option_value = '{self.NUMERICAL_OPTION_SIX}'),
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.issue WHERE issue_text = '{self.ISSUE_SELF_EFFICACY}' AND issue_type = '{self.ISSUE_TYPE_STRENGTH}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_FOUR}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_FOUR}' AND qbo.option_value = '{self.NUMERICAL_OPTION_SEVEN}'),
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
                    (SELECT id FROM nano_survey_configuration.issue WHERE issue_text = '{self.ISSUE_INTENT_TO_RETURN}' AND issue_type = '{self.ISSUE_TYPE_WEAKNESS}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = "{self.SURVEY_QUESTION_SIX}")),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = "{self.SURVEY_QUESTION_SIX}" AND qbo.option_value = '{self.NUMERICAL_OPTION_ONE}'),
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.issue WHERE issue_text = '{self.ISSUE_INTENT_TO_RETURN}' AND issue_type = '{self.ISSUE_TYPE_WEAKNESS}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = "{self.SURVEY_QUESTION_SIX}")),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = "{self.SURVEY_QUESTION_SIX}" AND qbo.option_value = '{self.NUMERICAL_OPTION_TWO}'),
                    2
                ),
                # Question six strength values
                (
                    (SELECT id FROM nano_survey_configuration.issue WHERE issue_text = '{self.ISSUE_INTENT_TO_RETURN}' AND issue_type = '{self.ISSUE_TYPE_STRENGTH}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = "{self.SURVEY_QUESTION_SIX}")),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = "{self.SURVEY_QUESTION_SIX}" AND qbo.option_value = '{self.NUMERICAL_OPTION_SIX}'),
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.issue WHERE issue_text = '{self.ISSUE_INTENT_TO_RETURN}' AND issue_type = '{self.ISSUE_TYPE_STRENGTH}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = "{self.SURVEY_QUESTION_SIX}")),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = "{self.SURVEY_QUESTION_SIX}" AND qbo.option_value = '{self.NUMERICAL_OPTION_SEVEN}'),
                    2
                ),
                # Question seven weakness values
                (
                    (SELECT id FROM nano_survey_configuration.issue WHERE issue_text = '{self.ISSUE_SATISFACTION}' AND issue_type = '{self.ISSUE_TYPE_WEAKNESS}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_SEVEN}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_SEVEN}' AND qbo.option_value = '{self.NUMERICAL_OPTION_ONE}'),
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.issue WHERE issue_text = '{self.ISSUE_SATISFACTION}' AND issue_type = '{self.ISSUE_TYPE_WEAKNESS}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_SEVEN}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_SEVEN}' AND qbo.option_value = '{self.NUMERICAL_OPTION_TWO}'),
                    2
                ),
                # Question seven strength values
                (
                    (SELECT id FROM nano_survey_configuration.issue WHERE issue_text = '{self.ISSUE_SATISFACTION}' AND issue_type = '{self.ISSUE_TYPE_STRENGTH}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_SEVEN}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_SEVEN}' AND qbo.option_value = '{self.NUMERICAL_OPTION_SIX}'),
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.issue WHERE issue_text = '{self.ISSUE_SATISFACTION}' AND issue_type = '{self.ISSUE_TYPE_STRENGTH}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_SEVEN}')),
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
                # Question nine weakness values
                (
                    (SELECT id FROM nano_survey_configuration.issue WHERE issue_text = '{self.ISSUE_STUDENT_INVOLVEMENT}' AND issue_type = '{self.ISSUE_TYPE_WEAKNESS}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_NINE}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_NINE}' AND qbo.option_value = '{self.NUMERICAL_OPTION_ONE}'),
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.issue WHERE issue_text = '{self.ISSUE_STUDENT_INVOLVEMENT}' AND issue_type = '{self.ISSUE_TYPE_WEAKNESS}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_NINE}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_NINE}' AND qbo.option_value = '{self.NUMERICAL_OPTION_TWO}'),
                    2
                ),
                # Question nine strength values
                (
                    (SELECT id FROM nano_survey_configuration.issue WHERE issue_text = '{self.ISSUE_STUDENT_INVOLVEMENT}' AND issue_type = '{self.ISSUE_TYPE_STRENGTH}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_NINE}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_NINE}' AND qbo.option_value = '{self.NUMERICAL_OPTION_SIX}'),
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.issue WHERE issue_text = '{self.ISSUE_STUDENT_INVOLVEMENT}' AND issue_type = '{self.ISSUE_TYPE_STRENGTH}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_NINE}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_NINE}' AND qbo.option_value = '{self.NUMERICAL_OPTION_SEVEN}'),
                    2
                ),
                # Question ten weakness values inverse
                (
                    (SELECT id FROM nano_survey_configuration.issue WHERE issue_text = '{self.ISSUE_HEALTH_RELATED_STRESS}' AND issue_type = '{self.ISSUE_TYPE_WEAKNESS}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_TEN}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_TEN}' AND qbo.option_value = '{self.NUMERICAL_OPTION_SIX}'),
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.issue WHERE issue_text = '{self.ISSUE_HEALTH_RELATED_STRESS}' AND issue_type = '{self.ISSUE_TYPE_WEAKNESS}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_TEN}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_TEN}' AND qbo.option_value = '{self.NUMERICAL_OPTION_SEVEN}'),
                    2
                ),
                # Question ten strength values inverse
                (
                    (SELECT id FROM nano_survey_configuration.issue WHERE issue_text = '{self.ISSUE_HEALTH_RELATED_STRESS}' AND issue_type = '{self.ISSUE_TYPE_STRENGTH}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_TEN}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_TEN}' AND qbo.option_value = '{self.NUMERICAL_OPTION_ONE}'),
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.issue WHERE issue_text = '{self.ISSUE_HEALTH_RELATED_STRESS}' AND issue_type = '{self.ISSUE_TYPE_STRENGTH}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_TEN}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_TEN}' AND qbo.option_value = '{self.NUMERICAL_OPTION_TWO}'),
                    2
                ),
                # Question eleven weakness values
                (
                    (SELECT id FROM nano_survey_configuration.issue WHERE issue_text = '{self.ONLINE_CAMPUS_SERVICES}' AND issue_type = '{self.ISSUE_TYPE_WEAKNESS}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_ELEVEN}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_ELEVEN}' AND qbo.option_value = '{self.NUMERICAL_OPTION_ONE}'),
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.issue WHERE issue_text = '{self.ONLINE_CAMPUS_SERVICES}' AND issue_type = '{self.ISSUE_TYPE_WEAKNESS}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_ELEVEN}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_ELEVEN}' AND qbo.option_value = '{self.NUMERICAL_OPTION_TWO}'),
                    2
                ),
                # Question eleven strength values
                (
                    (SELECT id FROM nano_survey_configuration.issue WHERE issue_text = '{self.ONLINE_CAMPUS_SERVICES}' AND issue_type = '{self.ISSUE_TYPE_STRENGTH}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_ELEVEN}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_ELEVEN}' AND qbo.option_value = '{self.NUMERICAL_OPTION_SIX}'),
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.issue WHERE issue_text = '{self.ONLINE_CAMPUS_SERVICES}' AND issue_type = '{self.ISSUE_TYPE_STRENGTH}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_ELEVEN}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_ELEVEN}' AND qbo.option_value = '{self.NUMERICAL_OPTION_SEVEN}'),
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
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_TWO}' AND question_type = '{self.TEXT_CATEGORICAL}'),
                    2,
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
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_FOUR}' AND question_type = '{self.TEXT_SCALED}'),
                    4,
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
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = "{self.SURVEY_QUESTION_SIX}" AND question_type = '{self.TEXT_SCALED}'),
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
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_TWO}' AND question_type = '{self.TEXT_CATEGORICAL}'),
                    '{self.ISSUE_TYPE_WEAKNESS}',
                    '{self.QUESTION_TWO_TALKING_POINT_WEAKNESS}',
                    '{self.QUESTION_TWO_NEXT_STEPS}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_TWO}' AND question_type = '{self.TEXT_CATEGORICAL}'),
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
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_FOUR}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.ISSUE_TYPE_WEAKNESS}',
                    '{self.QUESTION_FOUR_TALKING_POINT_WEAKNESS}',
                    '{self.QUESTION_FOUR_NEXT_STEPS}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_FOUR}' AND question_type = '{self.TEXT_SCALED}'),
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
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = "{self.SURVEY_QUESTION_SIX}" AND question_type = '{self.TEXT_SCALED}'),
                    '{self.ISSUE_TYPE_WEAKNESS}',
                    '{self.QUESTION_SIX_TALKING_POINT_WEAKNESS}',
                    "{self.QUESTION_SIX_NEXT_STEPS}",
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = "{self.SURVEY_QUESTION_SIX}" AND question_type = '{self.TEXT_SCALED}'),
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
                    '{self.QUESTION_TEN_NEXT_STEPS}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_TEN}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.ISSUE_TYPE_STRENGTH}',
                    '{self.QUESTION_TEN_TALKING_POINT_STRENGTH}',
                    null,
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
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_TWO}' AND qbo.option_value = '{self.QUESTION_TWO_OPTION_THREE}'),
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.talking_point WHERE text = '{self.QUESTION_TWO_TALKING_POINT_WEAKNESS}' AND talking_point_type = '{self.ISSUE_TYPE_WEAKNESS}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_TWO}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_TWO}' AND qbo.option_value = '{self.QUESTION_TWO_OPTION_FOUR}'),
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.talking_point WHERE text = '{self.QUESTION_TWO_TALKING_POINT_WEAKNESS}' AND talking_point_type = '{self.ISSUE_TYPE_WEAKNESS}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_TWO}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_TWO}' AND qbo.option_value = '{self.QUESTION_TWO_OPTION_FIVE}'),
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.talking_point WHERE text = '{self.QUESTION_TWO_TALKING_POINT_STRENGTH}' AND talking_point_type = '{self.ISSUE_TYPE_STRENGTH}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_TWO}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_TWO}' AND qbo.option_value = '{self.QUESTION_TWO_OPTION_ONE}'),
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
                    (SELECT id FROM nano_survey_configuration.talking_point WHERE text = '{self.QUESTION_THREE_TALKING_POINT_WEAKNESS}' AND talking_point_type = '{self.ISSUE_TYPE_WEAKNESS}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_THREE}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_THREE}' AND qbo.option_value = '{self.QUESTION_THREE_OPTION_SIX}'),
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.talking_point WHERE text = '{self.QUESTION_THREE_TALKING_POINT_WEAKNESS}' AND talking_point_type = '{self.ISSUE_TYPE_WEAKNESS}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_THREE}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_THREE}' AND qbo.option_value = '{self.QUESTION_THREE_OPTION_SEVEN}'),
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
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_FOUR}' AND qbo.option_value = '{self.NUMERICAL_OPTION_ONE}'),
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.talking_point WHERE text = '{self.QUESTION_FOUR_TALKING_POINT_WEAKNESS}' AND talking_point_type = '{self.ISSUE_TYPE_WEAKNESS}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_FOUR}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_FOUR}' AND qbo.option_value = '{self.NUMERICAL_OPTION_TWO}'),
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.talking_point WHERE text = '{self.QUESTION_FOUR_TALKING_POINT_STRENGTH}' AND talking_point_type = '{self.ISSUE_TYPE_STRENGTH}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_FOUR}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_FOUR}' AND qbo.option_value = '{self.NUMERICAL_OPTION_SIX}'),
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.talking_point WHERE text = '{self.QUESTION_FOUR_TALKING_POINT_STRENGTH}' AND talking_point_type = '{self.ISSUE_TYPE_STRENGTH}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_FOUR}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_FOUR}' AND qbo.option_value = '{self.NUMERICAL_OPTION_SEVEN}'),
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
                    (SELECT id FROM nano_survey_configuration.talking_point WHERE text = '{self.QUESTION_SIX_TALKING_POINT_WEAKNESS}' AND talking_point_type = '{self.ISSUE_TYPE_WEAKNESS}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = "{self.SURVEY_QUESTION_SIX}")),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = "{self.SURVEY_QUESTION_SIX}" AND qbo.option_value = '{self.NUMERICAL_OPTION_ONE}'),
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.talking_point WHERE text = '{self.QUESTION_SIX_TALKING_POINT_WEAKNESS}' AND talking_point_type = '{self.ISSUE_TYPE_WEAKNESS}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = "{self.SURVEY_QUESTION_SIX}")),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = "{self.SURVEY_QUESTION_SIX}" AND qbo.option_value = '{self.NUMERICAL_OPTION_TWO}'),
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.talking_point WHERE text = '{self.QUESTION_SIX_TALKING_POINT_STRENGTH}' AND talking_point_type = '{self.ISSUE_TYPE_STRENGTH}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = "{self.SURVEY_QUESTION_SIX}")),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = "{self.SURVEY_QUESTION_SIX}" AND qbo.option_value = '{self.NUMERICAL_OPTION_SIX}'),
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.talking_point WHERE text = '{self.QUESTION_SIX_TALKING_POINT_STRENGTH}' AND talking_point_type = '{self.ISSUE_TYPE_STRENGTH}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = "{self.SURVEY_QUESTION_SIX}")),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = "{self.SURVEY_QUESTION_SIX}" AND qbo.option_value = '{self.NUMERICAL_OPTION_SEVEN}'),
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
                # Question nine
                (
                    (SELECT id FROM nano_survey_configuration.talking_point WHERE text = '{self.QUESTION_NINE_TALKING_POINT_WEAKNESS}' AND talking_point_type = '{self.ISSUE_TYPE_WEAKNESS}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_NINE}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_NINE}' AND qbo.option_value = '{self.NUMERICAL_OPTION_ONE}'),
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.talking_point WHERE text = '{self.QUESTION_NINE_TALKING_POINT_WEAKNESS}' AND talking_point_type = '{self.ISSUE_TYPE_WEAKNESS}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_NINE}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_NINE}' AND qbo.option_value = '{self.NUMERICAL_OPTION_TWO}'),
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.talking_point WHERE text = '{self.QUESTION_NINE_TALKING_POINT_STRENGTH}' AND talking_point_type = '{self.ISSUE_TYPE_STRENGTH}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_NINE}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_NINE}' AND qbo.option_value = '{self.NUMERICAL_OPTION_SIX}'),
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.talking_point WHERE text = '{self.QUESTION_NINE_TALKING_POINT_STRENGTH}' AND talking_point_type = '{self.ISSUE_TYPE_STRENGTH}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_NINE}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_NINE}' AND qbo.option_value = '{self.NUMERICAL_OPTION_SEVEN}'),
                    2
                ),
                # Question ten inverse
                (
                    (SELECT id FROM nano_survey_configuration.talking_point WHERE text = '{self.QUESTION_TEN_TALKING_POINT_WEAKNESS}' AND talking_point_type = '{self.ISSUE_TYPE_WEAKNESS}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_TEN}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_TEN}' AND qbo.option_value = '{self.NUMERICAL_OPTION_SIX}'),
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.talking_point WHERE text = '{self.QUESTION_TEN_TALKING_POINT_WEAKNESS}' AND talking_point_type = '{self.ISSUE_TYPE_WEAKNESS}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_TEN}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_TEN}' AND qbo.option_value = '{self.NUMERICAL_OPTION_SEVEN}'),
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.talking_point WHERE text = '{self.QUESTION_TEN_TALKING_POINT_STRENGTH}' AND talking_point_type = '{self.ISSUE_TYPE_STRENGTH}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_TEN}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_TEN}' AND qbo.option_value = '{self.NUMERICAL_OPTION_ONE}'),
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.talking_point WHERE text = '{self.QUESTION_TEN_TALKING_POINT_STRENGTH}' AND talking_point_type = '{self.ISSUE_TYPE_STRENGTH}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_TEN}')),
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
                );
            """
        }


        self.sql_dictionary = collections.OrderedDict(sorted(self.sql.items()))
