const fs = require('fs');
const path = require('path');
const countStudents = require('./2-read_file');

jest.mock('fs');

describe('countStudents', () => {
  it('should log the correct output for a valid CSV file', () => {
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

    fs.readFileSync.mockReturnValue(mockData);

    console.log = jest.fn();

    countStudents('database.csv');

    expect(console.log).toHaveBeenCalledWith('Number of students: 10');
    expect(console.log).toHaveBeenCalledWith(
      'Number of students in CS: 6. List: Johann, Arielle, Jonathan, Emmanuel, Guillaume, Katie'
    );
    expect(console.log).toHaveBeenCalledWith(
      'Number of students in SWE: 4. List: Guillaume, Joseph, Paul, Tommy'
    );
  });

  it('should throw an error when the file does not exist', () => {
    fs.readFileSync.mockImplementation(() => {
      throw new Error('File not found');
    });

    expect(() => countStudents('invalid.csv')).toThrow(
      'Cannot load the database'
    );
  });
});
