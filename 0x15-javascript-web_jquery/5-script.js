$(function () {
	$('DIV#add_item').click(function () {
		new_element = "<li>Item</li>";
		$('UL.my_list').append(new_element);
	});
});
