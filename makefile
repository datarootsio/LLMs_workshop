usage:
	echo 'You can use the Makefile by calling make with one of the following commands:'
	@grep '^[^#[:space:]].*:' Makefile | sed 's/://'

generate-post:
	streamlit run ./applications/1_dataroots_recruitment.py

extract-info-parse:
	streamlit run ./applications/2_dataroots_recruitment_parser.py

launch-chatbot:
	streamlit run ./applications/3_chatbot_dataroots_website.py
