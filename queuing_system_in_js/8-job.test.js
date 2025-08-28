// 8-job.js
export default function createPushNotificationsJobs(jobs, queue) {
  if (!Array.isArray(jobs)) {
    throw new Error('Jobs is not an array');
  }

  jobs.forEach((data) => {
    const job = queue.create('push_notification_code_3', data);

    job.save((err) => {
      if (!err) {
        // En test mode, job.id peut être undefined -> on protège
        const id = (job && typeof job.id !== 'undefined') ? job.id : '';
        console.log(`Notification job created: ${id}`);
      }
    });

    job.on('complete', () => {
      console.log(`Notification job ${job.id} completed`);
    });

    job.on('failed', (error) => {
      console.log(`Notification job ${job.id} failed: ${error}`);
    });

    job.on('progress', (progress) => {
      console.log(`Notification job ${job.id} ${progress}% complete`);
    });
  });
}
