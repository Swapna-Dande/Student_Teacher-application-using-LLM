import streamlit as st
import auth_functions
page_bg_img ="""
<style>
[data-testid="stAppViewContainer"]{
    background-image: url("https://www.google.com/imgres?q=pastel%20aesthetic%20background%20wallpaper%20for%20web%20applications&imgurl=https%3A%2F%2Fmarketplace.canva.com%2FEAFLJuy-Cfc%2F2%2F0%2F1600w%2Fcanva-pink-pastel-abstract-watercolor-seek-magic-everyday-quote-desktop-wallpaper-vb3Iv3AjFas.jpg&imgrefurl=https%3A%2F%2Fwww.canva.com%2Fdesktop-wallpapers%2Ftemplates%2Fpastel%2F&docid=JMT0u3abomAFhM&tbnid=_jZm3sggcRYg3M&vet=12ahUKEwip08mc1a-FAxUlwzgGHSCLB1IQM3oECGIQAA..i&w=1600&h=900&hcb=2&ved=2ahUKEwip08mc1a-FAxUlwzgGHSCLB1IQM3oECGIQAA")
    background-size: cover;  
}
</style>
"""
st.header('Acumen Chat Academy')
st.write('Welcome to Application ')
## -------------------------------------------------------------------------------------------------
## Not logged in -----------------------------------------------------------------------------------
## -------------------------------------------------------------------------------------------------
if 'user_info' not in st.session_state:
    st.session_state.is_authenticated = False
    st.session_state.user_type=""
    col1,col2,col3 = st.columns([1,2,1])
    user_type = col2.selectbox(label='User Type', options=('Teacher', 'Student'))
    # Authentication form layout
    do_you_have_an_account = col2.selectbox(label='Do you have an account?',options=('Yes','No','I forgot my password'))
    auth_form = col2.form(key='Authentication form',clear_on_submit=False)
    email = auth_form.text_input(label='Email')
    password = auth_form.text_input(label='Password',type='password') if do_you_have_an_account in {'Yes','No'} else auth_form.empty()
    auth_notification = col2.empty()

    # Sign In

    if do_you_have_an_account == 'Yes' and auth_form.form_submit_button(label='Sign In',use_container_width=True,type='primary'):
        with auth_notification, st.spinner('Signing in'):
            auth_functions.sign_in(email,password)
            # Initialize the user type in the session state
        
            #if user_type == 'Student':
             #   student_main.StudentMain()
            #else:
            #    st.write('cant open')
        

    # Create Account
    elif do_you_have_an_account == 'No' and auth_form.form_submit_button(label='Create Account',use_container_width=True,type='primary'):
        with auth_notification, st.spinner('Creating account'):
            auth_functions.create_account(email,password, user_type)

    # Password Reset
    elif do_you_have_an_account == 'I forgot my password' and auth_form.form_submit_button(label='Send Password Reset Email',use_container_width=True,type='primary'):
        with auth_notification, st.spinner('Sending password reset link'):
            auth_functions.reset_password(email)

    # Authentication success and warning messages
    if 'auth_success' in st.session_state:
        auth_notification.success(st.session_state.auth_success)
        del st.session_state.auth_success
    elif 'auth_warning' in st.session_state:
        auth_notification.warning(st.session_state.auth_warning)
        del st.session_state.auth_warning

## -------------------------------------------------------------------------------------------------
## Logged in --------------------------------------------------------------------------------------
## -------------------------------------------------------------------------------------------------
else:
    
    
    # Sign out
    st.session_state.is_authenticated = False
    st.header('Sign out:')
    st.button(label='Sign Out',on_click=auth_functions.sign_out,type='primary')

    # Delete Account
    st.header('Delete account:')
    password = st.text_input(label='Confirm your password',type='password')
    st.button(label='Delete Account',on_click=auth_functions.delete_account,args=[password],type='primary')