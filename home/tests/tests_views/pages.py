from django.urls import reverse


HOME_PAGE = reverse("home:index")
INVITE_PAGE = reverse("home:invite")
SETTINGS_PAGE = reverse("home:settings", kwargs={"pk": 1})
PROFILE_PAGE = reverse("home:profile")
USER_DETAIL_PAGE = reverse("home:user_detail", kwargs={"pk": 1})