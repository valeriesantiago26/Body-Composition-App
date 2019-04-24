angular.module('bodyCompApp', [])
  .controller('homeController', ['$scope', '$window', '$location', function($scope, $window, $location) {

    $scope.unit = "0";

    const urlParams = new URLSearchParams(window.location.search);
    $scope.method = urlParams.get('method');

    $scope.bmi = function(){
    	window.location.href = "/information?method=bmi";
    };

    $scope.fold3 = function(){
    	window.location.href = "/information?method=fold3";
    };

    $scope.fold7 = function(){
    	window.location.href = "/information?method=fold7";
    };

    $scope.personalInfoReDirect = function () {
    	switch ($scope.method) {
    		case "bmi":
    			window.location.href = "/bmi"
		}
    };


  }]);