# CHANGELOG 
### HOME PAGE :
              v 1.0.0 : + added home page
              
### SIGNUP PAGE :
	      v 1.0.0 : +added signup page
		      : changed "ROLL NO" to "EXAM ROLL NO"	
		      : +added form validation through javascript
		      : +added link to login page
### LOGIN PAGE :
	      v 1.0.0 : +added login page
	      	      : changed "USERNAME/ROLL NO" to "EXAM ROLL NO"
		      : +added link to signup page
### USERS.VIEWS.PY :
	      v 1.0.0 : +added profile view to show the details of 
		      :	logged in user
		      : +added home view to render the home page of 
			blog
		      :	+added default view to catch all the 'tampered'
			urls
		      :	+added signup view to enable user signups
		      :	+added error view to deal with errors in various views
		      :	+added dashboard view for best UI experience
		      :	+added success view to deal with success in some views
		      :	+added login view to make some use of signup view
		      :	+added logout view to free users from their pain
		      :	+added create_posts view to prevent boredom of users from 
			clicking the 4 links on the dashboard.
		      :	+added functionality that redirects users to dashboard if
            user attempts to view login or signup page after logging in
          v 1.0.1 : users now redirect to dashboard instead of home page if they are 
			logged in.
### USER.forms.py :
		  v 1.0.0 : +added signup form to enable user signup 
            	    +added login form to enable user login
                    +added postform to enable creating and viewing posts
### USER.models.py :
		  v 1.0.0 : +added posts model to store posts and manage them