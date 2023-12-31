var createError = require('http-errors');
var express = require('express');
var path = require('path');
var cookieParser = require('cookie-parser');
var logger = require('morgan');
var cors = require('cors');
var mongoose = require('mongoose');
var dotenv = require('dotenv/config');

var indexRouter = require('./routes/index');
var stocksRouter = require('./routes/stocks');

var app = express();

app.use(cors()); // Enable CORS for all routes

// app.use((req, res, next) => {
//   // console.log('app.js: req.headers', req.headers)
//   // console.log('app.js: req.headers.orgin', req.headers.origin)

//   //fs.writeFileSync('req.json', JSON.stringify(req));

//   //console.log('req.header=', req.header)

//   //
//   // Dynamically setting Access-Control-Allow-Origin. This is basically allowing all incoming request
//   // this can be used to limit the access. 
//   // By not setting * always is to allow the requesters to have the cridential in the request
//   // 
//   if (req.headers.origin) {
//     console.log('setting req.headers.origin for cors')
//     res.append('Access-Control-Allow-Origin', req.headers.origin);
//   }

//   res.append('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,PATCH');
//   res.append('Access-Control-Allow-Credentials', 'true');
//   res.append('Access-Control-Allow-Headers', 'Content-Type,*');
//   next();
// });

//const db_server = process.env.DB_SERVER;
//const db_server = "mongodb://172.200.0.2"

const db_server = "mongodb://user:kjk759843@apps.monocycle18.com:5051"
const db_name = "stock";
const public_dir = "./public"

console.log('DB_SERVER===>', db_server);
console.log('DB_NAME===>', db_name);

mongoose.connect(`${db_server}/${db_name}`, { useNewUrlParser: true, useUnifiedTopology: true })
  .then(data => {
    console.log('db connection successful!.')
  })
  .catch(err => {
    console.log(err);
    process.exit();
  });

// view engine setup
app.set('views', path.join(__dirname, 'views'));
app.set('view engine', 'hbs');

app.use(logger('dev'));
app.use(express.json());
app.use(express.urlencoded({ extended: false }));
app.use(cookieParser());

//app.use(express.static(path.join(__dirname, 'public')));
console.log('public_dir=', public_dir)
app.use(express.static(public_dir));

app.use('/', indexRouter);
app.use('/stocks', stocksRouter);

// catch 404 and forward to error handler
app.use(function (req, res, next) {
  next(createError(404));
});

// error handler
app.use(function (err, req, res, next) {
  // set locals, only providing error in development
  res.locals.message = err.message;
  res.locals.error = req.app.get('env') === 'development' ? err : {};

  // render the error page
  res.status(err.status || 500);
  res.render('error');
});

module.exports = app;
