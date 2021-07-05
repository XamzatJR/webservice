const coverTemplate = `<div class="card-custom-img"
style="background-image: url(<%-cover%>)"
></div>`;
const coverHexTemplate = `<div class="card-custom-img"
style="background-color: <%-hexcolor%>"
></div>`;
const logoTemplate = `<img class="img-fluid" src="<%-photo%>"/>`;
const logoDefaultTemplate = `<img class="img-fluid"
src="http://res.cloudinary.com/d3/image/upload/c_pad,g_center,h_200,q_auto:eco,w_200/bootstrap-logo_u3c8dx.jpg"
/>`;
const template = `
<div class="col-md-6 col-lg-4 pb-3">
<div
  class="card card-custom bg-white border-white border-0"
  style="height: 450px"
>
  <%=cover%>
  <div class="card-custom-avatar">
    <%=photo%>
  </div>
  <div class="card-body" style="overflow-y: auto">
    <h4 class="card-title"><%-name%></h4>
    <small>от <a href="#"><%-user%></h4></a></small>
    <p class="card-text"><%-note%></p>
  </div>
  <div
    class="card-footer"
    style="background: inherit; border-color: inherit"
  >
    <div class="d-flex justify-content-between mb-2">
      <div class="p-2 flex-grow-1"><span class="fa fa-star checked"></span> <%-rating%></div>
      <div class="p-2"><a href="/projects/<%-pk%>" class="btn btn-outline-dark">Подробнее</a></div>
      <div class="p-2"><a href="<%-site%>" target="_blank" class="btn btn-outline-dark ">Сайт проекта</a></div>
    </div>
  </div>
</div>
</div>`;

const url = "/api/projects";
function getQuery(date = null) {
  const name = $("#name").val();
  const user = $("#user").val();
  const responsible = $("#responsible").val();
  axios
    .get(url, {
      params: {
        search: name,
        user: user,
        responsible: responsible,
        date: date,
      },
    })
    .then(function (response) {
      $(".row.pt-5").html("");
      response.data.forEach((el) => {
        if (el.cover) {
          el.cover = _.template(coverTemplate)({ cover: el.cover });
        } else {
          el.cover = _.template(coverHexTemplate)({ hexcolor: el.hex_color });
        }
        if (el.photo) {
          el.photo = _.template(logoTemplate)({
            photo: el.photo,
          });
        } else {
          el.photo = logoDefaultTemplate;
        }
        const html = _.template(template)({
          cover: el.cover,
          photo: el.photo,
          pk: el.pk,
          site: el.site,
          name: el.name,
          user: el.user,
          note: el.note,
          rating: el.rating,
        });
        $(".row.pt-5").html($(".row.pt-5").html() + html);
      });
    })
    .catch(function (error) {
      console.log(error);
    });
}

$("#name").keyup(function () {
  getQuery();
});

$("#user").change(function () {
  getQuery();
});

$("#responsible").change(function () {
  getQuery();
});

$(function () {
  $.datepicker.regional["ru"] = {
    closeText: "Закрыть",
    prevText: "Предыдущий",
    nextText: "Следующий",
    currentText: "Сегодня",
    monthNames: [
      "Январь",
      "Февраль",
      "Март",
      "Апрель",
      "Май",
      "Июнь",
      "Июль",
      "Август",
      "Сентябрь",
      "Октябрь",
      "Ноябрь",
      "Декабрь",
    ],
    monthNamesShort: [
      "Янв",
      "Фев",
      "Мар",
      "Апр",
      "Май",
      "Июн",
      "Июл",
      "Авг",
      "Сен",
      "Окт",
      "Ноя",
      "Дек",
    ],
    dayNames: [
      "воскресенье",
      "понедельник",
      "вторник",
      "среда",
      "четверг",
      "пятница",
      "суббота",
    ],
    dayNamesShort: ["вск", "пнд", "втр", "срд", "чтв", "птн", "сбт"],
    dayNamesMin: ["Вс", "Пн", "Вт", "Ср", "Чт", "Пт", "Сб"],
    weekHeader: "Не",
    dateFormat: "dd.mm.yy",
    firstDay: 1,
    isRTL: false,
    showMonthAfterYear: false,
    yearSuffix: "",
  };
  $.datepicker.setDefaults($.datepicker.regional["ru"]);

  $("#date_range").datepicker({
    numberOfMonths: 1,

    onSelect: function (dateText, inst, extensionRange) {
      getQuery(dateText);
    },
  });
});
