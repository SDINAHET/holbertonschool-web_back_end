// // 6-final-user.js
// import signUpUser from './4-user-promise.js';
// import uploadPhoto from './5-photo-reject.js';

// export default function handleProfileSignup(firstName, lastName, fileName) {
//     // Appeler les fonctions et gérer les promesses
//     const signUpPromise = signUpUser(firstName, lastName);
//     const uploadPromise = uploadPhoto(fileName);

//     return Promise.allSettled([signUpPromise, uploadPromise])
//         .then(results => results.map(result => ({
//             status: result.status,
//             value: result.status === 'fulfilled' ? result.value : result.reason
//         })));
// }

import signUpUser from './4-user-promise.js';
import uploadPhoto from './5-photo-reject.js';

export default async function handleProfileSignup(firstName, lastName, fileName) {
  try {
    const results = await Promise.allSettled([
      signUpUser(firstName, lastName),
      uploadPhoto(fileName),
    ]);

    return results.map((result) => {
      if (result.status === 'fulfilled') {
        return { status: 'fulfilled', value: result.value };
      } else {
        return { status: 'rejected', value: String(result.reason) };
      }
    });
  } catch (error) {
    throw new Error(`Unexpected error in handleProfileSignup: ${error.message}`);
  }
}


// import signUpUser from './4-user-promise.js';
// import uploadPhoto from './5-photo-reject.js';

// export default async function handleProfileSignup(firstName, lastName, fileName) {
//   const results = await Promise.allSettled([
//     signUpUser(firstName, lastName),
//     uploadPhoto(fileName),
//   ]);

//   return results.map((result) => ({
//     status: result.status,
//     value: result.status === 'fulfilled' ? result.value : String(result.reason),
//   }));
// }

// import signUpUser from './4-user-promise';
// import uploadPhoto from './5-photo-reject';

// export default async function handleProfileSignup(firstName, lastName, fileName) {
//   return Promise
//     .allSettled([signUpUser(firstName, lastName), uploadPhoto(fileName)])
//     .then((res) => (
//       res.map((o) => ({
//         status: o.status,
//         value: o.status === 'fulfilled' ? o.value : String(o.reason),
//       }))
//     ));
// }

// // 6-final-user.js
// import signUpUser from './4-user-promise.js';
// import uploadPhoto from './5-photo-reject.js';

// /**
//  * Handles profile signup by calling functions that return promises.
//  * @param {string} firstName - The user's first name.
//  * @param {string} lastName - The user's last name.
//  * @param {string} fileName - The filename for photo upload.
//  * @returns {Promise<Array>} A promise resolving to an array of results.
//  */
// export default function handleProfileSignup(firstName, lastName, fileName) {
//   const signUpPromise = signUpUser(firstName, lastName);
//   const uploadPromise = uploadPhoto(fileName);

//   return Promise.allSettled([signUpPromise, uploadPromise])
//     .then((results) =>
//       results.map((result) => ({
//         status: result.status,
//         value: result.status === 'fulfilled' ? result.value : result.reason,
//       }))
//     );
// }


// // 6-final-user.js
// import signUpUser from './4-user-promise.js';
// import uploadPhoto from './5-photo-reject.js';

// export default function handleProfileSignup(firstName, lastName, fileName) {
//     // Appeler les fonctions et gérer les promesses
//     const signUpPromise = signUpUser(firstName, lastName);
//     const uploadPromise = uploadPhoto(fileName);

//     return Promise.allSettled([signUpPromise, uploadPromise])
//         .then(results => results.map(result => ({
//             status: result.status,
//             value: result.status === 'fulfilled' ? result.value : result.reason
//         })));
// }

// import signUpUser from './4-user-promise';
// import uploadPhoto from './5-photo-reject';

// export default async function handleProfileSignup(firstName, lastName, fileName) {
//   const promises = [
//     signUpUser(firstName, lastName),
//     uploadPhoto(fileName)
//   ];

//   const results = await Promise.allSettled(promises)
//     .then((results) => results.map(result => ({
//       status: result.status,
//       value: result.status === 'fulfilled' ? result.value : result.reason
//     })));

//   return results;
// }


// import signUpUser from './4-user-promise.js';
// import uploadPhoto from './5-photo-reject.js';

// export default function handleProfileSignup(firstName, lastName, fileName) {
//   const user = signUpUser(firstName, lastName);
//   const photo = uploadPhoto(fileName);

//   return Promise.allSettled([user, photo]).then((results) => {
//     return results.map((result) => ({
//       status: result.status,
//       value: result.value || result.reason,
//     }));
//   });
// }

// import signUpUser from './4-user-promise';
// import uploadPhoto from './5-photo-reject';

// export default function handleProfileSignup(firstName, lastName, fileName) {
//   const signUpPromise = signUpUser(firstName, lastName);
//   const uploadPhotoPromise = uploadPhoto(fileName);

//   return Promise.allSettled([signUpPromise, uploadPhotoPromise]).then((results) =>
//     results.map((result) => {
//       if (result.status === 'fulfilled') {
//         return { status: 'fulfilled', value: result.value };
//       }
//       return { status: 'rejected', value: result.reason };
//     })
//   );
// }
