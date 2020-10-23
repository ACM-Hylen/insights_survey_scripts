
from sql.nano_survey_configuration.base_migration import BaseMigration
import collections

class MigrationScript(BaseMigration):
    """
        Fall 2020 Outcomes Survey
    """
    sql = None
    sql_dictionary = None

    SURVEY_TEMPLATE_INTERNAL_KEY = 'outcomes_2020_fall'

    # Purpose text
    SURVEY_WHY_TEXT = 'This survey allows you to quickly collect data from your students on their experiences during the term, including their perceptions of services and the institution. This data is useful for helping your campus to evaluate how well you did, show if your work to support students identified by other surveys was successful, and begin planning future student support strategies.'
    SURVEY_HOW_TEXT = 'This survey uses data from Mapworks to select questions that are tied to retention and academic success.'
    SURVEY_HOVER_TEXT = 'Quickly collect outcome data.'
    # New questions
    SURVEY_QUESTION_ONE = "    To what degree do you intend to come back to this institution for the next academic term? (If you are graduating this term, please leave this question blank.)"
    SURVEY_QUESTION_TWO = '    What was/do you think your GPA will be this term?'
    SURVEY_QUESTION_THREE = '    To what degree are you satisfied with this institution?'
    SURVEY_QUESTION_FOUR = '    To what degree are you satisfied with campus services?'
    SURVEY_QUESTION_FIVE = '    To what degree are you satisfied with your academic life?'
    SURVEY_QUESTION_SIX = '    To what degree are you satisfied with your social life?'
    SURVEY_QUESTION_SEVEN = '    To what degree do you belong here?'
    SURVEY_QUESTION_EIGHT = '    To what degree did you experience stress because of COVID-19 health and safety concerns at your institution?'
    SURVEY_QUESTION_NINE = "    To what degree are you satisfied with your institution's response to COVID-19?"
    # Categorical question options
    QUESTION_TWO_OPTION_ONE = 'GPA of 3.50 or higher (Mostly As)'
    QUESTION_TWO_OPTION_TWO = 'GPA of 3.00 to 3.49 (Mostly Bs)'
    QUESTION_TWO_OPTION_THREE = 'GPA of 2.50 to 2.99 (Some Bs and Cs)'
    QUESTION_TWO_OPTION_FOUR = 'GPA of 2.00 to 2.49 (Mostly Cs)'
    QUESTION_TWO_OPTION_FIVE = 'GPA less than 2.00 (Lower than Cs)'
    # Issue text for this template
    ISSUE_INTENT_TO_RETURN = "Intent to Return - Fall 2020 Outcomes"
    ISSUE_EXPECTED_GPA = "Expected GPA - Fall 2020 Outcomes"
    ISSUE_SATISFACTION = "Overall Satisfaction - Fall 2020 Outcomes"
    ISSUE_CAMPUS_SERVICES = "Campus Services - Fall 2020 Outcomes"
    ISSUE_ACADEMIC_INTEGRATION = "Academic Integration - Fall 2020 Outcomes"
    ISSUE_SOCIAL_INTEGRATION = "Social Integration - Fall 2020 Outcomes"
    ISSUE_SENSE_OF_BELONGING = "Sense of Belonging - Fall 2020 Outcomes"
    ISSUE_HEALTH_RELATED_STRESS = "Health-Related Stress - Fall 2020 Outcomes"
    ISSUE_RESPONSE_SATISFACTION = "COVID-19 Response Satisfaction - Fall 2020 Outcomes"
    # Talking Points
    QUESTION_ONE_TALKING_POINT_WEAKNESS = 'Student is unlikely to term next year. This response is a strong predictor of attrition.'
    QUESTION_ONE_TALKING_POINT_STRENGTH = 'Student intends to return next term.'
    QUESTION_ONE_NEXT_STEPS = "Students who say they don't intend to return, often don't. Intervening with these students may help them to continue their education."
    QUESTION_TWO_TALKING_POINT_WEAKNESS = 'Student reports a term GPA for 2.0 or lower. Poor academic performance is a strong predictor of attrition. Identify the reasons for poor performance and connect the student to support resources.'
    QUESTION_TWO_TALKING_POINT_STRENGTH = 'Student reports a term GPA above 3.50.'
    QUESTION_TWO_NEXT_STEPS = 'Intervene with students with low GPAs. Students who struggle may not know the resources available to help them.'
    QUESTION_THREE_TALKING_POINT_WEAKNESS = 'Student reports low satisfaction with the institution.'
    QUESTION_THREE_TALKING_POINT_STRENGTH = 'Student reports high satisfaction with this institution.'
    QUESTION_THREE_NEXT_STEPS = 'Dissatisfaction with the institution is correlated with lower retention. Identifying the cause of their dissatisfaction may help retain the student at the institution.'
    QUESTION_FOUR_TALKING_POINT_WEAKNESS = 'Student reports low satisfaction with campus services. Outreach may be necessary to resolve issus or understand specific concerns.'
    QUESTION_FOUR_TALKING_POINT_STRENGTH = 'Student reports a high satisfacation with campus services.'
    QUESTION_FIVE_TALKING_POINT_WEAKNESS = 'Student reports low satisfaction with academics.'
    QUESTION_FIVE_TALKING_POINT_STRENGTH = 'Student reports high satisfaction with academic life.'
    QUESTION_SIX_TALKING_POINT_WEAKNESS = 'Student reports low social integration.'
    QUESTION_SIX_TALKING_POINT_STRENGTH = 'Student reports high satifaction with social life.'
    QUESTION_SEVEN_TALKING_POINT_WEAKNESS = "Doesn't feel he/she belongs at this school. Strong predictor of attrition. Explore issue(s), discuss getting involved in student organizations."
    QUESTION_SEVEN_TALKING_POINT_STRENGTH = 'Feels he/she belongs at this school. Strong predictor of retention.'
    QUESTION_SEVEN_NEXT_STEPS = 'Help students make connections to peers and organizations on campus and in the community.'
    QUESTION_EIGHT_TALKING_POINT_WEAKNESS = 'This student is experience stress related to COVID-19 and attending this institution. Ensure this student knows what the institution is doing to ensure health and safety.'
    QUESTION_EIGHT_TALKING_POINT_STRENGTH = 'Student does not report stress related to attending class amid the changes caused by COVID-19.'
    QUESTION_EIGHT_NEXT_STEPS = 'Keep students informed about what the institution is doing to keep the campus community safe. Students may need support or feel heard about concerns.'
    QUESTION_NINE_TALKING_POINT_WEAKNESS = 'Student reports low satisfaction with campus response to COVID-19'
    QUESTION_NINE_TALKING_POINT_STRENGTH = 'Student reports high satisfaction with campus response to COVID-19.'
    # Other
    CONSENT_STATEMENT = "Macmillan Learning is conducting the following survey on behalf of your organization/institution. Your survey responses are submitted to us utilizing data encryption methodology (SSL) used to protect financial transactions conducted over the internet and we handle your data pursuant to the <a target='_blank' href='https://store.macmillanlearning.com/us/privacy-notice'>Macmillan Learning Privacy Notice.</a> Your responses will be collected by us in a personally identifiable format and we will provide it to your organization/institutions linked to your personal identifiers.  Your organization/institution can use your personal information and survey results pursuant to their own Privacy Policy, including using the results of your survey responses in an aggregated and anonymized form in connection with its presentations, reports and publications. Macmillan Learning may de-identify your survey responses and analyze the data to improve its educational products and services, including to create aggregated or statistical insights and baseline reports that are not identifiable to you or any other individual for use in other Macmillan Learning educational products and services.  If you prefer not to participate in this survey, you may leave questions blank or close the browser and leave the survey.  Contact your organisation/institution for more information about its use of the responses."

    def __init__(self):
        super().__init__()
        self.sql = {
            1: f"""
                INSERT INTO nano_survey_configuration.survey_template (title, internal_key, hover_text, time_to_complete, user_data_consent_statement, created_by, modified_by) VALUES
                ('Fall 2020 Outcomes Survey', '{self.SURVEY_TEMPLATE_INTERNAL_KEY}', '{self.SURVEY_HOVER_TEXT}', 6, "{self.CONSENT_STATEMENT}", 2, 2);
            """,
            2: f"""
                INSERT INTO nano_survey_configuration.survey_purpose (section, purpose_text, section_title, icon_filename, created_by, modified_by) VALUES
                ('How', '{self.SURVEY_HOW_TEXT}', 'How was this survey created?', 'question_mark_in_lightbulb.svg', 2, 2)
                ;
            """,
            3: f"""
                INSERT INTO nano_survey_configuration.question_bank (question_text, alternate_question_text, question_type, created_by, modified_by) VALUES
                ("{self.SURVEY_QUESTION_ONE}", '', '{self.TEXT_SCALED}', 2, 2),
                ('{self.SURVEY_QUESTION_TWO}', '', '{self.TEXT_CATEGORICAL}', 2, 2),
                ('{self.SURVEY_QUESTION_THREE}', '', '{self.TEXT_SCALED}', 2, 2),
                ('{self.SURVEY_QUESTION_FOUR}', '', '{self.TEXT_SCALED}', 2, 2),
                ('{self.SURVEY_QUESTION_FIVE}', '', '{self.TEXT_SCALED}', 2, 2),
                ('{self.SURVEY_QUESTION_SIX}', '', '{self.TEXT_SCALED}', 2, 2),
                ('{self.SURVEY_QUESTION_SEVEN}', '', '{self.TEXT_SCALED}', 2, 2),
                ('{self.SURVEY_QUESTION_EIGHT}', '', '{self.TEXT_SCALED}', 2, 2),
                ("{self.SURVEY_QUESTION_NINE}", '', '{self.TEXT_SCALED}', 2, 2);
            """,
            4: f"""
                INSERT INTO nano_survey_configuration.question_bank_option (question_bank_id, option_value, additional_text, option_type, created_by, modified_by) VALUES
                (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = "{self.SURVEY_QUESTION_ONE}" AND question_type = '{self.TEXT_SCALED}'),
                    '{self.NUMERICAL_OPTION_ONE}',
                    'Not at All',
                    '{self.TYPE_INTEGER}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = "{self.SURVEY_QUESTION_ONE}" AND question_type = '{self.TEXT_SCALED}'),
                    '{self.NUMERICAL_OPTION_TWO}',
                    null,
                    '{self.TYPE_INTEGER}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = "{self.SURVEY_QUESTION_ONE}" AND question_type = '{self.TEXT_SCALED}'),
                    '{self.NUMERICAL_OPTION_THREE}',
                    null,
                    '{self.TYPE_INTEGER}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = "{self.SURVEY_QUESTION_ONE}" AND question_type = '{self.TEXT_SCALED}'),
                    '{self.NUMERICAL_OPTION_FOUR}',
                    null,
                    '{self.TYPE_INTEGER}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = "{self.SURVEY_QUESTION_ONE}" AND question_type = '{self.TEXT_SCALED}'),
                    '{self.NUMERICAL_OPTION_FIVE}',
                    null,
                    '{self.TYPE_INTEGER}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = "{self.SURVEY_QUESTION_ONE}" AND question_type = '{self.TEXT_SCALED}'),
                    '{self.NUMERICAL_OPTION_SIX}',
                    null,
                    '{self.TYPE_INTEGER}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = "{self.SURVEY_QUESTION_ONE}" AND question_type = '{self.TEXT_SCALED}'),
                    '{self.NUMERICAL_OPTION_SEVEN}',
                    'Extremely',
                    '{self.TYPE_INTEGER}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = "{self.SURVEY_QUESTION_ONE}" AND question_type = '{self.TEXT_SCALED}'),
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
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_THREE}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.NUMERICAL_OPTION_ONE}',
                    'Not at All',
                    '{self.TYPE_INTEGER}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_THREE}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.NUMERICAL_OPTION_TWO}',
                    null,
                    '{self.TYPE_INTEGER}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_THREE}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.NUMERICAL_OPTION_THREE}',
                    null,
                    '{self.TYPE_INTEGER}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_THREE}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.NUMERICAL_OPTION_FOUR}',
                    null,
                    '{self.TYPE_INTEGER}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_THREE}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.NUMERICAL_OPTION_FIVE}',
                    null,
                    '{self.TYPE_INTEGER}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_THREE}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.NUMERICAL_OPTION_SIX}',
                    null,
                    '{self.TYPE_INTEGER}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_THREE}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.NUMERICAL_OPTION_SEVEN}',
                    'Extremely',
                    '{self.TYPE_INTEGER}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_THREE}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.NUMERICAL_OPTION_99}',
                    'Not Applicable',
                    '{self.TYPE_INTEGER}',
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
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_FIVE}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.NUMERICAL_OPTION_ONE}',
                    'Not at All',
                    '{self.TYPE_INTEGER}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_FIVE}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.NUMERICAL_OPTION_TWO}',
                    null,
                    '{self.TYPE_INTEGER}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_FIVE}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.NUMERICAL_OPTION_THREE}',
                    null,
                    '{self.TYPE_INTEGER}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_FIVE}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.NUMERICAL_OPTION_FOUR}',
                    null,
                    '{self.TYPE_INTEGER}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_FIVE}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.NUMERICAL_OPTION_FIVE}',
                    null,
                    '{self.TYPE_INTEGER}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_FIVE}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.NUMERICAL_OPTION_SIX}',
                    null,
                    '{self.TYPE_INTEGER}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_FIVE}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.NUMERICAL_OPTION_SEVEN}',
                    'Extremely',
                    '{self.TYPE_INTEGER}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_FIVE}' AND question_type = '{self.TEXT_SCALED}'),
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
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_SIX}'  AND question_type = '{self.TEXT_SCALED}'),
                    '{self.NUMERICAL_OPTION_TWO}',
                    null,
                    '{self.TYPE_INTEGER}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_SIX}'  AND question_type = '{self.TEXT_SCALED}'),
                    '{self.NUMERICAL_OPTION_THREE}',
                    null,
                    '{self.TYPE_INTEGER}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_SIX}'  AND question_type = '{self.TEXT_SCALED}'),
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
                    'Not at All',
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
                    'Extremely',
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
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = "{self.SURVEY_QUESTION_NINE}" AND question_type = '{self.TEXT_SCALED}'),
                    '{self.NUMERICAL_OPTION_ONE}',
                    'Not at All',
                    '{self.TYPE_INTEGER}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = "{self.SURVEY_QUESTION_NINE}" AND question_type = '{self.TEXT_SCALED}'),
                    '{self.NUMERICAL_OPTION_TWO}',
                    null,
                    '{self.TYPE_INTEGER}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = "{self.SURVEY_QUESTION_NINE}" AND question_type = '{self.TEXT_SCALED}'),
                    '{self.NUMERICAL_OPTION_THREE}',
                    null,
                    '{self.TYPE_INTEGER}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = "{self.SURVEY_QUESTION_NINE}" AND question_type = '{self.TEXT_SCALED}'),
                    '{self.NUMERICAL_OPTION_FOUR}',
                    null,
                    '{self.TYPE_INTEGER}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = "{self.SURVEY_QUESTION_NINE}" AND question_type = '{self.TEXT_SCALED}'),
                    '{self.NUMERICAL_OPTION_FIVE}',
                    null,
                    '{self.TYPE_INTEGER}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = "{self.SURVEY_QUESTION_NINE}" AND question_type = '{self.TEXT_SCALED}'),
                    '{self.NUMERICAL_OPTION_SIX}',
                    null,
                    '{self.TYPE_INTEGER}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = "{self.SURVEY_QUESTION_NINE}" AND question_type = '{self.TEXT_SCALED}'),
                    '{self.NUMERICAL_OPTION_SEVEN}',
                    'Extremely',
                    '{self.TYPE_INTEGER}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = "{self.SURVEY_QUESTION_NINE}" AND question_type = '{self.TEXT_SCALED}'),
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
                    (SELECT id FROM nano_survey_configuration.reporting_category WHERE text = '{self.REPORTING_CATEGORY_INSTITUTIONAL}'),
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = "{self.SURVEY_QUESTION_ONE}" AND question_type = '{self.TEXT_SCALED}'),
                    '{self.ISSUE_INTENT_TO_RETURN}',
                    '{self.ISSUE_TYPE_WEAKNESS}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.reporting_category WHERE text = '{self.REPORTING_CATEGORY_INSTITUTIONAL}'),
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = "{self.SURVEY_QUESTION_ONE}" AND question_type = '{self.TEXT_SCALED}'),
                    '{self.ISSUE_INTENT_TO_RETURN}',
                    '{self.ISSUE_TYPE_STRENGTH}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.reporting_category WHERE text = '{self.REPORTING_CATEGORY_ACADEMIC}'),
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_TWO}' AND question_type = '{self.TEXT_CATEGORICAL}'),
                    '{self.ISSUE_EXPECTED_GPA}',
                    '{self.ISSUE_TYPE_WEAKNESS}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.reporting_category WHERE text = '{self.REPORTING_CATEGORY_ACADEMIC}'),
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_TWO}' AND question_type = '{self.TEXT_CATEGORICAL}'),
                    '{self.ISSUE_EXPECTED_GPA}',
                    '{self.ISSUE_TYPE_STRENGTH}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.reporting_category WHERE text = '{self.REPORTING_CATEGORY_INSTITUTIONAL}'),
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_THREE}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.ISSUE_SATISFACTION}',
                    '{self.ISSUE_TYPE_WEAKNESS}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.reporting_category WHERE text = '{self.REPORTING_CATEGORY_INSTITUTIONAL}'),
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_THREE}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.ISSUE_SATISFACTION}',
                    '{self.ISSUE_TYPE_STRENGTH}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.reporting_category WHERE text = '{self.REPORTING_CATEGORY_INSTITUTIONAL}'),
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_FOUR}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.ISSUE_CAMPUS_SERVICES}',
                    '{self.ISSUE_TYPE_WEAKNESS}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.reporting_category WHERE text = '{self.REPORTING_CATEGORY_INSTITUTIONAL}'),
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_FOUR}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.ISSUE_CAMPUS_SERVICES}',
                    '{self.ISSUE_TYPE_STRENGTH}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.reporting_category WHERE text = '{self.REPORTING_CATEGORY_ACADEMIC}'),
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_FIVE}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.ISSUE_ACADEMIC_INTEGRATION}',
                    '{self.ISSUE_TYPE_WEAKNESS}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.reporting_category WHERE text = '{self.REPORTING_CATEGORY_ACADEMIC}'),
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_FIVE}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.ISSUE_ACADEMIC_INTEGRATION}',
                    '{self.ISSUE_TYPE_STRENGTH}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.reporting_category WHERE text = '{self.REPORTING_CATEGORY_SOCIAL}'),
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_SIX}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.ISSUE_SOCIAL_INTEGRATION}',
                    '{self.ISSUE_TYPE_WEAKNESS}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.reporting_category WHERE text = '{self.REPORTING_CATEGORY_SOCIAL}'),
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_SIX}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.ISSUE_SOCIAL_INTEGRATION}',
                    '{self.ISSUE_TYPE_STRENGTH}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.reporting_category WHERE text = '{self.REPORTING_CATEGORY_SOCIAL}'),
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_SEVEN}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.ISSUE_SENSE_OF_BELONGING}',
                    '{self.ISSUE_TYPE_WEAKNESS}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.reporting_category WHERE text = '{self.REPORTING_CATEGORY_SOCIAL}'),
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_SEVEN}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.ISSUE_SENSE_OF_BELONGING}',
                    '{self.ISSUE_TYPE_STRENGTH}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.reporting_category WHERE text = '{self.REPORTING_CATEGORY_INSTITUTIONAL}'),
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_EIGHT}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.ISSUE_ISSUE_HEALTH_RELATED_STRESS}',
                    '{self.ISSUE_TYPE_WEAKNESS}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.reporting_category WHERE text = '{self.REPORTING_CATEGORY_INSTITUTIONAL}'),
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_EIGHT}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.ISSUE_ISSUE_HEALTH_RELATED_STRESS}',
                    '{self.ISSUE_TYPE_STRENGTH}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.reporting_category WHERE text = '{self.REPORTING_CATEGORY_INSTITUTIONAL}'),
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = "{self.SURVEY_QUESTION_NINE}" AND question_type = '{self.TEXT_SCALED}'),
                    '{self.ISSUE_RESPONSE_SATISFACTION}',
                    '{self.ISSUE_TYPE_WEAKNESS}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.reporting_category WHERE text = '{self.REPORTING_CATEGORY_INSTITUTIONAL}'),
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = "{self.SURVEY_QUESTION_NINE}" AND question_type = '{self.TEXT_SCALED}'),
                    '{self.ISSUE_RESPONSE_SATISFACTION}',
                    '{self.ISSUE_TYPE_STRENGTH}',
                    2,
                    2
                );
            """,
            6: f"""
                INSERT INTO nano_survey_configuration.issue_question_bank_option (issue_id, question_bank_option_id, created_by) VALUES
                # Question one weakness values
                (
                    (SELECT id FROM nano_survey_configuration.issue WHERE issue_text = '{self.ISSUE_INTENT_TO_RETURN}' AND issue_type = '{self.ISSUE_TYPE_WEAKNESS}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = "{self.SURVEY_QUESTION_ONE}")),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = "{self.SURVEY_QUESTION_ONE}" AND qbo.option_value = '{self.NUMERICAL_OPTION_ONE}'),
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.issue WHERE issue_text = '{self.ISSUE_INTENT_TO_RETURN}' AND issue_type = '{self.ISSUE_TYPE_WEAKNESS}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = "{self.SURVEY_QUESTION_ONE}")),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = "{self.SURVEY_QUESTION_ONE}" AND qbo.option_value = '{self.NUMERICAL_OPTION_TWO}'),
                    2
                ),
                # Question one strength values
                (
                    (SELECT id FROM nano_survey_configuration.issue WHERE issue_text = '{self.ISSUE_INTENT_TO_RETURN}' AND issue_type = '{self.ISSUE_TYPE_STRENGTH}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = "{self.SURVEY_QUESTION_ONE}")),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = "{self.SURVEY_QUESTION_ONE}" AND qbo.option_value = '{self.NUMERICAL_OPTION_SIX}'),
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.issue WHERE issue_text = '{self.ISSUE_INTENT_TO_RETURN}' AND issue_type = '{self.ISSUE_TYPE_STRENGTH}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = "{self.SURVEY_QUESTION_ONE}")),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = "{self.SURVEY_QUESTION_ONE}" AND qbo.option_value = '{self.NUMERICAL_OPTION_SEVEN}'),
                    2
                ),
                # Question two weakness values
                (
                    (SELECT id FROM nano_survey_configuration.issue WHERE issue_text = '{self.ISSUE_EXPECTED_GPA}' AND issue_type = '{self.ISSUE_TYPE_WEAKNESS}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_TWO}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_TWO}' AND qbo.option_value = '{self.QUESTION_TWO_OPTION_FIVE}'),
                    2
                ),
                # Question two strength values
                (
                    (SELECT id FROM nano_survey_configuration.issue WHERE issue_text = '{self.ISSUE_EXPECTED_GPA}' AND issue_type = '{self.ISSUE_TYPE_STRENGTH}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_TWO}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_TWO}' AND qbo.option_value = '{self.QUESTION_TWO_OPTION_ONE}'),
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.issue WHERE issue_text = '{self.ISSUE_EXPECTED_GPA}' AND issue_type = '{self.ISSUE_TYPE_STRENGTH}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_TWO}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_TWO}' AND qbo.option_value = '{self.QUESTION_TWO_OPTION_TWO}'),
                    2
                ),
                # Question three weakness values
                (
                    (SELECT id FROM nano_survey_configuration.issue WHERE issue_text = '{self.ISSUE_SATISFACTION}' AND issue_type = '{self.ISSUE_TYPE_WEAKNESS}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_THREE}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_THREE}' AND qbo.option_value = '{self.NUMERICAL_OPTION_ONE}'),
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.issue WHERE issue_text = '{self.ISSUE_SATISFACTION}' AND issue_type = '{self.ISSUE_TYPE_WEAKNESS}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_THREE}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_THREE}' AND qbo.option_value = '{self.NUMERICAL_OPTION_TWO}'),
                    2
                ),
                # Question three strength values
                (
                    (SELECT id FROM nano_survey_configuration.issue WHERE issue_text = '{self.ISSUE_SATISFACTION}' AND issue_type = '{self.ISSUE_TYPE_STRENGTH}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_THREE}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_THREE}' AND qbo.option_value = '{self.NUMERICAL_OPTION_SIX}'),
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.issue WHERE issue_text = '{self.ISSUE_SATISFACTION}' AND issue_type = '{self.ISSUE_TYPE_STRENGTH}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_THREE}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_THREE}' AND qbo.option_value = '{self.NUMERICAL_OPTION_SEVEN}'),
                    2
                ),
                # Question four weakness values
                (
                    (SELECT id FROM nano_survey_configuration.issue WHERE issue_text = '{self.ISSUE_CAMPUS_SERVICES}' AND issue_type = '{self.ISSUE_TYPE_WEAKNESS}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_FOUR}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_FOUR}' AND qbo.option_value = '{self.NUMERICAL_OPTION_ONE}'),
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.issue WHERE issue_text = '{self.ISSUE_CAMPUS_SERVICES}' AND issue_type = '{self.ISSUE_TYPE_WEAKNESS}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_FOUR}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_FOUR}' AND qbo.option_value = '{self.NUMERICAL_OPTION_TWO}'),
                    2
                ),
                # Question four strength values
                (
                    (SELECT id FROM nano_survey_configuration.issue WHERE issue_text = '{self.ISSUE_CAMPUS_SERVICES}' AND issue_type = '{self.ISSUE_TYPE_STRENGTH}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_FOUR}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_FOUR}' AND qbo.option_value = '{self.NUMERICAL_OPTION_SIX}'),
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.issue WHERE issue_text = '{self.ISSUE_CAMPUS_SERVICES}' AND issue_type = '{self.ISSUE_TYPE_STRENGTH}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_FOUR}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_FOUR}' AND qbo.option_value = '{self.NUMERICAL_OPTION_SEVEN}'),
                    2
                ),
                # Question five weakness values
                (
                    (SELECT id FROM nano_survey_configuration.issue WHERE issue_text = '{self.ISSUE_ACADEMIC_INTEGRATION}' AND issue_type = '{self.ISSUE_TYPE_WEAKNESS}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_FIVE}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_FIVE}' AND qbo.option_value = '{self.NUMERICAL_OPTION_ONE}'),
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.issue WHERE issue_text = '{self.ISSUE_ACADEMIC_INTEGRATION}' AND issue_type = '{self.ISSUE_TYPE_WEAKNESS}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_FIVE}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_FIVE}' AND qbo.option_value = '{self.NUMERICAL_OPTION_TWO}'),
                    2
                ),
                # Question five strength values
                (
                    (SELECT id FROM nano_survey_configuration.issue WHERE issue_text = '{self.ISSUE_ACADEMIC_INTEGRATION}' AND issue_type = '{self.ISSUE_TYPE_STRENGTH}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_FIVE}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_FIVE}' AND qbo.option_value = '{self.NUMERICAL_OPTION_SIX}'),
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.issue WHERE issue_text = '{self.ISSUE_ACADEMIC_INTEGRATION}' AND issue_type = '{self.ISSUE_TYPE_STRENGTH}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_FIVE}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_FIVE}' AND qbo.option_value = '{self.NUMERICAL_OPTION_SEVEN}'),
                    2
                ),
                # Question six weakness values
                (
                    (SELECT id FROM nano_survey_configuration.issue WHERE issue_text = '{self.ISSUE_SOCIAL_INTEGRATION}' AND issue_type = '{self.ISSUE_TYPE_WEAKNESS}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_SIX}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_SIX}' AND qbo.option_value = '{self.NUMERICAL_OPTION_ONE}'),
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.issue WHERE issue_text = '{self.ISSUE_SOCIAL_INTEGRATION}' AND issue_type = '{self.ISSUE_TYPE_WEAKNESS}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_SIX}'})),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_SIX}' AND qbo.option_value = '{self.NUMERICAL_OPTION_TWO}'),
                    2
                ),
                # Question six strength values
                (
                    (SELECT id FROM nano_survey_configuration.issue WHERE issue_text = '{self.ISSUE_SOCIAL_INTEGRATION}' AND issue_type = '{self.ISSUE_TYPE_STRENGTH}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_SIX}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_SIX}' AND qbo.option_value = '{self.NUMERICAL_OPTION_SIX}'),
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.issue WHERE issue_text = '{self.ISSUE_SOCIAL_INTEGRATION}' AND issue_type = '{self.ISSUE_TYPE_STRENGTH}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_SIX}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_SIX}' AND qbo.option_value = '{self.NUMERICAL_OPTION_SEVEN}'),
                    2
                ),
                # Question seven weakness values
                (
                    (SELECT id FROM nano_survey_configuration.issue WHERE issue_text = '{self.ISSUE_SENSE_OF_BELONGING}' AND issue_type = '{self.ISSUE_TYPE_WEAKNESS}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_SEVEN}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_SEVEN}' AND qbo.option_value = '{self.NUMERICAL_OPTION_ONE}'),
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.issue WHERE issue_text = '{self.ISSUE_SENSE_OF_BELONGING}' AND issue_type = '{self.ISSUE_TYPE_WEAKNESS}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_SEVEN}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_SEVEN}' AND qbo.option_value = '{self.NUMERICAL_OPTION_TWO}'),
                    2
                ),
                # Question seven strength values
                (
                    (SELECT id FROM nano_survey_configuration.issue WHERE issue_text = '{self.ISSUE_SENSE_OF_BELONGING}' AND issue_type = '{self.ISSUE_TYPE_STRENGTH}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_SEVEN}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_SEVEN}' AND qbo.option_value = '{self.NUMERICAL_OPTION_SIX}'),
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.issue WHERE issue_text = '{self.ISSUE_SENSE_OF_BELONGING}' AND issue_type = '{self.ISSUE_TYPE_STRENGTH}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_SEVEN}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_SEVEN}' AND qbo.option_value = '{self.NUMERICAL_OPTION_SEVEN}'),
                    2
                ),
                # Question eight weakness values - inverse
                (
                    (SELECT id FROM nano_survey_configuration.issue WHERE issue_text = '{self.ISSUE_HEALTH_RELATED_STRESS}' AND issue_type = '{self.ISSUE_TYPE_WEAKNESS}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_EIGHT}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_EIGHT}' AND qbo.option_value = '{self.NUMERICAL_OPTION_SIX}'),
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.issue WHERE issue_text = '{self.ISSUE_HEALTH_RELATED_STRESS}' AND issue_type = '{self.ISSUE_TYPE_WEAKNESS}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_EIGHT}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_EIGHT}' AND qbo.option_value = '{self.NUMERICAL_OPTION_SEVEN}'),
                    2
                ),
                # Question eight strength values - inverse
                (
                    (SELECT id FROM nano_survey_configuration.issue WHERE issue_text = '{self.ISSUE_HEALTH_RELATED_STRESS}' AND issue_type = '{self.ISSUE_TYPE_STRENGTH}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_EIGHT}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_EIGHT}' AND qbo.option_value = '{self.NUMERICAL_OPTION_ONE}'),
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.issue WHERE issue_text = '{self.ISSUE_HEALTH_RELATED_STRESS}' AND issue_type = '{self.ISSUE_TYPE_STRENGTH}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_EIGHT}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_EIGHT}' AND qbo.option_value = '{self.NUMERICAL_OPTION_TWO}'),
                    2
                ),
                # Question nine weakness values
                (
                    (SELECT id FROM nano_survey_configuration.issue WHERE issue_text = '{self.ISSUE_RESPONSE_SATISFACTION}' AND issue_type = '{self.ISSUE_TYPE_WEAKNESS}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = "{self.SURVEY_QUESTION_NINE}")),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = "{self.SURVEY_QUESTION_NINE}" AND qbo.option_value = '{self.NUMERICAL_OPTION_ONE}'),
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.issue WHERE issue_text = '{self.ISSUE_RESPONSE_SATISFACTION}' AND issue_type = '{self.ISSUE_TYPE_WEAKNESS}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = "{self.SURVEY_QUESTION_NINE}")),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = "{self.SURVEY_QUESTION_NINE}" AND qbo.option_value = '{self.NUMERICAL_OPTION_TWO}'),
                    2
                ),
                # Question nine strength values
                (
                    (SELECT id FROM nano_survey_configuration.issue WHERE issue_text = '{self.ISSUE_RESPONSE_SATISFACTION}' AND issue_type = '{self.ISSUE_TYPE_STRENGTH}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = "{self.SURVEY_QUESTION_NINE}")),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = "{self.SURVEY_QUESTION_NINE}" AND qbo.option_value = '{self.NUMERICAL_OPTION_SIX}'),
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.issue WHERE issue_text = '{self.ISSUE_RESPONSE_SATISFACTION}' AND issue_type = '{self.ISSUE_TYPE_STRENGTH}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = "{self.SURVEY_QUESTION_NINE}")),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = "{self.SURVEY_QUESTION_NINE}" AND qbo.option_value = '{self.NUMERICAL_OPTION_SEVEN}'),
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
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = "{self.SURVEY_QUESTION_ONE}" AND question_type = '{self.TEXT_SCALED}'),
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
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_THREE}' AND question_type = '{self.TEXT_SCALED}'),
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
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_FIVE}' AND question_type = '{self.TEXT_SCALED}'),
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
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = "{self.SURVEY_QUESTION_NINE}" AND question_type = '{self.TEXT_SCALED}'),
                    7,
                    2,
                    2
                );
            """,
            9: f"""
                INSERT INTO nano_survey_configuration.talking_point (question_bank_id, talking_point_type, text, next_steps, created_by, modified_by) VALUES
                (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = "{self.SURVEY_QUESTION_ONE}" AND question_type = '{self.TEXT_SCALED}'),
                    '{self.ISSUE_TYPE_WEAKNESS}',
                    '{self.QUESTION_ONE_TALKING_POINT_WEAKNESS}',
                    "{self.QUESTION_ONE_NEXT_STEPS}",
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text ="{self.SURVEY_QUESTION_ONE}" AND question_type = '{self.TEXT_SCALED}'),
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
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_THREE}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.ISSUE_TYPE_WEAKNESS}',
                    '{self.QUESTION_THREE_TALKING_POINT_WEAKNESS}',
                    '{self.QUESTION_THREE_NEXT_STEPS}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_THREE}' AND question_type = '{self.TEXT_SCALED}'),
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
                    null,
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
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_FIVE}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.ISSUE_TYPE_WEAKNESS}',
                    '{self.QUESTION_FIVE_TALKING_POINT_WEAKNESS}',
                    null,
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_FIVE}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.ISSUE_TYPE_STRENGTH}',
                    '{self.QUESTION_FIVE_TALKING_POINT_STRENGTH}',
                    null,
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_SIX}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.ISSUE_TYPE_WEAKNESS}',
                    '{self.QUESTION_SIX_TALKING_POINT_WEAKNESS}',
                    null,
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
                    "{self.QUESTION_SEVEN_TALKING_POINT_WEAKNESS}",
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
                    '{self.QUESTION_EIGHT_TALKING_POINT_WEAKNESS}',
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
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = "{self.SURVEY_QUESTION_NINE}" AND question_type = '{self.TEXT_SCALED}'),
                    '{self.ISSUE_TYPE_WEAKNESS}',
                    '{self.QUESTION_NINE_TALKING_POINT_WEAKNESS}',
                    null,
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = "{self.SURVEY_QUESTION_NINE}" AND question_type = '{self.TEXT_SCALED}'),
                    '{self.ISSUE_TYPE_STRENGTH}',
                    '{self.QUESTION_NINE_TALKING_POINT_STRENGTH}',
                    null,
                    2,
                    2
                );
                """,
                10: f"""
                    INSERT INTO nano_survey_configuration.talking_point_question_bank_option (talking_point_id, question_bank_option_id, created_by) VALUES
                    # Question one
                    (
                        (SELECT id FROM nano_survey_configuration.talking_point WHERE text = '{self.QUESTION_ONE_TALKING_POINT_WEAKNESS}' AND talking_point_type = '{self.ISSUE_TYPE_WEAKNESS}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = "{self.SURVEY_QUESTION_ONE}")),
                        (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = "{self.SURVEY_QUESTION_ONE}" AND qbo.option_value = '{self.NUMERICAL_OPTION_ONE}'),
                        2
                    ),
                    (
                        (SELECT id FROM nano_survey_configuration.talking_point WHERE text = '{self.QUESTION_ONE_TALKING_POINT_WEAKNESS}' AND talking_point_type = '{self.ISSUE_TYPE_WEAKNESS}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = "{self.SURVEY_QUESTION_ONE}")),
                        (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = "{self.SURVEY_QUESTION_ONE}" AND qbo.option_value = '{self.NUMERICAL_OPTION_TWO}'),
                        2
                    ),
                    (
                        (SELECT id FROM nano_survey_configuration.talking_point WHERE text = '{self.QUESTION_ONE_TALKING_POINT_STRENGTH}' AND talking_point_type = '{self.ISSUE_TYPE_STRENGTH}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = "{self.SURVEY_QUESTION_ONE}")),
                        (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = "{self.SURVEY_QUESTION_ONE}" AND qbo.option_value = '{self.NUMERICAL_OPTION_SIX}'),
                        2
                    ),
                    (
                        (SELECT id FROM nano_survey_configuration.talking_point WHERE text = '{self.QUESTION_ONE_TALKING_POINT_STRENGTH}' AND talking_point_type = '{self.ISSUE_TYPE_STRENGTH}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = "{self.SURVEY_QUESTION_ONE}")),
                        (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = "{self.SURVEY_QUESTION_ONE}" AND qbo.option_value = '{self.NUMERICAL_OPTION_SEVEN}'),
                        2
                    ),
                    # Question two
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
                    (
                        (SELECT id FROM nano_survey_configuration.talking_point WHERE text = '{self.QUESTION_TWO_TALKING_POINT_STRENGTH}' AND talking_point_type = '{self.ISSUE_TYPE_STRENGTH}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_TWO}')),
                        (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_TWO}' AND qbo.option_value = '{self.QUESTION_TWO_OPTION_TWO}'),
                        2
                    ),
                    # Question three
                    (
                        (SELECT id FROM nano_survey_configuration.talking_point WHERE text = '{self.QUESTION_THREE_TALKING_POINT_WEAKNESS}' AND talking_point_type = '{self.ISSUE_TYPE_WEAKNESS}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_THREE}')),
                        (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_THREE}' AND qbo.option_value = '{self.NUMERICAL_OPTION_ONE}'),
                        2
                    ),
                    (
                        (SELECT id FROM nano_survey_configuration.talking_point WHERE text = '{self.QUESTION_THREE_TALKING_POINT_WEAKNESS}' AND talking_point_type = '{self.ISSUE_TYPE_WEAKNESS}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_THREE}')),
                        (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_THREE}' AND qbo.option_value = '{self.NUMERICAL_OPTION_TWO}'),
                        2
                    ),
                    (
                        (SELECT id FROM nano_survey_configuration.talking_point WHERE text = '{self.QUESTION_THREE_TALKING_POINT_STRENGTH}' AND talking_point_type = '{self.ISSUE_TYPE_STRENGTH}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_THREE}')),
                        (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_THREE}' AND qbo.option_value = '{self.NUMERICAL_OPTION_SIX}'),
                        2
                    ),
                    (
                        (SELECT id FROM nano_survey_configuration.talking_point WHERE text = '{self.QUESTION_THREE_TALKING_POINT_STRENGTH}' AND talking_point_type = '{self.ISSUE_TYPE_STRENGTH}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_THREE}')),
                        (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_THREE}' AND qbo.option_value = '{self.NUMERICAL_OPTION_SEVEN}'),
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
                    # Question five
                    (
                        (SELECT id FROM nano_survey_configuration.talking_point WHERE text = '{self.QUESTION_FIVE_TALKING_POINT_WEAKNESS}' AND talking_point_type = '{self.ISSUE_TYPE_WEAKNESS}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_FIVE}')),
                        (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_FIVE}' AND qbo.option_value = '{self.NUMERICAL_OPTION_ONE}'),
                        2
                    ),
                    (
                        (SELECT id FROM nano_survey_configuration.talking_point WHERE text = '{self.QUESTION_FIVE_TALKING_POINT_WEAKNESS}' AND talking_point_type = '{self.ISSUE_TYPE_WEAKNESS}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_FIVE}')),
                        (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_FIVE}' AND qbo.option_value = '{self.NUMERICAL_OPTION_TWO}'),
                        2
                    ),
                    (
                        (SELECT id FROM nano_survey_configuration.talking_point WHERE text = '{self.QUESTION_FIVE_TALKING_POINT_STRENGTH}' AND talking_point_type = '{self.ISSUE_TYPE_STRENGTH}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_FIVE}')),
                        (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_FIVE}' AND qbo.option_value = '{self.NUMERICAL_OPTION_SIX}'),
                        2
                    ),
                    (
                        (SELECT id FROM nano_survey_configuration.talking_point WHERE text = '{self.QUESTION_FIVE_TALKING_POINT_STRENGTH}' AND talking_point_type = '{self.ISSUE_TYPE_STRENGTH}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_FIVE}')),
                        (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_FIVE}' AND qbo.option_value = '{self.NUMERICAL_OPTION_SEVEN}'),
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
                        (SELECT id FROM nano_survey_configuration.talking_point WHERE text = "{self.QUESTION_SEVEN_TALKING_POINT_WEAKNESS}" AND talking_point_type = '{self.ISSUE_TYPE_WEAKNESS}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_SEVEN}')),
                        (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_SEVEN}' AND qbo.option_value = '{self.NUMERICAL_OPTION_ONE}'),
                        2
                    ),
                    (
                        (SELECT id FROM nano_survey_configuration.talking_point WHERE text = "{self.QUESTION_SEVEN_TALKING_POINT_WEAKNESS}" AND talking_point_type = '{self.ISSUE_TYPE_WEAKNESS}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_SEVEN}')),
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
                    # Question eight - inverse
                    (
                        (SELECT id FROM nano_survey_configuration.talking_point WHERE text = '{self.QUESTION_EIGHT_TALKING_POINT_WEAKNESS}' AND talking_point_type = '{self.ISSUE_TYPE_WEAKNESS}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_EIGHT}')),
                        (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_EIGHT}' AND qbo.option_value = '{self.NUMERICAL_OPTION_SIX}'),
                        2
                    ),
                    (
                        (SELECT id FROM nano_survey_configuration.talking_point WHERE text = '{self.QUESTION_EIGHT_TALKING_POINT_WEAKNESS}' AND talking_point_type = '{self.ISSUE_TYPE_WEAKNESS}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_EIGHT}')),
                        (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_EIGHT}' AND qbo.option_value = '{self.NUMERICAL_OPTION_SEVEN}'),
                        2
                    ),
                    (
                        (SELECT id FROM nano_survey_configuration.talking_point WHERE text = '{self.QUESTION_EIGHT_TALKING_POINT_STRENGTH}' AND talking_point_type = '{self.ISSUE_TYPE_STRENGTH}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_EIGHT}')),
                        (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_EIGHT}' AND qbo.option_value = '{self.NUMERICAL_OPTION_ONE}'),
                        2
                    ),
                    (
                        (SELECT id FROM nano_survey_configuration.talking_point WHERE text = '{self.QUESTION_EIGHT_TALKING_POINT_STRENGTH}' AND talking_point_type = '{self.ISSUE_TYPE_STRENGTH}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_EIGHT}')),
                        (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_EIGHT}' AND qbo.option_value = '{self.NUMERICAL_OPTION_TWO}'),
                        2
                    ),
                    # Question nine
                    (
                        (SELECT id FROM nano_survey_configuration.talking_point WHERE text = '{self.QUESTION_NINE_TALKING_POINT_WEAKNESS}' AND talking_point_type = '{self.ISSUE_TYPE_WEAKNESS}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = "{self.SURVEY_QUESTION_NINE}")),
                        (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = "{self.SURVEY_QUESTION_NINE}" AND qbo.option_value = '{self.NUMERICAL_OPTION_ONE}'),
                        2
                    ),
                    (
                        (SELECT id FROM nano_survey_configuration.talking_point WHERE text = '{self.QUESTION_NINE_TALKING_POINT_WEAKNESS}' AND talking_point_type = '{self.ISSUE_TYPE_WEAKNESS}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = "{self.SURVEY_QUESTION_NINE}")),
                        (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = "{self.SURVEY_QUESTION_NINE}" AND qbo.option_value = '{self.NUMERICAL_OPTION_TWO}'),
                        2
                    ),
                    (
                        (SELECT id FROM nano_survey_configuration.talking_point WHERE text = '{self.QUESTION_NINE_TALKING_POINT_STRENGTH}' AND talking_point_type = '{self.ISSUE_TYPE_STRENGTH}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = "{self.SURVEY_QUESTION_NINE}")),
                        (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = "{self.SURVEY_QUESTION_NINE}" AND qbo.option_value = '{self.NUMERICAL_OPTION_SIX}'),
                        2
                    ),
                    (
                        (SELECT id FROM nano_survey_configuration.talking_point WHERE text = '{self.QUESTION_NINE_TALKING_POINT_STRENGTH}' AND talking_point_type = '{self.ISSUE_TYPE_STRENGTH}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = "{self.SURVEY_QUESTION_NINE}")),
                        (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = "{self.SURVEY_QUESTION_NINE}" AND qbo.option_value = '{self.NUMERICAL_OPTION_SEVEN}'),
                        2
                    );
                """
            }


            self.sql_dictionary = collections.OrderedDict(sorted(self.sql.items()))
