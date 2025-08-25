const fs = require('fs');
const countStudents = require('./3-read_file_async');

jest.mock('fs');

describe('countStudents', () => {
  it('should log the correct output for a valid CSV file', async () => {
    const mockData = `
      firstname,lastname,age,field
      Johann,Kerbrou,30,CS
      Guillaume,Salou,30,SWE
      Arielle,Salou,20,CS
      Jonathan,Benou,30,CS
      Emmanuel,Turlou,40,CS
      Guillaume,Plessous,35,CS
      Joseph,Crisou,34,SWE
      Paul,Schneider,60,SWE
      Tommy,Schoul,32,SWE
      Katie,Shirou,21,CS
    `.trim();

    fs.readFile.mockImplementation((path, encoding, callback) => {
      callback(null, mockData);
    });

    console.log = jest.fn();

    await countStudents('database.csv');

    expect(console.log).toHaveBeenCalledWith('Number of students: 10');
    expect(console.log).toHaveBeenCalledWith(
      'Number of students in CS: 6. List: Johann, Arielle, Jonathan, Emmanuel, Guillaume, Katie'
    );
    expect(console.log).toHaveBeenCalledWith(
      'Number of students in SWE: 4. List: Guillaume, Joseph, Paul, Tommy'
    );
  });

  it('should throw an error when the file does not exist', async () => {
    fs.readFile.mockImplementation((path, encoding, callback) => {
      callback(new Error('File not found'), null);
    });

    await expect(countStudents('invalid.csv')).rejects.toThrow(
      'Cannot load the database'
    );
  });
});
