# Setting up LUIS via CLI:

This README contains information on how to create and deploy a LUIS application. When the bot is ready to be deployed to production, we recommend creating a LUIS Endpoint Resource for usage with your LUIS App.

> For instructions on how to create a LUIS Application via the LUIS portal, see these Quickstart steps:
> 1. [Quickstart: Create a new app in the LUIS portal][Quickstart-create]
> 2. [Quickstart: Deploy an app in the LUIS portal][Quickstart-deploy]

  [Quickstart-create]: https://docs.microsoft.com/azure/cognitive-services/luis/get-started-portal-build-app
  [Quickstart-deploy]:https://docs.microsoft.com/azure/cognitive-services/luis/get-started-portal-deploy-app

## Table of Contents:

- [Prerequisites](#Prerequisites)
- [Import a new LUIS Application using a local LUIS application](#Import-a-new-LUIS-Application-using-a-local-LUIS-application)
- [How to create a LUIS Endpoint resource in Azure and pair it with a LUIS Application](#How-to-create-a-LUIS-Endpoint-resource-in-Azure-and-pair-it-with-a-LUIS-Application)

___

## [Prerequisites](#Table-of-Contents):

#### Install Azure CLI >=2.0.61:

Visit the following page to find the correct installer for your OS:
- https://docs.microsoft.com/en-us/cli/azure/install-azure-cli?view=azure-cli-latest

#### Install LUIS CLI >=2.4.0:

Open a CLI of your choice and type the following:

bash
npm i -g luis-apis@^2.4.0


#### LUIS portal account:

You should already have a LUIS account with either https://luis.ai, https://eu.luis.ai, or https://au.luis.ai. To determine where to create a LUIS account, consider where you will deploy your LUIS applications, and then place them in [the corresponding region][LUIS-Authoring-Regions].

After you've created your account, you need your [Authoring Key][LUIS-AKey] and a LUIS application ID.

  [LUIS-Authoring-Regions]: https://docs.microsoft.com/azure/cognitive-services/luis/luis-reference-regions#luis-authoring-regions]
  [LUIS-AKey]: https://docs.microsoft.com/azure/cognitive-services/luis/luis-concept-keys#authoring-key

___

## [Import a new LUIS Application using a local LUIS application](#Table-of-Contents)

### 1. Import the local LUIS application to luis.ai

bash
luis import application --region "LuisAppAuthoringRegion" --authoringKey "LuisAuthoringKey" --appName "FlightBooking" --in "./cognitiveModels/FlightBooking.json"


Outputs the following JSON:

json
{
    "id": "########-####-####-####-############",
    "name": "FlightBooking",
    "description": "A LUIS model that uses intent and entities.",
    "culture": "en-us",
    "usageScenario": "",
    "domain": "",
    "versionsCount": 1,
    "createdDateTime": "2019-03-29T18:32:02Z",
    "endpoints": {},
    "endpointHitsCount": 0,
    "activeVersion": "0.1",
    "ownerEmail": "bot@contoso.com",
    "tokenizerVersion": "1.0.0"
}


For the next step, you'll need the "id"