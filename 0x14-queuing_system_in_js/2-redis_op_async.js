import redis from 'redis'
import { promisify } from 'util'

const client = redis.createClient();

client.on("error", function(error) {
  console.error(`Redis client not connected to the server: ${error}`);
});

client.on('connect', function() {
  console.log('Redis client connected to the server');
});

const setNewSchool = (schoolName, value) => {
  client.set(schoolName, value, redis.print)
}

const displaySchoolValue = async (schoolName) => {
    const asyncGet = promisify(client.get).bind(client);
    console.log(await asyncGet(schoolName));
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
