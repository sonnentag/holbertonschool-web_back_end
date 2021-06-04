import redis from 'redis'

const client = redis.createClient();

client.on("error", function(error) {
  console.error(`Redis client not connected to the server: ${error}`);
});

client.on('connect', function() {
  console.log('Redis client connected to the server');
});

const hashKey = 'HolbertonSchools';

const multiSet = ["Portland", "50", "Seattle", "80", "New York", "20", "Bogota", "20", "Cali", "40", "Paris", "2"]

client.hset(hashKey, multiSet, redis.print)
client.hgetall(hashKey, (err, val) => {
  console.log(val)
})
