# RobotArm_3axis

## Image Manipulate
### get_channel
* get channel of image  
* return  
    + 3 : 3 channel image (R, G, B)
    + 4 : 4 channel image with Transparency (R, G, B, A)

### channel_3to4
* change 3 channel image to 4 channel image  
  
### channel_4to3
* change 4 channel image to 3 channel image  
  
### combine4
* combines 4 channel image with certain offset  
* parameters
    + bg : background image you want (4 channel)  
    + img : 4 channel image with transparent background  
    + y_offset : y offset  
    + x_offset : x offset  
    + a_offset : img with transparency over a_offset will be merged  
  
### remove_bg  
* automatically remove image background  
* parameters  
    + image : image you want  
    + savepath : save result img on savepath if savepath if savepath is not empty string   
    + setChroma : if True, background will be filled with chroma  
* return  
    + 4 channel img when setChroma == False  
    + 3 channel img when setChroma == True  

### combine_chroma  
* combine chroma image with background  
* Parameters  
    + chromaimg : img you want (with chromakey background)  
    + destimg : background destination image you want  
    + y_offset : y offset  
    + x_offset : x offset  

