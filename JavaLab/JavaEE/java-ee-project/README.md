# Java EE Project

This is a Java EE project that follows a standard structure for web applications. 

## Project Structure

- **src/main/java/com/example/config**: Contains configuration classes for the application, such as database configuration and application settings.
- **src/main/java/com/example/controllers**: Contains controller classes that handle incoming requests and return responses.
- **src/main/java/com/example/models**: Contains model classes that represent the data structure of the application.
- **src/main/java/com/example/repositories**: Contains repository interfaces or classes that handle data access logic.
- **src/main/java/com/example/services**: Contains service classes that contain business logic and interact with the repositories and controllers.
- **src/main/resources/META-INF/persistence.xml**: Configures the persistence unit for JPA.
- **src/main/resources/META-INF/beans.xml**: Configures CDI (Contexts and Dependency Injection) in the application.
- **src/main/webapp/WEB-INF/web.xml**: The deployment descriptor for the web application.
- **src/main/webapp/index.html**: The main HTML page of the web application.
- **src/test/java/com/example**: Contains test classes for unit and integration testing.
- **pom.xml**: The configuration file for Maven.

## Getting Started

1. Clone the repository.
2. Navigate to the project directory.
3. Use Maven to build the project: `mvn clean install`.
4. Deploy the application to a Java EE server.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.