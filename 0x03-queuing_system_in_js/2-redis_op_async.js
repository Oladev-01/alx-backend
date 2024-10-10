import { createClient } from 'redis';
import { promisify } from 'util';

// creating a redis client
const client = createClient();

client.on('connect', () => {
    console.log('Redis client connected to the server');
});

client.on('error', (err) => {
    console.log(`Redis client not connected to the server: ${err.message}`)
});
//client.connect();

const getAsync = promisify(client.get).bind(client);
client.set('Holberton', 'School', (err, res) => {
    if (err) throw err;
    console.log(res);
});

const displaySchoolValue = () => {
    getAsync('Holberton')
        .then((data) => console.log(data))
        .catch((err) => console.log(err));
}

displaySchoolValue();
