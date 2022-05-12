#!/usr/bin/env node
import * as cdk from '@aws-cdk/core';
import { DiscordInteractionsStack } from './interactions-stack';
import { ValheimWorldStack } from './valheim-world-stack';

const app = new cdk.App();

const env: cdk.Environment = {
    account: '464584493694',
    region: 'ap-southeast-1',
}

const azureValheimServerStack = new ValheimWorldStack(app, 'AzurePlaysWorld', {
    env,
    passwordSecretId: 'valheimServerPass',
    environment: {
        SERVER_NAME: "AzurePlays's Server",
        WORLD_NAME: "AzureValhalla",
    },
})

const newWorldServerStack = new ValheimWorldStack(app, 'NewWorld', {
    env,
    passwordSecretId: 'valheimServerPass',
    environment: {
        SERVER_NAME: "AzurePlays's Server - To The North",
        WORLD_NAME: "AzureToTheNorth",
    },
})

new DiscordInteractionsStack(app, 'DiscordInteractionsStack', {
    env,
    clientIdSecretId: 'discordValheimBotClientPublicKey',
    servers: {
        'valhalla': azureValheimServerStack.world,
        'newWorld': newWorldServerStack.world
    },
});
