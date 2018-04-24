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

        var string = JSON.stringify(data);
        var objectValue = JSON.parse(string);

        console.log(objectValue['valName'] +" - "+ objectValue['valAlarm'] +" - "+ objectValue['valLock'] +" - "+ objectValue['valPosition'])

        io.emit('return rpi connection', { valName: objectValue['valName'], valAlarm: objectValue['valAlarm'], valLock: objectValue['valLock'], valPosition: objectValue['valPosition'] });
    });
    client.on('rpi position', function(data){
        console.log('rpi position');

        var string = JSON.stringify(data);
        var objectValue = JSON.parse(string);

        io.emit('return rpi position', { valLatitude: objectValue['valLatitude'], valLongitude: objectValue['valLongitude'] });
    });
    client.on('rpi alarm', function(data){
        console.log('rpi alarm');
        io.emit('return rpi alarm', { valAlarm: data[0] });
    });
});
server.listen(5000);