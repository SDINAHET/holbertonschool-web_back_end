// import uploadPhoto from './utils.js';
// import createUser from './utils.js';

// export default function handleProfileSignup() {
//   return Promise.all([uploadPhoto(), createUser()])
//     .then(([photo, user]) => {
//       console.log(`${photo.body} ${user.firstName} ${user.lastName}`);
//     })
//     .catch(() => console.log('Signup system offline'));
// }

import { uploadPhoto, createUser } from './utils';

export default function handleProfileSignup() {
  return Promise.all([uploadPhoto(), createUser()])
    .then((results) => {
      const [photoResponse, userResponse] = results;
      console.log(`${photoResponse.body} ${userResponse.firstName} ${userResponse.lastName}`);
    })
    .catch(() => {
      console.log('Signup system offline');
    });
}
