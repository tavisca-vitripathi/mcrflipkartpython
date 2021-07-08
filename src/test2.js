function trms_api_call(postData,options) {
    dataString= ''
   const response = await new Promise((resolve, reject) => {
    const req = https.request(options, function(res) {
      res.on('data', chunk => {
        dataString += chunk;
      });
      res.on('end', () => {
        resolve({
            statusCode: 200,
            body: JSON.stringify(JSON.parse(dataString))
        });
      });
    });
   
    req.on('error', (e) => {
      reject({
          statusCode: 500,
          body: 'Something went wrong!'
      });
    });
    req.write(postData);
    req.end();
    
  });
  return response;
}