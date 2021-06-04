export default function createPushNotificationsJobs(jobs, queue) {
  if (!Array.isArray(jobs)) throw 'Jobs is not an array'

  jobs.forEach(job => {
  const queueJob = queue.create('push_notification_code_3', job).save(error => {
    if (!error) console.log(`Notification job created: ${queueJob.id}`);
  });

  queueJob.on('complete', () => console.log(`Notification job ${queueJob.id} completed`));
  queueJob.on('failed', (error) => console.log(`Notification job ${queueJob.id} failed: ${error}`));
  queueJob.on('progress', (progress) => console.log(`Notification job ${queueJob.id} ${progress}% complete`));
  });
}
