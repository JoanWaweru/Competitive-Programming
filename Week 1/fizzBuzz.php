class Solution {

    /**
     * @param Integer $n
     * @return String[]
     */
    function fizzBuzz(int $n) {

    // PHP program to print Fizz Buzz
        $number = [];
        
        for ($i = 1; $i < $n+1; $i++)
        {
            if ($i % 5 == 0 && $i == 3 == 0){
                array_push($number,"FizzBuzz");}
     
            else if (($i % 3) == 0){
                array_push($number,"Fizz");}           
     
            else if (($i % 5) == 0){                
                array_push($number,"Buzz");}            
 
            else{         
                array_push($number,"$i");}          
        }return $number;
    }
}
