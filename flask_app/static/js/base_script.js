// users_crud_video, great_number_game_video, portfolio_video


// Targeting video element  
let users_crud_video = document.getElementById("users_crud_video");


/* Applying mouseover event on video clip  
and then we call play() function to play  
the video when the mouse is over the video */ 

// play video on mouseover
users_crud_video.addEventListener("mouseover", function (e) { 
    users_crud_video.play(); 
}) 

/* Applying mouseout event on video clip  
and then we call pause() function to stop  
the video when the mouse is out the video */ 

// pause video on mouseout
users_crud_video.addEventListener("mouseout", function (e) { 
    users_crud_video.pause(); 
}) 


/* Applying mouseover event on video clip  
and then we call play() function to play  
the video when the mouse is over the video */ 

// play video on mouseover
great_number_game_video.addEventListener("mouseover", function (e) { 
    great_number_game_video.play(); 
}) 

/* Applying mouseout event on video clip  
and then we call pause() function to stop  
the video when the mouse is out the video */ 

// pause video on mouseout
great_number_game_video.addEventListener("mouseout", function (e) { 
    great_number_game_video.pause(); 
}) 

/* Applying mouseover event on video clip  
and then we call play() function to play  
the video when the mouse is over the video */ 

// play video on mouseover
portfolio_video.addEventListener("mouseover", function (e) { 
    portfolio_video.play(); 
}) 

/* Applying mouseout event on video clip  
and then we call pause() function to stop  
the video when the mouse is out the video */ 

// pause video on mouseout
portfolio_video.addEventListener("mouseout", function (e) { 
    portfolio_video.pause(); 
}) 
