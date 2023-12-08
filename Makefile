usage:
	@echo 'You can use the Makefile by calling make with one of the following commands:'
	@grep '^[^#[:space:]].*:' Makefile | sed 's/://'

generate-post:
	streamlit run ./applications/social_media_post_generator.py

extract-info-parse:
	streamlit run ./applications/extract_info_parser.py

launch-chatbot:
	streamlit run ./applications/chatbot_dataroots_website.py
