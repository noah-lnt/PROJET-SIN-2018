var server = require('http').createServer();
var io = require('socket.io')(server);
io.on('connection', function(client){
    console.log('---- NEW CONNECTION ----');

    // ANDROID function
    client.on('client connection', function(data){
        console.log('client connection');
        io.emit('return client connection', { data: 'connection' });
    });

    client.on('client start alarm', function(data){
        console.log('client start alarm');
        io.emit('return client start alarm', { data: 'alarm' });
    });
    client.on('client stop alarm', function(data){
        console.log('client stop alarm');
        io.emit('return client stop alarm', { data: 'alarm' });
    });

    client.on('client lock', function(data){
        console.log('client lock');
        io.emit('return client lock', { data: 'lock' });
    });
    client.on('client unlock', function(data){
        console.log('client unlock');
        io.emit('return client unlock', { data: 'unlock' });
    });

    client.on('client start position', function(data){
        console.log('client start position');
        io.emit('return client start position', { data: 'position' });
    });
    client.on('client stop position', function(data){
        console.log('client stop position');
        io.emit('return client stop position', { data: 'position' });
    });

    // RPI function
    client.on('rpi connection', function(data){
        console.log('rpi connection');
        console.log(data[0])
        console.log(data[1])
        console.log(data[2])
        io.emit('return rpi connection', { valAlarm: data[0], valLock: data[1], valPosition: data[2] });
    });
    client.on('rpi position', function(data){
        console.log('rpi position');
        io.emit('return rpi position', { valLatitude: data[0], valLongitude: data[1] });
    });
    client.on('rpi alarm', function(data){
        console.log('rpi alarm');
        io.emit('return rpi alarm', { valAlarm: data[0] });
    });
});
server.listen(5000);