// 8-job.test.js
import { expect } from 'chai';
import kue from 'kue';
import createPushNotificationsJobs from './8-job.js';

describe('createPushNotificationsJobs', () => {
  const queue = kue.createQueue();

  before(() => {
    // Enter Kue test mode (no job processing)
    queue.testMode.enter();
  });

  afterEach(() => {
    // Clear jobs between tests
    queue.testMode.clear();
  });

  after(() => {
    // Exit test mode
    queue.testMode.exit();
  });

  it('display a error message if jobs is not an array', () => {
    expect(() => createPushNotificationsJobs({}, queue)).to.throw('Jobs is not an array');
    expect(() => createPushNotificationsJobs('nope', queue)).to.throw('Jobs is not an array');
    expect(() => createPushNotificationsJobs(42, queue)).to.throw('Jobs is not an array');
    expect(() => createPushNotificationsJobs(null, queue)).to.throw('Jobs is not an array');
  });

  it('create two new jobs to the queue', () => {
    const list = [
      { phoneNumber: '4153518780', message: 'This is the code 1234 to verify your account' },
      { phoneNumber: '4153518781', message: 'This is the code 4562 to verify your account' },
    ];

    createPushNotificationsJobs(list, queue);

    const jobs = queue.testMode.jobs;
    expect(jobs).to.have.lengthOf(2);

    expect(jobs[0].type).to.equal('push_notification_code_3');
    expect(jobs[0].data).to.deep.equal(list[0]);

    expect(jobs[1].type).to.equal('push_notification_code_3');
    expect(jobs[1].data).to.deep.equal(list[1]);
  });
});
