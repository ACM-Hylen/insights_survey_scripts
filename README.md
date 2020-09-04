# inst_nano1
#COMMENTS and TABLE ORDER from Josh Oryall... 

# The patterns you see in this survey template migration script will generally remain the same for each future
    #   survey template migration script. The migration script's name - 1585938572.py - is just the UNIX TIMESTAMP of
    #   the current time when the script was created. This helps the lambda that executes the migrations run them in
    #   order. Once the migration has been ran, that file name is placed along with the completion time in the
    #   sql_migration_version table of the respective nano-survey schema. Check the base_migration parent class for that
    #   schema

    # Helpful migration script tips
    # - Put all reusable keys / text in a constant - anything that you'll have to use more than twice.
    #       there's already constants defined in the base_migration.py file for this directory that are inherited here
    # - Never reference the primary key ID field in a migration script - those IDs could change per environment and will ruin your associations
    # - Each of the query entries is a formatted string (f"""""") so that interpolation ('{self.variable}') can be utilized


    # This value is simply a key we can use to reference the template internally if we have to code to specific templates.
    # Totally up to the developer what this value is, but we usually have it match up with the template title name. 



 #Index 1 Each element in the ordered dictionary corresponds to one query being run. Each query is executed in index order.
            # First, let's create the survey template record, since the template ID will be reused in several later queries.
            # The template record contains basic metadata about the survey template - title, internal key, description, etc.
		INSERT INTO nano_survey_configuration.survey_template (title, internal_key, hover_text, time_to_complete, user_data_consent_statement, created_by, modified_by) VALUES
		
 # Index 2 Now that the template has been added, we need to create the purpose text. This is the text that appears
            # on the second page of the survey launch process, talking about how the survey was created and why the
            # survey should be used. If the why or how text is repeated from a previous survey, don't duplicate it.
            # - Get the text and put it in a constant for reference later
		INSERT INTO nano_survey_configuration.survey_purpose (section, purpose_text, section_title, icon_filename, created_by, modified_by) VALUES

 # Index 3 The next query is where you'll add the questions for the survey to the question bank.
            # BE SURE TO CHECK THE EXISTING QUESTION BANK TABLE TO ENSURE THAT THE QUESTIONS DONT ALREADY EXIST.
            # If the questions do already exist, don't add them here. Get the QUESTION TEXT for those and make a constant for them for later reference.
            # You'll notice that four, nine, and ten do not have entries in this query but will be used later on. They already exist in Nano
            # Alternate question text does not typically have values
            # Scaled questions - answers are on a numerical scale. Categorical questions are a choice from a list of text options.
			INSERT INTO nano_survey_configuration.question_bank (question_text, alternate_question_text, question_type, created_by, modified_by) VALUES

# Index 4 This query will add the options for the individual questions, and the linkage back to the question.
            # Here is where you'll start reusing a bunch of the previous constants for the questions.
            # Additional text functions the same on the option that it does on the question.
            # Option type is an indicator that's used by the FE later on to determine display properties.
            # Each option will have it's own record.
            # Notice that the question ID lookup is being done instead of referencing the primary key ID of the question bank record.
            # Notice that option 99 has optional text - "not applicable"
			INSERT INTO nano_survey_configuration.question_bank_option (question_bank_id, option_value, additional_text, option_type, created_by, modified_by) VALUES

# Index 5 was intentionally left out here - this would be where, if there was a new reporting category to
            #   be added, this record would be created. See previous templates for an example on how to do that.
            # Reporting categories are basically issue groups. An issue is a problem that a student has indicated they
            #   have based on a survey response.
	 
# Index 6 creates the issues records, as described in the comment above. They link a reporting category
            #   to a question, with text explaining what it is the student is facing. It could either be a
            #   problem (Weakness issue) or a strength (Strength issue). Each question gets a record in this table for
            #   both issue types for each issue it's options are associated with.
            # You'll notice that the existing questions do not have entries here because they're already linked to
            #   their respective issues.
	    # Multiple questions could also aggregate into the same issue.
		 INSERT INTO nano_survey_configuration.issue (reporting_category_id, question_bank_id, issue_text, issue_type, created_by, modified_by) VALUES

# Index 7 Now that you've linked the issue to the question, you'll need to link the individual option values to
            #       those issues as well.
            # There won't be a linkage here per each option for the question,
            #       but only for the specified strength or weakness options.
            #   For example, if options 1-2 are flagged as weaknesses and 6-7 are flagged as strengths,
            #       then options 3-5 will not have records in the query below
            # Options could also be linked to the same issue (weakness for a specific value or values,
            #       strength for others), or to different issues (each option ties to it's own individual issue)
            # Questions and options could also not have issues tied to them altogether
            # Also note here that the existing questions and options aren't present in this query because the linkages
            #   are already there
            # Not all questions will have issues, or even strength or weakness variations
			INSERT INTO nano_survey_configuration.issue_question_bank_option (issue_id, question_bank_option_id, created_by) VALUES

# Index 8 Now you'll need to create the linkage between the why / how text you added earlier and the template with
            #   which it goes. If you did not create why / how text above, and there's why / how text to reuse from another existing template,
            #   you'll still create that here.
		   INSERT INTO nano_survey_configuration.survey_template_purpose (survey_template_id, survey_purpose_id) VALUES

# Index 9 Here is where you'll create the relationship between the question bank record and the survey template.
            #   Each question, existing and new, will need a record in this query.
            #   The sequence column is simply the order the questions should appear in on the survey
		   INSERT INTO nano_survey_configuration.survey_template_question (survey_template_id, question_bank_id, sequence, created_by, modified_by) VALUES

# The final two queries deal with linking the question and their respective options to talking points.
            #   Talking points are discussion aids that a user should use when discussing potential issues with a student.
	NO TEN?	

# Index 11 The first query creates a relationship between the question and talking point. Questions could have
            #   zero or more talking points associated with them.
            # Talking points also have issue types - a talking point can be a weakness or strength.
            # Next step text is what the user should follow up with the student on after discussing talking points. Only
            #   weakness talking points have next steps. Existing questions will not have records in this query because
            #   they're already linked to their respective talking points
		INSERT INTO nano_survey_configuration.talking_point (question_bank_id, talking_point_type, text, next_steps, created_by, modified_by) VALUES

# Index 12 the options are linked to their respective talking points. The same caveats and rules apply
            #   with these records as the issue's question options
		INSERT INTO nano_survey_configuration.talking_point_question_bank_option (talking_point_id, question_bank_option_id, created_by) VALUES
