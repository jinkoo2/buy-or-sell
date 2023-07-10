const mongoose = require('mongoose');
// const bcrypt = require('bcrypt');

// const saltRounds = 10;

const PtSchema = mongoose.Schema(
    {
      Id: { 
        type: String, 
//        required:true, 
        unique: true, 
      },

      Sex: { 
            type: String, 
            //required:true, 
            //minlength:10,
            //maxlength:500
      },
      
      DateOfBirth: { 
        type: String, 
        //unique: true, 
        //required: true,
        ///minlength:3,
        //maxlength:100
      },

        cs_list: [Object],
        img_list: [Object],
        ps_list: [Object],
        sset_list: [Object],
    },
    {
        timestamps:true
    }
);

// UserSchema.pre('save', function(next) {
//     ////////////////////////////////////////////////////////////////////
//     // Hash passwrod if this is a new user, or the password has changed, 
//     if (this.isNew || this.isModified('password')) {
//       // Saving reference to this because of changing scopes
//       const document = this;
//       console.log('hasing password')
//       bcrypt.hash(document.password, saltRounds,
//         function(err, hashedPassword) {
//         if (err) {
//           console.error("hasing failed! err=>", err)
//           next(err);
//         }
//         else {
//           document.password = hashedPassword;
//           next();
//         }
//       });
//     } else {
//       next();
//     }
//   });

// UserSchema.methods.isCorrectPassword = function(password, callback){
//   bcrypt.compare(password, this.password, function(err, same) {
//     if (err) {
//       callback(err);
//     } else {
//       callback(err, same);
//     }
//   });
// }

// UserSchema.methods.hashPassword = function(password, callback){
//   bcrypt.hash(password, saltRounds,
//     function(err, hashedPassword) {
//     if (err) {
//       callback(err)
//     }
//     else {
//       callback(err,hashedPassword)
//     }
//    });
// }


module.exports = mongoose.model('Pt', PtSchema);