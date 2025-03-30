# Import the create_app function from our package
from app import create_app

# Create the Flask application using our factory function
app = create_app()

# Only run the server if this file is executed directly
if __name__ == '__main__':
    # Run the Flask development server with debug mode enabled
    app.run(debug=True)
