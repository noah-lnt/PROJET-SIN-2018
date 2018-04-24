var server = require('http').createServer();
var io = require('socket.io')(server);
io.on('connection', function(client){
    console.log('ter');
    client.on('event', function(data){});
    client.on('disconnect', function(){});

    client.on('connection client', function(data){
        console.log('connection client');
    });
});
server.listen(5000);