const discord = require('discord.js');
// const {
//     Client,
//     Attachment
// } = require('discord.js');

const bot = new discord.Client();
const cheerio = require('cheerio');
const request = require('request');
const fs = require('fs');

const config = require("./config.json");



const token = config.TOKEN
const PREFIX = config.PREFIX
const time = config.TIME


var version = '1.3';



// Bot start up
bot.on('ready', () => {
    console.log('This bot is online version ' + version);
    console.log(`${bot.user.username}`);

});

// Load commands
bot.commands = new discord.Collection();
fs.readdir("./commands/", (err, files) => {
    if (err) console.error(err);
    let jsfiles = files.filter(f => f.split(".").pop() === "js");

    if (jsfiles.length <= 0) return console.log("There are no commands to load...");

    console.log(`Loading ${jsfiles.length} commands...`);
    jsfiles.forEach((f, i) => {
        let props = require(`./commands/${f}`);
        console.log(`${i + 1}: ${f} loaded!`);
        bot.commands.set(props.help.name, props);
    });
});

// Message Event
bot.on('message', async message => {
    let args = message.content.substring(PREFIX.length).split(" ");
    
    let messageArray = message.content.split(" ");
    let command  = messageArray[0].toLowerCase();

    if (!command.startsWith(PREFIX)) return;

    let cmd = bot.commands.get(command.slice(PREFIX.length));
    if (cmd) cmd.run(bot,message, args);



    switch(args[0]) {
        case 'ping':
            message.reply('pong!') // replys @user
            // message.channel.sendMessage('pong') // replies with just the message 
            break;

        case 'clear':
            if(!message.member.roles.cache.some(r => r.name === "root")) return message.channel.send('CuteBot winks at you ^_^')
            .then(msg => msg.delete({timeout:5000}));
            if(!args[1]) return message.reply('Error please define second argument')
            message.channel.bulkDelete(args[1]);
            break;


        case 'bless_me':
            // message.channel.bulkDelete(1);
            message.delete({timeout:5000})
            message.reply('CuteBot blesses you with...')
            .then(msg => msg.delete({timeout:time}));
            image(message);

            break;        
    }
    

});



function image(message){
    let args = message.content.slice(PREFIX.length).split(" ");
    var search  = args.toString();

    var options = {
        url: "http://results.dogpile.com/serp?qc=images&q=" + "cursed image", //insert image subject
        // url: "http://results.dogpile.com/serp?qc=images&q=" + search + ' image', //insert image subject
        method: "GET",
        headers: {
            "Accept": "text/html",
            "User-Agent": "Chrome"
        }
    };


    // request grabs options we created
    // returns error if we get one
    // response is image we GET back from the search
    // responseBody loads request we obtain
    request(options, function(error, response, responseBody) {
        if (error) {
            return;
        }
 
        $ = cheerio.load(responseBody);
 
        //grabs only an image uing cheerio?
        var links = $(".image a.link");
 
        var urls = new Array(links.length).fill(0).map((v, i) => links.eq(i).attr("href"));
       
        console.log(urls);
        
        // if no url was found, exit
        if (!urls.length) {
           
            return;
        }
 
        // Send result
        message.channel.send( urls[Math.floor(Math.random() * urls.length)])
        .then(msg => msg.delete({timeout:time}));
    });


}

bot.login(token);