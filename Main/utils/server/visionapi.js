module.exports.getTags = function(client, image){
	client
	.labelDetection(image).then(results => {
    	const labels = results[0].labelAnnotations;

    	console.log('Labels:');
    	labels.forEach(label => console.log(label.description));
  	})
  	.catch(err => {
    	console.error('ERROR:', err);
  	});
};