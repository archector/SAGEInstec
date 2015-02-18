function ProgressBar(idContainer, idFill, minValue, maxValue) {
    //case 1 from minus to plus
    //case 2 from minus to minus
    //case 3 from plus to plus 
    //case 1,2 are not treated here 

    this.maxValue = maxValue;
    this.minValue = minValue;
    this.idContainer = idContainer;
    this.width = $("#" + idContainer).width();
    this.fillElement = $("#" + idFill);

    this.GetWidth = function (currentValue) {
        ///
        ///		Calculate the progressBarFill width
        ///
        ///	

        //currentValue is smaller or equal to 0
        if (currentValue <= this.minValue) {
	    
            return this.minValue *(this.width / 100); 

        }

        //currentValue is smaller then maximum
        if (currentValue < this.maxValue) {
            return currentValue * (this.width / 100);
        } //currentValue is bigger then maximum
        else {
            
	    return this.maxValue * (this.width / 100);
	    
        }
	
		
	

    };


}
