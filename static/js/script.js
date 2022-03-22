$(document).ready(function( $ ){     
    $(".openPopup").on("click", function(event) {  //팝업오픈 버튼 누르면
    $("#popup").show();   //팝업 오픈
    $("body").append('<div class="back"></div>'); //뒷배경 생성
    });
    
    $("body").on("click", function(event) { 
        if(event.target.className == 'close' || event.target.className == 'back'){
            $("#popup").hide(); //close버튼 이거나 뒷배경 클릭시 팝업 삭제
              $(".back").hide();
        }
      });
 
  });

$(document).ready(function( $ ){     
    $(".openPopupFollow").on("click", function(event) {  //팝업오픈 버튼 누르면
    $("#popupf").show();   //팝업 오픈
    $("body").append('<div class="back"></div>'); //뒷배경 생성
    });
    
    $("body").on("click", function(event) { 
        if(event.target.className == 'close' || event.target.className == 'back'){
            $("#popupf").hide(); //close버튼 이거나 뒷배경 클릭시 팝업 삭제
              $(".back").hide();
        }
      });
 
});  

$(document).ready(function( $ ){     
    $(".openPopupFollower").on("click", function(event) {  //팝업오픈 버튼 누르면
    $("#popupfr").show();   //팝업 오픈
    $("body").append('<div class="back"></div>'); //뒷배경 생성
    });
    
    $("body").on("click", function(event) { 
        if(event.target.className == 'close' || event.target.className == 'back'){
            $("#popupfr").hide(); //close버튼 이거나 뒷배경 클릭시 팝업 삭제
              $(".back").hide();
        }
      });
 
});  

// 경고메세지
function ale1() {
    alert("염장은 신고할 수 없습니다");
    }
    
function ale2() {
    alert("팔로우 취소가 가능할 줄 알았다면 당신은 바보");
    }   