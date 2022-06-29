using System.Windows;

namespace bazPlannerWPF
{
    public partial class create_user : Window
    {
       
        public create_user()
        {
            InitializeComponent();
        }

        private void Add_to_DB(object sender, RoutedEventArgs e)
        {
            Owner asd = new Owner
            {
                nameOwner = username.Text,
                passwordOwner = userpswd.Text
            };
        }
    }
}
