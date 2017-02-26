angular.module('rml', [])
.controller('MainController', ['$http', function($http) {
    var self = this
    self.currentPage = 'index'
    self.searchText = ''
    self.landlords = []
    self.currentLandlord = null;
    self.currentComments = []

    self.search = function() {
        $http.get('/searchlandlords', {
            params: {
                q: self.searchText
            }
        }).then(function(success) {
            self.landlords = success.data.landlords
            console.log(self.landlords)
            self.currentPage = 'searchResults'
        })
    }

    self.showDetails = function(index) {
        var lid = self.landlords[index].id
        $http.get('/landlord/' + lid)
        .then(function(success) {
            console.log(success.data);
            self.currentPage = 'addcomments'
            self.currentLandlord = success.data.landlord
            self.currentComments = success.data.comments
        });
    }

    self.addFeedback = function() {
        var lid = self.currentLandlord.id
        $http.post('/addcomment/' + lid + '/', {
            params: {
                reviewerName: self.txtName,
                reviewerEmail: self.txtEmail,
                reviewText: self.feedback,
                starRating: self.starRating
            }
        }).then(function(success) {
            console.log('added comment')
            console.log(success)
            self.currentComments.push(success.data.review)
        })
    }


}])
.config(function($interpolateProvider) {
    $interpolateProvider.startSymbol('{[{');
    $interpolateProvider.endSymbol('}]}');
  });
