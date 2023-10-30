from kivy.app import App
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image
from kivy.uix.dropdown import DropDown
from kivy.graphics import Color, Rectangle

from kivy_garden.mapview import MapView, MapMarker

Window.clearcolor = (1, 1, 1, 1)
Window.size = (360, 780)


class WelcomeBar(GridLayout):
    def __init__(self, screen_manager, **kwargs):
        super().__init__(**kwargs)
        self.cols = 1
        self.padding = [10, 5, 10, 5]

        self.screen_manager = screen_manager

        # need to make into image
        self.logo = Image(source="logo.png", size=(20, 20))
        self.add_widget(self.logo)

        self.welcome_text = Label(text="Welcome to McDonald's!", font_name='Roboto', color=(0, 0, 0, 1))
        self.add_widget(self.welcome_text)


class NavigationBar(BoxLayout):
    def __init__(self, screen_manager, **kwargs):
        super().__init__(**kwargs)
        self.screen_manager = screen_manager

        # Create navigation
        # Create a layout for page navigation buttons
        self.navigation_layout = GridLayout(cols=4, row_force_default=True, row_default_height=60)
        self.order_button = Button(text="Order", font_name='Roboto', color=(0, 0, 0, 1),
                                   background_normal='', background_color=(.95, .95, .95, 1))
        self.navigation_layout.add_widget(self.order_button)
        self.order_button.bind(on_release=self.change_screen_to_order_page)

        self.rewards_button = Button(text="Rewards", font_name='Roboto', color=(0, 0, 0, 1),
                                     background_normal='', background_color=(.95, .95, .95, 1))
        self.navigation_layout.add_widget(self.rewards_button)
        self.rewards_button.bind(on_release=self.change_screen_to_rewards_page)

        self.cart_button = Button(text="Cart", font_name='Roboto', color=(0, 0, 0, 1),
                                  background_normal='', background_color=(.95, .95, .95, 1))
        self.navigation_layout.add_widget(self.cart_button)
        self.cart_button.bind(on_release=self.change_screen_to_cart_page)

        self.settings_button = Button(text="Settings", font_name='Roboto', color=(0, 0, 0, 1),
                                      background_normal='', background_color=(.95, .95, .95, 1))
        self.navigation_layout.add_widget(self.settings_button)
        self.settings_button.bind(on_release=self.change_screen_to_settings_page)

        self.add_widget(self.navigation_layout)

    def change_screen_to_order_page(self, *args):
        cart_screen = self.screen_manager.get_screen("Cart")
        cart_screen.remove_all_cart_items()

        self.screen_manager.current = "Order"

    def change_screen_to_rewards_page(self, *args):
        cart_screen = self.screen_manager.get_screen("Cart")
        cart_screen.remove_all_cart_items()

        self.screen_manager.current = "Rewards"

    def change_screen_to_cart_page(self, *args):
        if self.screen_manager.current != "Cart":
            cart_screen = self.screen_manager.get_screen("Cart")
            cart_screen.add_widgets()

            self.screen_manager.current = "Cart"

    def change_screen_to_settings_page(self, *args):
        cart_screen = self.screen_manager.get_screen("Cart")
        cart_screen.remove_all_cart_items()

        self.screen_manager.current = "Settings"


class Order(Screen):
    def __init__(self, screen_manager, **kwargs):
        super().__init__(**kwargs)
        self.screen_manager = screen_manager
        # Create a ScrollView
        scroll_view = ScrollView()

        # Create a GridLayout to hold the buttons
        self.layout = GridLayout(cols=1, row_force_default=True, row_default_height=60, padding=[10, 0, 10, 20],
                                 spacing=5, size_hint_y=None)
        self.layout.bind(minimum_height=self.layout.setter('height'))

        # Burgers
        self.burger_label = Label(text='Burgers', font_name='Roboto', font_size=24, bold=True, color=(0, 0, 0, 1))
        self.layout.add_widget(self.burger_label)

        self.big_mac_grid = GridLayout(rows=1)
        self.big_mac_icon = Image(source='big_mac_icon.png', size_hint=(None, None), size=(50, 50))
        self.big_mac_grid.add_widget(self.big_mac_icon)
        self.big_mac_button = Button(text='Big Mac', font_name='Roboto', halign='left', valign="middle",
                                     padding=(10, 0), background_normal='', background_color=(0.95, 0.95, 0.95, 1),
                                     color=(0, 0, 0, 1))
        self.big_mac_button.bind(size=self.big_mac_button.setter('text_size'),
                                 on_release=lambda btn: self.change_to_specific_itemorder("big_mac"))
        self.big_mac_grid.add_widget(self.big_mac_button)
        self.layout.add_widget(self.big_mac_grid)

        self.filet_o_fish_grid = GridLayout(rows=1)
        filet_o_fish_icon = Image(source='filet_o_fish_icon.png', size_hint=(None, None), size=(50, 50))
        self.filet_o_fish_grid.add_widget(filet_o_fish_icon)
        self.filet_o_fish_button = Button(text='Filet-o-Fish', font_name='Roboto', halign='left', valign="middle",
                                          padding=(10, 0), background_normal='', background_color=(0.95, 0.95, 0.95, 1),
                                          color=(0, 0, 0, 1))
        self.filet_o_fish_button.bind(size=self.filet_o_fish_button.setter('text_size'),
                                      on_release=lambda btn: self.change_to_specific_itemorder("filet_o_fish"))
        self.filet_o_fish_grid.add_widget(self.filet_o_fish_button)
        self.layout.add_widget(self.filet_o_fish_grid)

        self.mcchicken_grid = GridLayout(rows=1)
        mcchicken_icon = Image(source='mcchicken_icon.png', size_hint=(None, None), size=(50, 50))
        self.mcchicken_grid.add_widget(mcchicken_icon)
        self.mcchicken_button = Button(text='McChicken', font_name='Roboto', halign='left', valign="middle",
                                       padding=(10, 0), background_normal='', background_color=(0.95, 0.95, 0.95, 1),
                                       color=(0, 0, 0, 1))
        self.mcchicken_button.bind(size=self.mcchicken_button.setter('text_size'),
                                   on_release=lambda btn: self.change_to_specific_itemorder("mcchicken"))
        self.mcchicken_grid.add_widget(self.mcchicken_button)
        self.layout.add_widget(self.mcchicken_grid)

        self.mcdouble_grid = GridLayout(rows=1)
        mcdouble_icon = Image(source='mcdouble_icon.png', size_hint=(None, None), size=(50, 50))
        self.mcdouble_grid.add_widget(mcdouble_icon)
        self.mcdouble_button = Button(text='McDouble', font_name='Roboto', halign='left', valign="middle",
                                      padding=(10, 0), background_normal='', background_color=(0.95, 0.95, 0.95, 1),
                                      color=(0, 0, 0, 1))
        self.mcdouble_button.bind(size=self.mcdouble_button.setter('text_size'),
                                  on_release=lambda btn: self.change_to_specific_itemorder("mcdouble"))
        self.mcdouble_grid.add_widget(self.mcdouble_button)
        self.layout.add_widget(self.mcdouble_grid)

        # Shareables
        self.shareables_label = Label(text='Shareables',
                                      font_name='Roboto', font_size=24, bold=True, color=(0, 0, 0, 1))
        self.layout.add_widget(self.shareables_label)

        self.mcnuggets_10_grid = GridLayout(rows=1)
        mcnuggets_10_icon = Image(source='mcnuggets_10_icon.png', size_hint=(None, None), size=(50, 50))
        self.mcnuggets_10_grid.add_widget(mcnuggets_10_icon)
        self.mcnuggets_10_button = Button(text='McNuggets 10 Piece', font_name='Roboto', halign='left', valign="middle",
                                          padding=(10, 0), background_normal='', background_color=(0.95, 0.95, 0.95, 1),
                                          color=(0, 0, 0, 1))
        self.mcnuggets_10_button.bind(size=self.mcnuggets_10_button.setter('text_size'),
                                      on_release=lambda btn: self.change_to_specific_itemorder("mcnuggets_10"))
        self.mcnuggets_10_grid.add_widget(self.mcnuggets_10_button)
        self.layout.add_widget(self.mcnuggets_10_grid)

        self.mcnuggets_6_grid = GridLayout(rows=1)
        mcnuggets_6_icon = Image(source='mcnuggets_6_icon.png', size_hint=(None, None), size=(50, 50))
        self.mcnuggets_6_grid.add_widget(mcnuggets_6_icon)
        self.mcnuggets_6_button = Button(text='McNuggets 6 Piece', font_name='Roboto', halign='left', valign="middle",
                                         padding=(10, 0), background_normal='', background_color=(0.95, 0.95, 0.95, 1),
                                         color=(0, 0, 0, 1))
        self.mcnuggets_6_button.bind(size=self.mcnuggets_6_button.setter('text_size'),
                                     on_release=lambda btn: self.change_to_specific_itemorder("mcnuggets_6"))
        self.mcnuggets_6_grid.add_widget(self.mcnuggets_6_button)
        self.layout.add_widget(self.mcnuggets_6_grid)

        self.large_fries_grid = GridLayout(rows=1)
        large_fries_icon = Image(source='large_fries_icon.png', size_hint=(None, None), size=(50, 50))
        self.large_fries_grid.add_widget(large_fries_icon)
        self.large_fries_button = Button(text='Large Fries', font_name='Roboto', halign='left', valign="middle",
                                         padding=(10, 0), background_normal='', background_color=(0.95, 0.95, 0.95, 1),
                                         color=(0, 0, 0, 1))
        self.large_fries_button.bind(size=self.large_fries_button.setter('text_size'),
                                     on_release=lambda btn: self.change_to_specific_itemorder("large_fries"))
        self.large_fries_grid.add_widget(self.large_fries_button)
        self.layout.add_widget(self.large_fries_grid)

        self.medium_fries_grid = GridLayout(rows=1)
        medium_fries_icon = Image(source='medium_fries_icon.png', size_hint=(None, None), size=(50, 50))
        self.medium_fries_grid.add_widget(medium_fries_icon)
        self.medium_fries_button = Button(text='Medium Fries', font_name='Roboto', halign='left', valign="middle",
                                          padding=(10, 0), background_normal='', background_color=(0.95, 0.95, 0.95, 1),
                                          color=(0, 0, 0, 1))
        self.medium_fries_button.bind(size=self.medium_fries_button.setter('text_size'),
                                      on_release=lambda btn: self.change_to_specific_itemorder("medium_fries"))
        self.medium_fries_grid.add_widget(self.medium_fries_button)
        self.layout.add_widget(self.medium_fries_grid)

        self.small_fries_grid = GridLayout(rows=1)
        small_fries_icon = Image(source='small_fries_icon.png', size_hint=(None, None), size=(50, 50))
        self.small_fries_grid.add_widget(small_fries_icon)
        self.small_fries_button = Button(text='Small Fries', font_name='Roboto', halign='left', valign="middle",
                                         padding=(10, 0), background_normal='', background_color=(0.95, 0.95, 0.95, 1),
                                         color=(0, 0, 0, 1))
        self.small_fries_button.bind(size=self.small_fries_button.setter('text_size'),
                                     on_release=lambda btn: self.change_to_specific_itemorder("small_fries"))
        self.small_fries_grid.add_widget(self.small_fries_button)
        self.layout.add_widget(self.small_fries_grid)

        # Drinks
        self.shareables_label = Label(text='Drinks', font_name='Roboto', font_size=24, bold=True, color=(0, 0, 0, 1))
        self.layout.add_widget(self.shareables_label)

        self.fountain_drink_grid = GridLayout(rows=1)
        fountain_drink_icon = Image(source='fountain_drink_icon.png', size_hint=(None, None), size=(50, 50))
        self.fountain_drink_grid.add_widget(fountain_drink_icon)
        self.fountain_drink_button = Button(text='Any Size Fountain Drink', font_name='Roboto', halign='left',
                                            valign="middle", padding=(10, 0), background_normal='',
                                            background_color=(0.95, 0.95, 0.95, 1), color=(0, 0, 0, 1))
        self.fountain_drink_button.bind(size=self.fountain_drink_button.setter('text_size'),
                                        on_release=lambda btn: self.change_to_specific_itemorder("fountain_drink"))
        self.fountain_drink_grid.add_widget(self.fountain_drink_button)
        self.layout.add_widget(self.fountain_drink_grid)

        self.iced_mocha_grid = GridLayout(rows=1)
        iced_mocha_icon = Image(source='iced_mocha_icon.png', size_hint=(None, None), size=(50, 50))
        self.iced_mocha_grid.add_widget(iced_mocha_icon)
        self.iced_mocha_button = Button(text='Iced Mocha', font_name='Roboto', halign='left', valign="middle",
                                        padding=(10, 0), background_normal='', background_color=(0.95, 0.95, 0.95, 1),
                                        color=(0, 0, 0, 1))
        self.iced_mocha_button.bind(size=self.iced_mocha_button.setter('text_size'),
                                    on_release=lambda btn: self.change_to_specific_itemorder("iced_mocha"))
        self.iced_mocha_grid.add_widget(self.iced_mocha_button)
        self.layout.add_widget(self.iced_mocha_grid)

        # Add the GridLayout to the ScrollView
        scroll_view.add_widget(self.layout)

        # Add the ScrollView to the Order screen
        self.add_widget(scroll_view)

    def change_to_specific_itemorder(self, item):
        item_order_screen = self.screen_manager.get_screen("ItemOrder")
        item_order_screen.change_label(item)
        self.change_screen_to_itemorder_page()

    def change_screen_to_itemorder_page(self, *args):
        cart_screen = self.screen_manager.get_screen("Cart")
        cart_screen.remove_all_cart_items()

        self.screen_manager.current = "ItemOrder"


class Rewards(Screen):
    def __init__(self, screen_manager, **kwargs):
        super().__init__(**kwargs)
        self.screen_manager = screen_manager
        # Create a ScrollView
        scroll_view = ScrollView()

        # Create a GridLayout to hold the buttons
        self.layout = GridLayout(cols=1, row_default_height=60, padding=[10, 0, 10, 20],
                                 spacing=5, size_hint_y=None)
        self.layout.bind(minimum_height=self.layout.setter('height'))

        # Rewards
        rewards_label = Label(text='Rewards', font_name='Roboto', font_size=24, bold=True, color=(0, 0, 0, 1))
        self.layout.add_widget(rewards_label)

        # Rewards Buttons
        bogo_big_mac_grid = GridLayout(rows=1)
        bogo_big_mac_icon = Image(source='bogo_big_mac_icon.png', size_hint=(None, None), size=(50, 50))
        bogo_big_mac_grid.add_widget(bogo_big_mac_icon)
        bogo_big_mac_button = Button(text='Buy One Big Mac, Get One Free!', font_name='Roboto', halign='left',
                                     valign="middle", padding=(10, 0), background_normal='',
                                     background_color=(0.95, 0.95, 0.95, 1), color=(0, 0, 0, 1))
        bogo_big_mac_button.bind(size=bogo_big_mac_button.setter('text_size'),
                                 on_release=lambda btn: self.change_to_rewards_confirmation("bogo_big_mac"))
        bogo_big_mac_grid.add_widget(bogo_big_mac_button)
        self.layout.add_widget(bogo_big_mac_grid)

        bagf_large_fries_grid = GridLayout(rows=1)
        bagf_large_fries_icon = Image(source='large_fries_icon.png', size_hint=(None, None), size=(50, 50))
        bagf_large_fries_grid.add_widget(bagf_large_fries_icon)
        bagf_large_fries_button = Button(text='Spend Atleast $1, Get a Free Large Fries!', font_name='Roboto',
                                         halign='left', valign="middle", padding=(10, 0), background_normal='',
                                         background_color=(0.95, 0.95, 0.95, 1), color=(0, 0, 0, 1))
        bagf_large_fries_button.bind(size=bagf_large_fries_button.setter('text_size'),
                                     on_release=lambda btn: self.change_to_rewards_confirmation("bagf_large_fries"))
        bagf_large_fries_grid.add_widget(bagf_large_fries_button)
        self.layout.add_widget(bagf_large_fries_grid)

        twenty_percent_off_grid = GridLayout(rows=1)
        twenty_percent_off_icon = Image(source='meal_icon.png', size_hint=(None, None), size=(50, 50))
        twenty_percent_off_grid.add_widget(twenty_percent_off_icon)
        twenty_percent_off_button = Button(text='Spend Atleast $15, Get 20% Off!', font_name='Roboto',
                                           halign='left', valign="middle", padding=(10, 0), background_normal='',
                                           background_color=(0.95, 0.95, 0.95, 1), color=(0, 0, 0, 1))
        twenty_percent_off_button.bind(size=twenty_percent_off_button.setter('text_size'),
                                       on_release=lambda btn: self.change_to_rewards_confirmation("twenty_percent_off"))
        twenty_percent_off_grid.add_widget(twenty_percent_off_button)
        self.layout.add_widget(twenty_percent_off_grid)

        thirty_percent_off_grid = GridLayout(rows=1)
        thirty_percent_off_icon = Image(source='meal_icon.png', size_hint=(None, None), size=(50, 50))
        thirty_percent_off_grid.add_widget(thirty_percent_off_icon)
        thirty_percent_off_button = Button(text='Spend Atleast $30, Get 30% Off!', font_name='Roboto',
                                           halign='left', valign="middle", padding=(10, 0), background_normal='',
                                           background_color=(0.95, 0.95, 0.95, 1), color=(0, 0, 0, 1))
        thirty_percent_off_button.bind(size=thirty_percent_off_button.setter('text_size'),
                                       on_release=lambda btn: self.change_to_rewards_confirmation("thirty_percent_off"))
        thirty_percent_off_grid.add_widget(thirty_percent_off_button)
        self.layout.add_widget(thirty_percent_off_grid)

        # Add the GridLayout to the ScrollView
        scroll_view.add_widget(self.layout)

        # Add the ScrollView to the Order screen
        self.add_widget(scroll_view)

    def change_to_rewards_confirmation(self, rewards):
        rewards_confirmation_screen = self.screen_manager.get_screen("RewardsConfirmation")
        rewards_confirmation_screen.change_label(rewards)

        self.change_screen_to_rewardsconfirmation_page()

    def change_screen_to_rewardsconfirmation_page(self, *args):
        cart_screen = self.screen_manager.get_screen("Cart")
        cart_screen.remove_all_cart_items()

        self.screen_manager.current = "RewardsConfirmation"


class RewardsConfirmation(Screen):
    def __init__(self, screen_manager, **kwargs):
        super().__init__(**kwargs)
        self.screen_manager = screen_manager
        self.rewards = ""

        scroll_view = ScrollView()

        self.layout = GridLayout(cols=1, row_force_default=True, row_default_height=60, padding=[10, 60, 10, 0],
                                 spacing=10, size_hint_y=None)
        self.layout.minimum_height = 200

        # add content widgets
        # image
        self.image = Image(source='big_mac_icon.png', size_hint_y=None, size=(100, 100))

        # Rewards text
        self.rewards_label = Label(text='Rewards', font_name='Roboto', font_size=24, color=(0, 0, 0, 1),
                                   size_hint_y=None)
        self.rewards_type_label = Label(text="", halign="center", font_name='Roboto', font_size=24, color=(0, 0, 0, 1),
                                        size_hint_y=None)

        # apply_rewards button
        apply_rewards_layout = GridLayout(cols=1, row_force_default=True, row_default_height=60, spacing=10,
                                          size_hint_y=None)
        apply_rewards_button = Button(text="Apply Rewards", font_name="Roboto", font_size=24, color=(0, 0, 0, 1),
                                      size_hint_y=None, background_normal='', background_color=(.95, .95, .95, 1))
        apply_rewards_button.bind(on_release=lambda btn: self.apply_rewards())
        apply_rewards_layout.add_widget(apply_rewards_button)

        # spacer
        spacer1 = Label(text="", font_size=24, size_hint_y=None)
        spacer2 = Label(text="", font_size=24, size_hint_y=None)
        spacer3 = Label(text="", font_size=24, size_hint_y=None)
        spacer4 = Label(text="", font_size=24, size_hint_y=None)

        # back button
        back_button_layout = GridLayout(cols=1, row_force_default=True, row_default_height=60, spacing=10,
                                        size_hint_y=None)
        back_button = Button(text="Return to rewards page.", font_name="Roboto", font_size=24, color=(0, 0, 0, 1),
                             size_hint_y=None, background_normal='', background_color=(.95, .95, .95, 1))
        back_button.bind(on_release=lambda btn: self.change_screen_to_rewards_page())
        back_button_layout.add_widget(back_button)

        # add all widgets
        self.layout.add_widget(self.image)
        self.layout.add_widget(self.rewards_label)
        self.layout.add_widget(self.rewards_type_label)
        self.layout.add_widget(spacer1)
        self.layout.add_widget(apply_rewards_layout)
        self.layout.add_widget(spacer2)
        self.layout.add_widget(spacer3)
        self.layout.add_widget(spacer4)
        self.layout.add_widget(back_button_layout)

        scroll_view.add_widget(self.layout)
        self.add_widget(scroll_view)

    def change_label(self, rewards):
        self.rewards = rewards
        if rewards == "bogo_big_mac":
            self.rewards_type_label.text = "Buy One Big Mac,\nGet One Free"
            self.image.source = "bogo_big_mac_icon.png"
            return
        elif rewards == "bagf_large_fries":
            self.rewards_type_label.text = "Spend Atleast $1,\nGet a Free Large Fries"
            self.image.source = "large_fries_icon.png"
            return
        elif rewards == "twenty_percent_off":
            self.rewards_type_label.text = "Spend Atleast $15,\nGet 20% Off!"
        elif rewards == "thirty_percent_off":
            self.rewards_type_label.text = "Spend Atleast $30,\nGet 30% Off!"
        self.image.source = f"meal_icon.png"

    def change_screen_to_rewards_page(self, *args):
        cart_screen = self.screen_manager.get_screen("Cart")
        cart_screen.remove_all_cart_items()

        self.screen_manager.current = "Rewards"

    def apply_rewards(self):
        Cart.rewards = self.rewards

        transition_screen = self.screen_manager.get_screen("RewardsTransition")
        transition_screen.change_label(Cart.rewards)

        self.change_screen_to_rewardstransitionscreen()

    def change_screen_to_rewardstransitionscreen(self, *args):
        cart_screen = self.screen_manager.get_screen("Cart")
        cart_screen.remove_all_cart_items()

        self.screen_manager.current = "RewardsTransition"


class TransitionScreenAfterAddingReward(Screen):
    def __init__(self, screen_manager, **kwargs):
        super().__init__(**kwargs)
        self.screen_manager = screen_manager
        transition_screen = BoxLayout(orientation="vertical")

        # Create Image
        self.image = Image(source='bogo_big_mac_icon.png', size_hint_y=None, size=(100, 100))
        transition_screen.add_widget(self.image)

        # Create Label
        self.post_order_label = Label(text=f"You have added applied\nno rewards\nto your order.", halign="center",
                                      font_name='Roboto', font_size=18, color=(0, 0, 0, 1))
        transition_screen.add_widget(self.post_order_label)

        # Create Buttons (order more & view cart)
        order_more_button = Button(text="Order Menu Items", font_name='Roboto', font_size=24, color=(0, 0, 0, 1),
                                   size=(20, 20), background_normal='', background_color=(.95, .95, .95, 1))
        order_more_button.bind(on_release=lambda btn: self.change_screen_to_order_page())
        go_to_cart_button = Button(text="View Cart", font_name='Roboto', font_size=24, color=(0, 0, 0, 1),
                                   size=(20, 20), background_normal='', background_color=(.95, .95, .95, 1))
        go_to_cart_button.bind(on_release=lambda btn: self.change_screen_to_cart())
        transition_screen.add_widget(order_more_button)
        transition_screen.add_widget(go_to_cart_button)

        self.add_widget(transition_screen)

    def change_label(self, rewards):
        if rewards == "bogo_big_mac":
            self.post_order_label.text = 'You have added applied\n"Buy One Big Mac, Get One Free"\nto your order.'
            self.image.source = "bogo_big_mac_icon.png"
        elif rewards == "bagf_large_fries":
            self.post_order_label.text = ('You have added applied\n'
                                          '"Spend Atleast $1, Get a Free Large Fries"\nto your order.')
            self.image.source = "large_fries_icon.png"
        elif rewards == "twenty_percent_off":
            self.post_order_label.text = 'You have added applied\n"Spend Atleast $15, Get 20% Off"\nto your order.'
            self.image.source = "large_fries_icon.png"
        elif rewards == "thirty_percent_off":
            self.post_order_label.text = 'You have added applied\n"Spend Atleast $30, Get 30% Off"\nto your order.'
            self.image.source = "large_fries_icon.png"

    def change_screen_to_order_page(self, *args):
        cart_screen = self.screen_manager.get_screen("Cart")
        cart_screen.remove_all_cart_items()

        self.screen_manager.current = "Order"

    def change_screen_to_cart(self, *args):
        cart_screen = self.screen_manager.get_screen("Cart")
        cart_screen.add_widgets()

        self.screen_manager.current = "Cart"


class Settings(Screen):
    accounts = [("awesome_customer@gmail.com", "password123", "James"), ("biz_owner@biz.com", "biz123", "Timothy"),
                ("felix_lengyel@juicer.com", "xqc", "Felix"), ("trainwrecks@hips.com", "HIPSHIPSHIPS", "Tyler"),
                ("ohnepixel@gambler.com", "GOLDGOLDGOLD", "Mark")]
    true_if_logged_in = False

    # Location, Lat, Long
    locations = [("Mansion McDonald's, ME", 43.860330, -70.101730), ("Retro McDonald's, MA", 41.641020, -70.885730),
                 ("Denton House, NY", 40.736568, -73.673378), ("Skinny McDonald's, NY", 40.718510, -74.001160),
                 ("Fancy McDonald's, OH", 40.741895, -73.989308), ("Global Headquarters, IL", 41.8839957, -87.6536578),
                 ("Entertainment McDonald's, FL", 28.451286, -81.4590985),
                 ("Highway McDonald's, OK", 36.6206902, -95.1540993), ("UFO McDonald's, NM", 33.4004561, -104.5232474),
                 ("Teal Arches McDonald's, AZ", 34.863219, -111.802064),
                 ("Oldest McDonald's, CA", 33.947145, -118.1171592),
                 ("Train McDonald's, CA", 34.8861485, -116.9938098), ("Vegas McDonald's, NV", 36.1193033, -115.1711625)]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = ScrollView()
        page_gridlayout = GridLayout(cols=1, row_force_default=False, row_default_height=180, size_hint_y=None)

        settings_gridlayout = GridLayout(cols=1, row_force_default=True, row_default_height=60,
                                         padding=[10, 0, 10, 20], size_hint_y=1)

        # header
        settings_header_label = Label(text="Settings", font_name='Roboto', font_size=24, bold=True, color=(0, 0, 0, 1),
                                      size_hint_y=1)
        settings_gridlayout.add_widget(settings_header_label)

        # email
        email_gridlayout = GridLayout(cols=2, row_force_default=True, row_default_height=40, size_hint_y=1)
        email_label = Label(text="Email:", halign="right", font_name='Roboto', font_size=18, color=(0, 0, 0, 1),
                            size_hint=(None, 1), width=100)
        self.email_textinput = TextInput(font_name='Roboto', font_size=18, size_hint_y=1, _hint_text="Your Email Here",
                                         multiline=False)
        email_gridlayout.add_widget(email_label)
        email_gridlayout.add_widget(self.email_textinput)
        settings_gridlayout.add_widget(email_gridlayout)

        # password
        password_gridlayout = GridLayout(cols=2, row_force_default=True, row_default_height=40, size_hint_y=1)
        password_label = Label(text="Password:", halign="right", font_name='Roboto', font_size=18, color=(0, 0, 0, 1),
                               size_hint=(None, 1), width=100)
        self.password_textinput = TextInput(font_name='Roboto', font_size=18, size_hint_y=1, multiline=False,
                                            _hint_text="Your Password Here", password=True, password_mask="*")
        password_gridlayout.add_widget(password_label)
        password_gridlayout.add_widget(self.password_textinput)
        settings_gridlayout.add_widget(password_gridlayout)

        # sign_in button and check label
        sign_in_gridlayout = GridLayout(rows=1, row_force_default=True, row_default_height=40, size_hint_y=1)
        sign_in_button = Button(text="Sign-in", font_name='Roboto', font_size=14, color=(0, 0, 0, 1),
                                size_hint=(None, 1), size=(100, 40),
                                background_normal='', background_color=(0.95, 0.95, 0.95, 1))
        sign_in_button.bind(on_release=lambda btn: self.sign_in())
        self.sign_in_check_label = Label(text="", font_name='Roboto', font_size=14, color=(0, 0, 0, 1),
                                         size_hint_y=1)
        sign_in_gridlayout.add_widget(sign_in_button)
        sign_in_gridlayout.add_widget(self.sign_in_check_label)
        settings_gridlayout.add_widget(sign_in_gridlayout)

        page_gridlayout.add_widget(settings_gridlayout)
        # Locations
        locations_grid = GridLayout(cols=1, row_force_default=True, row_default_height=60,
                                    padding=[10, 60, 10, 0], size_hint_y=1)
        location_header_label = Label(text="Location", font_name='Roboto', font_size=24, bold=True, color=(0, 0, 0, 1),
                                      size_hint_y=1)
        locations_grid.add_widget(location_header_label)
        dropdown_grid = GridLayout(cols=2, row_force_default=True, row_default_height=40, size_hint_y=1)
        locations_grid.add_widget(dropdown_grid)
        # Label
        location_label = Label(text="Location:", font_name='Roboto', font_size=18, color=(0, 0, 0, 1), halign="center",
                               size_hint=(None, 1), width=100)

        # Dropdown Selector
        store_locations_dropdown = DropDown()
        for location, latitude, longitude in Settings.locations:
            button = Button(text=f"{location}", size_hint_y=None, height=40)
            button.bind(on_release=lambda btn: store_locations_dropdown.select(btn))
            store_locations_dropdown.add_widget(button)

        self.store_locations_mainbutton = Button(text="Mansion McDonald's, ME")
        self.store_locations_mainbutton.bind(on_release=store_locations_dropdown.open)

        store_locations_dropdown.bind(on_select=self.update_selected_location)

        dropdown_grid.add_widget(location_label)
        dropdown_grid.add_widget(self.store_locations_mainbutton)
        page_gridlayout.add_widget(locations_grid)

        # MapView
        self.map_grid = GridLayout(cols=1, row_force_default=True, row_default_height=300, size_hint_y=1)

        page_gridlayout.add_widget(self.map_grid)
        self.layout.add_widget(page_gridlayout)

        with self.layout.canvas.before:
            Color(1, 1, 1, 1)  # Set color to white
            self.rect = Rectangle(pos=self.layout.pos, size=(500, 1000))

        self.add_widget(self.layout)

    def sign_in(self):
        first_name = self.check_if_combination_is_true()
        if first_name is None:
            self.sign_in_check_label.text = "Email or password is incorrect!"
        else:
            self.sign_in_check_label.text = f"Welcome, {first_name}!"
            Cart.first_name = f"{first_name}"
            Settings.true_if_logged_in = True

    def check_if_combination_is_true(self):
        for email, password, first_name in Settings.accounts:
            if self.email_textinput.text == email and self.password_textinput.text == password:
                return first_name
        return None

    def update_selected_location(self, instance, value):
        self.store_locations_mainbutton.text = f"{value.text}"
        Cart.location = value.text
        for location, latitude, longitude in Settings.locations:
            if value.text == location:
                # update mapview and mapmarker
                self.update_mapview_and_mapmarker(latitude, longitude)
                return

    def update_mapview_and_mapmarker(self, latitude, longitude):
        """
        updating mapview doesn't seem to work. might be a problem with mapview or the current version...
        this is a workaround.
        """
        # checks if mapview is present, then deletes if one is present.
        if self.map_grid.children is not None:
            widgets_to_remove = self.map_grid.children[:]
            for widget in widgets_to_remove:
                self.map_grid.remove_widget(widget)

        # creates new mapview always.
        # Create a MapView
        mapview = MapView(zoom=15, lat=latitude, lon=longitude)

        # Create a MapMarker
        mapview_mapmarker = MapMarker(lat=latitude, lon=longitude)

        # Add the MapMarker to the MapView
        mapview.add_marker(mapview_mapmarker)

        self.map_grid.add_widget(mapview)


class ItemOrder(Screen):
    def __init__(self, screen_manager, **kwargs):
        super().__init__(**kwargs)
        self.screen_manager = screen_manager

        scroll_view = ScrollView()

        # stores the current menu item
        self.current_menu_item = ""
        # stores how many current items are in cart
        self.number_of_items = 0

        self.layout = GridLayout(cols=1, row_force_default=True, row_default_height=60, padding=[10, 60, 10, 0],
                                 spacing=10, size_hint_y=None)
        self.layout.minimum_height = 200

        # image
        self.image = Image(source='big_mac_icon.png', size_hint_y=None, size=(100, 100))

        # "ordering" text
        self.order_label = Label(text='Ordering', font_name='Roboto', font_size=24, color=(0, 0, 0, 1),
                                 size_hint_y=None)

        # number of items (buttons and label)
        number_gridlayout = GridLayout(rows=1, row_force_default=True, row_default_height=60, size_hint_y=None)
        decrease_button = Button(text="-", font_name='Roboto', font_size=24, color=(0, 0, 0, 1),
                                 size=(20, 20), background_normal='', background_color=(.95, .95, .95, 1))
        decrease_button.bind(on_release=lambda btn: self.change_number_of_items("subtraction"))
        self.item_count = Label(text=str(self.number_of_items), font_name='Roboto', font_size=24, color=(0, 0, 0, 1))
        increase_button = Button(text="+", font_name='Roboto', font_size=24, color=(0, 0, 0, 1),
                                 size=(20, 20), background_normal='', background_color=(.95, .95, .95, 1))
        increase_button.bind(on_release=lambda btn: self.change_number_of_items("addition"))
        number_gridlayout.add_widget(decrease_button)
        number_gridlayout.add_widget(self.item_count)
        number_gridlayout.add_widget(increase_button)

        # item
        item_layout = GridLayout(cols=1, row_force_default=True, row_default_height=60, spacing=10, size_hint_y=None)
        self.item_label = Label(text="", font_name='Roboto', font_size=24, color=(0, 0, 0, 1), size_hint_y=None)
        item_layout.add_widget(self.item_label)

        # add-to-cart button
        add_to_cart_layout = GridLayout(cols=1, row_force_default=True, row_default_height=60, spacing=10,
                                        size_hint_y=None)
        add_to_cart_button = Button(text="Add to Cart", font_name="Roboto", font_size=24, color=(0, 0, 0, 1),
                                    size_hint_y=None, background_normal='', background_color=(.95, .95, .95, 1))
        add_to_cart_button.bind(on_release=lambda btn: self.add_to_cart())
        add_to_cart_layout.add_widget(add_to_cart_button)

        # spacer
        spacer1 = Label(text="", font_size=24, size_hint_y=None)
        spacer2 = Label(text="", font_size=24, size_hint_y=None)
        spacer3 = Label(text="", font_size=24, size_hint_y=None)

        # back button
        back_button_layout = GridLayout(cols=1, row_force_default=True, row_default_height=60, spacing=10,
                                        size_hint_y=None)
        back_button = Button(text="Return to order menu.", font_name="Roboto", font_size=24, color=(0, 0, 0, 1),
                             size_hint_y=None, background_normal='', background_color=(.95, .95, .95, 1))
        back_button.bind(on_release=lambda btn: self.change_screen_to_order_page())
        back_button_layout.add_widget(back_button)

        # add all widgets
        self.layout.add_widget(self.image)
        self.layout.add_widget(self.order_label)
        self.layout.add_widget(number_gridlayout)
        self.layout.add_widget(item_layout)
        self.layout.add_widget(add_to_cart_layout)
        self.layout.add_widget(spacer1)
        self.layout.add_widget(spacer2)
        self.layout.add_widget(spacer3)
        self.layout.add_widget(back_button_layout)

        scroll_view.add_widget(self.layout)
        self.add_widget(scroll_view)

    def change_label(self, item):
        if item == "big_mac":
            self.item_label.text = "Big Mac(s)"
        elif item == "filet_o_fish":
            self.item_label.text = "Filet-o-Fish"
        elif item == "mcchicken":
            self.item_label.text = "McChicken(s)"
        elif item == "mcdouble":
            self.item_label.text = "McDouble(s)"
        elif item == "mcnuggets_10":
            self.item_label.text = "10-piece McNuggets"
        elif item == "mcnuggets_6":
            self.item_label.text = "6-piece McNuggets"
        elif item == "large_fries":
            self.item_label.text = "Large Fries"
        elif item == "medium_fries":
            self.item_label.text = "Medium Fries"
        elif item == "small_fries":
            self.item_label.text = "Small Fries"
        elif item == "fountain_drink":
            self.item_label.text = "Fountain Drink(s)"
        elif item == "iced_mocha":
            self.item_label.text = "Iced Mocha(s)"
        self.current_menu_item = item
        self.image.source = f"{item}_icon.png"

    def change_number_of_items(self, operation):
        if operation == "addition":
            self.number_of_items += 1
        elif operation == "subtraction" and self.number_of_items is not 0:
            self.number_of_items -= 1
        self.item_count.text = f"{self.number_of_items}"

    def add_to_cart(self):
        if self.number_of_items == 0:
            return

        if self.current_menu_item == "big_mac":
            Cart.number_of_big_mac += self.number_of_items
        elif self.current_menu_item == "filet_o_fish":
            Cart.number_of_filet_o_fish += self.number_of_items
        elif self.current_menu_item == "mcchicken":
            Cart.number_of_mcchicken += self.number_of_items
        elif self.current_menu_item == "mcdouble":
            Cart.number_of_mcdouble += self.number_of_items
        elif self.current_menu_item == "mcnuggets_10":
            Cart.number_of_mcnuggets_10 += self.number_of_items
        elif self.current_menu_item == "mcnuggets_6":
            Cart.number_of_mcnuggets_6 += self.number_of_items
        elif self.current_menu_item == "large_fries":
            Cart.number_of_large_fries += self.number_of_items
        elif self.current_menu_item == "medium_fries":
            Cart.number_of_medium_fries += self.number_of_items
        elif self.current_menu_item == "small_fries":
            Cart.number_of_small_fries += self.number_of_items
        elif self.current_menu_item == "fountain_drink":
            Cart.number_of_fountain_drink += self.number_of_items
        elif self.current_menu_item == "iced_mocha":
            Cart.number_of_iced_mocha += self.number_of_items

        # Change label for Transition Screen, then changing to Transition Screen
        transition_screen = self.screen_manager.get_screen("Transition")
        transition_screen.change_label(self.current_menu_item, self.number_of_items)

        # Reset number of items for next order
        self.number_of_items = 0
        self.item_count.text = f"{self.number_of_items}"

        self.change_screen_to_transition_page()

    def change_screen_to_transition_page(self, *args):
        cart_screen = self.screen_manager.get_screen("Cart")
        cart_screen.remove_all_cart_items()

        self.screen_manager.current = "Transition"

    def change_screen_to_order_page(self, *args):
        cart_screen = self.screen_manager.get_screen("Cart")
        cart_screen.remove_all_cart_items()

        self.screen_manager.current = "Order"


class TransitionScreenAfterAddingToCart(Screen):
    def __init__(self, screen_manager, **kwargs):
        super().__init__(**kwargs)
        self.screen_manager = screen_manager
        transition_screen = BoxLayout(orientation="vertical")

        # Create Image
        self.image = Image(source='big_mac_icon.png', size_hint_y=None, size=(100, 100))
        transition_screen.add_widget(self.image)

        # Create Label
        self.post_order_label = Label(text=f"You have added 0 items to your cart.", halign="center",
                                      font_name='Roboto', font_size=18, color=(0, 0, 0, 1))
        transition_screen.add_widget(self.post_order_label)

        # Create Buttons (order more & view cart)
        order_more_button = Button(text="Order More", font_name='Roboto', font_size=24, color=(0, 0, 0, 1),
                                   size=(20, 20), background_normal='', background_color=(.95, .95, .95, 1))
        order_more_button.bind(on_release=lambda btn: self.change_screen_to_order_page())
        go_to_cart_button = Button(text="View Cart", font_name='Roboto', font_size=24, color=(0, 0, 0, 1),
                                   size=(20, 20), background_normal='', background_color=(.95, .95, .95, 1))
        go_to_cart_button.bind(on_release=lambda btn: self.change_screen_to_cart())
        transition_screen.add_widget(order_more_button)
        transition_screen.add_widget(go_to_cart_button)

        self.add_widget(transition_screen)

    def change_label(self, item, number_of_items):
        if item == "big_mac":
            self.post_order_label.text = f"You have added {number_of_items}\nBig Mac(s) to your cart."
        elif item == "filet_o_fish":
            self.post_order_label.text = f"You have added {number_of_items}\nFilet-o-Fish to your cart."
        elif item == "mcchicken":
            self.post_order_label.text = f"You have added {number_of_items}\nMcChicken(s) to your cart."
        elif item == "mcdouble":
            self.post_order_label.text = f"You have added {number_of_items}\nMcDouble(s) to your cart."
        elif item == "mcnuggets_10":
            self.post_order_label.text = f"You have added {number_of_items}\n10-piece McNuggets to your cart."
        elif item == "mcnuggets_6":
            self.post_order_label.text = f"You have added {number_of_items}\n6-piece McNuggets to your cart."
        elif item == "large_fries":
            self.post_order_label.text = f"You have added {number_of_items}\nLarge Fries to your cart."
        elif item == "medium_fries":
            self.post_order_label.text = f"You have added {number_of_items}\nMedium Fries to your cart."
        elif item == "small_fries":
            self.post_order_label.text = f"You have added {number_of_items}\nSmall Fries to your cart."
        elif item == "fountain_drink":
            self.post_order_label.text = f"You have added {number_of_items}\nFountain Drink(s) to your cart."
        elif item == "iced_mocha":
            self.post_order_label.text = f"You have added {number_of_items}\nIced Mocha(s) to your cart."
        self.image.source = f"{item}_icon.png"

    def change_screen_to_order_page(self, *args):
        cart_screen = self.screen_manager.get_screen("Cart")
        cart_screen.remove_all_cart_items()

        self.screen_manager.current = "Order"

    def change_screen_to_cart(self, *args):
        cart_screen = self.screen_manager.get_screen("Cart")
        cart_screen.add_widgets()

        self.screen_manager.current = "Cart"


class Cart(Screen):
    # define variables that are accessible
    number_of_big_mac = 0
    number_of_filet_o_fish = 0
    number_of_mcchicken = 0
    number_of_mcdouble = 0
    number_of_mcnuggets_10 = 0
    number_of_mcnuggets_6 = 0
    number_of_large_fries = 0
    number_of_medium_fries = 0
    number_of_small_fries = 0
    number_of_fountain_drink = 0
    number_of_iced_mocha = 0

    price_of_big_mac = 5.00
    price_of_filet_o_fish = 5.00
    price_of_mcchicken = 1.00
    price_of_mcdouble = 2.00
    price_of_mcnuggets_10 = 4.00
    price_of_mcnuggets_6 = 3.00
    price_of_large_fries = 4.00
    price_of_medium_fries = 3.50
    price_of_small_fries = 2.00
    price_of_fountain_drink = 1.00
    price_of_iced_mocha = 2.00

    rewards = ""
    coupons_applied_successfully = False

    location = "Mansion McDonald's, ME"
    delivery_option = "delivery"
    first_name = "Person"

    def __init__(self, screen_manager, **kwargs):
        super().__init__(**kwargs)
        self.screen_manager = screen_manager
        self.scroll_view = ScrollView()

        self.cart_items_grid = GridLayout(cols=1, row_force_default=True, row_default_height=120,
                                          padding=[10, 20, 10, 20], spacing=20, size_hint_y=None)

        self.scroll_view.add_widget(self.cart_items_grid)
        self.add_widget(self.scroll_view)

    def add_widgets(self):
        array_of_amount_of_menu_items = [Cart.number_of_big_mac, Cart.number_of_filet_o_fish,
                                         Cart.number_of_mcchicken, Cart.number_of_mcdouble,
                                         Cart.number_of_mcnuggets_10, Cart.number_of_mcnuggets_6,
                                         Cart.number_of_large_fries, Cart.number_of_medium_fries,
                                         Cart.number_of_small_fries, Cart.number_of_fountain_drink,
                                         Cart.number_of_iced_mocha]
        if array_of_amount_of_menu_items == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] and Cart.rewards == "":
            spacer = Label(text="", font_name='Roboto', font_size=24)
            self.cart_items_grid.add_widget(spacer)
            empty_cart_label = Label(text="Your cart is empty...",
                                     font_name='Roboto', font_size=24, color=(0, 0, 0, 1))
            self.cart_items_grid.add_widget(empty_cart_label)
            sad_face = Image(source="widepeepoSad.png", size_hint_y=None)
            self.cart_items_grid.add_widget(sad_face)
            return

        # location information & button, delivery/pickup options
        location_gridlayout = GridLayout(cols=1, row_force_default=True, row_default_height=40, size_hint_y=1)
        location_gridlayout.id = "None"
        location_button = Button(text="Change\nlocation", font_name='Roboto', font_size=14, color=(0, 0, 0, 1),
                                 background_normal='', background_color=(.95, .95, .95, 1))
        self.location_label = Label(text=f"You are ordering {Cart.delivery_option}\nfrom {Cart.location}.",
                                    halign="center", font_name='Roboto', font_size=14, bold=True, color=(0, 0, 0, 1))
        location_button.bind(on_release=lambda btn: self.change_screen_to_settings_page())
        delivery_options_gridlayout = GridLayout(cols=3, row_force_default=True, row_default_height=40, size_hint_y=1)
        delivery_button = Button(text="Delivery", font_name='Roboto', font_size=14, color=(0, 0, 0, 1),
                                 background_normal='', background_color=(.95, .95, .95, 1))
        delivery_button.bind(on_release=lambda btn: self.change_delivery_option("delivery"))
        pick_up_button = Button(text="Pick-up", font_name='Roboto', font_size=14, color=(0, 0, 0, 1),
                                background_normal='', background_color=(.90, .90, .90, 1))
        pick_up_button.bind(on_release=lambda btn: self.change_delivery_option("pick_up"))
        curbside_button = Button(text="Curbside", font_name='Roboto', font_size=14, color=(0, 0, 0, 1),
                                 background_normal='', background_color=(.95, .95, .95, 1))
        curbside_button.bind(on_release=lambda btn: self.change_delivery_option("curbside"))
        delivery_options_gridlayout.add_widget(delivery_button)
        delivery_options_gridlayout.add_widget(pick_up_button)
        delivery_options_gridlayout.add_widget(curbside_button)
        location_gridlayout.add_widget(location_button)
        location_gridlayout.add_widget(self.location_label)
        location_gridlayout.add_widget(delivery_options_gridlayout)
        self.cart_items_grid.add_widget(location_gridlayout)

        # Applied Rewards Indicator. if a reward was applied, it will show here
        if Cart.rewards != "":
            rewards_grid = GridLayout(rows=1)
            rewards_grid.id = "None"
            if Cart.rewards == "bogo_big_mac":
                rewards_icon = Image(source='bogo_big_mac_icon.png', size_hint=(None, None), size=(75, 75))
                rewards_grid.add_widget(rewards_icon)
                rewards_label = Label(text='Rewards Applied:\nBuy One Big Mac, Get One Free!', font_name='Roboto',
                                      size_hint_y=None, halign='left', valign="middle", padding=(10, 0),
                                      color=(0, 0, 0, 1))
                rewards_label.bind(size=rewards_label.setter('text_size'))
                rewards_grid.add_widget(rewards_label)
            elif Cart.rewards == "bagf_large_fries":
                rewards_icon = Image(source='large_fries_icon.png', size_hint=(None, None), size=(75, 75))
                rewards_grid.add_widget(rewards_icon)
                rewards_label = Label(text='Rewards Applied:\nSpend Atleast $1, Get a Free Large Fries!',
                                      font_name='Roboto', size_hint_y=None, halign='left', valign="middle",
                                      padding=(10, 0), color=(0, 0, 0, 1))
                rewards_label.bind(size=rewards_label.setter('text_size'))
                rewards_grid.add_widget(rewards_label)
            elif Cart.rewards == "twenty_percent_off":
                rewards_icon = Image(source='meal_icon.png', size_hint=(None, None), size=(75, 75))
                rewards_grid.add_widget(rewards_icon)
                rewards_label = Label(text='Rewards Applied:\nSpend Atleast $15, Get 20% Off!', font_name='Roboto',
                                      size_hint_y=None, halign='left', valign="middle", padding=(10, 0),
                                      color=(0, 0, 0, 1))
                rewards_label.bind(size=rewards_label.setter('text_size'))
                rewards_grid.add_widget(rewards_label)
            elif Cart.rewards == "thirty_percent_off":
                rewards_icon = Image(source='meal_icon.png', size_hint=(None, None), size=(75, 75))
                rewards_grid.add_widget(rewards_icon)
                rewards_label = Label(text='Rewards Applied:\nSpend Atleast $30, Get 30% Off!', font_name='Roboto',
                                      size_hint_y=None, halign='left', valign="middle", padding=(10, 0),
                                      color=(0, 0, 0, 1))
                rewards_label.bind(size=rewards_label.setter('text_size'))
                rewards_grid.add_widget(rewards_label)
            self.cart_items_grid.add_widget(rewards_grid)

        if Cart.rewards != "" and array_of_amount_of_menu_items == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]:
            cart_empty_but_rewards_applied_grid = GridLayout(rows=1)
            cart_empty_but_rewards_applied_grid.id = "None"
            cart_empty_but_rewards_applied_icon = Image(source='logo.png', size_hint=(None, None), size=(75, 75))
            cart_empty_but_rewards_applied_grid.add_widget(cart_empty_but_rewards_applied_icon)
            cart_empty_but_rewards_applied_label = Label(text='You applied a reward,\nbut your cart is empty!',
                                                         font_name='Roboto', halign='left', valign="middle",
                                                         size_hint_y=None, padding=(10, 0), color=(0, 0, 0, 1))
            cart_empty_but_rewards_applied_label.bind(size=cart_empty_but_rewards_applied_label.setter('text_size'))
            cart_empty_but_rewards_applied_grid.add_widget(cart_empty_but_rewards_applied_label)
            self.cart_items_grid.add_widget(cart_empty_but_rewards_applied_grid)

            go_add_a_menu_item_button = Button(text="Go add a menu item!", font_name='Roboto', font_size=14,
                                               color=(0, 0, 0, 1), background_normal='',
                                               background_color=(.95, .95, .95, 1))
            go_add_a_menu_item_button.id = "None"
            go_add_a_menu_item_button.bind(on_release=lambda btn: self.change_screen_to_order_page())
            self.cart_items_grid.add_widget(go_add_a_menu_item_button)

        menu_items = [("Big Mac", "big_mac", Cart.number_of_big_mac, Cart.price_of_big_mac),
                      ("Filet-o-Fish", "filet_o_fish", Cart.number_of_filet_o_fish, Cart.price_of_filet_o_fish),
                      ("McChicken", "mcchicken", Cart.number_of_mcchicken, Cart.price_of_mcchicken),
                      ("McDouble", "mcdouble", Cart.number_of_mcdouble, Cart.price_of_mcdouble),
                      ("10-piece McNuggets", "mcnuggets_10", Cart.number_of_mcnuggets_10, Cart.price_of_mcnuggets_10),
                      ("6-piece McNuggets", "mcnuggets_6", Cart.number_of_mcnuggets_6, Cart.price_of_mcnuggets_6),
                      ("Large Fries", "large_fries", Cart.number_of_large_fries, Cart.price_of_large_fries),
                      ("Medium Fries", "medium_fries", Cart.number_of_medium_fries, Cart.price_of_medium_fries),
                      ("Small Fries", "small_fries", Cart.number_of_small_fries, Cart.price_of_small_fries),
                      ("Fountain Drink", "fountain_drink", Cart.number_of_fountain_drink, Cart.price_of_fountain_drink),
                      ("Iced Mocha", "iced_mocha", Cart.number_of_iced_mocha, Cart.price_of_iced_mocha)
                      ]
        for item, item_code, quantity, price in menu_items:
            if quantity > 0:
                # item_grid
                item_grid = GridLayout(rows=3, cols=2, row_force_default=True, row_default_height=40,
                                       size_hint_y=None)
                item_grid.id = f'{item_code}'
                # image
                image = Image(source=f"{item_code}_icon.png", size_hint_y=None, size=(60, 60))
                item_grid.add_widget(image)
                # label_name
                label_name = Label(text=f"{item}", font_name='Roboto', font_size=14, color=(0, 0, 0, 1))
                item_grid.add_widget(label_name)
                # quantity label
                quantity_label = Label(text=f"Quantity: {quantity}", font_name='Roboto', font_size=14,
                                       color=(0, 0, 0, 1))
                item_grid.add_widget(quantity_label)
                # total_price label
                total_price_label = Label(text=f"${price:.2f} x {quantity} = "
                                               f"${self.calculate_individual_item_price(item_code):.2f}",
                                          font_name='Roboto', font_size=14, color=(0, 0, 0, 1))
                item_grid.add_widget(total_price_label)
                # delete button
                delete_button = Button(text=f"Delete {item}", font_name='Roboto', font_size=14, color=(0, 0, 0, 1),
                                       width=120, background_normal='', background_color=(.95, .95, .95, 1))
                delete_button.bind(on_release=lambda btn, item_code=item_code: self.delete_items_from_cart(item_code))
                item_grid.add_widget(delete_button)
                self.cart_items_grid.add_widget(item_grid)

        # cart total price label
        cart_total_and_submit_button_gridlayout = GridLayout(cols=2, row_force_default=True, row_default_height=40,
                                                             size_hint_y=1)
        cart_total_and_submit_button_gridlayout.id = "None"
        cart_total_price_spacer = Label(text="", font_name='Roboto', font_size=14)
        cart_total_price_number_label = Label(text=f"Total Price: ${self.calculate_total_price():.2f}",
                                              font_name='Roboto', font_size=14, bold=True, color=(0, 0, 0, 1))
        cart_total_and_submit_button_gridlayout.add_widget(cart_total_price_spacer)
        cart_total_and_submit_button_gridlayout.add_widget(cart_total_price_number_label)

        # submit order with location (theoretically)
        cart_submit_spacer = Label(text="", font_name='Roboto', font_size=14)
        cart_submit_button = Button(text="Complete Order", font_name='Roboto', font_size=14, color=(0, 0, 0, 1),
                                    width=120, background_normal='', background_color=(.95, .95, .95, 1))
        cart_submit_button.bind(on_release=lambda btn: self.send_data())
        cart_total_and_submit_button_gridlayout.add_widget(cart_submit_spacer)
        cart_total_and_submit_button_gridlayout.add_widget(cart_submit_button)

        self.cart_items_grid.add_widget(cart_total_and_submit_button_gridlayout)

    def remove_all_cart_items(self):
        if self.cart_items_grid.children is None:
            return
        # fixes for loop by using local variable instead of having widgets_to_remove being updated live
        widgets_to_remove = self.cart_items_grid.children[:]
        for widget in widgets_to_remove:
            self.cart_items_grid.remove_widget(widget)

    def delete_items_from_cart(self, item_code):
        for menu_item in self.cart_items_grid.children:
            if menu_item.id == item_code:
                self.cart_items_grid.remove_widget(menu_item)
        if item_code == "big_mac":
            Cart.number_of_big_mac = 0
        elif item_code == "filet_o_fish":
            Cart.number_of_filet_o_fish = 0
        elif item_code == "mcchicken":
            Cart.number_of_mcchicken = 0
        elif item_code == "mcdouble":
            Cart.number_of_mcdouble = 0
        elif item_code == "mcnuggets_10":
            Cart.number_of_mcnuggets_10 = 0
        elif item_code == "mcnuggets_6":
            Cart.number_of_mcnuggets_6 = 0
        elif item_code == "large_fries":
            Cart.number_of_large_fries = 0
        elif item_code == "medium_fries":
            Cart.number_of_medium_fries = 0
        elif item_code == "small fries":
            Cart.number_of_small_fries = 0
        elif item_code == "fountain_drink":
            Cart.number_of_fountain_drink = 0
        elif item_code == "iced_mocha":
            Cart.number_of_iced_mocha = 0

    def calculate_individual_item_price(self, item_code):
        price = 0.00
        if item_code == "big_mac":
            price = Cart.number_of_big_mac * Cart.price_of_big_mac
        elif item_code == "filet_o_fish":
            price = Cart.number_of_filet_o_fish * Cart.price_of_filet_o_fish
        elif item_code == "mcchicken":
            price = Cart.number_of_mcchicken * Cart.price_of_mcchicken
        elif item_code == "mcdouble":
            price = Cart.number_of_mcdouble * Cart.price_of_mcdouble
        elif item_code == "mcnuggets_10":
            price = Cart.number_of_mcnuggets_10 * Cart.price_of_mcnuggets_10
        elif item_code == "mcnuggets_6":
            price = Cart.number_of_mcnuggets_6 * Cart.price_of_mcnuggets_6
        elif item_code == "large_fries":
            price = Cart.number_of_large_fries * Cart.price_of_large_fries
        elif item_code == "medium_fries":
            price = Cart.number_of_medium_fries * Cart.price_of_medium_fries
        elif item_code == "small_fries":
            price = Cart.number_of_small_fries * Cart.price_of_small_fries
        elif item_code == "fountain_drink":
            price = Cart.number_of_fountain_drink * Cart.price_of_fountain_drink
        elif item_code == "iced_mocha":
            price = Cart.number_of_iced_mocha * Cart.price_of_iced_mocha
        return price

    def calculate_total_price(self):
        total_price = ((Cart.number_of_big_mac * Cart.price_of_big_mac) +
                       (Cart.number_of_filet_o_fish * Cart.price_of_filet_o_fish) +
                       (Cart.number_of_mcchicken * Cart.price_of_mcchicken) +
                       (Cart.number_of_mcdouble * Cart.price_of_mcdouble) +
                       (Cart.number_of_mcnuggets_10 * Cart.price_of_mcnuggets_10) +
                       (Cart.number_of_mcnuggets_6 * Cart.price_of_mcnuggets_6) +
                       (Cart.number_of_large_fries * Cart.price_of_large_fries) +
                       (Cart.number_of_medium_fries * Cart.price_of_medium_fries) +
                       (Cart.number_of_small_fries * Cart.price_of_small_fries) +
                       (Cart.number_of_fountain_drink * Cart.price_of_fountain_drink) +
                       (Cart.number_of_iced_mocha * Cart.price_of_iced_mocha)
                       )
        if Cart.rewards == "bogo_big_mac" and Cart.number_of_big_mac >= 2:
            total_price = ((Cart.number_of_big_mac * Cart.price_of_big_mac - Cart.price_of_big_mac) +
                           (Cart.number_of_filet_o_fish * Cart.price_of_filet_o_fish) +
                           (Cart.number_of_mcchicken * Cart.price_of_mcchicken) +
                           (Cart.number_of_mcdouble * Cart.price_of_mcdouble) +
                           (Cart.number_of_mcnuggets_10 * Cart.price_of_mcnuggets_10) +
                           (Cart.number_of_mcnuggets_6 * Cart.price_of_mcnuggets_6) +
                           (Cart.number_of_large_fries * Cart.price_of_large_fries) +
                           (Cart.number_of_medium_fries * Cart.price_of_medium_fries) +
                           (Cart.number_of_small_fries * Cart.price_of_small_fries) +
                           (Cart.number_of_fountain_drink * Cart.price_of_fountain_drink) +
                           (Cart.number_of_iced_mocha * Cart.price_of_iced_mocha)
                           )
            Cart.coupons_applied_successfully = True
        elif Cart.rewards == "bagf_large_fries":
            if Cart.number_of_large_fries > 1:
                total_price_without_1_large_fries = ((Cart.number_of_big_mac * Cart.price_of_big_mac) +
                                                     (Cart.number_of_filet_o_fish * Cart.price_of_filet_o_fish) +
                                                     (Cart.number_of_mcchicken * Cart.price_of_mcchicken) +
                                                     (Cart.number_of_mcdouble * Cart.price_of_mcdouble) +
                                                     (Cart.number_of_mcnuggets_10 * Cart.price_of_mcnuggets_10) +
                                                     (Cart.number_of_mcnuggets_6 * Cart.price_of_mcnuggets_6) +
                                                     ((Cart.number_of_large_fries - 1) * Cart.price_of_large_fries) +
                                                     (Cart.number_of_medium_fries * Cart.price_of_medium_fries) +
                                                     (Cart.number_of_small_fries * Cart.price_of_small_fries) +
                                                     (Cart.number_of_fountain_drink * Cart.price_of_fountain_drink) +
                                                     (Cart.number_of_iced_mocha * Cart.price_of_iced_mocha)
                                                     )
                if total_price_without_1_large_fries > 1:
                    Cart.coupons_applied_successfully = True
                    return total_price_without_1_large_fries
            elif Cart.number_of_large_fries == 1:
                total_price_without_large_fries = ((Cart.number_of_big_mac * Cart.price_of_big_mac) +
                                                   (Cart.number_of_filet_o_fish * Cart.price_of_filet_o_fish) +
                                                   (Cart.number_of_mcchicken * Cart.price_of_mcchicken) +
                                                   (Cart.number_of_mcdouble * Cart.price_of_mcdouble) +
                                                   (Cart.number_of_mcnuggets_10 * Cart.price_of_mcnuggets_10) +
                                                   (Cart.number_of_mcnuggets_6 * Cart.price_of_mcnuggets_6) +
                                                   (Cart.number_of_medium_fries * Cart.price_of_medium_fries) +
                                                   (Cart.number_of_small_fries * Cart.price_of_small_fries) +
                                                   (Cart.number_of_fountain_drink * Cart.price_of_fountain_drink) +
                                                   (Cart.number_of_iced_mocha * Cart.price_of_iced_mocha)
                                                   )
                if total_price_without_large_fries > 1:
                    Cart.coupons_applied_successfully = True
                    return total_price_without_large_fries
            else:
                Cart.coupons_applied_successfully = False
            return total_price
        elif Cart.rewards == "twenty_percent_off" and total_price >= 15:
            total_price = total_price * 0.85
            Cart.coupons_applied_successfully = True
        elif Cart.rewards == "thirty_percent_off" and total_price >= 30:
            total_price = total_price * 0.7
            Cart.coupons_applied_successfully = True
        return total_price

    def send_data(self):
        """
        Sending data to each individual store's system can be sorted out by location coords, but they probably
        have location codes and get sorted by a main system. Because I do not have access to these things and
        this is practice for making a bare-bones app, I will just print out the data that is required.
        """
        array_of_amount_of_menu_items = [Cart.number_of_big_mac, Cart.number_of_filet_o_fish,
                                         Cart.number_of_mcchicken, Cart.number_of_mcdouble,
                                         Cart.number_of_mcnuggets_10, Cart.number_of_mcnuggets_6,
                                         Cart.number_of_large_fries, Cart.number_of_medium_fries,
                                         Cart.number_of_small_fries, Cart.number_of_fountain_drink,
                                         Cart.number_of_iced_mocha]
        if array_of_amount_of_menu_items == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]:
            return

        data_string = f"{Cart.first_name} is ordering "

        item_array = [("Big Mac", Cart.number_of_big_mac),
                      ("Filet-o-Fish", Cart.number_of_filet_o_fish),
                      ("McChicken", Cart.number_of_mcchicken),
                      ("McDouble", Cart.number_of_mcdouble),
                      ("10-piece McNuggets", Cart.number_of_mcnuggets_10),
                      ("6-piece McNuggets", Cart.number_of_mcnuggets_6),
                      ("Large Fries", Cart.number_of_large_fries),
                      ("Medium Fries", Cart.number_of_medium_fries),
                      ("Small Fries", Cart.number_of_small_fries),
                      ("Fountain Drink", Cart.number_of_fountain_drink),
                      ("Iced Mocha", Cart.number_of_iced_mocha)]

        for menu_item, amount in item_array:
            if amount > 0:
                data_string += f"[({amount}) {menu_item}] "

        if Cart.rewards is not None and Cart.coupons_applied_successfully is True:
            data_string += f"with [{Cart.rewards}] discount "

        data_string += f"at {Cart.location} "

        if Cart.delivery_option == "delivery":
            data_string += f"for delivery."
        elif Cart.delivery_option == "pick_up":
            data_string += f"for pick-up."
        elif Cart.delivery_option == "curbside":
            data_string += f"for curbside pick-up."
        print(data_string)

    def change_delivery_option(self, delivery_option):
        if delivery_option == "delivery":
            Cart.delivery_option = "delivery"
            self.location_label.text = f"You are ordering delivery\nfrom {Cart.location}."
        elif delivery_option == "pick_up":
            Cart.delivery_option = "pick_up"
            self.location_label.text = f"You are ordering pick-up\nfrom {Cart.location}."
        elif delivery_option == "curbside":
            Cart.delivery_option = "curbside"
            self.location_label.text = f"You are ordering curbside\nfrom {Cart.location}."

    def change_screen_to_settings_page(self, *args):
        cart_screen = self.screen_manager.get_screen("Cart")
        cart_screen.remove_all_cart_items()

        self.screen_manager.current = "Settings"

    def change_screen_to_order_page(self, *args):
        cart_screen = self.screen_manager.get_screen("Cart")
        cart_screen.remove_all_cart_items()

        self.screen_manager.current = "Order"


class McDonaldsApp(App):
    def build(self):
        Window.clearcolor = (1, 1, 1, 1)

        screen_manager = ScreenManager(transition=NoTransition())
        screen_manager.add_widget(Order(name='Order', screen_manager=screen_manager))
        screen_manager.add_widget(Rewards(name='Rewards', screen_manager=screen_manager))
        screen_manager.add_widget(RewardsConfirmation(name='RewardsConfirmation', screen_manager=screen_manager))
        screen_manager.add_widget(TransitionScreenAfterAddingReward(name='RewardsTransition',
                                                                    screen_manager=screen_manager))
        screen_manager.add_widget(Settings(name='Settings'))
        screen_manager.add_widget(ItemOrder(name='ItemOrder', screen_manager=screen_manager))
        screen_manager.add_widget(TransitionScreenAfterAddingToCart(name='Transition', screen_manager=screen_manager))
        screen_manager.add_widget(Cart(name='Cart', screen_manager=screen_manager))

        navigation_bar = NavigationBar(screen_manager=screen_manager)
        navigation_bar.size_hint_y = None
        navigation_bar.height = 60

        welcome_bar = WelcomeBar(screen_manager=screen_manager)
        welcome_bar.size_hint_y = None
        welcome_bar.height = 60

        main_screen = BoxLayout(orientation='vertical')
        main_screen.add_widget(welcome_bar)
        main_screen.add_widget(screen_manager)
        main_screen.add_widget(navigation_bar)

        return main_screen


if __name__ == '__main__':
    McDonaldsApp().run()
