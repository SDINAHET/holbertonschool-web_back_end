import handleResponseFromAPI from './2-then';

const promise = Promise.resolve();
handleResponseFromAPI(promise);

// import handleResponseFromAPI from './2-then';

// const promise = Promise.resolve(); // Example of a resolved promise
// handleResponseFromAPI(promise);

// const rejectedPromise = Promise.reject(); // Example of a rejected promise
// handleResponseFromAPI(rejectedPromise);
