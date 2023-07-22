from flask import Flask, request
from flask_restful import Resource, Api, reqparse
import mysql.connector

DB_HOST = 'localhost'
DB_USER = 'root'
DB_PASSWORD = 'June741+'
DB_NAME = 'projectPrism'

app = Flask(__name__)
api = Api(app)

def create_db_connection():
    return mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )

def close_db_connection(connection):
    connection.close()

class PortfolioManagerResource(Resource):
    def get(self, id=None):
        connection = create_db_connection()
        cursor = connection.cursor()

        if id is None:
            query = "SELECT * FROM portfolio_managers"
            cursor.execute(query)
            portfolio_managers = cursor.fetchall()
            return jsonify(portfolio_managers)
        else:
            query = "SELECT * FROM portfolio_managers WHERE Id = %s"
            cursor.execute(query, (id,))
            portfolio_manager = cursor.fetchone()
            if portfolio_manager:
                return jsonify(portfolio_manager)
            else:
                return {"message": "Portfolio Manager not found"}, 404

        close_db_connection(connection)

    def post(self):
        data = request.get_json()
        parser = reqparse.RequestParser()
        parser.add_argument('Name', type=str, required=True)
        parser.add_argument('Status', type=str, required=True)
        parser.add_argument('Role', type=str, required=True)
        parser.add_argument('Bio', type=str, required=True)
        parser.add_argument('Start Date', type=str, required=True)
        args = parser.parse_args()

        connection = create_db_connection()
        cursor = connection.cursor()

        query = "INSERT INTO portfolio_managers (Name, Status, Role, Bio, StartDate) VALUES (%s, %s, %s, %s, %s)"
        values = (args['Name'], args['Status'], args['Role'], args['Bio'], args['Start Date'])
        cursor.execute(query, values)
        connection.commit()

        close_db_connection(connection)

        return {"message": "Portfolio Manager created successfully"}, 201

    def put(self, id):
        data = request.get_json()
        parser = reqparse.RequestParser()
        parser.add_argument('Name', type=str, required=True)
        parser.add_argument('Status', type=str, required=True)
        parser.add_argument('Role', type=str, required=True)
        parser.add_argument('Bio', type=str, required=True)
        parser.add_argument('Start Date', type=str, required=True)
        args = parser.parse_args()

        connection = create_db_connection()
        cursor = connection.cursor()

        query = "UPDATE portfolio_managers SET Name = %s, Status = %s, Role = %s, Bio = %s, StartDate = %s WHERE Id = %s"
        values = (args['Name'], args['Status'], args['Role'], args['Bio'], args['Start Date'], id)
        cursor.execute(query, values)
        connection.commit()

        close_db_connection(connection)

        return {"message": "Portfolio Manager updated successfully"}

    def delete(self, id):
        connection = create_db_connection()
        cursor = connection.cursor()

        query = "DELETE FROM portfolio_managers WHERE Id = %s"
        cursor.execute(query, (id,))
        connection.commit()

        close_db_connection(connection)

        return {"message": "Portfolio Manager deleted successfully"}

class ProjectResource(Resource):
    def get(self, id=None):
        connection = create_db_connection()
        cursor = connection.cursor()

        if id is None:
            query = "SELECT * FROM projects"
            cursor.execute(query)
            projects = cursor.fetchall()
            return jsonify(projects)
        else:
            query = "SELECT * FROM projects WHERE Id = %s"
            cursor.execute(query, (id,))
            project = cursor.fetchone()
            if project:
                return jsonify(project)
            else:
                return {"message": "Project not found"}, 404

        close_db_connection(connection)

    def post(self):
        data = request.get_json()
        parser = reqparse.RequestParser()
        parser.add_argument('ProjectName', type=str, required=True)
        parser.add_argument('Status', type=str, required=True)
        parser.add_argument('StartDate', type=str, required=True)
        parser.add_argument('EndDate', type=str, required=True)
        parser.add_argument('PortfolioManagerId', type=int, required=True)
        args = parser.parse_args()

        connection = create_db_connection()
        cursor = connection.cursor()

        query = "INSERT INTO projects (ProjectName, Status, StartDate, EndDate, PortfolioManagerId) VALUES (%s, %s, %s, %s, %s)"
        values = (args['ProjectName'], args['Status'], args['StartDate'], args['EndDate'], args['PortfolioManagerId'])
        cursor.execute(query, values)
        connection.commit()

        close_db_connection(connection)

        return {"message": "Project created successfully"}, 201

    def put(self, id):
        data = request.get_json()
        parser = reqparse.RequestParser()
        parser.add_argument('ProjectName', type=str, required=True)
        parser.add_argument('Status', type=str, required=True)
        parser.add_argument('StartDate', type=str, required=True)
        parser.add_argument('EndDate', type=str, required=True)
        parser.add_argument('PortfolioManagerId', type=int, required=True)
        args = parser.parse_args()

        connection = create_db_connection()
        cursor = connection.cursor()

        query = "UPDATE projects SET ProjectName = %s, Status = %s, StartDate = %s, EndDate = %s, PortfolioManagerId = %s WHERE Id = %s"
        values = (args['ProjectName'], args['Status'], args['StartDate'], args['EndDate'], args['PortfolioManagerId'], id)
        cursor.execute(query, values)
        connection.commit()

        close_db_connection(connection)

        return {"message": "Project updated successfully"}

    def delete(self, id):
        connection = create_db_connection()
        cursor = connection.cursor()

        query = "DELETE FROM projects WHERE Id = %s"
        cursor.execute(query, (id,))
        connection.commit()

        close_db_connection(connection)

        return {"message": "Project deleted successfully"}

# Define API endpoints
api.add_resource(PortfolioManagerResource, '/api/portfolio-managers', '/api/portfolio-managers/<int:id>')
api.add_resource(ProjectResource, '/api/projects', '/api/projects/<int:id>')

if __name__ == '__main__':
    app.run(debug=True)
