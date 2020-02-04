process.env.NODE_ENV = 'test';

//Require the dev-dependencies
let chai = require('chai');
let chaiHttp = require('chai-http');
let server = require('../server');
let should = chai.should();

chai.use(chaiHttp);
//Our parent block
describe('API', () => {

  /*
    * Test the /GET route
    */
  describe('/GET home', () => {
    it('it should GET any reply', (done) => {
      chai.request(server)
        .get('/')
        .end((err, res) => {
          res.should.have.status(200);
          done();
        });
    });
  });

  /**
   * Test /movies
   */
  describe('/movies', () => {
    it('It should get the movies', (done) => {
      chai.request(server)
        .get('/movies')
        .end((err, res) => {
          res.should.have.status(200);
          done();
        });
    });
  });

  /**
   * Test /reviewers
   */
  describe('/reviewers', () => {
    it('It should get the reviewers', (done) => {
      chai.request(server)
        .get('/reviewers')
        .end((err, res) => {
          res.should.have.status(200);
          done();
        });
    });
  });

  /**
   * Test /publications
   */
  describe('/publications', () => {
    it('It should get the publications', (done) => {
      chai.request(server)
        .get('/publications')
        .end((err, res) => {
          res.should.have.status(200);
          done();
        });
    });
  });

});