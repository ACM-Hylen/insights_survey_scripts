from sql.nano_survey_configuration.base_migration import BaseMigration
import collections


class MigrationScript(BaseMigration):
    """
        Readiness Survey - Fall 2020 Non Residential
    """
    sql = None
    sql_dictionary = None

    SURVEY_TEMPLATE_INTERNAL_KEY = 'readiness_2020_fall_non_residential'

    # Purpose text
    SURVEY_WHY_TEXT = 'The start of a new year used to mean excitement, but this year is different and has introduced anxiety and uncertainty. This survey will help identify students with concerns, changing plans, and those that may not feel ready for the start of the year so that you can intervene and assist students in need.'
    SURVEY_HOW_TEXT = 'To capture quick, meaningful insights, we took some of the best questions from the Mapworks Transition Survey. The content was built and tested over 3 decades using data from 200+ institutions and 1 million+ students. We combined those with additional questions to provide data on how students are feeling about the upcoming year. We focused the survey content to be a quick check-in for students that provides actionable data.'
    SURVEY_HOVER_TEXT = 'Pre-arrival survey to identify areas of concern'
    # New questions
    SURVEY_QUESTION_ONE = 'To what extent do you intend to attend this institution for the upcoming academic term?'
    SURVEY_QUESTION_TWO = 'To what extent do you feel you have been given the necessary information to start the term?'
    SURVEY_QUESTION_THREE = 'To what extent do you have the technology resources to accommodate online classes?'
    SURVEY_QUESTION_FOUR = 'To what extent are you experiencing stress because of COVID-19 health and safety concerns in attending your institution?'
    SURVEY_QUESTION_FIVE = "To what extent are you confident that you can pay for this term's tuition and fees?"
    SURVEY_QUESTION_SIX = 'To what extent are you academically prepared for the upcoming term?'
    SURVEY_QUESTION_SEVEN = 'To what extent are you academically motivated for the upcoming term?'
    SURVEY_QUESTION_EIGHT = 'To what extent do you belong at this institution?'
    # Issue text for this template
    ISSUE_INTENT_TO_RETURN = "Intent to Return - Readiness Survey"
    ISSUE_INFORMED_READINESS = "Informed Readiness - Readiness Survey"
    ISSUE_TECH_READINESS = "Tech Readiness - Readiness Survey"
    ISSUE_HEALTH_RELATED_STRESS = "Health-Related Stress - Readiness Survey"
    ISSUE_HOUSING_PLANS = "Housing Plans  - Readiness Survey"
    ISSUE_FINANCIAL_MEANS = "Financial Means -  Readiness Survey"
    ISSUE_ACADEMIC_PREPAREDNESS = "Academic Preparedness  - Readiness Survey"
    ISSUE_ACADEMIC_MOTIVATION = "Academic Motivation - Readiness Survey"
    ISSUE_SENSE_OF_BELONGING = "Sense of Belonging  - Readiness Survey"
    # Talking Points
    QUESTION_ONE_TALKING_POINT_WEAKNESS = 'Student is questioning or reconsidering their decision to attend this institution. Reach out to this student to understand their decision and future plans.'
    QUESTION_ONE_TALKING_POINT_STRENGTH = 'Student intends to enroll this term.'
    QUESTION_ONE_NEXT_STEPS = "Students who say they don't intend to return, often don't. Intervening early with these students might help identify issues and increase the likelihood that they continue their education"
    QUESTION_TWO_TALKING_POINT_WEAKNESS = ' Student feels they do not have the information they need to start the upcoming term. Additional outreach to this student may help clarify any questions they have.'
    QUESTION_TWO_TALKING_POINT_STRENGTH = 'Student feels they have the necessary information to start the term.'
    QUESTION_TWO_NEXT_STEPS = 'Uncertainty over the upcoming term may cause stress and cause students to questions enrollment decisions. Provide students with information about what the institution is doing and what is expected of them when they arrive on campus. '
    QUESTION_THREE_TALKING_POINT_WEAKNESS = 'Student indicates they lack access to technology resources necessary to complete coursework virtually. This could make completing courses that are hybrid or entirely online challenging.'
    QUESTION_THREE_TALKING_POINT_STRENGTH = 'Student feels technologically equipped for online course'
    QUESTION_THREE_NEXT_STEPS = 'If course delivery methods change to hybrid or online instruction, students without proper resources may struggle to attend class sessions, engage, and complete coursework. Making students aware of resources ahead of the term may help prevent technology from adversely affecting their experience.'
    QUESTION_FOUR_TALKING_POINT_WEAKNESS = 'Student is experiencing stress related to COVID-19 and attending this institution. Outreach can ensure they understand what the institution is doing to protect their health and safety, know what to expect for the start of the term, and identify resources the student could benefit from.'
    QUESTION_FOUR_TALKING_POINT_STRENGTH = 'Student does not report stress related to attending class amid the changes caused by COVID-19.'
    QUESTION_FOUR_NEXT_STEPS = 'Keep students informed about what the institution is doing to keep the campus community safe. Students may need support or feel heard about concerns.'
    QUESTION_FIVE_TALKING_POINT_WEAKNESS = "Student expects difficulties paying this term's tuition and fees. Resolving these issues before classes begin can help reduce stress and enable students to register for future terms. Refer this student to financial aid resources."
    QUESTION_FIVE_TALKING_POINT_STRENGTH = 'Student is confident they can pay this terms tuition and fees.'
    QUESTION_FIVE_NEXT_STEPS = 'Students who lack confidence to pay their tuition and fees may experience stress from upcoming bills and may need support. Ensure students know about the financial aid office and services available to them.'
    QUESTION_SIX_TALKING_POINT_WEAKNESS = 'Student does not feel academically prepared for the upcoming term. Given the range of possible issues, early outreach can help identify the nature of these issues so they can be connected to the right resources as early as possible.'
    QUESTION_SIX_TALKING_POINT_STRENGTH = 'Student feels academically prepared for the upcoming term.'
    QUESTION_SIX_NEXT_STEPS = 'The pandemic disrupted the academic work in the spring and students may not feel prepared to advance their academic progress. The transition that incoming students are experiencing is unprecedented and they may need additional support. '
    QUESTION_SEVEN_TALKING_POINT_WEAKNESS = 'Student lacks motivation for the start of classes. Motivation struggles can be the result of a wide range of other issues. Therefore, early outreach to better understand the source of motivation struggles is important.'
    QUESTION_SEVEN_TALKING_POINT_STRENGTH = 'Student reports being motivated to begin classes.'
    QUESTION_SEVEN_NEXT_STEPS = 'Help students find what motivates them to complete their course and their degree. Discussing their motivation may help explore root causes and provide opportunities to connect the student to resources. '
    QUESTION_EIGHT_TALKING_POINT_WEAKNESS = 'Student does not feel like they belong at this institution. Feeling or achieving a sense of belonging may be more challenging as the institution responds to the pandemic and the need to social distance. '
    QUESTION_EIGHT_TALKING_POINT_STRENGTH = 'Student feels like they belong at this institution. '
    QUESTION_EIGHT_NEXT_STEPS = 'Sense of belonging is a strong predictor of retention. Help students make connections to peers and organizations on campus and in the community, whether in-person or virtually. '

    # Other
    CONSENT_STATEMENT = "Macmillan Learning is conducting the following survey on behalf of your organization/institution. Your survey responses are submitted to us utilizing data encryption methodology (SSL) used to protect financial transactions conducted over the internet and we handle your data pursuant to the <a target='_blank' href='https://store.macmillanlearning.com/us/privacy-notice'>Macmillan Learning Privacy Notice.</a> Your responses will be collected by us in a personally identifiable format and we will provide it to your organization/institutions linked to your personal identifiers.  Your organization/institution can use your personal information and survey results pursuant to their own Privacy Policy, including using the results of your survey responses in an aggregated and anonymized form in connection with its presentations, reports and publications. Macmillan Learning may de-identify your survey responses and analyze the data to improve its educational products and services, including to create aggregated or statistical insights and baseline reports that are not identifiable to you or any other individual for use in other Macmillan Learning educational products and services.  If you prefer not to participate in this survey, you may leave questions blank or close the browser and leave the survey.  Contact your organisation/institution for more information about its use of the responses."


    def __init__(self):
        super().__init__()
        self.sql = {
            1: f"""
                INSERT INTO nano_survey_configuration.survey_template (title, internal_key, hover_text, time_to_complete, user_data_consent_statement, created_by, modified_by) VALUES
                ('Readiness Survey - Fall 2020', '{self.SURVEY_TEMPLATE_INTERNAL_KEY}', '{self.SURVEY_HOVER_TEXT}', 5, "{self.CONSENT_STATEMENT}", 2, 2);
            """,
            3: f"""
                INSERT INTO nano_survey_configuration.question_bank (question_text, alternate_question_text, question_type, created_by, modified_by) VALUES
                ('{self.SURVEY_QUESTION_ONE}', '', '{self.TEXT_SCALED}', 2, 2),
                ('{self.SURVEY_QUESTION_TWO}', '', '{self.TEXT_SCALED}', 2, 2),
                ('{self.SURVEY_QUESTION_THREE}', '', '{self.TEXT_SCALED}', 2, 2),
                ('{self.SURVEY_QUESTION_FOUR}', '', '{self.TEXT_SCALED}', 2, 2),
                ("{self.SURVEY_QUESTION_FIVE}", '', '{self.TEXT_SCALED}', 2, 2),
                ('{self.SURVEY_QUESTION_SIX}', '', '{self.TEXT_SCALED}', 2, 2),
                ('{self.SURVEY_QUESTION_SEVEN}', '', '{self.TEXT_SCALED}', 2, 2),
                ('{self.SURVEY_QUESTION_EIGHT}', '', '{self.TEXT_SCALED}', 2, 2);
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
                    'Not at All',
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
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_SIX}' AND question_type = '{self.TEXT_SCALED}'),
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
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_SIX}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.NUMERICAL_OPTION_SEVEN}',
                    'Extremely',
                    '{self.TYPE_INTEGER}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_SIX}' AND question_type = '{self.TEXT_SCALED}'),
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
                );
            """,

            5: f"""
                INSERT INTO nano_survey_configuration.issue (reporting_category_id, question_bank_id, issue_text, issue_type, created_by, modified_by) VALUES
                (
                    (SELECT id FROM nano_survey_configuration.reporting_category WHERE text = '{self.REPORTING_CATEGORY_INSTITUTIONAL}'),
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_ONE}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.ISSUE_INTENT_TO_RETURN}',
                    '{self.ISSUE_TYPE_WEAKNESS}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.reporting_category WHERE text = '{self.REPORTING_CATEGORY_INSTITUTIONAL}'),
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_ONE}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.ISSUE_INTENT_TO_RETURN}',
                    '{self.ISSUE_TYPE_STRENGTH}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.reporting_category WHERE text = '{self.REPORTING_CATEGORY_INSTITUTIONAL}'),
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_TWO}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.ISSUE_INFORMED_READINESS}',
                    '{self.ISSUE_TYPE_WEAKNESS}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.reporting_category WHERE text = '{self.REPORTING_CATEGORY_INSTITUTIONAL}'),
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_TWO}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.ISSUE_INFORMED_READINESS}',
                    '{self.ISSUE_TYPE_STRENGTH}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.reporting_category WHERE text = '{self.REPORTING_CATEGORY_INSTITUTIONAL}'),
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_THREE}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.ISSUE_TECH_READINESS}',
                    '{self.ISSUE_TYPE_WEAKNESS}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.reporting_category WHERE text = '{self.REPORTING_CATEGORY_INSTITUTIONAL}'),
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_THREE}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.ISSUE_TECH_READINESS}',
                    '{self.ISSUE_TYPE_STRENGTH}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.reporting_category WHERE text = '{self.REPORTING_CATEGORY_INSTITUTIONAL}'),
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_FOUR}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.ISSUE_HEALTH_RELATED_STRESS}',
                    '{self.ISSUE_TYPE_WEAKNESS}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.reporting_category WHERE text = '{self.REPORTING_CATEGORY_INSTITUTIONAL}'),
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_FOUR}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.ISSUE_HEALTH_RELATED_STRESS}',
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
                    (SELECT id FROM nano_survey_configuration.reporting_category WHERE text = '{self.REPORTING_CATEGORY_FINANCIAL}'),
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = "{self.SURVEY_QUESTION_FIVE}" AND question_type = '{self.TEXT_SCALED}'),
                    '{self.ISSUE_FINANCIAL_MEANS}',
                    '{self.ISSUE_TYPE_STRENGTH}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.reporting_category WHERE text = '{self.REPORTING_CATEGORY_ACADEMIC}'),
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_SIX}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.ISSUE_ACADEMIC_PREPAREDNESS}',
                    '{self.ISSUE_TYPE_WEAKNESS}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.reporting_category WHERE text = '{self.REPORTING_CATEGORY_ACADEMIC}'),
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_SIX}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.ISSUE_ACADEMIC_PREPAREDNESS}',
                    '{self.ISSUE_TYPE_STRENGTH}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.reporting_category WHERE text = '{self.REPORTING_CATEGORY_ACADEMIC}'),
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_SEVEN}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.ISSUE_ACADEMIC_MOTIVATION}',
                    '{self.ISSUE_TYPE_WEAKNESS}',
                    2,
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.reporting_category WHERE text = '{self.REPORTING_CATEGORY_ACADEMIC}'),
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_SEVEN}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.ISSUE_ACADEMIC_MOTIVATION}',
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
                )
                ;
            """,
            6: f"""
                INSERT INTO nano_survey_configuration.issue_question_bank_option (issue_id, question_bank_option_id, created_by) VALUES
                # Question one weakness values
                (
                    (SELECT id FROM nano_survey_configuration.issue WHERE issue_text = '{self.ISSUE_INTENT_TO_RETURN}' AND issue_type = '{self.ISSUE_TYPE_WEAKNESS}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_ONE}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_ONE}' AND qbo.option_value = '{self.NUMERICAL_OPTION_ONE}'),
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.issue WHERE issue_text = '{self.ISSUE_INTENT_TO_RETURN}' AND issue_type = '{self.ISSUE_TYPE_WEAKNESS}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_ONE}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_ONE}' AND qbo.option_value = '{self.NUMERICAL_OPTION_TWO}'),
                    2
                ),
                # Question one strength values
                (
                    (SELECT id FROM nano_survey_configuration.issue WHERE issue_text = '{self.ISSUE_INTENT_TO_RETURN}' AND issue_type = '{self.ISSUE_TYPE_STRENGTH}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_ONE}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_ONE}' AND qbo.option_value = '{self.NUMERICAL_OPTION_SIX}'),
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.issue WHERE issue_text = '{self.ISSUE_INTENT_TO_RETURN}' AND issue_type = '{self.ISSUE_TYPE_STRENGTH}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_ONE}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_ONE}' AND qbo.option_value = '{self.NUMERICAL_OPTION_SEVEN}'),
                    2
                ),
                # Question two weakness values
                (
                    (SELECT id FROM nano_survey_configuration.issue WHERE issue_text = '{self.ISSUE_INFORMED_READINESS}' AND issue_type = '{self.ISSUE_TYPE_WEAKNESS}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_TWO}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_TWO}' AND qbo.option_value = '{self.NUMERICAL_OPTION_ONE}'),
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.issue WHERE issue_text = '{self.ISSUE_INFORMED_READINESS}' AND issue_type = '{self.ISSUE_TYPE_WEAKNESS}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_TWO}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_TWO}' AND qbo.option_value = '{self.NUMERICAL_OPTION_TWO}'),
                    2
                ),
                # Question two strength values
                (
                    (SELECT id FROM nano_survey_configuration.issue WHERE issue_text = '{self.ISSUE_INFORMED_READINESS}' AND issue_type = '{self.ISSUE_TYPE_STRENGTH}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_TWO}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_TWO}' AND qbo.option_value = '{self.NUMERICAL_OPTION_SIX}'),
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.issue WHERE issue_text = '{self.ISSUE_INFORMED_READINESS}' AND issue_type = '{self.ISSUE_TYPE_STRENGTH}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_TWO}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_TWO}' AND qbo.option_value = '{self.NUMERICAL_OPTION_SEVEN}'),
                    2
                ),
                # Question three weakness values
                (
                    (SELECT id FROM nano_survey_configuration.issue WHERE issue_text = '{self.ISSUE_TECH_READINESS}' AND issue_type = '{self.ISSUE_TYPE_WEAKNESS}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_THREE}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_THREE}' AND qbo.option_value = '{self.NUMERICAL_OPTION_ONE}'),
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.issue WHERE issue_text = '{self.ISSUE_TECH_READINESS}' AND issue_type = '{self.ISSUE_TYPE_WEAKNESS}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_THREE}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_THREE}' AND qbo.option_value = '{self.NUMERICAL_OPTION_TWO}'),
                    2
                ),
                # Question three strength values
                (
                    (SELECT id FROM nano_survey_configuration.issue WHERE issue_text = '{self.ISSUE_TECH_READINESS}' AND issue_type = '{self.ISSUE_TYPE_STRENGTH}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_THREE}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_THREE}' AND qbo.option_value = '{self.NUMERICAL_OPTION_SIX}'),
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.issue WHERE issue_text = '{self.ISSUE_TECH_READINESS}' AND issue_type = '{self.ISSUE_TYPE_STRENGTH}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_THREE}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_THREE}' AND qbo.option_value = '{self.NUMERICAL_OPTION_SEVEN}'),
                    2
                ),
                # Question four weakness values
                (
                    (SELECT id FROM nano_survey_configuration.issue WHERE issue_text = '{self.ISSUE_HEALTH_RELATED_STRESS}' AND issue_type = '{self.ISSUE_TYPE_WEAKNESS}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_FOUR}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_FOUR}' AND qbo.option_value = '{self.NUMERICAL_OPTION_SIX}'),
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.issue WHERE issue_text = '{self.ISSUE_HEALTH_RELATED_STRESS}' AND issue_type = '{self.ISSUE_TYPE_WEAKNESS}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_FOUR}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_FOUR}' AND qbo.option_value = '{self.NUMERICAL_OPTION_SEVEN}'),
                    2
                ),
                # Question four strength values
                (
                    (SELECT id FROM nano_survey_configuration.issue WHERE issue_text = '{self.ISSUE_HEALTH_RELATED_STRESS}' AND issue_type = '{self.ISSUE_TYPE_STRENGTH}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_FOUR}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_FOUR}' AND qbo.option_value = '{self.NUMERICAL_OPTION_ONE}'),
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.issue WHERE issue_text = '{self.ISSUE_HEALTH_RELATED_STRESS}' AND issue_type = '{self.ISSUE_TYPE_STRENGTH}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_FOUR}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_FOUR}' AND qbo.option_value = '{self.NUMERICAL_OPTION_TWO}'),
                    2
                ),
                # Question five weakness values
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
                # Question FIVE strength values
                (
                    (SELECT id FROM nano_survey_configuration.issue WHERE issue_text = '{self.ISSUE_FINANCIAL_MEANS}' AND issue_type = '{self.ISSUE_TYPE_STRENGTH}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = "{self.SURVEY_QUESTION_FIVE}")),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = "{self.SURVEY_QUESTION_FIVE}" AND qbo.option_value = '{self.NUMERICAL_OPTION_SIX}'),
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.issue WHERE issue_text = '{self.ISSUE_FINANCIAL_MEANS}' AND issue_type = '{self.ISSUE_TYPE_STRENGTH}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = "{self.SURVEY_QUESTION_FIVE}")),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = "{self.SURVEY_QUESTION_FIVE}" AND qbo.option_value = '{self.NUMERICAL_OPTION_SEVEN}'),
                    2
                ),
                # Question SIX weakness values
                (
                    (SELECT id FROM nano_survey_configuration.issue WHERE issue_text = '{self.ISSUE_ACADEMIC_PREPAREDNESS}' AND issue_type = '{self.ISSUE_TYPE_WEAKNESS}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_SIX}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_SIX}' AND qbo.option_value = '{self.NUMERICAL_OPTION_ONE}'),
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.issue WHERE issue_text = '{self.ISSUE_ACADEMIC_PREPAREDNESS}' AND issue_type = '{self.ISSUE_TYPE_WEAKNESS}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_SIX}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_SIX}' AND qbo.option_value = '{self.NUMERICAL_OPTION_TWO}'),
                    2
                ),
                # Question SIX strength values
                (
                    (SELECT id FROM nano_survey_configuration.issue WHERE issue_text = '{self.ISSUE_ACADEMIC_PREPAREDNESS}' AND issue_type = '{self.ISSUE_TYPE_STRENGTH}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_SIX}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_SIX}' AND qbo.option_value = '{self.NUMERICAL_OPTION_SIX}'),
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.issue WHERE issue_text = '{self.ISSUE_ACADEMIC_PREPAREDNESS}' AND issue_type = '{self.ISSUE_TYPE_STRENGTH}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_SIX}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_SIX}' AND qbo.option_value = '{self.NUMERICAL_OPTION_SEVEN}'),
                    2
                ),
                # Question SEVEN weakness values
                (
                    (SELECT id FROM nano_survey_configuration.issue WHERE issue_text = '{self.ISSUE_ACADEMIC_MOTIVATION}' AND issue_type = '{self.ISSUE_TYPE_WEAKNESS}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_SEVEN}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_SEVEN}' AND qbo.option_value = '{self.NUMERICAL_OPTION_ONE}'),
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.issue WHERE issue_text = '{self.ISSUE_ACADEMIC_MOTIVATION}' AND issue_type = '{self.ISSUE_TYPE_WEAKNESS}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_SEVEN}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_SEVEN}' AND qbo.option_value = '{self.NUMERICAL_OPTION_TWO}'),
                    2
                ),
                # Question SEVEN strength values
                (
                    (SELECT id FROM nano_survey_configuration.issue WHERE issue_text = '{self.ISSUE_ACADEMIC_MOTIVATION}' AND issue_type = '{self.ISSUE_TYPE_STRENGTH}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_SEVEN}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_SEVEN}' AND qbo.option_value = '{self.NUMERICAL_OPTION_SIX}'),
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.issue WHERE issue_text = '{self.ISSUE_ACADEMIC_MOTIVATION}' AND issue_type = '{self.ISSUE_TYPE_STRENGTH}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_SEVEN}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_SEVEN}' AND qbo.option_value = '{self.NUMERICAL_OPTION_SEVEN}'),
                    2
                ),
                # Question EIGHT weakness values
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
                # Question EIGHT strength values
                (
                    (SELECT id FROM nano_survey_configuration.issue WHERE issue_text = '{self.ISSUE_SENSE_OF_BELONGING}' AND issue_type = '{self.ISSUE_TYPE_STRENGTH}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_EIGHT}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_EIGHT}' AND qbo.option_value = '{self.NUMERICAL_OPTION_SIX}'),
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.issue WHERE issue_text = '{self.ISSUE_SENSE_OF_BELONGING}' AND issue_type = '{self.ISSUE_TYPE_STRENGTH}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_EIGHT}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_EIGHT}' AND qbo.option_value = '{self.NUMERICAL_OPTION_SEVEN}'),
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
                );
            """,
            9: f"""
                INSERT INTO nano_survey_configuration.talking_point (question_bank_id, talking_point_type, text, next_steps, created_by, modified_by) VALUES
                (
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_ONE}' AND question_type = '{self.TEXT_SCALED}'),
                    '{self.ISSUE_TYPE_WEAKNESS}',
                    '{self.QUESTION_ONE_TALKING_POINT_WEAKNESS}',
                    "{self.QUESTION_ONE_NEXT_STEPS}",
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
                    (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = "{self.SURVEY_QUESTION_FIVE}" AND question_type = '{self.TEXT_SCALED}'),
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
                    '{self.QUESTION_SIX_NEXT_STEPS}',
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
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_TWO}' AND qbo.option_value = '{self.NUMERICAL_OPTION_ONE}'),
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.talking_point WHERE text = '{self.QUESTION_TWO_TALKING_POINT_WEAKNESS}' AND talking_point_type = '{self.ISSUE_TYPE_WEAKNESS}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_TWO}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_TWO}' AND qbo.option_value = '{self.NUMERICAL_OPTION_TWO}'),
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.talking_point WHERE text = '{self.QUESTION_TWO_TALKING_POINT_STRENGTH}' AND talking_point_type = '{self.ISSUE_TYPE_STRENGTH}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_TWO}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_TWO}' AND qbo.option_value = '{self.NUMERICAL_OPTION_SIX}'),
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.talking_point WHERE text = '{self.QUESTION_TWO_TALKING_POINT_STRENGTH}' AND talking_point_type = '{self.ISSUE_TYPE_STRENGTH}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_TWO}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_TWO}' AND qbo.option_value = '{self.NUMERICAL_OPTION_SEVEN}'),
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
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_FOUR}' AND qbo.option_value = '{self.NUMERICAL_OPTION_SIX}'),
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.talking_point WHERE text = '{self.QUESTION_FOUR_TALKING_POINT_WEAKNESS}' AND talking_point_type = '{self.ISSUE_TYPE_WEAKNESS}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_FOUR}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_FOUR}' AND qbo.option_value = '{self.NUMERICAL_OPTION_SEVEN}'),
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.talking_point WHERE text = '{self.QUESTION_FOUR_TALKING_POINT_STRENGTH}' AND talking_point_type = '{self.ISSUE_TYPE_STRENGTH}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_FOUR}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_FOUR}' AND qbo.option_value = '{self.NUMERICAL_OPTION_ONE}'),
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.talking_point WHERE text = '{self.QUESTION_FOUR_TALKING_POINT_STRENGTH}' AND talking_point_type = '{self.ISSUE_TYPE_STRENGTH}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = '{self.SURVEY_QUESTION_FOUR}')),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = '{self.SURVEY_QUESTION_FOUR}' AND qbo.option_value = '{self.NUMERICAL_OPTION_TWO}'),
                    2
                ),
                # Question five
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
                (
                    (SELECT id FROM nano_survey_configuration.talking_point WHERE text = '{self.QUESTION_FIVE_TALKING_POINT_STRENGTH}' AND talking_point_type = '{self.ISSUE_TYPE_STRENGTH}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = "{self.SURVEY_QUESTION_FIVE}")),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = "{self.SURVEY_QUESTION_FIVE}" AND qbo.option_value = '{self.NUMERICAL_OPTION_SIX}'),
                    2
                ),
                (
                    (SELECT id FROM nano_survey_configuration.talking_point WHERE text = '{self.QUESTION_FIVE_TALKING_POINT_STRENGTH}' AND talking_point_type = '{self.ISSUE_TYPE_STRENGTH}' AND question_bank_id = (SELECT id FROM nano_survey_configuration.question_bank WHERE question_text = "{self.SURVEY_QUESTION_FIVE}")),
                    (SELECT qbo.id FROM nano_survey_configuration.question_bank_option qbo JOIN nano_survey_configuration.question_bank qb ON qb.id = qbo.question_bank_id WHERE qb.question_text = "{self.SURVEY_QUESTION_FIVE}" AND qbo.option_value = '{self.NUMERICAL_OPTION_SEVEN}'),
                    2
                ),
                # Question SIX
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
                # Question SEVEN
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
                );
            """
        }


        self.sql_dictionary = collections.OrderedDict(sorted(self.sql.items()))
