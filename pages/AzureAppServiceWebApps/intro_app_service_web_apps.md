# Introduction to Azure App Service

## What is Azure App Service

Azure app service is PaaS provided by Microsoft that provides a platform for deploying several types of applications on infrastructure that is fully managed by Azure.

It provides support for runtimes for several languages and frameworks: .Net, Python, Node.js, Java, etc.. so you can focus on developing your application and easily deploy into the app service.

## App types

1. Web apps - web applications
2. API apps
3. Logic apps - 
4. Function apps - Write serverless functions that execute on events.

#### Why use App service?

- Allows you to focus on development of application rather than adminstrating and orchestrating infrastructure that the application will run on.
    - No need to manage patching, updating, configuring, installing runtimes on a virtual machine. All is managed for you.
- Dynamic vertical and horizontal scaling of compute resources.
- Can deploy multiple types of application under a single app service (though typically separate is used).
- Easily manage deployment slots for production, testing and staging, with 
- Devops integration for CI/CD.
- Integration with Azure and microsoft services.
- Good IDE support for Visual Studio.