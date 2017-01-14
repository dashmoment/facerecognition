# Face Recognition

Sample code: cd ~/facerec/py/apps/videofacerec

### Use sample code : python simple_videofacerec.py -t data/ test_model.pkl


## Test model by image
This sample code will show the tag of test person. 
If you want to change test person, please change line 110 in simple_videofacerec.py

line 110: frame = cv2.imread('test/s4/9.pgm')


## Test model by Video
Please modify line 252 in simple_videofacerec.py

App(model=model,
        camera_id=options.camera_id,
        cascade_filename=options.cascade_filename).run()   

## App.run() function is used to detect face in video


Original from :https://github.com/bytefish/facerec

Reference document :http://bytefish.de/blog/videofacerec/
