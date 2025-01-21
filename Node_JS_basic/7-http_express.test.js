const request = require('supertest');
const fs = require('fs');
const app = require('./7-http_express');

// Mock the database file content
const mockDatabase = `firstname,lastname,age,field
Johann,Kerbrou,30,CS
Guillaume,Salou,30,SWE
Arielle,Salou,20,CS
Jonathan,Benou,30,CS
Emmanuel,Turlou,40,CS
Guillaume,Plessous,35,CS
Joseph,Crisou,34,SWE
Paul,Schneider,60,SWE
Tommy,Schoul,32,SWE
Katie,Shirou,21,CS`;

beforeAll(() => {
  // Write the mock database to a temporary file
  fs.writeFileSync('test_database.csv', mockDatabase, 'utf-8');
});

afterAll(() => {
  // Clean up the temporary database file
  fs.unlinkSync('test_database.csv');
});

describe('7-http_express', () => {
  it('should return "Hello Holberton School!" for the root route', async () => {
    const response = await request(app).get('/');
    expect(response.statusCode).toBe(200);
    expect(response.text).toBe('Hello Holberton School!');
  });

  it('should return the list of students for the /students route', async () => {
    process.argv[2] = 'test_database.csv'; // Set the database argument
    const response = await request(app).get('/students');
    expect(response.statusCode).toBe(200);
    expect(response.text).toContain('This is the list of our students');
    expect(response.text).toContain('Number of students: 10');
    expect(response.text).toContain('Number of students in CS: 6. List: Johann, Arielle, Jonathan, Emmanuel, Guillaume, Katie');
    expect(response.text).toContain('Number of students in SWE: 4. List: Guillaume, Joseph, Paul, Tommy');
  });

  it('should return an error if the database is missing', async () => {
    process.argv[2] = 'missing_database.csv'; // Set a non-existent database argument
    const response = await request(app).get('/students');
    expect(response.statusCode).toBe(500);
    expect(response.text).toBe('This is the list of our students\nCannot load the database');
  });
});
