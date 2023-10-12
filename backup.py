# <li hidden class="pt-2 pb-1 font_anim"><small>Payment Number</small><span class="position-absolute end-0 rem_btn bi bi-dash-circle text-success"></span></li>
# <li hidden class="pt-1 pb-1 font_anim"><small>Customer Name</small><span class="position-absolute end-0 rem_btn bi bi-dash-circle text-success"></span></li>
# <li hidden class="pt-1 pb-1 font_anim"><small>Date</small><span class="position-absolute end-0 rem_btn bi bi-dash-circle text-success"></span></li>
# <li hidden class="pt-1 pb-1 font_anim"><small>Rerence Number</small><span class="position-absolute end-0 rem_btn bi bi-dash-circle text-success"></span></li>
# <li hidden class="pt-1 pb-1 font_anim"><small>Payment Mode</small><span class="position-absolute end-0 rem_btn bi bi-dash-circle text-success"></span></li>
# <li hidden class="pt-1 pb-1 font_anim"><small>Notes</small><span class="position-absolute end-0 rem_btn bi bi-dash-circle text-success"></span></li>
# <li hidden class="pt-1 pb-1 font_anim"><small>Amount Applied</small><span class="position-absolute end-0 rem_btn bi bi-dash-circle text-success"></span></li>
# <li hidden class="pt-1 pb-1 font_anim"><small>Applied Date</small><span class="position-absolute end-0 rem_btn bi bi-dash-circle text-success"></span></li>
# <li hidden class="pt-1 pb-1 font_anim"><small>Refund Amount (BCY)</small><span class="position-absolute end-0 rem_btn bi bi-dash-circle text-success"></span></li>
# <li hidden class="pt-1 pb-1 font_anim"><small>Refund Amount (FCY)</small><span class="position-absolute end-0 rem_btn bi bi-dash-circle text-success"></span></li>
# <li hidden class="pt-1 pb-1 font_anim"><small>Amount (FCY)</small><span class="position-absolute end-0 rem_btn bi bi-dash-circle text-success"></span></li>
# <li hidden class="pt-1 pb-1 font_anim"><small>Unused Amount (FCY)</small><span class="position-absolute end-0 rem_btn bi bi-dash-circle text-success"></span></li>
# <li hidden class="pt-1 pb-1 font_anim"><small>Amount (BCY)</small><span class="position-absolute end-0 rem_btn bi bi-dash-circle text-success"></span></li>
# <li hidden class="pt-1 pb-1 font_anim"><small>Unused Amount (BCY)</small><span class="position-absolute end-0 rem_btn bi bi-dash-circle text-success"></span></li>
# <li hidden class="pt-1 pb-2 font_anim"><small>Payment Number</small><span class="position-absolute end-0 rem_btn bi bi-dash-circle text-success"></span></li>
# <li hidden class="pt-2 pb-1 font_anim"><small>Company Name</small><span class="position-absolute end-0 add_btn  bi bi-dash-circle text-success"></span></li>
# <li hidden class="pt-1 pb-1 font_anim"><small>First Name</small><span class="position-absolute end-0 add_btn  bi bi-dash-circle text-success"></span></li>
# <li hidden class="pt-1 pb-1 font_anim"><small>Last Name</small><span class="position-absolute end-0 add_btn  bi bi-dash-circle text-success"></span></li>
# <li hidden class="pt-1 pb-1 font_anim"><small>Website</small><span class="position-absolute end-0 add_btn  bi bi-dash-circle text-success"></span></li>
# <li hidden class="pt-1 pb-1 font_anim"><small>Customer Email</small><span class="position-absolute end-0 add_btn  bi bi-dash-circle text-success"></span></li>
# <li hidden class="pt-1 pb-1 font_anim"><small>Mobile Phone</small><span class="position-absolute end-0 add_btn  bi bi-dash-circle text-success"></span></li>
# <li hidden class="pt-1 pb-1 font_anim"><small>Work Phone</small><span class="position-absolute end-0 add_btn  bi bi-dash-circle text-success"></span></li>
# <li hidden class="pt-1 pb-1 font_anim"><small>Department</small><span class="position-absolute end-0 add_btn  bi bi-dash-circle text-success"></span></li>
# <li hidden class="pt-1 pb-1 font_anim"><small>Designation</small><span class="position-absolute end-0 add_btn  bi bi-dash-circle text-success"></span></li>
# <li hidden class="pt-1 pb-2 font_anim"><small>Ownder Name</small><span class="position-absolute end-0 add_btn  bi bi-dash-circle text-success"></span></li>

# <li class="pt-1 pb-2 font_anim"><small>'+span_tag.html()+'</small><span class="position-absolute end-0 add_btn bi bi-dash-circle text-success"></span></li>





# <!DOCTYPE html>
# {% load static %}
# <link rel="stylesheet" href="{% static 'css/my_calendar.css' %}">

# <div class="row" style="display: flex;align-items: center;justify-content: center;min-height: 10vh;background: rgba(222, 0, 222, 0);">

#     <div class="col-sm-12 col-xl-6 border d-flex justify-content-center">
#         <div class="wrapper border border-light" style="width: 450px;border-radius: 10px;background: transparent;">
#             <header style="display: flex;align-items: center;justify-content: space-between;padding: 25px;">
#                 <p class="current-date gg" style="font-size: 1.45rem;font-weight: 500;">September 2023</p>
#                 <div class="icons pb-3">
#                     <span class="bi bi-chevron-left p-2" style="height: 38px;width: 38px;background: rgba(0, 0, 0, 0.24);border-radius: 2px;border-radius: 50%;"></span>
#                     <span class="bi bi-chevron-right p-2" style="height: 38px;width: 38px;background: rgb(0, 0, 0,0.24);border-radius: 2px;border-radius: 50%;"></span>
#                 </div>
#             </header>
#             <div class="calendar" style="display: flex;flex-wrap: wrap;">
#                 <ul style="display: flex;list-style: none;flex-wrap: wrap;padding: 0;margin: 0;" class="weeks">
#                     <li>Sun</li>
#                     <li>Mon</li>
#                     <li>Tue</li>
#                     <li>Wed</li>
#                     <li>Thu</li>
#                     <li>Fri</li>
#                     <li>Sat</li>
#                 </ul>
#                 <ul style="display: flex;list-style: none;flex-wrap: wrap;padding: 0;margin: 0;" class="days">
#                     <li>28</li>
#                     <li>29</li>
#                     <li>30</li>
#                     <li>31</li>
#                     <li>1</li>
#                     <li>2</li>
#                     <li>3</li>
#                     <li>4</li>
#                     <li>5</li>
#                     <li>6</li>
#                     <li>7</li>
#                     <li>8</li>
#                     <li>9</li>
#                     <li>10</li>
#                     <li>11</li>
#                     <li>12</li>
#                     <li>13</li>
#                     <li>14</li>
#                     <li>15</li>
#                     <li>16</li>
#                     <li>17</li>
#                     <li>18</li>
#                     <li>19</li>
#                     <li>20</li>
#                     <li>21</li>
#                     <li>22</li>
#                     <li>23</li>
#                     <li>24</li>
#                     <li>25</li>
#                     <li>26</li>
#                     <li>27</li>
#                     <li>28</li>
#                     <li>29</li>
#                     <li>30</li>
#                     <li>1</li>
#                 </ul>
#             </div>
#         </div>
#     </div>










#     <div class="col-sm-12 col-xl-6 border">
        
#     </div>
# </div>

# <script src="{% static 'js/my_calendar.js' %}"></script>