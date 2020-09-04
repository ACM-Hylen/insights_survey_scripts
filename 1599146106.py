from sql.nano_survey_configuration.base_migration import BaseMigration
import collections


class MigrationScript(BaseMigration):
    """
        Student Success Survey - Fall 2020 Residential
    """
    sql = None
    sql_dictionary = None

    SURVEY_TEMPLATE_INTERNAL_KEY = 'student_success_2020_Fall_resident'

    # Purpose text
    SURVEY_WHY_TEXT = 'By asking students to answer these questions, we can provide you with actionable data. These insights and reports will help foster student success.'
    SURVEY_HOW_TEXT = 'To capture quick, meaningful insights, we took some of the best questions from the Mapworks Transition Survey. The content was built and tested over 3 decades using data from 200+ institutions and 1 million+ students. We reduced this survey to cover the most critical questions. This focused content was vetted with student success practitioners, and students.'
    SURVEY_HOVER_TEXT = 'Identify students in need of support and get actionable data to help students succeed.'

    # New questions
    SURVEY_QUESTION_EIGHT = 'To what degree do you intend to come back to this institution for the next academic term?'
    SURVEY_QUESTION_THIRTEEN = 'To what degree are you experiencing stress because of COVID-19 health and safety concerns at your institution?'
    SURVEY_QUESTION_FOURTEEN = 'To what degree are you able to access campus services online?'
    SURVEY_QUESTION_FIFTEEN = 'If your courses are online, to what degree are you able to access the course content? (Please skip if all of your courses are in person)'

    # Existing questions
    SURVEY_QUESTION_ONE = 'To what degree are you keeping current with your academic work?'
    SURVEY_QUESTION_TWO = 'To what extent do you work harder in a course, when you get a poor grade?'
    SURVEY_QUESTION_THREE = 'How many of your scheduled classes have you attended this term?'
    SURVEY_QUESTION_FOUR = 'How many courses are you struggling in?'
    SURVEY_QUESTION_FIVE = 'To what extent do you do everything you can to meet the academic goals you set at the beginning of the semester?'
    SURVEY_QUESTION_SIX = 'To what degree are you certain that you can do well in your hardest course?'
    SURVEY_QUESTION_SEVEN = "To what degree are you confident that you can pay for next term's tuition and fees?"
    SURVEY_QUESTION_NINE = 'How would you rate your experience at this institution?'
    SURVEY_QUESTION_TEN = 'To what degree do you regret leaving home to go to school?'
    SURVEY_QUESTION_ELEVEN = 'To what degree do you belong here?'
    SURVEY_QUESTION_TWELVE = 'During this term, to what degree do you intend to participate in a student organization?'

    # Issue text for this template
    ISSUE_ACADEMIC_COURSEWORK = "Academic Coursework - Fall 2020"
    ISSUE_ACADEMIC_RESILIENCY = "Academic Resilience - Fall 2020"
    ISSUE_CLASS_ATTENDANCE = "Class Attendance - Missed class (self-report) - Fall 2020"
    ISSUE_GOAL_SETTING = "Goal Setting - Fall 2020"
    ISSUE_FINANCIAL_MEANS = "Financial Means -  Fall 2020"
    ISSUE_INTENT_TO_RETURN = "Intent to Return - Fall 2020"
    ISSUE_OVERALL_SATISFACTION = "Overall Satisfaction - Fall 2020"
    ISSUE_HOMESICKNESS = "Homesickness - Fall 2020"
    ISSUE_SENSE_OF_BELONGING = "Sense of Belonging  - Fall 2020"
    ISSUE_HEALTH_RELATED_STRESS = "Health-Related Stress - Fall 2020"
    ONLINE_CAMPUS_SERVICES = "Online Campus Services - Fall 2020"


# Talking Point text for this template
    QUESTION_EIGHT_TALKING_POINT_WEAKNESS = 'Student is unlikely to return next term. This response is a strong predictor of attrition.'
    QUESTION_EIGHT_TALKING_POINT_STRENGTH = 'Student intends to return next term.'
    QUESTION_EIGHT_NEXT_STEPS = "Students who say they don't intend to return, often don't. Intervening with these students may help them to continue their education."
    QUESTION_THIRTEEN_TALKING_POINT_WEAKNESS = 'This student is experience stress related to COVID-19 and attending this institution. Ensure this student knows what the institution is doing to ensure health and safety.'
    QUESTION_THIRTEEN_TALKING_POINT_STRENGTH = 'Student does not report stress related to attending class amid the changes caused by COVID-19.'
    QUESTION_THIRTEEN_NEXT_STEPS = 'Keep students informed about what the institution is doing to keep the campus community safe. Students may need support or feel heard about concerns.'
    QUESTION_FOURTEEN_TALKING_POINT_WEAKNESS = 'Student is having difficulty accessing campus services online.'
    QUESTION_FOURTEEN_TALKING_POINT_STRENGTH = 'Student is able to access campus services online.'
    QUESTION_FOURTEEN_NEXT_STEPS = 'Students who struggle to access campus services may be at increased risk of not returning to the institution. Reach out to these students to further investigate why they are having difficulty accessing services or provide them with resources on how to access services virtually.'
    QUESTION_FIFTEEN_TALKING_POINT_WEAKNESS = 'Student is having difficulty accessing campus services online.'
    QUESTION_FIFTEEN_TALKING_POINT_STRENGTH = 'Student is able to access course content online.'
    QUESTION_FIFTEEN_NEXT_STEPS = 'Students who have difficulty accessing course content virtually may perform poorly. Share resources on how to be successful in virtual courses and explore reasons why students are struggling to access virtual course materials and content.'

    # OTHER
    CONSENT_STATEMENT = "Macmillan Learning is conducting the following survey on behalf of your organization/institution. Your survey responses are submitted to us utilizing data encryption methodology (SSL) used to protect financial transactions conducted over the internet and we handle your data pursuant to the <a target='_blank' href='https://store.macmillanlearning.com/us/privacy-notice'>Macmillan Learning Privacy Notice.</a> Your responses will be collected by us in a personally identifiable format and we will provide it to your organization/institutions linked to your personal identifiers.  Your organization/institution can use your personal information and survey results pursuant to their own Privacy Policy, including using the results of your survey responses in an aggregated and anonymized form in connection with its presentations, reports and publications. Macmillan Learning may de-identify your survey responses and analyze the data to improve its educational products and services, including to create aggregated or statistical insights and baseline reports that are not identifiable to you or any other individual for use in other Macmillan Learning educational products and services.  If you prefer not to participate in this survey, you may leave questions blank or close the browser and leave the survey.  Contact your organisation/institution for more information about its use of the responses."


    def __init__(self):
        super().__init__()
        self.sql = {
            1: f"""
                INSERT INTO nano_survey_configuration.survey_template (title, internal_key, hover_text, time_to_complete, user_data_consent_statement, created_by, modified_by) VALUES
                ('Student Success Survey - Fall 2020 Residential', '{self.SURVEY_TEMPLATE_INTERNAL_KEY}', '{self.SURVEY_HOVER_TEXT}', 8, "{self.CONSENT_STATEMENT}", 2, 2);
            """,
            2: f"""
                INSERT INTO nano_survey_configuration.survey_purpose (section, purpose_text, section_title, icon_filename, created_by, modified_by) VALUES
                ('Why', '{self.SURVEY_WHY_TEXT}', 'Why should you use this survey?', 'institute_student_rotation.svg', 2, 2),
                ('How', '{self.SURVEY_HOW_TEXT}', 'How was this survey created?', 'question_mark_in_lightbulb.svg', 2, 2);
            """,
            3: f"""
                INSERT INTO nano_survey_configuration.question_bank (question_text, alternate_question_text, question_type, created_by, modified_by) VALUES
                ('{self.SURVEY_QUESTION_EIGHT}', '', '{self.TEXT_SCALED}', 2, 2),
                ('{self.SURVEY_QUESTION_THIRTEEN}', '', '{self.TEXT_SCALED}', 2, 2),
                ('{self.SURVEY_QUESTION_FOURTEEN}', '', '{self.TEXT_SCALED}', 2, 2),
                ('{self.SURVEY_QUESTION_FIFTEEN}', '', '{self.TEXT_SCALED}', 2, 2);
            """,
            4: f"""
                INSERT INTO nano_survey_configuration.question_bank_option (question_bank_id, option_value, additional_text, option_type, created_by, modified_by) VALUES
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
               # question thirteen
                (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_THIRTEEN}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.NUMERICAL_OPTION_ONE}',
                    'Not at All',
                    '{self.TYPE_INTEGER}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_THIRTEEN}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.NUMERICAL_OPTION_TWO}',
                    null,
                    '{self.TYPE_INTEGER}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_THIRTEEN}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.NUMERICAL_OPTION_THREE}',
                    null,
                    '{self.TYPE_INTEGER}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_THIRTEEN}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.NUMERICAL_OPTION_FOUR}',
                    null,
                    '{self.TYPE_INTEGER}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_THIRTEEN}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.NUMERICAL_OPTION_FIVE}',
                    null,
                    '{self.TYPE_INTEGER}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_THIRTEEN}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.NUMERICAL_OPTION_SIX}',
                    null,
                    '{self.TYPE_INTEGER}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_THIRTEEN}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.NUMERICAL_OPTION_SEVEN}',
                    'Extremely',
                    '{self.TYPE_INTEGER}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_THIRTEEN}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.NUMERICAL_OPTION_99}',
                    'Not Applicable',
                    '{self.TYPE_INTEGER}',
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
                # question FIFTEEN
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
            6: f"""
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
                    '{self.ISSUE_ACADEMIC_RESILIENCY}',
                    '{self.ISSUE_TYPE_WEAKNESS}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.reporting_category WHERE text = '{self.REPORTING_CATEGORY_ACADEMIC}'),
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_TWO}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.ISSUE_ACADEMIC_RESILIENCY}',
                    '{self.ISSUE_TYPE_STRENGTH}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.reporting_category WHERE text = '{self.REPORTING_CATEGORY_ACADEMIC}'),
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_THREE}' AND question_type = '{self.TEXT_CATEGORICAL}'),
                    '{ISSUE_CLASS_ATTENDANCE}',
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
                    (SELECT id FROM nano_survey_configuration.reporting_category WHERE text = '{self.REPORTING_CATEGORY_ACADEMIC}'),
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_FIVE}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.ISSUE_GOAL_SETTING}',
                    '{self.ISSUE_TYPE_WEAKNESS}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.reporting_category WHERE text = '{self.REPORTING_CATEGORY_ACADEMIC}'),
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_FIVE}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.ISSUE_GOAL_SETTING}',
                    '{self.ISSUE_TYPE_STRENGTH}',
                    2,
                    2
                ),
                  (
                    (SELECT id FROM nano_survey_configuration.reporting_category WHERE text = '{self.REPORTING_CATEGORY_ACADEMIC}'),
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_SIX}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.ISSUE_SELF_EFFICACY}',
                    '{self.ISSUE_TYPE_WEAKNESS}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.reporting_category WHERE text = '{self.REPORTING_CATEGORY_ACADEMIC}'),
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_SIX}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.ISSUE_SELF_EFFICACY}',
                    '{self.ISSUE_TYPE_STRENGTH}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.reporting_category WHERE text = '{self.REPORTING_CATEGORY_FINANCIAL}'),
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = "{self.SURVEY_QUESTION_SEVEN}" AND question_type = '{self.TEXT_SCALED}'),
                    '{self.ISSUE_FINANCIAL_MEANS}',
                    '{self.ISSUE_TYPE_WEAKNESS}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.reporting_category WHERE text = '{self.REPORTING_CATEGORY_INSTITUTIONAL}'),
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_EIGHT}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.ISSUE_INTENT_TO_RETURN}',
                    '{self.ISSUE_TYPE_WEAKNESS}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.reporting_category WHERE text = '{self.REPORTING_CATEGORY_INSTITUTIONAL}'),
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_EIGHT}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.ISSUE_INTENT_TO_RETURN}',
                    '{self.ISSUE_TYPE_STRENGTH}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.reporting_category WHERE text = '{self.REPORTING_CATEGORY_INSTITUTIONAL}'),
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_NINE}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.ISSUE_ISSUE_OVERALL_SATISFACTION}',
                    '{self.ISSUE_TYPE_WEAKNESS}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.reporting_category WHERE text = '{self.REPORTING_CATEGORY_INSTITUTIONAL}'),
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_NINE}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.ISSUE_ISSUE_OVERALL_SATISFACTION}',
                    '{self.ISSUE_TYPE_STRENGTH}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.reporting_category WHERE text = '{self.REPORTING_CATEGORY_SOCIAL}'),
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_TEN}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.ISSUE_HOMESICKNESS}',
                    '{self.ISSUE_TYPE_WEAKNESS}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.reporting_category WHERE text = '{self.REPORTING_CATEGORY_SOCIAL}'),
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_ELEVEN}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.ISSUE_SENSE_OF_BELONGING}',
                    '{self.ISSUE_TYPE_WEAKNESS}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.reporting_category WHERE text = '{self.REPORTING_CATEGORY_SOCIAL}'),
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_ELEVEN}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.ISSUE_SENSE_OF_BELONGING}',
                    '{self.ISSUE_TYPE_STRENGTH}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.reporting_category WHERE text = '{self.REPORTING_CATEGORY_SOCIAL}'),
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_TWELVE}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.ISSUE_STUDENT_INVOLVEMENT}',
                    '{self.ISSUE_TYPE_WEAKNESS}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.reporting_category WHERE text = '{self.REPORTING_CATEGORY_SOCIAL}'),
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_TWELVE}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.ISSUE_STUDENT_INVOLVEMENT}',
                    '{self.ISSUE_TYPE_STRENGTH}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.reporting_category WHERE text = '{self.REPORTING_CATEGORY_INSTITUTIONAL}'),
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_THIRTEEN}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.ISSUE_HEALTH_RELATED_STRESS}',
                    '{self.ISSUE_TYPE_WEAKNESS}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.reporting_category WHERE text = '{self.REPORTING_CATEGORY_INSTITUTIONAL}'),
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_THIRTEEN}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.ISSUE_ISSUE_HEALTH_RELATED_STRESS}',
                    '{self.ISSUE_TYPE_STRENGTH}',
                    2,
                    2
                )
                (
                    (SELECT id FROM nano_survey_configuration.reporting_category WHERE text = '{self.REPORTING_CATEGORY_ACADEMIC}'),
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_FOURTEEN}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.ONLINE_CAMPUS_SERVICES}',
                    '{self.ISSUE_TYPE_WEAKNESS}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.reporting_category WHERE text = '{self.REPORTING_CATEGORY_ACADEMIC}'),
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_FOURTEEN}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.ONLINE_CAMPUS_SERVICES}',
                    '{self.ISSUE_TYPE_STRENGTH}',
                    2,
                    2
                )
                (
                    (SELECT id FROM nano_survey_configuration.reporting_category WHERE text = '{self.REPORTING_CATEGORY_ACADEMIC}'),
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_FIFTEEN}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.ONLINE_COURSE_CONTENT}',
                    '{self.ISSUE_TYPE_WEAKNESS}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.reporting_category WHERE text = '{self.REPORTING_CATEGORY_ACADEMIC}'),
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_FIFTEEN}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.ONLINE_COURSE_CONTENT}',
                    '{self.ISSUE_TYPE_STRENGTH}',
                    2,
                    2
                )
                ;
            """,
            7: f"""
                INSERT INTO nano_survey_configuration.issue_question_bank_option (issue_id, question_bank_option_id, created_by) VALUES
                # Question EIGHT weakness values
                (
                    (SELECT id FROM nano_survey_configuration.issue WHERE issue_text = '{self.ISSUE_INTENT_TO_RETURN}' AND issue_type = '{self.ISSUE_TYPE_WEAKNESS}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_EIGHT}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_EIGHT}' AND qbo.option_value = '{self.NUMERICAL_OPTION_ONE}'),
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.issue WHERE issue_text = '{self.ISSUE_INTENT_TO_RETURN}' AND issue_type = '{self.ISSUE_TYPE_WEAKNESS}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_EIGHT}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_EIGHT}' AND qbo.option_value = '{self.NUMERICAL_OPTION_TWO}'),
                    2
                ),
                # Question EIGHT strength values
                (
                    (SELECT id FROM nano_survey_configuration.issue WHERE issue_text = '{self.ISSUE_INTENT_TO_RETURN}' AND issue_type = '{self.ISSUE_TYPE_STRENGTH}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_EIGHT}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_EIGHT}' AND qbo.option_value = '{self.NUMERICAL_OPTION_SIX}'),
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.issue WHERE issue_text = '{self.ISSUE_INTENT_TO_RETURN}' AND issue_type = '{self.ISSUE_TYPE_STRENGTH}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_EIGHT}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_EIGHT}' AND qbo.option_value = '{self.NUMERICAL_OPTION_SEVEN}'),
                    2
                ),
                # Question THIRTEEN weakness values INVERSE
                (
                    (SELECT id FROM nano_survey_configuration.issue WHERE issue_text = '{self.ISSUE_HEALTH_RELATED_STRESS}' AND issue_type = '{self.ISSUE_TYPE_WEAKNESS}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_THIRTEEN}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_THIRTEEN}' AND qbo.option_value = '{self.NUMERICAL_OPTION_SIX}'),
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.issue WHERE issue_text = '{self.ISSUE_ISSUE_HEALTH_RELATED_STRESS}' AND issue_type = '{self.ISSUE_TYPE_WEAKNESS}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_THIRTEEN}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_THIRTEEN}' AND qbo.option_value = '{self.NUMERICAL_OPTION_SEVEN}'),
                    2
                ),
                # Question THIRTEEN strength values INVERSE
                (
                    (SELECT id FROM nano_survey_configuration.issue WHERE issue_text = '{self.ISSUE_HEALTH_RELATED_STRESS}' AND issue_type = '{self.ISSUE_TYPE_STRENGTH}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_THIRTEEN}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_THIRTEEN}' AND qbo.option_value = '{self.NUMERICAL_OPTION_ONE}'),
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.issue WHERE issue_text = '{self.ISSUE_HEALTH_RELATED_STRESS}' AND issue_type = '{self.ISSUE_TYPE_STRENGTH}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_THIRTEEN}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_THIRTEEN}' AND qbo.option_value = '{self.NUMERICAL_OPTION_TWO}'),
                    2
                ),
                # Question FOURTEEN weakness values
                (
                    (SELECT id FROM nano_survey_configuration.issue WHERE issue_text = '{self.ONLINE_CAMPUS_SERVICES}' AND issue_type = '{self.ISSUE_TYPE_WEAKNESS}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_FOURTEEN}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_FOURTEEN}' AND qbo.option_value = '{self.NUMERICAL_OPTION_ONE}'),
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.issue WHERE issue_text = '{self.ONLINE_CAMPUS_SERVICES}' AND issue_type = '{self.ISSUE_TYPE_WEAKNESS}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_FOURTEEN}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_FOURTEEN}' AND qbo.option_value = '{self.NUMERICAL_OPTION_TWO}'),
                    2
                ),
                # Question FOURTEEN strength values
                (
                    (SELECT id FROM nano_survey_configuration.issue WHERE issue_text = '{self.ONLINE_CAMPUS_SERVICES}' AND issue_type = '{self.ISSUE_TYPE_STRENGTH}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_FOURTEEN}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_FOURTEEN}' AND qbo.option_value = '{self.NUMERICAL_OPTION_SIX}'),
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.issue WHERE issue_text = '{self.ONLINE_CAMPUS_SERVICES}' AND issue_type = '{self.ISSUE_TYPE_STRENGTH}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_FOURTEEN}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_FOURTEEN}' AND qbo.option_value = '{self.NUMERICAL_OPTION_SEVEN}'),
                    2
                ),
                # Question FIFTEEN weakness values
                (
                    (SELECT id FROM nano_survey_configuration.issue WHERE issue_text = '{self.ONLINE_COURSE_CONTENT}' AND issue_type = '{self.ISSUE_TYPE_WEAKNESS}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_FIFTEEN}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_FIFTEEN}' AND qbo.option_value = '{self.NUMERICAL_OPTION_ONE}'),
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.issue WHERE issue_text = '{self.ONLINE_COURSE_CONTENT}' AND issue_type = '{self.ISSUE_TYPE_WEAKNESS}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_FIFTEEN}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_FIFTEEN}' AND qbo.option_value = '{self.NUMERICAL_OPTION_TWO}'),
                    2
                ),
                # Question FIFTEEN strength values
                (
                    (SELECT id FROM nano_survey_configuration.issue WHERE issue_text = '{self.ONLINE_COURSE_CONTENT}' AND issue_type = '{self.ISSUE_TYPE_STRENGTH}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_FIFTEEN}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_FIFTEEN}' AND qbo.option_value = '{self.NUMERICAL_OPTION_SIX}'),
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.issue WHERE issue_text = '{self.ONLINE_COURSE_CONTENT}' AND issue_type = '{self.ISSUE_TYPE_STRENGTH}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_FIFTEEN}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_FIFTEEN}' AND qbo.option_value = '{self.NUMERICAL_OPTION_SEVEN}'),
                    2
                );
            """,
            8: f"""
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
            9: f"""
                INSERT INTO nano_survey_configuration.survey_template_question (survey_template_id, question_bank_id, sequence, created_by, modified_by) VALUES
                (
                    (SELECT id FROM nano_survey_configuration.survey_template WHERE internal_key = '{self.SURVEY_TEMPLATE_INTERNAL_KEY}'),
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_EIGHT}' AND question_type = '{self.TEXT_SCALED}'),
                    1,
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.survey_template WHERE internal_key = '{self.SURVEY_TEMPLATE_INTERNAL_KEY}'),
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_THIRTEEN}' AND question_type = '{self.TEXT_SCALED}'),
                    2,
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.survey_template WHERE internal_key = '{self.SURVEY_TEMPLATE_INTERNAL_KEY}'),
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_FOURTEEN}' AND question_type = '{self.TEXT_SCALED}'),
                    3,
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.survey_template WHERE internal_key = '{self.SURVEY_TEMPLATE_INTERNAL_KEY}'),
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_FIFTEEN}' AND question_type = '{self.TEXT_SCALED}'),
                    4,
                    2,
                    2
                );
            """,
            10: f"""
                INSERT INTO nano_survey_configuration.talking_point (question_bank_id, talking_point_type, text, next_steps, created_by, modified_by) VALUES
                (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_EIGHT}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.ISSUE_TYPE_WEAKNESS}',
                    '{self.QUESTION_EIGHT_TALKING_POINT_WEAKNESS}',
                    "{self.QUESTION_EIGHT_NEXT_STEPS}",
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
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_THIRTEEN}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.ISSUE_TYPE_WEAKNESS}',
                    '{self.QUESTION_THIRTEEN_TALKING_POINT_WEAKNESS}',
                    '{self.QUESTION_THIRTEEN_NEXT_STEPS}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_THIRTEEN}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.ISSUE_TYPE_STRENGTH}',
                    '{self.QUESTION_THIRTEEN_TALKING_POINT_STRENGTH}',
                    null,
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_FOURTEEN}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.ISSUE_TYPE_WEAKNESS}',
                    '{self.QUESTION_FOURTEEN_TALKING_POINT_WEAKNESS}',
                    '{self.QUESTION_FOURTEEN_NEXT_STEPS}',
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
            11: f"""
                INSERT INTO nano_survey_configuration.talking_point_question_bank_option (talking_point_id, question_bank_option_id, created_by) VALUES
                # Question EIGHT
                (
                    (SELECT id FROM nano_survey_configuration.talking_point WHERE text = '{self.QUESTION_EIGHT_TALKING_POINT_WEAKNESS}' AND talking_point_type = '{self.ISSUE_TYPE_WEAKNESS}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_EIGHT}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_EIGHT}' AND qbo.option_value = '{self.NUMERICAL_OPTION_ONE}'),
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.talking_point WHERE text = '{self.QUESTION_EIGHT_TALKING_POINT_WEAKNESS}' AND talking_point_type = '{self.ISSUE_TYPE_WEAKNESS}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_EIGHT}')),
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
                # Question THIRTEEN
                (
                    (SELECT id FROM nano_survey_configuration.talking_point WHERE text = '{self.QUESTION_THIRTEEN_TALKING_POINT_WEAKNESS}' AND talking_point_type = '{self.ISSUE_TYPE_WEAKNESS}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_THIRTEEN}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_THIRTEEN}' AND qbo.option_value = '{self.NUMERICAL_OPTION_SIX}'),
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.talking_point WHERE text = '{self.QUESTION_THIRTEEN_TALKING_POINT_WEAKNESS}' AND talking_point_type = '{self.ISSUE_TYPE_WEAKNESS}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_THIRTEEN}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_THIRTEEN}' AND qbo.option_value = '{self.NUMERICAL_OPTION_SEVEN}'),
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.talking_point WHERE text = '{self.QUESTION_THIRTEEN_TALKING_POINT_STRENGTH}' AND talking_point_type = '{self.ISSUE_TYPE_STRENGTH}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_THIRTEEN}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_THIRTEEN}' AND qbo.option_value = '{self.NUMERICAL_OPTION_ONE}'),
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.talking_point WHERE text = '{self.QUESTION_THIRTEEN_TALKING_POINT_STRENGTH}' AND talking_point_type = '{self.ISSUE_TYPE_STRENGTH}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_THIRTEEN}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_THIRTEEN}' AND qbo.option_value = '{self.NUMERICAL_OPTION_TWO}'),
                    2
                ),
                # Question FOURTEEN
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
                # Question FIFTEEN
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
