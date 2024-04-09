import streamlit as st
from streamlit_option_menu import option_menu
import chat_doc, student_about, resume_ats,YT_Summarizer,course_roadmap

def StudentMain():
    class MultiApp:
        def __init__(self):
            self.apps = []

        def add_app(self, title, func):

            self.apps.append({
                "title": title,
                "function": func
             })

        def run():
            if 'is_authenticated' in st.session_state and not st.session_state.is_authenticated and not st.session_state.user_type == 'Student':
                st.error("Please login to access this page")
                return
               
            app = option_menu(
                menu_title= None,
                options=['Chat with File','Smart ATS','Course Roadmap Generator','YT Summarizer','About'],
                icons=['chat-fill','file-earmark-person-fill','diagram-3-fill','youtube','info-circle-fill'],
                menu_icon='chat-text-fill',
                default_index=0,
                orientation="horizontal",
                styles={
                    "container": {"padding": "5!important","background-color":'black'},
            "icon": {"color": "white", "font-size": "8px"}, 
            "nav-link": {"color":"white","font-size": "10px", "text-align": "middle", "margin":"0px", "--hover-color": "blue"},
            "nav-link-selected": {"background-color": "#02ab21"},}
                
                )

        
            if app == "Chat with File":
                chat_doc.app()
            if app == "Smart ATS":
                resume_ats.app() 
            if app == "Course Roadmap Generator":
                course_roadmap.app() 
            if app == "YT Summarizer":
                YT_Summarizer.app()      
            if app == "About":
                student_about.app()                    
                        
    MultiApp.run()


StudentMain()