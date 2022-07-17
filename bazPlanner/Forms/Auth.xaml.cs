using System.Windows;
using bazPlanner.Models;
using System.Diagnostics;

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
            if (Database.SelectOwner(textOwnerName.Text, textOwnerPass.Password.ToString()) == 1)
            {
                Debug.WriteLine("Success!");
                ((MainWindow)Application.Current.MainWindow).labelAuth.Content = textOwnerName.Text;
            }
            else
            {
                Debug.WriteLine("Abort!");
            }
            Close();
        }
    }
}
