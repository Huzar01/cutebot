const discord = require("discord.js")

module.exports.run = async ( bot, message, args) => {

    return message.channel.send('Hello Young Thug'); 
};


module.exports.help = {
    name: "test"
};