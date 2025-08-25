export default class AppController {
  /**
   * Handles the root route request.
   * @param {Object} req - The HTTP request object.
   * @param {Object} res - The HTTP response object.
   */
  static getHomepage(req, res) {
      res.status(200).send('Hello Holberton School!');
  }
}
