function add_db1() {
  const mongoose = require("mongoose");

  const db_server = "mongodb://root:kjk759843@apps.monocycle18.com:5051";
  const db_name = "buyorsell";

  console.log("DB_SERVER===>", db_server);
  console.log("DB_NAME===>", db_name);

  mongoose
    .connect("mongodb://apps.monocycle18.com:5051/admin", {
      useNewUrlParser: true,
      useUnifiedTopology: true,
      auth: {
        user: "root",
        password: "kjk759843",
      },
    })
    .then((data) => {
      console.log("db connection successful!.");

      return checkDatabaseExists(db_name);
    })
    .then((exists) => {
      console.log(`Database exists: ${exists}`);

      if (!exists) {
        return mongoose.connection.db.createCollection(
          db_name,
          (err, result) => {
            if (err) {
              console.error("Error creating new database:", err);
            } else {
              console.log("New database created:", result);

              // add a new user
              mongoose.connection.db.command(
                {
                  createUser: "user1",
                  pwd: "kjk759843",
                  roles: [{ role: "readWrite", db: db_name }],
                },
                (err, result) => {
                  if (err) {
                    console.error("Error creating new user:", err);
                  } else {
                    console.log("New user created:", result);
                  }
                }
              );
            }
          }
        );
      }
    })
    .catch((err) => {
      console.log(err);
      process.exit();
    })
    .finally(() => {
      //mongoose.connection.close();
    });

  // Function to check if a database exists
  function checkDatabaseExists(databaseName) {
    return new Promise((resolve, reject) => {
      mongoose.connection.db
        .listCollections({ name: databaseName })
        .next((err, collinfo) => {
          if (err) {
            reject(err);
          } else {
            resolve(collinfo !== null);
          }
        });
    });
  }

  // Usage example
  // checkDatabaseExists(db_name)
  //   .then((exists) => {
  //     console.log(`Database exists: ${exists}`);
  //   })
  //   .catch((err) => {
  //     console.error('Error checking database:', err);
  //   })
  //   .finally(() => {
  //     mongoose.connection.close();
  //   });
}

function add_db2(){
    const db_server = "mongodb://root:kjk759843@apps.monocycle18.com:5051";
    const db_name = "buyorsell";
  
    console.log("DB_SERVER===>", db_server);
    console.log("DB_NAME===>", db_name);

    const MongoClient = require('mongodb').MongoClient;

    // Connection URL
    const url = db_server
    
    // Database name
    const dbName = 'admin';
    
    // User credentials
    const rootUsername = 'root';
    const rootPassword = 'kjk759843';
    const newDatabase = db_name;
    const newUser = 'user1';
    const userPassword = 'kjk759843';
    
    // Create a new MongoClient
    const client = new MongoClient(url, { useUnifiedTopology: true });
    
    // Connect to the MongoDB server
    console.log('connecting...')
    client.connect(function (err) {
      if (err) {
        console.error('Error connecting to the server:', err);
        return;
      }
    
      console.log('Connected successfully to the server');
    
      // Access the admin database
      const adminDb = client.db(dbName);
    
      // Authenticate with root credentials
      adminDb.authenticate(rootUsername, rootPassword, function (err) {
        if (err) {
          console.error('Error authenticating with root credentials:', err);
          client.close();
          return;
        }
    
        console.log('Authenticated successfully as root');
    
        // Create a new database
        client.db(newDatabase);
    
        // Create a new user with appropriate privileges on the new database
        adminDb.addUser(newUser, userPassword, {
          roles: [{ role: 'readWrite', db: newDatabase }],
        }, function (err, result) {
          if (err) {
            console.error('Error creating a new user:', err);
          } else {
            console.log('User created successfully:', result);
          }
    
          // Close the connection
          client.close();
        });
      });
    });
   
}

try{
    add_db2()
}
catch(err){
    console.log(err)
}
