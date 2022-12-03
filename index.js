const { Client, GatewayIntentBits, EmbedBuilder, PermissionsBitField, Permissions } = require('discord.js');
const { readFileSync, promises: fsPromises } = require('fs');
const execSync = require('child_process').execSync;
const output = execSync('python main.py', { encoding: 'utf-8' });

const prefix = '>';
const client = new Client({ intents: [GatewayIntentBits.Guilds, GatewayIntentBits.GuildMessages, GatewayIntentBits.MessageContent] });

// read secret
function syncReadFile(filename) {
    const contents = readFileSync(filename, 'utf-8');
    const arr = contents.split(/\r?\n/);
    console.log("TOKEN:" + arr[0]);
    return arr[0];
}

client.on("messageCreate", (message) => {
    if (message.content.startsWith(prefix)) {
        const args = message.content.slice(prefix.length).trim().split(/ +/);
        const command = args.shift().toLowerCase();
        console.log("Command: " + command);

        if (command === "cloud") {
            message.channel.send(output);
        }

        if (command === "status"){
            message.channel.send("Im still running");
        }
    }
})

client.on("ready", () => {
    console.log("Bot is ready!");

    // execute every 5 seconds
    setInterval(async () => {
        console.log("-- HOURLY EXECUTION --");
        client.channels.fetch('1048616470021672990').then(channel => {
            channel.send(output)
        }, 3600000);
    }, );

    
})

client.login(syncReadFile('secret.txt'));  