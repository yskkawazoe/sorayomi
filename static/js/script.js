// alert("This Page is Index.html");

$(function() {
    $('.btn').on('click', function() {
        $('.btn').hide();
        $('.loading').show();
    });
});

// $(function() {
// 	setTimeout(function(){
// 		$('.start p').fadeIn(1600);
// 	},500); //0.5秒後にロゴをフェードイン!
// 	setTimeout(function(){
// 		$('.start').fadeOut(500);
// 	},2500); //2.5秒後にロゴ含め真っ白背景をフェードアウト！
// });

// window.onpageshow = function() {
//     $("#prefec,#s").each(function(){
//       $(this).val("");
//     });
//   }

// $(function() {
//     $('.btn').on('click', function() {
//         $('.btn').hide();
//         $('.loading').show();
 
//         // 3秒後に元に戻す
//         setTimeout(function() {
//             $('.btn').show();
//             $('.loading').hide();
//         }, 10000);
//     });
// });