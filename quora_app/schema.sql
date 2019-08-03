--DROP TABLE IF EXISTS user;
--DROP TABLE IF EXISTS key;
--image_file BLOB NOT NULL,
CREATE TABLE user (
  user_id INT Primary key NOT NULL AUTO_INCREMENT,
  username VARCHAR(50) NOT NULL UNIQUE,
  email VARCHAR(120) NOT NULL UNIQUE,
  password TEXT NOT NULL
);

CREATE TABLE key (
  key_id INT Primary Key AUTOINCREMENT NOT NULL,
  key_search CHAR(60) NOT NULL,
  user_id INT,
  FOREIGN KEY(user_id) REFERENCES user(user_id)
);


"""def convertToBinaryData(filename):
    #Convert digital data to binary format
    with open(filename, 'rb') as file:
        binaryData = file.read()
    return binaryData"""

"""empPicture = convertToBinaryData(photo)
   file = convertToBinaryData(biodataFile)"""
