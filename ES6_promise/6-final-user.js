// 6-final-user.js
import signUpUser from './4-user-promise.js';
import uploadPhoto from './5-photo-reject.js';

export default function handleProfileSignup(firstName, lastName, fileName) {
    // Appeler les fonctions et gérer les promesses
    const signUpPromise = signUpUser(firstName, lastName);
    const uploadPromise = uploadPhoto(fileName);

    return Promise.allSettled([signUpPromise, uploadPromise])
        .then(results => results.map(result => ({
            status: result.status,
            value: result.status === 'fulfilled' ? result.value : result.reason
        })));
}
