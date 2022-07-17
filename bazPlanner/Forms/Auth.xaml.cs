using System.Windows;
using bazPlanner.Models;

namespace bazPlanner.Forms
{
    public partial class Auth : Window
    {
        public Auth()
        {
            InitializeComponent();
        }

        private void ClickForAuth(object sender, RoutedEventArgs e)
        {
            Database.SelectOwner(textOwnerName.Text, textOwnerPass.Password.ToString());
        }
    }
}
